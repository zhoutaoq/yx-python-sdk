#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

from loguru import logger


def setup_logging():
    """配置日志记录"""
    # 禁用 Uvicorn 的默认访问日志记录器，避免重复记录
    logging.getLogger("uvicorn.access").disabled = True

    # 配置 loguru 日志记录
    logger.remove()  # 移除所有默认的处理器
    logger.add(
        "logs/{time:YYYY-MM-DD}.log",
        format="{time} | {level} | {message}",
        rotation="00:00",
        retention="10 days",
        compression="zip",
        level="INFO"
    )
    logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO")

    return logger


# 创建全局日志记录器实例
app_logger = setup_logging()
