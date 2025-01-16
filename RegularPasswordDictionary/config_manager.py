# -*- coding: utf-8 -*-
# @Time    : 17 1月 2025 12:53上午
# @Author  : codervibe
# @File    : config_manager.py.py
# @Project : CryptographicDictGenerator

import json
import yaml
from RegularPasswordDictionary.logger import logger

def save_config(filename, config):
    """
    保存配置到文件
    :param filename: 配置文件名
    :param config: 配置字典
    """
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        with open(filename, 'w') as f:
            yaml.dump(config, f)
    else:
        with open(filename, 'w') as f:
            json.dump(config, f)

def load_config(filename):
    """
    从文件加载配置
    :param filename: 配置文件名
    :return: 配置字典或None
    """
    try:
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(filename, 'r') as f:
                return yaml.safe_load(f)
        else:
            with open(filename, 'r') as f:
                return json.load(f)
    except FileNotFoundError:
        logger.error(f"配置文件 {filename} 未找到")
        return None
