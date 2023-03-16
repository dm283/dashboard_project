import os, dash_bootstrap_components as dbc
from dash import html
from content_create_functions import create_widget_dictionary


widget = create_widget_dictionary()[0]

#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите наименование вкладки
# label='Основные показатели'

#  Импортируйте необходимый модуль с макетом вкладки дашборда (макеты находятся в директории user_templates)
from widgets.user_templates import template_2

#  Поместите в ячейку соответствующий виджет
tab_content = template_2.create_template(
    widget_1_1=widget['label_cnt_emails'],
    widget_1_2=widget['label_cnt_telegrams'],
    widget_1_3=widget['label_cnt_telegram_chats'],
    widget_1_4=widget['table_telegram_chats_types'],
    widget_2_1=widget['graph_pie_msg_chanels'],
    widget_3_1=widget['table_messages_email'],
    )
