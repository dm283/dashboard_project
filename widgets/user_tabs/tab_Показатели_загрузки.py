import os, dash_bootstrap_components as dbc
from dash import html
from content_create_functions import create_widget_dictionary

widget = create_widget_dictionary()[0]


#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите наименование вкладки
# label='Показатели загрузки'

#  Формирование контента вкладки дашборда  -  сформируйте разметку ячеек дашборда и поместите в ячейку соответствующий виджет
tab_content = dbc.Row([
    'TAB 4 CONTENT'
    ], style={'margin': '2px 0px 2px 0px'})
