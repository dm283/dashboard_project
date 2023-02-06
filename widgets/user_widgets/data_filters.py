from dash import dcc, html

# FILTERS
data_filter = {}
# filter 1
data_filter[0] = [html.H6('Тип устройства пользователя', className='filter_label'),
                dcc.Dropdown(
                    options=['desktop', 'mobile'], 
                    value=None, 
                    placeholder="Выберите тип устройства", 
                    clearable=True,
                    className='filter_dropdown', 
                    id={'type': 'filter_dropdown', 'index': 'filter_device'}
                    )]
# filter 2
data_filter[1] = [html.H6('Страна пользователя', className='filter_label'),
                dcc.Dropdown(
                    options=['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada'], 
                    value=None, 
                    placeholder="Выберите страну", 
                    clearable=True,
                    className='filter_dropdown', 
                    id={'type': 'filter_dropdown', 'index': 'filter_country'}
                    )]
# filter 3
data_filter[2] = [html.H6('Веб-сервис', className='filter_label'),
                dcc.Dropdown(
                    options=['aDashboard', 'aMessenger'], 
                    value='aDashboard', 
                    placeholder="Выберите веб-сервис", 
                    clearable=False,
                    className='filter_dropdown', 
                    id={'type': 'filter_dropdown', 'index': 'filter_web_service'}
                    )]
