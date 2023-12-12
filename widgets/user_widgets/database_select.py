import sys, os, configparser
from pathlib import Path

config = configparser.ConfigParser()
config_file = os.path.join(Path(__file__).resolve().parent.parent.parent, 'config.ini')   
if os.path.exists(config_file):
  config.read(config_file, encoding='utf-8')
else:
  print("error! config file doesn't exist"); sys.exit()

DB_NAME = config['db']['db_name']
DB_SCHEMA = config['db']['db_schema']

select_query, select_columns = {}, {}


s1 = 'web_service_usage'
select_query[s1] = f"""
      select id, web_service, user_id, device, country, user_status, sign_date, signout_date
        from {DB_NAME}.{DB_SCHEMA}.web_service_usage
        where user_status = 'sign_in'
        order by sign_date desc
"""
select_columns[s1] = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']


s2 = 'telegram_chats'
select_query[s2] = f"""
      select id, chat_id, entity_name, bot_name, update_date 
        from {DB_NAME}.{DB_SCHEMA}.telegram_chats
        where is_active = 1
"""
select_columns[s2] = ['id', 'chat_id', 'entity_name', 'bot_name', 'update_date']


s3 = 'telegram_messages'
select_query[s3] = f"""
      select uniqueindexfield, adrto, attachmentfiles, datep, dates 
        from {DB_NAME}.{DB_SCHEMA}.telegram_messages
"""
select_columns[s3] = ['uniqueindexfield', 'adrto', 'attachmentfiles', 'datep', 'dates']


s4 = 'email_messages'
select_query[s4] = f"""
      select uniqueindexfield, adrto, attachmentfiles, datep, dates 
        from {DB_NAME}.{DB_SCHEMA}.uemail
"""
select_columns[s4] = ['uniqueindexfield', 'adrto', 'attachmentfiles', 'datep', 'dates']


s5 = 'count_messages'
select_query[s5] = f"""
  select count(uniqueindexfield) as msg_cnt, 'email' as channel
    from {DB_NAME}.{DB_SCHEMA}.uemail
  union all
  select count(uniqueindexfield) as cnt, 'telegram' as channel
    from {DB_NAME}.{DB_SCHEMA}.telegram_messages
"""
select_columns[s5] = ['msg_cnt', 'channel']


s6 = 'count_telegram_chats_types'
select_query[s6] = f"""
  select entity_type, count(id) as chat_cnt
    from {DB_NAME}.{DB_SCHEMA}.telegram_chats
    group by entity_type
"""
select_columns[s6] = ['entity_type', 'chat_cnt']


s7 = 'messages_email'
select_query[s7] = f"""
  select id, adrto, subj, textemail, attachmentfiles, datep, dates from {DB_NAME}.{DB_SCHEMA}.messages_email
"""
select_columns[s7] = ['id', 'adrto', 'subj', 'textemail', 'attachmentfiles', 'datep', 'dates']
