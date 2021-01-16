# -*- coding:utf-8 -*-
"""
@Time : 2021/1/16 00:16
@Author: langengel
@Des: 打包配置
"""

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="speewee",
    version="0.0.1",
    author="langengel",
    author_email="langengel@qq.com",
    description="Upgrade based on official peewee 3.14.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/langengel/speewee",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
