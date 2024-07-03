import os, dash_bootstrap_components as dbc
from dash import html
from content_create_functions import create_widget_dictionary


widget = create_widget_dictionary()[0]

#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите наименование вкладки
# label='Основные показатели'

#  Импортируйте необходимый модуль с макетом вкладки дашборда (макеты находятся в директории user_templates)
from widgets.user_templates import template_1

#  Поместите в ячейку соответствующий виджет
tab_content = template_1.create_template(
    widget_1_1_1=widget['label_cnt_users'], 
    widget_1_1_2=widget['label_workload'],
    widget_1_1_3=widget['label_cnt_countries'],
    widget_1_2_1=widget['graph_pie_devices'],
    widget_1_2_2=widget['graph_bar_countries'],
    widget_1_3_1=widget['graph_scatter_cnt_users'],
    widget_2_1=widget['table_record_details_1']
    )
