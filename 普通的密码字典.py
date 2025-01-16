# -*- coding: utf-8 -*-
# @Time    : 16 1月 2025 11:16 下午
# @Author  : codervibe
# @File    : 普通的密码字典.py
# @Project : CryptographicDictGenerator
import random
import secrets
import string
from argparse import ArgumentParser

# 创建命令行参数解析器
parser = ArgumentParser(
    prog="密码字典生成",
    description="密码字典生成器 可以生成各种形式的密码"
)
# 添加命令行参数
parser.add_argument("-l", "--lowercase", default=0, help="密码中小写字符的位数", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="密码中大写字符的位数", type=int)
parser.add_argument("-n", "--numbers", default=0, help="密码中数字的位数", type=int)
parser.add_argument("-s", "--symbols", "--special-chars", default=0, help="密码中特殊符号的位数", type=int)
parser.add_argument("-t", "--total-length", default=1, help="密码的总长度", type=int)
parser.add_argument("-rl", "--random-length", action="store_true", help="密码为随机长度")
parser.add_argument("-nu", "--number", default=1, help="生成密码的数量", type=int)

# 解析命令行参数
args = parser.parse_args()

# 初始化密码列表
passwords = []

# 根据指定的数量生成密码
for _ in range(args.number):
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

    # 如果指定了总长度且实际生成的字符数不足，则填充剩余部分
    current_length = len(passwd)
    if current_length < password_length:
        remaining_length = password_length - current_length
        all_chars = string.digits + string.ascii_letters + string.punctuation
        passwd.extend([secrets.choice(all_chars) for _ in range(remaining_length)])

    # 打乱字符顺序以增加随机性
    random.shuffle(passwd)
    # 将字符列表转换为字符串并添加到密码列表中
    passwords.append("".join(passwd))

# 输出生成的密码列表
print(passwords)
