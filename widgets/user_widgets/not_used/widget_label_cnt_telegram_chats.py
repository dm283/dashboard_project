from dash import dcc, html


id='label_cnt_users'
widget = [ html.H1(style={'color': 'DarkBlue'}, id=id), html.H6('Кол-во пользователей') ]

widget_update_data_type = 'children'

def widget_update(df, filter_values_list, n):
    #
    devices = ['desktop', 'mobile']
    countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']

    filter_device = devices if filter_values_list[0] == None else [filter_values_list[0]]
    filter_country = countries if filter_values_list[1] == None else [filter_values_list[1]]
    filter_web_service = [filter_values_list[2]] 

    return df[
        (df['web_service'].isin(filter_web_service)) & 
        (df['device'].isin(filter_device)) & 
        (df['country'].isin(filter_country))
        ]['id'].count()
        