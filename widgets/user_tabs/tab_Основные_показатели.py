import os, dash_bootstrap_components as dbc
from dash import html
from content_create_functions import create_widget_dictionary

widget = create_widget_dictionary()[0]

#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите наименование вкладки
# label='Основные показатели'

#  Формирование контента вкладки дашборда  -  сформируйте разметку ячеек дашборда и поместите в ячейку соответствующий виджет
tab_content = dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    html.Div(
                        widget['label_cnt_users'],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
                dbc.Col(
                    html.Div(
                        widget['label_workload'],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
                dbc.Col(
                    html.Div(
                        widget['label_cnt_countries'],
                        className='widget_cell_grid_div_label'),
                    className='widget_cell_grid', width=4),
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(
                        widget['graph_pie_devices'],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=6),
                dbc.Col(
                    html.Div(
                        widget['graph_bar_countries'],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=6),
            ]
            ),

            dbc.Row(
                dbc.Col(
                    html.Div(
                        widget['graph_scatter_cnt_users'],
                        className='widget_cell_grid_div_graph'),
                    className='widget_cell_grid', width=12),
            ),
        
        ], style={'backgroundColor': 'Gainsboro'}, width=7),


        dbc.Col(
            html.Div(
                widget['table_record_details'],
                className='widget_cell_grid_div_table'),
            className='widget_cell_grid', style={'backgroundColor': 'Gray'}, width=5),

    ], style={'margin': '2px 0px 2px 0px'})
