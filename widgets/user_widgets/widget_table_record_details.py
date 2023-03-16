import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL


id = 'table_record_details'
#  Модальное окно с расширенными данными о записи
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

#  Модальное окно сохранения данных таблицы
modal_save_table_data = dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Сохранение данных таблицы")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col(dbc.Label("Наименование файла"), width=7),
                            dbc.Col(dbc.Input(id='input_file_name', type='text'))
                        ], style={'marginBottom': '5px'}),
                    ]),
                    dbc.ModalFooter(html.Div([
                        dbc.Button("Сохранить", id='btn_modal_save_table_data_save', n_clicks=0,
                            style={'width': '120px', 'marginRight': '10px'}, color="success"), 
                        dbc.Button("Закрыть", id='btn_modal_save_table_data_close', n_clicks=0,
                            style={'width': '120px'}, color="warning" )
                        ]))
                ],
                id='modal_save_table_data',
                is_open=False
            )

#  Виджет "Таблица"
widget = [ modal_table_record,
           modal_save_table_data,
            html.H6([     
                html.Span(html.Img(src='assets/baseline_save_white.png', id='btn_open_modal_save_table_data', n_clicks=0,), 
                          className='icon_save_table_data'),
                html.Span('Детализация данных о пользователях онлайн', style={'marginLeft': '110px'}),
                ], style={'color': 'white', 'backgroundColor': 'None', 'marginBottom': '2px', 'textAlign': 'left'}), 
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in ['user_id', 'device', 'country', 'sign_date']],
                style_cell = {'font_size': '10px', 'textAlign': 'center'},
                page_action='none',
                style_table={'height': '720px', 'overflowY': 'auto'},
                style_header={'backgroundColor': 'Black', 'color': 'white'},
                style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                id=id
                ),
        ]

widget_update_data_type = 'data'
widget_select_index = 0


def widget_update(df, filter_values_list, n):
    #  Функция обновления данных таблицы
    
    devices = ['desktop', 'mobile']
    countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

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
