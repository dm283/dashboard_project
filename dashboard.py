import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL
from datetime import datetime

import functions_library as dfl
from objects import database_select, data_filters

#  Загрузка objects - select from database
select = database_select.select
column_names = database_select.column_names

#  Загрузка objects - filters
data_filter = data_filters.data_filter


update_date = datetime.now().strftime('%Y-%m-%d %H:%m')
countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']
devices = ['desktop', 'mobile']
web_services = ['aDashboard', 'aMessenger']
ax_msg, ay_msg, ax_dash, ay_dash = [], [], [], []
DATA_UPDATE_PERIOD = 10000

conn = dfl.get_db_connect()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Altasoft | Dashboard | Мониторинг загруженности веб-сервисов' 


# settings button & modal window
btn_settings = [
            dbc.Button("Настройки", id='btn_settings', n_clicks=0, 
                style={'width': '100%', 'backgroundColor': 'Green', 'border': 'None'}),
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Настройки дашборда")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col(dbc.Label("Период обновления данных (сек)"), width=7),
                            dbc.Col(dbc.Input(id='input_period', value=DATA_UPDATE_PERIOD, type='text'))
                        ], style={'marginBottom': '5px'}),
                        dbc.Row([
                            dbc.Col(dbc.Label('Цветовая тема'), width=7),
                            dbc.Col(dbc.Select(id='select_theme', options=['Светлая', 'Тёмная'], value='Светлая'))
                        ], style={'marginBottom': '5px'})
                    ]),
                    dbc.ModalFooter(html.Div([
                        dbc.Button("Применить", id='btn_settings_apply', n_clicks=0,
                            style={'width': '120px', 'marginRight': '10px'}, color="success"), 
                        dbc.Button("Закрыть", id='btn_settings_close', n_clicks=0,
                            style={'width': '120px'}, color="warning" )
                        ]))
                ],
                id='settings_modal_window',
                is_open=False
            ),
        ]

# update button
btn_update_data = dbc.Button(
                            "Обновить данные", id='btn_update_data', className="ms-auto", n_clicks=0, 
                                style={'width': '100%', 'backgroundColor': 'LightSalmon', 'border': 'None'}
                        )

# WIDGETS
widget = {}
# widget 1
widget[1] = [ html.H1(style={'color': 'DarkBlue'}, id='label_cnt_users'), html.H6('Кол-во пользователей') ]
# widget 2
widget[2] = [ html.H1(style={'color': 'DarkBlue'}, id='label_workload'), html.H6('Уровень загруженности') ]
# widget 3
widget[3] = [ html.H1(style={'color': 'DarkBlue'}, id='label_cnt_countries'), html.H6('Представлено стран') ]
# widget 4
widget[4] = dcc.Graph(id='pie_device')
# widget 5
widget[5] = dcc.Graph(id='bar_country')
# widget 6
widget[6] = dcc.Graph(id='scatter_cnt_users')
# widget 7
modal_table_record = dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle('Детализация данных о пользователях онлайн', style={'fontSize': '20px'})),
                    dbc.ModalBody(id='modal_table_record_content'),
                    dbc.ModalFooter(html.Div([
                        dbc.Button("Закрыть", id='btn_modal_table_record_close', n_clicks=0,
                            style={'width': '120px'}, color="warning" )
                        ]))
                ],
                id='modal_table_record',
                is_open=False
            )
widget[7] = [ modal_table_record,
                html.H6('Детализация данных о пользователях онлайн', style={'color': 'white'}),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in ['user_id', 'device', 'country', 'sign_date']],
                    style_cell = {'font_size': '10px', 'textAlign': 'center'},
                    page_action='none',
                    style_table={'height': '715px', 'overflowY': 'auto'},
                    style_header={'backgroundColor': 'Black', 'color': 'white'},
                    style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                    id='table_details'
                    ),
                 ]

# widget 8
widget[8] = dcc.Graph(id='pie_web_services')
# widget 9
widget[9] = [ html.H1(style={'color': 'DarkBlue'}, id='label_cnt_active_web_services'), html.H6('Сервисы с пользователями') ]


