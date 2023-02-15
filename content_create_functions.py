# БИБЛИОТЕКА ФУНКЦИЙ ФОРМИРОВАНИЯ КОНТЕНТА ДЛЯ DASHBOARD_PROJECT

import os, dash_bootstrap_components as dbc
from dash import Output
from widgets.user_widgets import data_filters
from widgets.user_tabs_list import tabs_list


def create_widget_dictionary():
    """
    Создает структуру данных (словарь) с параметрами виджетов,
    в том числе список Output для callback
    """
    # widget_list  -  Список файлов с виджетами (widget_*) из директории widgets/user_widgets
    # widget_update  -  Набор функций формирования/обновления виджетов
    # widget_update_data_type  -  набор типов данных, возвращаемых функцией формирования/обновления
    
    widget_list = [w.partition('.')[0] for w in os.listdir('widgets/user_widgets') if w.startswith('widget_')]
    widget, widget_id, widget_update, widget_update_data_type, output_list = {}, {}, {}, {}, []

    #  Импортирование модулей из widget_list и наполнение widget, widget_id
    for w in widget_list:
        import_name = __import__('widgets.user_widgets.' + w, fromlist=[w])
        widget_key = w.replace('widget_', '')
        widget[widget_key] = import_name.widget
        widget_id[widget_key] = import_name.id
        
        widget_update[widget_key] = import_name.widget_update
        widget_update_data_type[widget_key] = import_name.widget_update_data_type

        output_list.append( Output(widget_key, widget_update_data_type[widget_key]) )

    return widget, widget_id, widget_update, widget_update_data_type, output_list, widget_list


def create_widgets_area():
    """
    Формирует вкладки (tabs)
    """
    #  tabs_list - список вкладок дашбора
    #  tabs_labels_list - список ключей/системных наименований вкладок (наименование файла вкладки без префикса tab_)
    #  tab_content - структура данных с контентом вкладок
    #  tab_label - наименования вкладок как они отображаются в дашборде (tabs_labels_list без символов '_')

    tabs_labels_list = [ t.partition('_')[2] for t in tabs_list ]
    tab_content, tab_label = {}, {}

    #  Импортирование модулей перечисленных в tabs_list (файлы tab_*.py из директории widget/user_tabs) и наполнение tab_content, tab_label
    for i in range(len(tabs_list)):
        import_name = __import__('widgets.user_tabs.' + tabs_list[i], fromlist=[tabs_list[i]])
        tab_content[tabs_labels_list[i]] = import_name.tab_content
        #tab_label[tabs_labels_list[i]] = import_name.label # Вариант с указанием наименования вкладка в файле tab_* в переменной label
        tab_label[tabs_labels_list[i]] = tabs_labels_list[i].replace('_', ' ')  # Вариант с наименованием вкладки из имени соответствующего файла

    #  Формирование области виджетов дашборда
    tabs_area = []
    for label in tabs_labels_list:
        tabs_area.append( dbc.Tab(tab_content[label], label=tab_label[label]) )

    widgets_area = [dbc.Tabs(tabs_area)]

    return widgets_area


def create_filters_area():
    """
    Формирует область фильтров данных
    """
    data_filter = data_filters.data_filter  # фильтры данных

    filters_area = []
    for k in range(len(data_filter)):
        filters_area.append(
            dbc.Col( data_filter[k],
                    className='widget_cell_grid', 
                    style={'padding': '0px 10px 5px 10px', 'border': 'None'},
                    width=2 )
        )

    return filters_area
