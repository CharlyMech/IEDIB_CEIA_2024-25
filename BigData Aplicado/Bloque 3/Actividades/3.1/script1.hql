CREATE DATABASE soccer;
USE soccer;

-- Create table for results
-- I'll avoid the NOT NULL but should be used
CREATE TABLE soccer.results (
    date DATE,
    home_team STRING,
    away_team STRING,
    home_score INT,
    away_score INT,
    tournament STRING,
    city STRING,
    country STRING,
    neutral BOOLEAN
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Create table for goals
-- Again, avoiding NOT NULL but should be there
CREATE TABLE soccer.goalscorers (
    date STRING,
    home_team STRING,
    away_team STRING,
    team STRING,
    scorer STRING,
    minute INT,
    own_goal BOOLEAN,
    penalty BOOLEAN
)
ROW FORMAT DELIMITED  
FIELDS TERMINATED BY '\t' 
TBLPROPERTIES ("skip.header.line.count"="1");

-- Load data into tables
-- I did use the LOCAL way because I wasn't able to do it with HDFS
LOAD DATA LOCAL INPATH "/home/cloudera/block3/soccer/results.csv" INTO TABLE soccer.results;
LOAD DATA LOCAL INPATH "/home/cloudera/block3/soccer/goalscorers.csv" INTO TABLE soccer.goalscorers;


-- 1 
SELECT COUNT(*)
FROM soccer.goalscorers
WHERE own_goal=FALSE AND scorer = 'Lionel Messi';

-- 2
SELECT * 
FROM soccer.results
WHERE home_team = 'Spain' OR away_team = 'Spain'
ORDER BY date DESC
LIMIT 5;

-- 3
SELECT 
    SUM(CASE WHEN home_team = 'Spain' THEN home_score ELSE 0 END + 
        CASE WHEN away_team = 'Spain' THEN away_score ELSE 0 END)
FROM 
    soccer.results;

-- 4
SELECT scorer, COUNT(*) AS num_goals
FROM soccer.goalscorers
WHERE team = 'Spain' AND own_goal = FALSE
GROUP BY scorer
ORDER BY num_goals DESC
LIMIT 5;

-- 5
SELECT g.scorer
FROM soccer.goalscorers AS g
INNER JOIN soccer.results AS r ON r.date = g.date
WHERE g.penalty=TRUE AND g.team='Spain' AND r.tournament = 'UEFA Euro'
GROUP BY g.scorer
ORDER BY g.scorer DESC;