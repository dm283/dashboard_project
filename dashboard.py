import os, dash_bootstrap_components as dbc, pandas as pd
from dash import Dash, dcc, html, Input, Output, State, ALL
from datetime import datetime

import functions_library as dfl
from widgets import dashboard_tabs
from widgets.common_widgets import common_widgets
from widgets.user_widgets import database_select, data_filters, dashboard_header

#  Импортирование элементов дашборда
select = database_select.select # sql-запрос к базе данных
column_names = database_select.column_names # наименования полей pandas-датафрейма
data_filter = data_filters.data_filter  # фильтры данных
DATA_UPDATE_PERIOD = common_widgets.DATA_UPDATE_PERIOD  # период обновления данных
header = dashboard_header.header    # шапка дашборда
widgets_area = dashboard_tabs.widgets_area  # область вкладок с виджетами (основной контент)

#  Формирование области виджетов "фильтры"
filters_area = []
for k in range(len(data_filter)):
    filters_area.append(
        dbc.Col( data_filter[k],
                className='widget_cell_grid', 
                style={'padding': '0px 10px 5px 10px', 'border': 'None'},
                width=2 )
    )

#  Импортирование callback-функций формирования/обновления виджетов
widget_list = [w.partition('.')[0] for w in os.listdir('widgets/user_widgets') if w.startswith('widget_')]
widget_update = {}  # Набор функций формирования/обновления виджетов
widget_update_data_type = {}  # Набор типов данных, возвращаемых функцией формирования/обновления
for w in widget_list:
    import_name = __import__('widgets.user_widgets.' + w, fromlist=[w])
    widget_key = w.replace('widget_', '')
    widget_update[widget_key] = import_name.widget_update
    widget_update_data_type[widget_key] = import_name.widget_update_data_type

BNT_SAVE_TABLE_DATA = 0 # хранение кол-ва кликов на кнопке сохранения данных таблицы
ax_msg, ay_msg = [], []  # массивы хранения кол-ва пользователей для виджета scatter

#  Подключение к базе данных
conn = dfl.get_db_connect()

#  Создание dash-приложения
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Altasoft | Dashboard | Мониторинг загруженности веб-сервисов' 


# *************************** LAYOUT *********************************************************
app.layout = html.Div([
    #  ОБЛАСТЬ ШАПКИ ДАШБОРДА
    html.Header( header, className='header' ),
    #  ОБЛАСТЬ ФИЛЬТРОВ
    dbc.Row( filters_area, style={'margin': '0px 0px 1px 0px', 'backgroundColor': 'DeepSkyBlue'} ),
    #  ОБЛАСТЬ ВИДЖЕТОВ С ДАННЫМИ (ОСНОВНОЙ КОНТЕНТ ДАШБОРДА)
    dbc.Row([ 
        dbc.Col( widgets_area, style={'backgroundColor': 'GhostWhite', 'padding': '0'}, width=12),
        dcc.Interval( id='interval_component', n_intervals=0)   #  Компонент для периодического обновления данных
        ], style={'margin': '2px'})
    ])


# *************************** CALLBACKS ******************************************************
def create_output_widget_id_list() -> list:
    #  Формирует список Output содержащий id всех виджетов в нужном порядке - для @app.callback обновления всех виджетов
    output_list = []
    for w in widget_list:
        widget_key = w.replace('widget_', '')
        output_list.append( Output(widget_key, widget_update_data_type[widget_key]) )
    return output_list

@app.callback(
    create_output_widget_id_list(),
    Output('interval_component', 'interval'),
    Output('update_date', 'children'),
    Input({'type': 'filter_dropdown', 'index': ALL}, 'value'),  #  список значений всех фильтров
    Input('interval_component', 'n_intervals'),
    Input('btn_update_data', 'n_clicks')
)
def update_data(filter_values_list, n, n_update_btn):
    #  Обновляет все виджеты дашбода
    global ax_msg, ay_msg

    #  Загрузка датафрейма
    df = dfl.get_db_data_to_datafame(conn, select, column_names); df['cnt'] = 1

    update_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    #  Динамическое формирование набора функций обновлений виджетов
    return_functions = []
    for w in widget_list:
        widget_key = w.replace('widget_', '')
        if widget_key == 'graph_scatter_cnt_users':
            return_functions.append( widget_update[widget_key](df, filter_values_list, ax_msg, ay_msg, n) )
        else:
            return_functions.append( widget_update[widget_key](df, filter_values_list, n) )

    return return_functions + [ DATA_UPDATE_PERIOD * 1000 ] + [ update_date ]


@app.callback(
    Output('settings_modal_window', 'is_open'),
    [Input('btn_settings', 'n_clicks'), Input('btn_settings_close', 'n_clicks')],
    State('settings_modal_window', 'is_open'),
    Input('btn_settings_apply', 'n_clicks'),
    State('input_period', 'value')
)
def toggle_modal(n1, n2, is_open, n, period_value):
    #  Открывает/закрывает модальное окно с настройками
    global DATA_UPDATE_PERIOD

    if n:
        try:
            DATA_UPDATE_PERIOD = int(period_value)
        except:
            print('Недопустимое значение')

    if n1 or n2:
        return not is_open
    
    return is_open


@app.callback(
    Output('modal_table_record', 'is_open'),
    Output('modal_table_record_content', 'children'),
    Output('table_record_details', 'active_cell'),
    Input('table_record_details', 'active_cell'),
    State('table_record_details', 'data'),
    Input('btn_modal_table_record_close', 'n_clicks'),
    State('modal_table_record', 'is_open'),
)
def toggle_modal_table_records(active_cell, data, n_close, is_open):
    #  Открывает/закрывает модальное окно с данными из таблицы
    if active_cell:
        row_number = int(active_cell['row'])
        record = data[row_number]
        content = []
        for k in record.keys():
            value = record[k] if record[k] else 'None'
            row = dbc.Row([
                dbc.Col(dbc.Label(k), width=6),
                dbc.Col(dbc.Label(value), width=6),
            ], style={'marginBottom': '5px'})
            content.append(row)
    else:
        content = ''

    if active_cell or n_close:
        return not is_open, content, None

    return is_open, content, active_cell


@app.callback(
    Output('modal_save_table_data', 'is_open'),
    [Input('btn_open_modal_save_table_data', 'n_clicks'), Input('btn_modal_save_table_data_close', 'n_clicks')],
    State('modal_save_table_data', 'is_open'),
    Input('btn_modal_save_table_data_save', 'n_clicks'),
    State('table_record_details', 'data'),
    State('input_file_name', 'value')
)
def toggle_modal_save_table_data(n1, n2, is_open, n, data, file_name):
    #  Открывает/закрывает модальное окно сохранения данных таблицы
    global BNT_SAVE_TABLE_DATA

    if BNT_SAVE_TABLE_DATA < n:
        try:
            df = pd.DataFrame(data)
            file_name = f'saved_files/{file_name}.xlsx'
            df.to_excel(file_name)
            BNT_SAVE_TABLE_DATA = n
        except Exception as ex:
            print(ex)

    if n1 or n2:
        return not is_open
    
    return is_open



app.run_server(debug=True)
