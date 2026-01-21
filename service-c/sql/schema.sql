CREATE DATABASE IF NOT EXISTS WEATHER_DB;
USE WEATHER_DB;

CREATE TABLE IF NOT EXISTS records_weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    location_name VARCHAR(100),
    country VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    wind_speed FLOAT,
    humidity INT,
    temperature_category VARCHAR(100),
    wind_category VARCHAR(100)
);