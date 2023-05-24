BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS user (
	id_user	INTEGER,
	link_avatar	TEXT,
	ip_register	TEXT,
	device_name_register	TEXT,
	passwordd	TEXT,
	TimeOnline	TEXT,
	PRIMARY KEY(id_user)
);
CREATE TABLE IF NOT EXISTS mangaFavorite (
	id_like	INTEGER,
	id_user	TEXT,
	datetime_like	TEXT,
	ip_like	INTEGER,
	link_manga_like	INTEGER,
	name_device_like	TEXT,
	CONSTRAINT fk_user_mangaFavorite FOREIGN KEY(id_user) REFERENCES user(id_user),
	PRIMARY KEY(id_like)
);
CREATE TABLE IF NOT EXISTS recent_chapter_readed (
	id_readed	INTEGER,
	link_detail_chapter	TEXT,
	id_user	INTEGER,
	link_detail_manga	TEXT,
	ip_readed	TEXT,
	datetime	INTEGER,
	name_device_readed	TEXT,
	FOREIGN KEY(id_user) REFERENCES user(id_user),
	CONSTRAINT fk_recent_chapter_user PRIMARY KEY(id_readed)
);
CREATE TABLE IF NOT EXISTS comment_chapter (
	id_comment	INTEGER,
	link_chapter	TEXT,
	link_manga	TEXT,
	ip_comment	REAL COLLATE RTRIM,
	device_comment	TEXT,
	id_user	INTEGER,
	noidung_comment	TEXT,
	CONSTRAINT fk_comment_user FOREIGN KEY(id_user) REFERENCES user(id_user),
	PRIMARY KEY(id_comment)
);
CREATE TABLE IF NOT EXISTS comment_user (
	Id_User_Bi_Comment	INTEGER,
	Id_User_Comment	INTEGER,
	idComment_tt	INTEGER,
	NoiDungComment	TEXT,
	link_image_attach	TEXT,
	dateTimeComment	TEXT,
	nameDevice_Comment	TEXT,
	IPComment	TEXT
);

COMMIT;