tab_1 = dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    html.Div(
                        widget[1],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
                dbc.Col(
                    html.Div(
                        widget[2],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
                dbc.Col(
                    html.Div(
                        widget[3],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        widget[4],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=6),
                dbc.Col(
                    html.Div(
                        widget[5],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=6),
            ]
            ),

            dbc.Row(
                dbc.Col(
                    html.Div(
                        widget[6],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=12),
            ),
        
        ], style={'backgroundColor': 'Gainsboro'}, width=7),


        dbc.Col(
            html.Div(
                widget[7],
                className='widget_cell_grid_div_table'),
            className='widget_cell_grid', style={'backgroundColor': 'Gray'}, width=5),

    ], style={'margin': '2px 0px 2px 0px'})


tab_2 = dbc.Row([
    'TAB 2 CONTENT'
    ], style={'margin': '2px 0px 2px 0px'})


def create_filters(data_filter):
    #  Формирует область виджетов "фильтры"
    filters = []
    for k in range(len(data_filter)):
        filters.append(
            dbc.Row( html.Div( data_filter[k], className='widget_cell_grid_div' ), className='widget_cell_grid' )
        )

    return filters


# *************************** LAYOUT *********************************************************
app.layout = html.Div([
    #  HEADER AREA
    html.Header(children=[
        html.Span('Altasoft', className='header_1'),
        html.Span('Dashboard', className='header_2'),
        html.Span('Мониторинг загруженности веб-сервисов', className='header_3'),
        html.Span(f'Последнее обновление данных: {update_date}', id='update_date', className='update_date')
    ], className='header'),

    dbc.Row([

        #  Column of management
        dbc.Col([

            #  Area of management buttons
            dbc.Row( btn_settings, className='widget_cell_grid' ),
            dbc.Row( btn_update_data, className='widget_cell_grid' ),

            #  Area of filters
        ] + create_filters(data_filter)

        , style={'backgroundColor': 'GhostWhite'}, width=2),

        #  Column of widgets (main dashboard content)
        dbc.Col([
            dbc.Tabs([
            dbc.Tab([
                tab_1,
                ], label='Основные показатели'),
            dbc.Tab([
                tab_2,
                ], label='Динамика')
            ]),
        ], style={'backgroundColor': 'GhostWhite', 'padding': '0', 'border': 'None'}, width=10),
     
    #  INTERVAL 
    dcc.Interval(
            id='interval_component',
            n_intervals=0)

    ], style={'margin': '2px'})
])


# ************************ UPDATE WIDGETS FUNCTIONS ***********************
def update_label_cnt_users(df, filter_values_list, n):
    #
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    return df[
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]['id'].count()


def update_label_workload(df, filter_values_list, n):
    # 
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    return f"""{((df[
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]['id'].count()/30)*100).round()}"""[:-2] + "%"


def update_label_cnt_countries(df, filter_values_list, n):
    #
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    return len(df[
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]['country'].unique())


def update_pie_device(df, filter_values_list, n):
    #
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    df_pie = df[ 
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]
    figure = px.pie(df_pie, values='cnt', names='device', title='Устройства пользователей', height=345)
    return figure


def update_bar_country(df, filter_values_list, n):
    #
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    df_bar = df[ 
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]
    figure = px.bar(df_bar, y='country', x='cnt', title='Страны пользователей', height=345)
    return figure


def update_scatter_cnt_users(df, filter_values_list, n):
    #
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    cnt_users = df[
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]['id'].count()
    if len(ay_msg) == 0 or cnt_users != ay_msg[-1]:
        per_dt = str(datetime.now().strftime("%H:%M:%S"))
        ax_msg.append(per_dt)
        ay_msg.append(cnt_users)
        if len(ax_msg) > 9:
            ax_msg.pop(0)
            ay_msg.pop(0)
    figure = px.scatter(title='Кол-во пользователей онлайн', height=300)
    figure.add_traces(list(px.line(x=ax_msg, y=ay_msg, markers=True).select_traces()))
    return figure


def update_table_details(df, filter_values_list, n):
    #
    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    df_table = df[
        (df['web_service'].isin(filter_web_service)) &
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]
    data = df_table[['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']].to_dict('records')
    return data


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
    df = dfl.get_db_data_to_datafame(conn, select, column_names); df['cnt'] = 1

    return (
        update_label_cnt_users(df, filter_values_list, n),
        update_label_workload(df, filter_values_list, n),
        update_label_cnt_countries(df, filter_values_list, n),
        update_pie_device(df, filter_values_list, n),
        update_bar_country(df, filter_values_list, n),
        update_scatter_cnt_users(df, filter_values_list, n),
        update_table_details(df, filter_values_list, n),
        DATA_UPDATE_PERIOD
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
