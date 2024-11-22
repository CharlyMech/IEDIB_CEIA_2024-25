REGISTER /usr/lib/pig/piggybank.jar;

-- Load the data
data = LOAD 'prime/prime.csv' USING org.apache.pig.piggybank.storage.CSVExcelStorage(
  ',', 'NO_MULTILINE', 'UNIX', 'SKIP_INPUT_HEADER' )
 AS (
    url: chararray,
    title: chararray,
    type:chararray,
    genres:chararray,
    releaseYear: int,
    imdbId:chararray,
    imdbAverageRating: float,
    imdbNumVotes: int,
    availableCountries: chararray
);


-- 1 Total number of rows 
group_prime = GROUP prime ALL;
rows_count = FOREACH group_prime GENERATE COUNT(prime);
DUMP rows_count; 
-- OUTPUT: 47167


-- 2 Get the number of shows (series)
series = FILTER prime BY type == 'TV Series';
group_series = GROUP series ALL;
count_series = FOREACH group_series GENERATE COUNT(series);
DUMP count_series;
-- OUTPUT: 8332


-- 3 Show the average IMDB rating from movies that only have comedy as genre
comedies = FILTER prime BY type == 'Movie' AND genres MATCHES '^Comedy$';
avg_imdb = FOREACH (GROUP comedies ALL) GENERATE AVG(comedies.imdbAverageRating);
DUMP avg_imdb;
-- OUTPUT: 5.6117418668386945


-- 4 Show the number of movies available in spanish
esp_movies = FILTER prime BY type == 'Movie' AND availableCountries MATCHES '.*\\bES\\b.*';
count_esp_movies = FOREACH (GROUP esp_movies ALL) GENERATE COUNT(esp_movies);
DUMP count_esp_movies;
-- OUTPUT: 3543


-- 5 Show the total number of IMDB votes fro all sci-fi shows (there might be other genres)
scifi_series = FILTER prime BY type == 'TV Series' AND genres MATCHES '.*\\bSci-Fi\\b.*';
total_votes = FOREACH (GROUP scifi_series ALL) GENERATE SUM(scifi_series.imdbNumVotes);
DUMP total_votes;
-- OUTPUT: 3373251


-- 6 Show the average IMDB rating from movies and shows (separately) from 2024
year_2024 = FILTER prime BY releaseYear == 2024 AND (type == 'TV Series' OR type == 'Movie');
averages_2024 = FOREACH (GROUP year_2024 BY type) GENERATE group AS type, AVG(year_2024.imdbAverageRating);
DUMP averages_2024;
-- OUTPUT: (Movie,5.723170728218265), (TV Series,6.7458823512582216)


-- 7 Show the 10 years in which the most films have been released, ordered from the highest to the lowest number of films
movies = FILTER prime BY type == 'Movie';
movies_by_year = GROUP movies BY releaseYear;
count_movies_by_year = FOREACH movies_by_year GENERATE group AS year, COUNT(movies) AS total;
sort_count = ORDER count_movies_by_year BY total DESC;
DUMP sort_count;
/* OUTPUT: 
(2017,2643)
(2016,2425)
(2018,2358)
(2015,2252)
(2014,2073)
(2013,1931)
(2012,1544)
(2011,1313)
(2010,1146)
(2009,1082)
*/


-- 8 Displays the 5 years with the best average IMDB rating for their drama series (other genres may be present as well), sorted from highest to lowest rating
drama = FILTER prime BY type == 'TV Series' AND genres MATCHES '.*\\bDrama\\b.*';
drama_by_year = GROUP drama BY releaseYear;
avg_rating_by_year = FOREACH drama_by_year GENERATE group AS year, AVG(drama.imdbAverageRating) AS avg_rating;
sorted = ORDER avg_rating_by_year BY avg_rating DESC;
just_5 = LIMIT sorted 5;
DUMP just_5;
/* OUTPUT:
(1963,8.300000190734863)
(1967,8.150000095367432)
(1979,8.019999980926514)
(1972,8.0)
(1969,8.0)
*/


-- 9 Exports to a file the following fields of the 10 series since 2020 (included) with best rating: title, releaseYear, imdbAverageRating and imdbNumVotes
series_since_2020 = FILTER prime BY type == 'TV Series' AND releaseYear >= 2020;
sorted_series = ORDER series_since_2020 BY imdbAverageRating DESC;
just_10 = LIMIT sorted_series 10;
to_be_exported = FOREACH just_10 GENERATE title, releaseYear, imdbAverageRating, imdbNumVotes;
STORE to_be_exported INTO 'top_10_series_since_2020' USING PigStorage(',');
-- OUTPUT:


-- 10 Load the exported file and display the total IMDB votes of all the series it contains
data = LOAD 'top_10_series_since_2020'
        USING PigStorage(',')
        AS (
            	title:chararray,
                releaseYear:int,
                imdbAverageRating:float,
                imdbNumVotes:int
        );

votes = FOREACH (GROUP data ALL) GENERATE SUM(data.imdbNumVotes);
DUMP votes;
-- OUTPUT: 315240
