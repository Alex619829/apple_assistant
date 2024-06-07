import os

DIR = os.getcwd()

ENV = open(f'{DIR}/.env', 'r')

YANDEX_API_KEY = ENV.readline().removesuffix('\n'); ENV.close()

VA_NAME = "Яблоко"

VA_ALIAS = ("яблоко", "яблочко", "яблок")