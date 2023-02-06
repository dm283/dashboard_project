import dash_bootstrap_components as dbc
from dash import html

label='Динамика'

widget = {}

from widgets.user_widgets import (widget_graph_bar_countries, widget_graph_pie_devices, widget_graph_scatter_cnt_users, widget_label_cnt_countries,
    widget_label_cnt_users, widget_label_workload, widget_table_record_details)


tab_content = dbc.Row([
    'TAB 2 CONTENT'
    ], style={'margin': '2px 0px 2px 0px'})
