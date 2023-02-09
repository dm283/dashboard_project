select = """
      select id, web_service, user_id, device, country, user_status, sign_date, signout_date
        from dev_pg_1.public.web_service_usage
        where user_status = 'sign_in'
        order by sign_date desc
"""

column_names = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']
