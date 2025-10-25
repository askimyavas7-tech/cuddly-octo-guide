from setuptools import setup, find_packages

setup(
    name="prensesmuzik",
    version="1.0",
    description="Prenses Müzik Pro - Telegram Pyrogram Müzik Botu",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
)
