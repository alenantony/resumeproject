DELETE FROM projects_roles;
DELETE FROM projects_keywords;
DELETE FROM project_highlights;
DELETE FROM projects;
DELETE FROM REFERENCE;
DELETE FROM interests_keywords;
DELETE FROM interests;
DELETE FROM languages;
delete from skills_keywords;
delete from skills;
delete from publications;
delete from awards;
DELETE from education_courses;
DELETE from education;
delete from volunteer_highlights;
delete from volunteer;
delete from work_highlights;
delete from work;
delete from profiles;
delete from basics;



select * from basics;
SELECT * from profiles;
select * from work;
select * from work_highlights;
select * from volunteer;
select * from volunteer_highlights;
select * from education;
SELECT * FROM education_courses;
select * from awards;
select * from publications;
select * from skills;
select * from skills_keywords;
select * from languages;
select * from interests;
SELECT * FROM interests_keywords;
SELECT * FROM REFERENCE;
SELECT * FROM projects;
SELECT * FROM project_highlights;
SELECT * FROM projects_keywords;
SELECT * FROM projects_roles;





-- delete from basics;



-- delete from profiles;

-- select * from profiles;

-- delete from work;

-- SELECT * FROM  work;

-- delete from work_highlights;

-- SELECT * FROM work_highlights;


-- CREATE TABLE work_highlights(
--     workno INT,
--     id INT,
--     highlightsno INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     highlights TEXT,
--     FOREIGN KEY (workno) REFERENCES work(workno)
-- );

CREATE TABLE REFERENCE(
    referenceno INT AUTO_INCREMENT PRIMARY KEY,
    id INT,
    name TEXT,
    reference TEXT,
    FOREIGN KEY (id) REFERENCES basics(id)
);

-- CREATE TABLE work_highlights(
--     workno INT,
--     highlightsno INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     highlights TEXT,
--     FOREIGN KEY (workno) REFERENCES work(workno)
-- );


-- ALTER TABLE volunteer_highlights 
-- RENAME COLUMN highglightsno TO highlightsno;


-- ALTER TABLE project_highlights 
-- RENAME COLUMN highglightsno TO highlightsno;

ALTER TABLE work_keywords
RENAME COLUMN keywordssno TO keywordsno;

SELECT @j := json_object(
    'id', id, 
    'coverLetter', coverLetter
    )
FROM basics
WHERE id = 920;

SELECT @j;

Select json_array('id', id) FROM basics where id = 920;
select json_object('id',id,'name', name) from basics where id = 920 union select json_object('language', language, 'fluency', fluency) from languages where id = 920;
SELECT json_arrayagg(json_object(
    'id', id,
    'coverLetter', coverLetter
))
FROM basics;

SELECT 
    CONCAT("[",
        CONCAT("{id:'",id,"',"),
        CONCAT("coverletter:{coverLetter:'",coverLetter,"'}")
    ,"]")
as value FROM basics where id = 920;

SELECT
    CONCAT(
        CONCAT("["
            " { 'id' : ", id, 
            ", 'coverLetter' : '", coverLetter 
        ),
        CONCAT(
            "', 'basics' : { 'location' : '",address,"' } ]"
        ) 
    )
FROM basics where id = 920;

SELECT highlights from work_highlights where workno = 920;

SELECT work_highlights.highlights
FROM work
LEFT JOIN work_highlights
ON work.workno = work_highlights.workno
where work.id = 920;