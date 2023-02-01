# common functions for dash projects

import sys, psycopg2, pandas as pd, json, plotly.express as px
from dash import Dash, dcc, html, Input, Output


# select = """
#     select id, web_service, user_id, device, country, user_status, sign_date, signout_date
#       from dev_pg_1.public.web_service_usage
#       where user_status = 'sign_in'
#       order by sign_date desc
# """
# column_names = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']


def get_db_connect():
    """
    подключение к базе данных
    """
    conn = None
    try:
        print('connecting to data base ... ', end='')
        conn = psycopg2.connect(
            host='localhost',
            port='5432',
            database='dev_pg_1',
            user='postgres',
            password='s2d3f4!@'
        )
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
        sys.exit(1)
    print('OK')
    return conn


def get_db_data_to_datafame(conn, select, column_names):
    """
    загрузка из базы данных в pandas-датафрейм
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select)
    except (Exception, psycopg2.DatabaseError) as err:
        print('Error:', err)
        cursor.close()
        return 1
    tuples_list = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(tuples_list, columns=column_names)
    return df
