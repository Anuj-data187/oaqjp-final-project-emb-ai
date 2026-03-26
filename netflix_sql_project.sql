CREATE DATABASE netflix_db;

USE netflix_db;

CREATE TABLE netflix_titles (
    show_id VARCHAR(10),
    type VARCHAR(20),
    title VARCHAR(100),
    director VARCHAR(100),
    country VARCHAR(50),
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(20),
    listed_in VARCHAR(100)
);

INSERT INTO netflix_titles (show_id, type, title, director, country, release_year, rating, duration, listed_in)
VALUES
('s1','Movie','Red Notice','Rawson Marshall Thurber','United States',2021,'PG-13','118 min','Action & Adventure'),
('s2','TV Show','Stranger Things','The Duffer Brothers','United States',2016,'TV-14','4 Seasons','Sci-Fi & Fantasy'),
('s3','Movie','RRR','S. S. Rajamouli','India',2022,'TV-MA','187 min','Action & Adventure'),
('s4','Movie','The Gray Man','Anthony Russo','United States',2022,'PG-13','129 min','Thrillers'),
('s5','TV Show','Sacred Games','Anurag Kashyap','India',2018,'TV-MA','2 Seasons','Crime TV Shows'),
('s6','Movie','Extraction','Sam Hargrave','United States',2020,'R','116 min','Action & Adventure'),
('s7','TV Show','Money Heist','Álex Pina','Spain',2017,'TV-MA','5 Seasons','Crime TV Shows'),
('s8','Movie','Leo','Lokesh Kanagaraj','India',2023,'TV-MA','164 min','Action & Adventure'),
('s9','Movie','Glass Onion','Rian Johnson','United States',2022,'PG-13','139 min','Comedies'),
('s10','TV Show','Wednesday','Tim Burton','United States',2022,'TV-14','1 Season','Teen TV Shows'),
('s11','Movie','Jawan','Atlee','India',2023,'TV-MA','169 min','Action & Adventure'),
('s12','TV Show','Delhi Crime','Richie Mehta','India',2019,'TV-MA','2 Seasons','Crime TV Shows');



SELECT * FROM netflix_titles;


SELECT COUNT(*) AS total_titles
FROM netflix_titles;



SELECT type, COUNT(*) AS total
FROM netflix_titles
GROUP BY type;

SELECT country, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY country
ORDER BY total_titles DESC;

SELECT release_year, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY total_titles DESC;


SELECT listed_in, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY listed_in
ORDER BY total_titles DESC;


SELECT *
FROM netflix_titles
ORDER BY release_year DESC
LIMIT 1;


SELECT rating, COUNT(*) AS total
FROM netflix_titles
GROUP BY rating
ORDER BY total DESC
LIMIT 1;


SELECT *
FROM netflix_titles
WHERE country = 'India';

