#  Общие виджеты для всех типовых дашбордов

import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL

DATA_UPDATE_PERIOD = 10000

#  Кнопка НАСТРОЙКИ с модальным окном
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

#  Кнопка ОБНОВИТЬ ДАННЫЕ
btn_update_data = dbc.Button(
                            "Обновить данные", id='btn_update_data', className="ms-auto", n_clicks=0, 
                                style={'width': '100%', 'backgroundColor': 'LightSalmon', 'border': 'None'}
                        )
