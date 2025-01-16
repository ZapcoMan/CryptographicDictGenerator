# -*- coding: utf-8 -*-
# @Time    : 17 1月 2025 12:53上午
# @Author  : codervibe
# @File    : main.py
# @Project : CryptographicDictGenerator
import argparse
import json

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from RegularPasswordDictionary.config_manager import save_config, load_config
from RegularPasswordDictionary.logger import logger
from RegularPasswordDictionary.password_generator import generate_passwords

# 创建命令行参数解析器
parser = argparse.ArgumentParser(
    prog="密码字典生成",
    description="密码字典生成器 可以生成各种形式的密码",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
parser.add_argument("-o", "--output-file", default=None, help="将生成的密码保存到指定文件")

# 解析命令行参数
args = parser.parse_args()

# 加载配置
config = load_config(args.load_config) if args.load_config else {}
if config:
    for key, value in config.items():
        if hasattr(args, key):
            setattr(args, key, value)

# 生成密码
passwords = generate_passwords(args)

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
        "output_format": args.output_format,
        "output_file": args.output_file
    }
    save_config(args.save_config, config)

# 创建一个Console对象，用于更复杂的输出控制
console = Console()

# 输出生成的密码列表
if args.output_format == 'json':
    if isinstance(passwords, set):
        passwords = list(passwords)
    console.print(Panel(json.dumps(passwords, indent=4), title="生成的密码", style="bold blue"))
    if args.output_file:
        with open(args.output_file, 'w') as f:
            json.dump(passwords, f, indent=4)
        console.print(f"密码已保存到文件 {args.output_file}", style="bold green")
else:
    console.print(Panel(Text("生成的密码", style="bold yellow")))
    for password in passwords:
        console.print(password, style="bold green")
    if args.output_file:
        with open(args.output_file, 'w') as f:
            for password in passwords:
                f.write(password + '\n')
        console.print(f"密码已保存到文件 {args.output_file}", style="bold green")

logger.info(f"成功生成 {len(passwords)} 个密码")
