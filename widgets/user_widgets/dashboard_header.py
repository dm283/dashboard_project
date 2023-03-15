#  Формирование шапки дашборда

from dash import html

from widgets.common_widgets import common_widgets

btn_settings = common_widgets.btn_settings              #  Кнопка "Настройки"
btn_update_data = common_widgets.btn_update_data        #  Кнопка "Обновить данные"
btn_user_actions = common_widgets.btn_user_actions      #  Кнопка "Разлогиниться"
btn_show_filters = common_widgets.btn_show_filters      #  Кнопка "Показать область фильтров"


header = [
        html.Span('Altasoft', className='header_title', style={'marginLeft': '30px'}),
        html.Span('Dashboard', className='header_title'),
        html.Span('Мониторинг загруженности веб-сервисов', className='header_title', style={'border': 'None', 'width': '62%'}),
        html.Span(id='update_date', className='update_date'),
        html.Span(btn_update_data, className='header_icon', style={'marginLeft': '20px'}), 
        html.Span(btn_settings, className='header_icon', style={'marginLeft': '5px'}),
        html.Span(btn_user_actions, className='header_icon', style={'marginLeft': '5px'}),
        # html.Span(btn_show_filters, className='header_icon', style={'marginLeft': '5px'}),
        ]
