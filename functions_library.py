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


def get_db_connect():
  #  connects to database with defined in db argument type
  print(DB_CONNECTION_STRING)
  print('connect to database ..... ', end='')
  try:
    if DB_TYPE == '-p':
      CONN = psycopg2.connect(DB_CONNECTION_STRING)  # postgre database
    elif DB_TYPE == '-m':
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



# def get_db_connect():
#     """
#     Подключение к базе данных
#     """
#     conn = None
#     try:
#         print('connecting to data base ... ', end='')
#         conn = psycopg2.connect(
#             host='localhost',
#             port='5432',
#             database='dev_pg_1',
#             user='postgres',
#             password='s2d3f4!@'
#         )
#     except (Exception, psycopg2.DatabaseError) as err:
#         print(err)
#         sys.exit(1)
#     print('OK')
#     return conn


# def get_db_data_to_datafame(conn, select, column_names):
#     """
#     Загрузка из базы данных в pandas-датафрейм
#     """
#     cursor = conn.cursor()
#     try:
#         cursor.execute(select)
#     except (Exception, psycopg2.DatabaseError) as err:
#         print('Error:', err)
#         cursor.close()
#         return 1
#     tuples_list = cursor.fetchall()
#     cursor.close()
#     df = pd.DataFrame(tuples_list, columns=column_names)
#     return df
