CREATE DATABASE streaming;
USE streaming;

-- Create the table with partitioning
CREATE TABLE streaming.movies (
    title STRING,
    type STRING,
    genres STRING,
    releaseYear FLOAT,
    imdbId STRING,
    imdbAverageRating FLOAT,
    imdbNumVotes INT,
    availableCountries STRING
)
PARTITIONED BY(platform STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Load the data
LOAD DATA LOCAL INPATH '/home/cloudera/block3/streaming/amazon.csv' INTO TABLE streaming.movies
PARTITION(platform = 'amazon_prime');
LOAD DATA LOCAL INPATH '/home/cloudera/block3/streaming/apple.csv' INTO TABLE streaming.movies
PARTITION(platform = 'apple_tv');
LOAD DATA LOCAL INPATH '/home/cloudera/block3/streaming/hbo.csv' INTO TABLE streaming.movies
PARTITION(platform = 'hbo_max');
LOAD DATA LOCAL INPATH '/home/cloudera/block3/streaming/hulu.csv' INTO TABLE streaming.movies
PARTITION(platform = 'hulu');
LOAD DATA LOCAL INPATH '/home/cloudera/block3/streaming/netflix.csv' INTO TABLE streaming.movies
PARTITION(platform = 'netflix');

-- Just to know all possible type values
SELECT type, COUNT(*)
FROM streaming.movies
GROUP BY type;

-- 1
SELECT platform, COUNT(*) AS movie_count
FROM streaming.movies
WHERE type == 'movie'
GROUP BY platform
ORDER BY movie_count DESC
LIMIT 1;

-- 2
SELECT title, imdbaveragerating, platform
FROM streaming.movies
WHERE type = 'tv'
ORDER BY imdbaveragerating DESC
LIMIT 5;

-- 3
SELECT platform, SUM(imdbNumVotes) AS total_votes
FROM streaming.movies
WHERE genres LIKE '%Science Fiction%' 
   OR genres LIKE '%Sci-Fi%'
   AND type = 'tv'
GROUP BY platform
ORDER BY total_votes DESC;

-- 4
SELECT releaseyear, COUNT(*) AS movie_count
FROM streaming.movies
WHERE type = 'movie'
GROUP BY releaseYear
ORDER BY movie_count DESC
LIMIT 5;