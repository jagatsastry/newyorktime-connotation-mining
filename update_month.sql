SELECT 1987, curtime();
UPDATE words_1987 w SET w.month = (SELECT m.month FROM month_article_map m WHERE w.article_id = m.article_id);
SELECT 1990, curtime();
UPDATE words_1990 w SET w.month = (SELECT m.month FROM month_article_map m WHERE w.article_id = m.article_id);
