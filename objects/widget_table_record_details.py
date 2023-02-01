import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL

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
widget = [ modal_table_record,
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
