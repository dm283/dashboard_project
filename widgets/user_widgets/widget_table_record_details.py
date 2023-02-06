import plotly.express as px, dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State, dash_table, ALL


id = 'table_details'
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
                    style_table={'height': '657px', 'overflowY': 'auto'},
                    style_header={'backgroundColor': 'Black', 'color': 'white'},
                    style_data={'backgroundColor': 'DarkSlateGray', 'color': 'white'},
                    id=id
                    ),
                 ]


def update_table_details(df, filter_values_list, n):
    #
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
