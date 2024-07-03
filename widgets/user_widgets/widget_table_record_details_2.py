import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL


id = 'table_record_details_2'
table_name = 'Сообщения e-mail'
widget_update_data_type = 'data'         # тип данных для output - для таблицы всегда data
widget_select_index = 'messages_email'   # id соответствующего select из database_select.py
сolumns_displayed = ['id', 'adrto', 'subj', 'dates']
columns_all = ['id', 'adrto', 'subj', 'dates']

#  Модальное окно с расширенными данными о записи
modal_table_record = dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle(table_name, style={'fontSize': '20px'})),
                    dbc.ModalBody(id='modal_table_record_content_2'),
                    dbc.ModalFooter(html.Div([
                        dbc.Button("Закрыть", id='btn_modal_table_record_close_2', n_clicks=0,
                            style={'width': '120px'}, color="warning" )
                        ]))
                ],
                id='modal_table_record_2',
                is_open=False
            )

#  Модальное окно сохранения данных таблицы
modal_save_table_data = dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Сохранение данных таблицы")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col(dbc.Label("Наименование файла"), width=7),
                            dbc.Col(dbc.Input(id='input_file_name_2', type='text'))
                        ], style={'marginBottom': '5px'}),
                    ]),
                    dbc.ModalFooter(html.Div([
                        dbc.Button("Сохранить", id='btn_modal_save_table_data_save_2', n_clicks=0,
                            style={'width': '120px', 'marginRight': '10px'}, color="success"), 
                        dcc.Download(id="download_dataframe_xlsx_2"),
                        dbc.Button("Закрыть", id='btn_modal_save_table_data_close_2', n_clicks=0,
                            style={'width': '120px'}, color="warning" )
                        ]))
                ],
                id='modal_save_table_data_2',
                is_open=False
            )

#  Виджет "Таблица"
widget = [ modal_table_record,
           modal_save_table_data,
            html.H6([     
                html.Span(html.Img(src='assets/baseline_save_white.png', id='btn_open_modal_save_table_data_2', n_clicks=0,), 
                          className='icon_save_table_data'),
                html.Span(table_name, style={'marginLeft': '210px'}),
                ], style={'color': 'white', 'backgroundColor': 'None', 'marginBottom': '2px', 'textAlign': 'left'}), 
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in сolumns_displayed],
                style_cell = {'font_size': '10px', 'textAlign': 'center'},
                page_action='none',
                style_table={'height': '720px', 'overflowY': 'auto'},
                style_header={'backgroundColor': 'Black', 'color': 'white'},
                style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                id=id
                ),
        ]


def widget_update(df, filter_values_list, n):
    #  Функция обновления данных таблицы
    
    # devices = ['desktop', 'mobile']
    # countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']
    # filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    # filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    # filter_web_service = [filter_values_list[2]] 

    df_table = df

    #  добавляем необходимые фильтры данных
    if filter_values_list[3]:
        df_table = df_table[ df_table['adrto'].isin([filter_values_list[3]]) ]

    data = df_table[columns_all].to_dict('records')
    
    return data
