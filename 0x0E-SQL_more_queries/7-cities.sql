/* script that creates the database hbtn_0d_usa and the table cities
(in the database hbtn_0d_usa) on your MySQL server. */

-- create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    PRIMARY KEY (id),
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
)
