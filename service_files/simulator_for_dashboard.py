# simulator for users web services login.

import sys, asyncio, random, aioodbc
from datetime import datetime

DB_TABLE = 'dev_pg_1.public.web_service_usage'
CONNECTION_STRING = 'DSN=PostgreSQL_dev_1'


web_services = ['aMessenger', 'aDashboard']
user_id = int()  #  кол-во юзеров 300 чел
devices = ['desktop', 'mobile']
countries = ['India', 'Russia', 'England', 'US', 'Japan', 'China', 'Australia', 'Canada']
user_statuses = ['sign_in', 'sign_out']

#  основная структура данных, содержащая актуальную информацию о веб-сервисах
service_data = {
    'aMessenger': {
        'users_on_service': 0,      # кол-во юзеров на сервисе
        'signin_users_list': [],        # список user_id залогинившихся юзеров
        'signout_users_list': []         # список user_id разлогинившихся юзеров
    }, 
    'aDashboard': {
        'users_on_service': 0,
        'signin_users_list': [],
        'signout_users_list': []
    }
    }

LIMIT_USERS_ON_WEBSERVICE = 30  # максимальное кол-во юзеров на одном веб-сервисе
EXISTING_USERS_CNT = 100        # кол-во существующих в природе юзеров

cnxn, cursor = aioodbc.connection.Connection, aioodbc.cursor.Cursor


async def service_start():
    """
    Запуск сервисов с нулевым кол-вом юзеров на них (старые данные в таблице с БД при наличии удаляются)
    """
    global cnxn, cursor

    print(f'Старт веб-сервисов {web_services}')
    print('Подключение к базе данных ...', end='')
    try:
        cnxn = await aioodbc.connect(dsn=CONNECTION_STRING, loop=loop)
        cursor = await cnxn.cursor()
        print('OK')
    except Exception as ex:
        print('ОШИБКА', ex)
        return 1
    
    query = f'delete from {DB_TABLE}'
    await cursor.execute(query)
    await cnxn.commit()
    print('Удалена старая информация из базы данных')

    while True:
        await select_action_on_webservice()
        await asyncio.sleep(1)

    await cursor.close()
    await cnxn.close()


async def select_action_on_webservice() -> None:
    """
    Выбирает действия ['sign_in', 'sign_out', 'nothing']
    """
    web_service = random.choice(web_services)
    posible_actions = ['sign_in', 'sign_in', 'sign_out', 'nothing'] if service_data[web_service]['users_on_service'] > 0 else ['sign_in', 'nothing']
    action = random.choice(posible_actions)
    print('web_service: ', web_service, 'action: ', action)

    if action == 'sign_in':
        if service_data[web_service]['users_on_service'] == LIMIT_USERS_ON_WEBSERVICE:
            print(f'web_service {web_service} - вход нового пользователя отклонен - ' + 
                f'превышено максимальное кол-во ({LIMIT_USERS_ON_WEBSERVICE})')
        else:
            await sign_in_action(web_service)

    if action == 'sign_out':
        await sign_out_action(web_service)

    if action == 'nothing':
        pass


async def sign_out_action(web_service: str()) -> None:
    """
    Действие sign_out  -  апдейтит в БД запись с юзером (статус и дата выхода)
    """
    user_id = random.choice(service_data[web_service]['signin_users_list'])
    while user_id in service_data[web_service]['signout_users_list']:
        user_id = random.randint(1, EXISTING_USERS_CNT)  

    query = f"update {DB_TABLE} set user_status = 'sign_out', signout_date = now() where user_id = {user_id}"
    await cursor.execute(query)
    await cnxn.commit()

    dt = str(datetime.now().strftime("%Y-%m-%d"))
    print(f"updated  -  [{web_service}] [{user_id}] [status = 'sign_out'] [signout_date = {dt}]")

    service_data[web_service]['signin_users_list'].remove(user_id)
    service_data[web_service]['signout_users_list'].append(user_id)
    service_data[web_service]['users_on_service'] -= 1


async def sign_in_action(web_service: str()) -> None:
    """
    Действие sign_in  -  добавляет в БД новую запись о зашедшем на сервис юзере
    """
    user_id = random.randint(1, EXISTING_USERS_CNT)
    while user_id in service_data[web_service]['signin_users_list']:
        user_id = random.randint(1, EXISTING_USERS_CNT)    
    device = random.choice(devices)
    country = random.choice(countries)
    user_status = 'sign_in'
    
    query = f"""insert into {DB_TABLE} (web_service, user_id, device, country, user_status) values 
        ('{web_service}', '{user_id}', '{device}', '{country}', '{user_status}')"""
    await cursor.execute(query)
    await cnxn.commit()

    print(f'inserted  -  [{web_service}] [{user_id}] [{device}] [{country}]')

    service_data[web_service]['signin_users_list'].append(user_id)
    if user_id in service_data[web_service]['signout_users_list']:
        service_data[web_service]['signout_users_list'].remove(user_id)
    service_data[web_service]['users_on_service'] += 1


loop = asyncio.get_event_loop()
loop.run_until_complete(service_start())
