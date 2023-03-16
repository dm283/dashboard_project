# select = """
#       select id, web_service, user_id, device, country, user_status, sign_date, signout_date
#         from dev_pg_1.public.web_service_usage
#         where user_status = 'sign_in'
#         order by sign_date desc
# """
# column_names = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']


select_query, select_columns = {}, {}


select_query[0] = """
      select id, web_service, user_id, device, country, user_status, sign_date, signout_date
        from dev_pg_1.public.web_service_usage
        where user_status = 'sign_in'
        order by sign_date desc
"""
select_columns[0] = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']


select_query[1] = """
      select id, chat_id, entity_name, bot_name, update_date 
        from dev_pg_1.public.telegram_chats
        where is_active
"""
select_columns[1] = ['id', 'chat_id', 'entity_name', 'bot_name', 'update_date']


select_query[2] = """
      select uniqueindexfield, adrto, attachmentfiles, datep, dates 
        from dev_pg_1.public.telegram_messages
"""
select_columns[2] = ['uniqueindexfield', 'adrto', 'attachmentfiles', 'datep', 'dates']


select_query[3] = """
      select uniqueindexfield, adrto, attachmentfiles, datep, dates 
        from dev_pg_1.public.uemail
"""
select_columns[3] = ['uniqueindexfield', 'adrto', 'attachmentfiles', 'datep', 'dates']


select_query[4] = """
  select count(uniqueindexfield) as msg_cnt, 'email' as channel
    from dev_pg_1.public.uemail
  union all
  select count(uniqueindexfield) as cnt, 'telegram' as channel
    from dev_pg_1.public.telegram_messages
"""
select_columns[4] = ['msg_cnt', 'channel']


select_query[5] = """
  select entity_type, count(id) as chat_cnt
    from telegram_chats
    group by entity_type
"""
select_columns[5] = ['entity_type', 'chat_cnt']
