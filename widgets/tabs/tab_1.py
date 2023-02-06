import dash_bootstrap_components as dbc
from dash import html

label='Основные показатели'

widget = {}

from widgets.user_widgets import (widget_graph_bar_countries, widget_graph_pie_devices, widget_graph_scatter_cnt_users, widget_label_cnt_countries,
    widget_label_cnt_users, widget_label_workload, widget_table_record_details)

widget[0] = widget_label_cnt_users.widget
widget[1] = widget_label_workload.widget
widget[2] = widget_label_cnt_countries.widget
widget[3] = widget_graph_pie_devices.widget
widget[4] = widget_graph_bar_countries.widget
widget[5] = widget_graph_scatter_cnt_users.widget
widget[6] = widget_table_record_details.widget


tab_content = dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    html.Div(
                        widget[0],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
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
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        widget[3],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=6),
                dbc.Col(
                    html.Div(
                        widget[4],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=6),
            ]
            ),

            dbc.Row(
                dbc.Col(
                    html.Div(
                        widget[5],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=12),
            ),
        
        ], style={'backgroundColor': 'Gainsboro'}, width=7),


        dbc.Col(
            html.Div(
                widget[6],
                className='widget_cell_grid_div_table'),
            className='widget_cell_grid', style={'backgroundColor': 'Gray'}, width=5),

    ], style={'margin': '2px 0px 2px 0px'})
