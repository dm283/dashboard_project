-- ************************ POSTGRESQL *********************************
create database dev_pg_1;


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


CREATE TABLE IF NOT EXISTS dev_pg_1.public.telegram_chats
(
    id serial primary key,
    chat_id bigint NOT NULL,
    entity_name character varying(32),
    entity_type character varying(20),
    bot_name character varying(32),
    update_date timestamp without time zone NOT NULL DEFAULT now(),
    is_active boolean NOT NULL DEFAULT true
)


CREATE TABLE IF NOT EXISTS dev_pg_1.public.telegram_messages
(
    id character varying(8),
    app character varying(4),
    forms character varying(6),
    ids character varying(16),
    client integer,
    adrto character varying(500),
    subj character varying(100),
    msg_text character varying(600),
    attachmentfiles character varying(255),
    guid_doc character varying(36),
    datep timestamp without time zone,
    dates timestamp without time zone,
    datet timestamp without time zone,
    datef timestamp without time zone,
    fl integer,
    user_id character varying(3),
    status integer,
    uniqueindexfield serial primary key
)


CREATE TABLE IF NOT EXISTS dev_pg_1.public.uemail
(
    id character varying(8),
    app character varying(4),
    forms character varying(6),
    ids character varying(16),
    client integer,
    adrto character varying(500),
    subj character varying(100),
    textemail character varying(600),
    attachmentfiles character varying(255),
    guid_doc character varying(36),
    datep timestamp without time zone,
    dates timestamp without time zone,
    datet timestamp without time zone,
    datef timestamp without time zone,
    fl integer,
    user_id character varying(3),
    status integer,
    uniqueindexfield serial primary key
)


CREATE TABLE IF NOT EXISTS dev_pg_1.public.messages_email
(
    id serial primary key,
    app character varying(4),
    forms character varying(6),
    ids character varying(16),
    client integer,
    adrto character varying(500),
    subj character varying(100),
    textemail character varying(600),
    attachmentfiles character varying(255),
    guid_doc character varying(36),
    datep timestamp without time zone,
    dates timestamp without time zone,
    datet timestamp without time zone,
    datef timestamp without time zone,
    fl integer,
    user_id character varying(3),
    status integer
)



-- INSERT DATA
INSERT INTO telegram_chats(chat_id, entity_name, entity_type, bot_name, update_date, is_active)
	VALUES 
	(123, 'user1', 'user', 'bot1', '2022-12-14', True),
	(234, 'test-group', 'group', 'bot1', '2022-12-14', True),
	(345, 'user-admin', 'administrator', 'bot1', '2022-12-14', True);


INSERT INTO telegram_messages(adrto, msg_text, attachmentfiles, datep, dates)
	VALUES 
	('test-group', 'test', 'file1.jpg', '2022-12-16', '2022-12-16'),
	('user1', 'test', 'file2.jpg', '2022-12-17', '2022-12-17');


INSERT INTO uemail(adrto, subj, textemail, attachmentfiles, datep, dates)
	VALUES 
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17');


INSERT INTO messages_email(id, adrto, subj, textemail, attachmentfiles, datep, dates)
	VALUES 
	(1, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(2, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(3, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(4, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(5, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(6, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(7, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(8, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(9, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(10, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(11, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(12, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(13, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(14, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(15, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(16, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(17, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(18, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(19, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(20, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(21, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	(22, 'e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	(23, 'e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	(24, 'e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17');


INSERT INTO web_service_usage(web_service, user_id, device, country, user_status, sign_date)
	VALUES 
	('aMessenger', 18, 'desktop', 'Australia', 'sign_in', '2023-12-11'),
	('aDashboard', 19, 'desktop', 'India', 'sign_in', '2023-12-11'),
	('aDashboard', 20, 'mobile', 'Russia', 'sign_in', '2023-12-11'),
	('aMessenger', 21, 'mobile', 'Canada', 'sign_in', '2023-12-11'),
	('aMessenger', 22, 'desktop', 'Japan', 'sign_in', '2023-12-11');


-- select * from dev_pg_1.public.web_service_usage
-- where user_status = 'sign_in'
-- order by web_service, device

--delete from dev_pg_1.public.web_service_usage

