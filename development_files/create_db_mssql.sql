-- ************************ MS-SQL ************************
create database dev_db_1;

go

use dev_db_1;

go

create table [web_service_usage](
	[id] [int] IDENTITY(1,1) not null,
	[web_service] [varchar](24) not null,
	[user_id] [bigint] not null,
	[device] [varchar](24) not null,
	[country] [varchar](24) not null,
	[user_status] [varchar](24) not null,
	[sign_date] [datetime] default getdate() not null,
	[signout_date] [datetime] default null,
constraint [pk_web_service_usage] primary key clustered
([id] asc)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) on [primary]

go

-- создает таблицу чатов бота с юзерами и группами
CREATE TABLE [telegram_chats](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[chat_id] [bigint] NOT NULL,
	[entity_name] [varchar](32) NOT NULL,
	[entity_type] [varchar](20) NOT NULL,
	[bot_name] [varchar](32) NOT NULL,
	[update_date] [datetime] DEFAULT GETDATE() NOT NULL,
	[is_active] [bit] DEFAULT 1 NOT NULL,
 CONSTRAINT [pk_telegram_chats] PRIMARY KEY CLUSTERED 
([id] ASC)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

-- создает таблицу telegram-сообщений
CREATE TABLE [telegram_messages](
	[id] [varchar](8) NULL,
	[app] [varchar](4) NULL,
	[forms] [varchar](6) NULL,
	[ids] [varchar](16) NULL,
	[client] [int] NULL,
	[adrto] [varchar](500) NULL,
	[subj] [varchar](100) NULL,
	[msg_text] [varchar](600) NULL,
	[attachmentfiles] [varchar](255) NULL,
	[guid_doc] [varchar](36) NULL,
	[datep] [datetime] NULL,
	[dates] [datetime] NULL,
	[datet] [datetime] NULL,
	[datef] [datetime] NULL,
	[fl] [int] NULL,
	[user_id] [varchar](3) NULL,
	[status] [int] NULL,
	[UniqueIndexField] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [pk_telegram_messages] PRIMARY KEY CLUSTERED 
(
	[UniqueIndexField] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

-- создает таблицу email-сообщений
CREATE TABLE [uemail](
	[id] [varchar](8) NULL,
	[app] [varchar](4) NULL,
	[forms] [varchar](6) NULL,
	[ids] [varchar](16) NULL,
	[client] [int] NULL,
	[adrto] [varchar](500) NULL,
	[subj] [varchar](100) NULL,
	[textemail] [varchar](600) NULL,
	[attachmentfiles] [varchar](255) NULL,
	[guid_doc] [varchar](36) NULL,
	[datep] [datetime] NULL,
	[dates] [datetime] NULL,
	[datet] [datetime] NULL,
	[datef] [datetime] NULL,
	[fl] [int] NULL,
	[user_id] [varchar](3) NULL,
	[status] [int] NULL,
	[UniqueIndexField] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_uemail] PRIMARY KEY CLUSTERED 
(
	[UniqueIndexField] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

-- создает 2-ю таблицу email-сообщений
CREATE TABLE [messages_email](
	[id] [varchar](8) NULL,
	[app] [varchar](4) NULL,
	[forms] [varchar](6) NULL,
	[ids] [varchar](16) NULL,
	[client] [int] NULL,
	[adrto] [varchar](500) NULL,
	[subj] [varchar](100) NULL,
	[textemail] [varchar](600) NULL,
	[attachmentfiles] [varchar](255) NULL,
	[guid_doc] [varchar](36) NULL,
	[datep] [datetime] NULL,
	[dates] [datetime] NULL,
	[datet] [datetime] NULL,
	[datef] [datetime] NULL,
	[fl] [int] NULL,
	[user_id] [varchar](3) NULL,
	[status] [int] NULL,
	[UniqueIndexField] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_messages_email] PRIMARY KEY CLUSTERED 
(
	[UniqueIndexField] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO



-- INSERT DATA
INSERT INTO telegram_chats(chat_id, entity_name, entity_type, bot_name, update_date, is_active)
	VALUES 
	(123, 'user1', 'user', 'bot1', '2022-12-14', 1),
	(234, 'test-group', 'group', 'bot1', '2022-12-14', 1),
	(345, 'user-admin', 'administrator', 'bot1', '2022-12-14', 1);


INSERT INTO telegram_messages(adrto, msg_text, attachmentfiles, datep, dates)
	VALUES 
	('test-group', 'test', 'file1.jpg', '2022-12-16', '2022-12-16'),
	('user1', 'test', 'file2.jpg', '2022-12-17', '2022-12-17');


INSERT INTO uemail(adrto, subj, textemail, attachmentfiles, datep, dates)
	VALUES 
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17');


INSERT INTO messages_email(adrto, subj, textemail, attachmentfiles, datep, dates)
	VALUES 
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17'),
	('e1@gmail.com', 'test_msg', 'this is it', 'file1.txt', '2023-03-15', '2023-03-15'),
	('e2@gmail.com', 'test_msg', 'this is it', 'file2.txt', '2023-03-16', '2023-03-16'),
	('e3@gmail.com', 'test_msg', 'this is it', 'file3.txt', '2023-03-17', '2023-03-17');

	