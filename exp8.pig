--top 3 movie ratings
item = LOAD 'u.item' USING PigStorage('|') AS (movie_id:int, movie_title:chararray, release_date:chararray, video_release_date:chararray, imdb_url:chararray, unknown:chararray, action:chararray, adventure:chararray, animation:chararray, childrens:chararray, comedy:chararray, crime:chararray, documentary:chararray, drama:chararray, fantasy:chararray, film_noir:chararray, horror:chararray, musical:chararray, mystery:chararray, romance:chararray, sci_fi:chararray, thriller:chararray, war:chararray, western:chararray);
data = LOAD 'u.data' USING PigStorage('\t') AS (user_id:int, movie_id:int, rating:float, timestamp:int);
joined = JOIN item by movie_id, data by movie_id;
sorted = ORDER joined BY rating DESC;
top3 = LIMIT sorted 3;
dump top3;