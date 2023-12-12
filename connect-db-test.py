# БИБЛИОТЕКА СИСТЕМНЫХ ФУНКЦИЙ ДЛЯ DASHBOARD_PROJECT
import sys, os, configparser, psycopg2, pyodbc, pandas as pd
from pathlib import Path

config = configparser.ConfigParser()
config_file = os.path.join(Path(__file__).resolve().parent, 'config.ini')   
if os.path.exists(config_file):
  config.read(config_file, encoding='utf-8')
else:
  print("error! config file doesn't exist"); sys.exit()
  
DB_CONNECTION_STRING = config['db']['db_connection_string']
DB_TYPE = config['db']['db_type']
DB_NAME = config['db']['db_name']
DB_SCHEMA = config['db']['db_schema']

select_query = f"""
      select id, web_service, user_id, device, country, user_status, sign_date, signout_date
        from {DB_NAME}.{DB_SCHEMA}.web_service_usage
        where user_status = 'sign_in'
        order by sign_date desc
"""
select_columns = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']


def db_connection(db):
  #  connects to database with defined in db argument type
  print(DB_CONNECTION_STRING)
  print('connect to database ..... ', end='')
  try:
    if db == '-p':
      CONN = psycopg2.connect(DB_CONNECTION_STRING)  # postgre database
    elif db == '-m':
      CONN = pyodbc.connect(DB_CONNECTION_STRING)     # ms-sql database
    print('ok')
  except(Exception) as err:
    print('error database connection'); print(err)
    sys.exit(1)

  return CONN


def get_db_data_to_datafame(conn, select, column_names):
    """
    Загрузка из базы данных в pandas-датафрейм
    """
    df = pd.read_sql(select, conn)

    return df

#**********
db = DB_TYPE
conn = db_connection(db)
df = get_db_data_to_datafame(conn, select_query, select_columns)
print(df)
