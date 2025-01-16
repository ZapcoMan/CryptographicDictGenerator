# -*- coding: utf-8 -*-
# @Time    : 16 1月 2025 11:16 下午
# @Author  : codervibe
# @File    : 普通的密码字典.py
# @Project : CryptographicDictGenerator
import random
import secrets
import string
from argparse import ArgumentParser
import json
import yaml

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
parser.add_argument("-cs", "--custom-set", default=None, help="自定义字符集，多个字符之间无分隔符")
parser.add_argument("-pt", "--pattern", default=None, help="密码模式模板，如 'LNL' 表示大写字母-数字-小写字母")
parser.add_argument("-ex", "--exclude-chars", default="", help="排除的字符，多个字符之间无分隔符")
parser.add_argument("-sc", "--save-config", default=None, help="保存当前配置到指定文件")
parser.add_argument("-lc", "--load-config", default=None, help="从指定文件加载配置")
parser.add_argument("-of", "--output-format", choices=['text', 'json'], default='text', help="输出格式，默认为文本")

# 解析命令行参数
args = parser.parse_args()

def save_config(filename, config):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        with open(filename, 'w') as f:
            yaml.dump(config, f)
    else:
        with open(filename, 'w') as f:
            json.dump(config, f)

def load_config(filename):
    try:
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(filename, 'r') as f:
                return yaml.safe_load(f)
        else:
            with open(filename, 'r') as f:
                return json.load(f)
    except FileNotFoundError:
        return None

# 加载配置
config = load_config(args.load_config) if args.load_config else {}
if config:
    for key, value in config.items():
        if hasattr(args, key):
            setattr(args, key, value)

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

    # 根据模式生成密码
    if args.pattern:
        pattern_map = {'U': string.ascii_uppercase, 'L': string.ascii_lowercase, 'D': string.digits, 'S': string.punctuation}
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
    passwords.append("".join(passwd))

# 保存配置
if args.save_config:
    config = {
        "lowercase": args.lowercase,
        "uppercase": args.uppercase,
        "numbers": args.numbers,
        "symbols": args.symbols,
        "total_length": args.total_length,
        "random_length": args.random_length,
        "number": args.number,
        "custom_set": args.custom_set,
        "pattern": args.pattern,
        "exclude_chars": args.exclude_chars,
        "output_format": args.output_format
    }
    save_config(args.save_config, config)

# 输出生成的密码列表
if args.output_format == 'json':
    print(json.dumps(passwords))
else:
    print(passwords)
