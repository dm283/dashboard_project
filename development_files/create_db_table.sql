create table if not exists dev_pg_1.public.web_service_usage(
	id serial primary key,
	web_service varchar(24) not null,
	user_id int not null,
	device varchar(24) not null,
	country varchar(24) not null,
	user_status varchar(24) not null,
	sign_date timestamp default now() not null,
	signout_date timestamp default null
)


select * from dev_pg_1.public.web_service_usage
where user_status = 'sign_in'
order by web_service, device

--delete from dev_pg_1.public.web_service_usage