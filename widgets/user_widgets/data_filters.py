# FILTERS
from functions_library import create_filter, get_db_connect, get_db_data_to_datafame, DB_NAME, DB_SCHEMA

import warnings
warnings.filterwarnings('ignore')

conn = get_db_connect()
data_filter = {}

# filter 0
id = 0
f_type = 'dropdown'
name = 'Тип устройства'
placeholder = 'Выберите тип устройства'
value = None
clearable = True
column = 'device'
query = f"""
    select distinct device from {DB_NAME}.{DB_SCHEMA}.web_service_usage order by device
    """
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# filter 1
id = 1
f_type = 'dropdown'
name = 'Страна пользователя'
placeholder = 'Выберите страну'
value = None
clearable = True
column = 'country'
query = f"""
    select distinct country from {DB_NAME}.{DB_SCHEMA}.web_service_usage order by country
    """
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# filter 2
id = 2
f_type = 'dropdown'
name = 'Веб-сервис'
placeholder = 'Выберите веб-сервис'
value = 'aDashboard'
clearable = False
column = 'web_service'
query = f"""
    select distinct web_service from {DB_NAME}.{DB_SCHEMA}.web_service_usage order by web_service
    """
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# filter 3
id = 3
f_type = 'dropdown'
name = 'Адрес e-mail'
placeholder = 'Выберите адрес e-mail'
value = None
clearable = True
column = 'adrto'
query = f"""
    select distinct adrto from {DB_NAME}.{DB_SCHEMA}.messages_email order by adrto
    """
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)


# filter 4
id = 4
f_type = 'date_picker'
name = 'Дата обработки e-mail (dates)'
placeholder = 'Выберите date of e-mail'
value = None
clearable = True
column = 'dates'
query = ''
data_filter[id] = create_filter(f_type, name, placeholder, value, clearable, column, query, conn)

# fltr_list[3] = dfl.get_db_data_to_datafame(conn, 
#     f'select distinct adrto from {dfl.DB_NAME}.{dfl.DB_SCHEMA}.messages_email order by adrto'
#     )['adrto'].to_list()

# data_filter[3] = [html.Div('Адрес e-mail', className='filter_label'),
#                 dcc.Dropdown(
#                     options=fltr_list[3], 
#                     value=None, 
#                     placeholder="Выберите адрес e-mail", 
#                     clearable=True,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_web_service'},
#                     )]


# data_filter[0] = [html.Div('Тип устройства пользователя', className='filter_label'),
#                 dcc.Dropdown(
#                     options=['desktop', 'mobile'], 
#                     value=None, 
#                     placeholder="Выберите тип устройства", 
#                     clearable=True,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_device'},
#                     )]

# data_filter[2] = [html.Div('Веб-сервис', className='filter_label'),
#                 dcc.Dropdown(
#                     options=['aDashboard', 'aMessenger'], 
#                     value='aDashboard', 
#                     placeholder="Выберите веб-сервис", 
#                     clearable=False,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_web_service'},
#                     )]

# data_filter[1] = [html.Div('Страна пользователя', className='filter_label'),
#                 dcc.Dropdown(
#                     options=['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada'], 
#                     value=None, 
#                     placeholder="Выберите страну", 
#                     clearable=True,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_country'},
#                     )]
