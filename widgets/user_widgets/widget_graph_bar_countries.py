from dash import dcc, html
import plotly.express as px, dash_bootstrap_components as dbc


id = 'graph_bar_countries' #'bar_country'
widget = dcc.Graph(id=id)

widget_update_data_type = 'figure'

def widget_update(df, filter_values_list, n):
    #
    devices = ['desktop', 'mobile']
    countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    df_bar = df[ 
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]

    figure = px.bar(df_bar, y='country', x='cnt', title='Страны пользователей', height=335)
    
    return figure
