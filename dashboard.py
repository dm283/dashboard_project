import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, ALL
from datetime import datetime

import functions_library as dfl
from widgets import markup
from widgets.common_widgets import common_widgets
from widgets.user_widgets import database_select, data_filters
from widgets.user_widgets import (widget_graph_bar_countries, widget_graph_pie_devices, widget_graph_scatter_cnt_users, widget_label_cnt_countries,
    widget_label_cnt_users, widget_label_workload, widget_table_record_details)

#  Загрузка objects - select from database
select = database_select.select
column_names = database_select.column_names

#  Загрузка objects - filters
data_filter = data_filters.data_filter

#  Загрузка objects - common widgets
btn_settings = common_widgets.btn_settings
btn_update_data = common_widgets.btn_update_data
DATA_UPDATE_PERIOD = common_widgets.DATA_UPDATE_PERIOD

#  Загрузка objects - markup
widgets_area = markup.widgets_area

#  Формирование области виджетов "фильтры"
filters_area = []
for k in range(len(data_filter)):
    filters_area.append(
        dbc.Col( data_filter[k],   # html.Div( data_filter[k], className='widget_cell_grid_div' )
                className='widget_cell_grid', 
                style={'padding': '0px 5px 2px 5px'},  #'backgroundColor': 'orange', 
                width=2 )
    )

#  Загрузка objects - callback функции формирования/обновления виджетов
update_label_cnt_users = widget_label_cnt_users.update_label_cnt_users
update_label_workload = widget_label_workload.update_label_workload
update_label_cnt_countries = widget_label_cnt_countries.update_label_cnt_countries
update_pie_device = widget_graph_pie_devices.update_pie_device
update_bar_country = widget_graph_bar_countries.update_bar_country
update_scatter_cnt_users = widget_graph_scatter_cnt_users.update_scatter_cnt_users
update_table_details = widget_table_record_details.update_table_details

update_date = datetime.now().strftime('%Y-%m-%d %H:%m')
countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']
devices = ['desktop', 'mobile']
web_services = ['aDashboard', 'aMessenger']
ax_msg, ay_msg = [], []  # массивы хранения кол-ва пользователей для виджета scatter

#  Подключение к базе данных
conn = dfl.get_db_connect()

#  Создание dash-приложения
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Altasoft | Dashboard | Мониторинг загруженности веб-сервисов' 

# *************************** LAYOUT *********************************************************
app.layout = html.Div([
    #  ОБЛАСТЬ ШАПКИ ДАШБОРДА
    html.Header(children=[
        html.Span('Altasoft', className='header_title', style={'marginLeft': '30px'}),
        html.Span('Dashboard', className='header_title'),
        html.Span('Мониторинг загруженности веб-сервисов', className='header_title', style={'border': 'None', 'width': '66%'}),
        html.Span(update_date, id='update_date', className='update_date'),
        html.Span(btn_update_data, className='header_icon', style={'marginLeft': '20px'}), 
        html.Span(btn_settings, className='header_icon', style={'marginLeft': '5px'})
        ], className='header'),

    #  ОБЛАСТЬ ФИЛЬТРОВ
    dbc.Row( filters_area, style={'margin': '0px 0px 1px 0px', 'backgroundColor': 'MediumOrchid'} ),

    dbc.Row([
        #  **********  ОБЛАСТЬ ВИДЖЕТОВ УПРАВЛЕНИЯ ДАШБОРДОМ
        # dbc.Col(#filters_area,
        #         style={'backgroundColor': 'GhostWhite'}, 
        #         width=2),
        #  **********  ОБЛАСТЬ ВИДЖЕТОВ С ДАННЫМИ (ОСНОВНОЙ КОНТЕНТ ДАШБОРДА)
        dbc.Col(
            widgets_area,
            style={'backgroundColor': 'GhostWhite', 'padding': '0'}, 
            width=12),
     
        #  INTERVAL (компонент для периодического обновления данных)
        dcc.Interval(
                id='interval_component',
                n_intervals=0)

        ], style={'margin': '2px'})
    ])


# ****************** Callbacks *************************
@app.callback(
    Output('label_cnt_users', 'children'),
    Output('label_workload', 'children'),
    Output('label_cnt_countries', 'children'),
    Output('pie_device', 'figure'),
    Output('bar_country', 'figure'),
    Output('scatter_cnt_users', 'figure'),
    Output('table_details', 'data'),

    Output('interval_component', 'interval'),
    Input({'type': 'filter_dropdown', 'index': ALL}, 'value'),  #  список значений всех фильтров
    Input('interval_component', 'n_intervals'),
    Input('btn_update_data', 'n_clicks')
)

def update_data(filter_values_list, n, n_update_btn):
    #  Обновляет данные
    global ax_msg, ay_msg

    df = dfl.get_db_data_to_datafame(conn, select, column_names); df['cnt'] = 1

    return (
        update_label_cnt_users(df, filter_values_list, n),
        update_label_workload(df, filter_values_list, n),
        update_label_cnt_countries(df, filter_values_list, n),
        update_pie_device(df, filter_values_list, n),
        update_bar_country(df, filter_values_list, n),
        update_scatter_cnt_users(df, filter_values_list, ax_msg, ay_msg, n),
        update_table_details(df, filter_values_list, n),
        DATA_UPDATE_PERIOD * 1000
    )

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
    Output('table_details', 'active_cell'),
    Input('table_details', 'active_cell'),
    State('table_details', 'data'),
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



app.run_server(debug=True)
