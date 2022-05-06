
-- Delete the tables if they already exist
DROP TABLE myinput;
DROP TABLE wordcount;
CREATE TABLE myinput (line STRING);


LOAD DATA INPATH 'gs://hive-bucket2020/adventures.txt' INTO TABLE myinput;

-- Create a table with the words cleaned and counted.
-- The Java regex removes all punctuation and control characters.
CREATE TABLE wordcount AS
SELECT word, count(1) AS count 
FROM (SELECT EXPLODE(SPLIT(LCASE(REGEXP_REPLACE(line,'[\\p{Punct},\\p{Cntrl}]','')),' '))
AS word FROM myinput) words
GROUP BY word
-- Sort the output by count with the highest counts first
ORDER BY count DESC, word ASC;

-- Make the output look like the output of the Pig DUMP function 
-- so that we can diff this output with the Pig wordcount output
SELECT CONCAT_WS(',', CONCAT("\(",word), CONCAT(count,"\)")) FROM wordcount;