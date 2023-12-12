import os, dash_bootstrap_components as dbc
from dash import html


def create_template(
        widget_1_1, 
        widget_1_2, 
        widget_1_3,
        widget_1_4,
        widget_2_1,
        widget_3_1,
        ):
    """
    Создает макет дашборда (сетку)
    """

    template = [
        dbc.Col([
            dbc.Row(
                html.Div(
                    widget_1_1,
                    className='widget_cell_grid_div_label'),
                className='widget_cell_grid'
            ),
            dbc.Row(
                html.Div(
                    widget_1_2,
                    className='widget_cell_grid_div_label'),
                className='widget_cell_grid'
            ),
            dbc.Row(
                html.Div(
                    widget_1_3,
                    className='widget_cell_grid_div_label'),
                className='widget_cell_grid'
            ),
            dbc.Row(
                html.Div(
                    widget_1_4,
                    className='widget_cell_grid_div_table'),
                className='widget_cell_grid'
            ),
        ], style={'backgroundColor': 'Gainsboro'}, width=2),

        dbc.Col([
            dbc.Row(
                html.Div(
                    widget_2_1,
                    className='widget_cell_grid_div_graph'),
                className='widget_cell_grid'
            ),  
        ], style={'backgroundColor': 'Gainsboro'}, width=4),

        dbc.Col([
            dbc.Row(
                html.Div(
                    widget_3_1,
                    className='widget_cell_grid_div_table'),
                className='widget_cell_grid'
            ),  
        ], style={'backgroundColor': 'Gainsboro'}, width=6),
    ]


    return dbc.Row(template, style={'margin': '2px 0px 2px 0px'})
