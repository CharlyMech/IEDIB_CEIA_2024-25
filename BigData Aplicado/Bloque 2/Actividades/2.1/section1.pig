-- Load all the date from the file
quijote = LOAD 'quijote/quijote.txt' AS (line:chararray);
-- Split lines into words
words = FOREACH quijote GENERATE FLATTEN(TOKENIZE(line)) as word;
-- Filter the words with REGEX
regex = FILTER words BY word MATCHES '^[A-Z].*a$';
-- Count the number of occurrences
group_words = GROUP regex BY word;
count_words = FOREACH group_words GENERATE group as word, COUNT(regex) AS count;
-- Sort results by number of occurrences (desc) and alphabetically (asc)
sort_words = ORDER count_words BY count DESC, word ASC;
-- Dump the results
DUMP sort_words;