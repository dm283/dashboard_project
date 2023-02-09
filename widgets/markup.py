import dash_bootstrap_components as dbc

from widgets.tabs import tab_1, tab_2, tab_3, tab_4

tab_content_1 = tab_1.tab_content
tab_content_2 = tab_2.tab_content
tab_content_3 = tab_3.tab_content
tab_content_4 = tab_4.tab_content

tab_label_1 = tab_1.label
tab_label_2 = tab_2.label
tab_label_3 = tab_3.label
tab_label_4 = tab_4.label

#  Формирование области виджетов дашборда
widgets_area = [
            dbc.Tabs([
            dbc.Tab([
                tab_content_1,
                ], label=tab_label_1),
            dbc.Tab([
                tab_content_2,
                ], label=tab_label_2),
            dbc.Tab([
                tab_content_4,
                ], label=tab_label_3),
            dbc.Tab([
                tab_content_4,
                ], label=tab_label_4)
            ]),
        ]
