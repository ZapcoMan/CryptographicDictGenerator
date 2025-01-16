# -*- coding: utf-8 -*-
# @Time    : 17 1月 2025 12:55 上午
# @Author  : codervibe
# @File    : logger.py
# @Project : CryptographicDictGenerator

import logging

class ColoredFormatter(logging.Formatter):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    def format(self, record):
        if record.levelno == logging.ERROR:
            record.msg = f"{self.RED}{record.msg}{self.RESET}"
        elif record.levelno == logging.INFO:
            record.msg = f"{self.GREEN}{record.msg}{self.RESET}"
        return super().format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)
