import os, dash_bootstrap_components as dbc
from dash import html


#  ***************************************  СИСТЕМНЫЙ КОД  ************************************************************************
#  Список файлов с виджетами (widget_*) из директории widgets/user_widgets
widget_list = [w.partition('.')[0] for w in os.listdir('widgets/user_widgets') if w.startswith('widget_')]
#  Объявление структур данных с контентом и id виджетов
widget, widget_id = {}, {}

#  Импортирование модулей из widget_list и наполнение widget, widget_id
for w in widget_list:
    import_name = __import__('widgets.user_widgets.' + w, fromlist=[w])
    widget_key = w.replace('widget_', '')
    widget[widget_key] = import_name.widget
    widget_id[widget_key] = import_name.id



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
