/* script that creates a database and a user. */
-- create user user_0d_2
    CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- grant select previlege to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- create database hbtn_0d_2;
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
