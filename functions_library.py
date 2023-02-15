# БИБЛИОТЕКА СИСТЕМНЫХ ФУНКЦИЙ ДЛЯ DASHBOARD_PROJECT

import sys, psycopg2, pandas as pd, json, plotly.express as px
from dash import Dash, dcc, html, Input, Output


def get_db_connect():
    """
    Подключение к базе данных
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
    Загрузка из базы данных в pandas-датафрейм
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
