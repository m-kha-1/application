from dotenv import load_dotenv

import os

load_dotenv()

secret_key = os.getenv('password')
print(secret_key)


import pymysql
