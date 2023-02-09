#  Формирование шапки дашборда

from dash import html
from datetime import datetime

from widgets.common_widgets import common_widgets

update_date = datetime.now().strftime('%Y-%m-%d %H:%m')
btn_settings = common_widgets.btn_settings  #  Кнопка "Настройки"
btn_update_data = common_widgets.btn_update_data    #  Кнопка "Обносить данные"


header = [
        html.Span('Altasoft', className='header_title', style={'marginLeft': '30px'}),
        html.Span('Dashboard', className='header_title'),
        html.Span('Мониторинг загруженности веб-сервисов', className='header_title', style={'border': 'None', 'width': '66%'}),
        html.Span(update_date, id='update_date', className='update_date'),  # добавить динамическое изменения даты/времени
        html.Span(btn_update_data, className='header_icon', style={'marginLeft': '20px'}), 
        html.Span(btn_settings, className='header_icon', style={'marginLeft': '5px'})
        ]