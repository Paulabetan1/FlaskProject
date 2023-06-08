import os

USER_DB = os.environ.get('USER_DB')
PASS_DB = os.environ.get('PASS_DB')
URL_DB = os.environ.get('URL_DB')
NAME_DB = os.environ.get('NAME_DB')
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'




