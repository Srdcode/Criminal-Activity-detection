CREATE DATABASE labproject;
SHOW DATABASES;
USE labproject;

CREATE TABLE users (
	username VARCHAR(255),
	password VARCHAR(255)
);

INSERT INTO users 
	(username, password) VALUES
		('satya', 'satya');
        
select * from users;
drop table users;

CREATE TABLE predictions (
	video_location VARCHAR(255),
	predicted_activity VARCHAR(255)
);

INSERT INTO predictions 
	(video_location, predicted_activity) VALUES
		('desktop', 'normal');

select * from predictions;
delete from predictions where predicted_activity = "Fighting"; 