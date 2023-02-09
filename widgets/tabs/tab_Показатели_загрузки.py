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
# label='Показатели загрузки'

#  Формирование контента вкладки дашборда  -  сформируйте разметку ячеек дашборда и поместите в ячейку соответствующий виджет
tab_content = dbc.Row([
    'TAB 4 CONTENT'
    ], style={'margin': '2px 0px 2px 0px'})
