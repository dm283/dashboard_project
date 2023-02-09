from dash import dcc, html

# FILTERS
data_filter = {}
# filter 1
data_filter[0] = [html.Div('Тип устройства пользователя', className='filter_label'),
                dcc.Dropdown(
                    options=['desktop', 'mobile'], 
                    value=None, 
                    placeholder="Выберите тип устройства", 
                    clearable=True,
                    className='filter_dropdown', 
                    id={'type': 'filter_dropdown', 'index': 'filter_device'},
                    )]
# filter 2
data_filter[1] = [html.Div('Страна пользователя', className='filter_label'),
                dcc.Dropdown(
                    options=['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada'], 
                    value=None, 
                    placeholder="Выберите страну", 
                    clearable=True,
                    className='filter_dropdown', 
                    id={'type': 'filter_dropdown', 'index': 'filter_country'},
                    )]
# filter 3
data_filter[2] = [html.Div('Веб-сервис', className='filter_label'),
                dcc.Dropdown(
                    options=['aDashboard', 'aMessenger'], 
                    value='aDashboard', 
                    placeholder="Выберите веб-сервис", 
                    clearable=False,
                    className='filter_dropdown', 
                    id={'type': 'filter_dropdown', 'index': 'filter_web_service'},
                    )]

# # filter 4
# data_filter[3] = ['Веб-сервис',
#                 dcc.Dropdown(
#                     options=['aDashboard', 'aMessenger'], 
#                     value='aDashboard', 
#                     placeholder="Выберите веб-сервис", 
#                     clearable=False,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_web_service1'}
#                     )]
# # filter 5
# data_filter[4] = ['Веб-сервис',
#                 dcc.Dropdown(
#                     options=['aDashboard', 'aMessenger'], 
#                     value='aDashboard', 
#                     placeholder="Выберите веб-сервис", 
#                     clearable=False,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_web_service2'}
#                     )]
# # filter 6
# data_filter[5] = ['Веб-сервис',
#                 dcc.Dropdown(
#                     options=['aDashboard', 'aMessenger'], 
#                     value='aDashboard', 
#                     placeholder="Выберите веб-сервис", 
#                     clearable=False,
#                     className='filter_dropdown', 
#                     id={'type': 'filter_dropdown', 'index': 'filter_web_service3'}
#                     )]