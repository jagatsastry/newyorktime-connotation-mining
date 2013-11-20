 SELECT 1;
 CREATE TABLE all_aggregate 
 SELECT entity, lemma, sum(`count(*)`) count FROM  (
 (SELECT * FROM words_2007 )  UNION ALL 
 (SELECT * FROM words_2006 )  UNION ALL 
 (SELECT * FROM words_2005 )  UNION ALL 
 (SELECT * FROM words_2004 )  UNION ALL 
 (SELECT * FROM words_2003 )  UNION ALL 
 (SELECT * FROM words_2002 )  UNION ALL 
 (SELECT * FROM words_2001 )  UNION ALL 
 (SELECT * FROM words_2000 )  UNION ALL 
 (SELECT * FROM words_1999 )  UNION ALL 
 (SELECT * FROM words_1998 )  UNION ALL 
 (SELECT * FROM words_1997 )  UNION ALL 
 (SELECT * FROM words_1996 )  UNION ALL 
 (SELECT * FROM words_1995 )  UNION ALL 
 (SELECT * FROM words_1994 )  UNION ALL 
 (SELECT * FROM words_1993 )  UNION ALL 
 (SELECT * FROM words_1992 )  UNION ALL 
 (SELECT * FROM words_1991 )  UNION ALL 
 (SELECT * FROM words_1990 )  UNION ALL 
 (SELECT * FROM words_1989 )  UNION ALL 
 (SELECT * FROM words_1988 )  UNION ALL 
 (SELECT * FROM words_1987)  ) v ; 

SELECT 2;
CREATE INDEX all_aggregate_entity  ON all_aggregate(entity);
SELECT 3;
CREATE INDEX all_aggregate_lemma  ON all_aggregate(lemma);
SELECT 4;
CREATE INDEX all_aggregate_count  ON all_aggregate(count);
SELECT 5;
CREATE INDEX all_aggregate_entity_lemma  ON all_aggregate(entity, lemma);
SELECT 6;
