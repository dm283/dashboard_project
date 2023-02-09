import os, dash_bootstrap_components as dbc

#  ***************************************  ДЕЙСТВИЯ ПРИКЛАДНОГО ПРОГРАММИСТА  ****************************************************
#  Укажите вкладки, которые вы хотите видеть на дашборде (полное наименование соответствующих файлов из директории tabs)
tabs = [
    'tab_Основные_показатели.py',
    'tab_Динамика.py',
    'tab_Производительность.py',
    'tab_Показатели_загрузки.py',
]



#  ***************************************  СИСТЕМНЫЙ КОД  ************************************************************************
#  tabs_list - список файлов с вкладками дашбора
#  tabs_labels_list - список ключей/системных наименований вкладок
#  tab_content - структура данных с контентом вкладок
#  tab_label - наименования вкладок как они отображаются в дашборде
#tabs = os.listdir('widgets/tabs')    # Вариант с автоматической загрузкой всех файлов tab_* из директории widgets/tabs
tabs_list = [t.partition('.')[0] for t in tabs if t.startswith('tab_')]
tabs_labels_list = [t.partition('_')[2].partition('.')[0] for t in tabs if t.startswith('tab_')]
tab_content, tab_label = {}, {}

#  Импортирование модулей из tabs_list и наполнение tab_content, tab_label
for i in range(len(tabs_list)):
    import_name = __import__('widgets.tabs.' + tabs_list[i], fromlist=[tabs_list[i]])
    tab_content[tabs_labels_list[i]] = import_name.tab_content
    #tab_label[tabs_labels_list[i]] = import_name.label # Вариант с указанием наименования вкладка в файле tab_* в переменной label
    tab_label[tabs_labels_list[i]] = tabs_labels_list[i].replace('_', ' ')  # Вариант с наименованием вкладки из имя соответствующего файла

#  Формирование области виджетов дашборда
tabs_area = []
for label in tabs_labels_list:
    tabs_area.append( dbc.Tab(tab_content[label], label=tab_label[label]) )

widgets_area = [dbc.Tabs(tabs_area)]
