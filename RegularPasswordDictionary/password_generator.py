# -*- coding: utf-8 -*-
# @Time    : 17 1月 2025 12:54 上午
# @Author  : codervibe
# @File    : password_generator.py.py
# @Project : CryptographicDictGenerator

import random
import secrets
import string


def generate_passwords(args):
    """
    生成密码列表
    :param args: 命令行参数
    :return: 密码列表
    """
    passwords = set()  # 使用集合来存储密码，自动去重

    while len(passwords) < args.number:
        passwd = []

        # 确定密码长度
        if args.random_length:
            password_length = random.randint(1, args.total_length)
        else:
            password_length = args.total_length

        # 生成指定数量的数字字符
        for _ in range(args.numbers):
            passwd.append(secrets.choice(string.digits))
        # 生成指定数量的大写字符
        for _ in range(args.uppercase):
            passwd.append(secrets.choice(string.ascii_uppercase))
        # 生成指定数量的小写字符
        for _ in range(args.lowercase):
            passwd.append(secrets.choice(string.ascii_lowercase))
        # 生成指定数量的特殊符号
        for _ in range(args.symbols):
            passwd.append(secrets.choice(string.punctuation))

        # 根据模式生成密码
        if args.pattern:
            pattern_map = {'U': string.ascii_uppercase, 'L': string.ascii_lowercase, 'D': string.digits,
                           'S': string.punctuation}
            passwd = [secrets.choice(pattern_map[char]) for char in args.pattern]
            password_length = len(passwd)

        # 如果指定了总长度且实际生成的字符数不足，则填充剩余部分
        current_length = len(passwd)
        if current_length < password_length:
            remaining_length = password_length - current_length
            all_chars = string.digits + string.ascii_letters + string.punctuation
            if args.custom_set:
                all_chars = args.custom_set
            all_chars = ''.join([ch for ch in all_chars if ch not in args.exclude_chars])
            passwd.extend([secrets.choice(all_chars) for _ in range(remaining_length)])

        # 打乱字符顺序以增加随机性
        random.shuffle(passwd)
        # 将字符列表转换为字符串并添加到密码列表中
        password_str = "".join(passwd)
        passwords.add(password_str)

    return passwords

