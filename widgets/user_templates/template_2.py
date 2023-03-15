import os, dash_bootstrap_components as dbc
from dash import html


def create_template(
        widget_1_1, 
        widget_1_2, 
        widget_1_3, 
        ):
    """
    Создает макет дашборда (сетку)
    """

    template = [
        dbc.Col(
            html.Div(
                widget_1_1,
                className='widget_cell_grid_div_label'),
            className='widget_cell_grid', width=2),
        dbc.Col(
            html.Div(
                widget_1_2,
                className='widget_cell_grid_div_label'),
            className='widget_cell_grid', width=2),
        dbc.Col(
            html.Div(
                widget_1_3,
                className='widget_cell_grid_div_label'),
            className='widget_cell_grid', width=2),
    ]

    # template = [
    #     dbc.Col([
    #         dbc.Row([
    #             dbc.Col(
    #                 html.Div(
    #                     widget_1_1_1,
    #                     className='widget_cell_grid_div_label'),
    #                 className='widget_cell_grid', width=4),
    #             dbc.Col(
    #                 html.Div(
    #                     widget_1_1_2,
    #                     className='widget_cell_grid_div_label'),
    #                 className='widget_cell_grid', width=4),
    #             dbc.Col(
    #                 html.Div(
    #                     widget_1_1_3,
    #                     className='widget_cell_grid_div_label'),
    #                 className='widget_cell_grid', width=4),
    #         ]),

    #         dbc.Row([
    #             dbc.Col(
    #                 html.Div(
    #                     widget_1_2_1,
    #                     className='widget_cell_grid_div_graph'),
    #                 className='widget_cell_grid', width=6),
    #             dbc.Col(
    #                 html.Div(
    #                     widget_1_2_2,
    #                     className='widget_cell_grid_div_graph'),
    #                 className='widget_cell_grid', width=6),
    #         ]
    #         ),

    #         dbc.Row(
    #             dbc.Col(
    #                 html.Div(
    #                     widget_1_3_1,
    #                     className='widget_cell_grid_div_graph'),
    #                 className='widget_cell_grid', width=12),
    #         ),
        
    #     ], style={'backgroundColor': 'Gainsboro'}, width=7),


    #     dbc.Col(
    #         html.Div(
    #             widget_2_1,
    #             className='widget_cell_grid_div_table'),
    #         className='widget_cell_grid', style={'backgroundColor': 'Gray'}, width=5),

    # ]


    return dbc.Row(template, style={'margin': '2px 0px 2px 0px'})
