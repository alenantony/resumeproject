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
delete from work keywords;
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

Select json_array('id', id) FROM basics where id = 1;
select json_object('id',id,'name', name) from basics where id = 1  union select json_object('language', language, 'fluency', fluency) from languages where id = 1;
SELECT json_arrayagg(json_object(
    'id', id,
    'coverLetter', coverLetter
))
FROM basics where id =1;

SELECT 
    CONCAT("[",
        CONCAT("{id:'",id,"',"),
        CONCAT("coverletter:{coverLetter:'",coverLetter,"'}")
    ,"]")
as value FROM basics where id = 1;

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

SELECT json_arrayagg(json_object('highlights',work_highlights.highlights))
FROM work
LEFT JOIN work_highlights
ON work.workno = work_highlights.workno
where work.id = 1;

DROP TABLE work_keywords;


select 
     json_object("id",basics.resume_id,"coverLetter",basics.coverLetter,"basics",json_object("name",basics.name,"label",basics.label,"image",basics.image,"email",basics.email,"phone",basics.phone,"location",json_object("address",basics.address,"postalCode",basics.postalCode,"city",basics.city,"countryCode",basics.countryCode,"region",basics.region),"profiles",(select json_arrayagg(json_object("network", profiles.network, "username", profiles.username, "url", profiles.url)) from profiles where profiles.resume_id = basics.resume_id)),
     "work",(select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics.resume_id = work.resume_id),
     "volunteer",(select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics.resume_id = volunteer.resume_id),
     "education",(select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score)) from education where basics.resume_id = education.resume_id),
     "awards",(select json_arrayagg(json_object("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) from awards where basics.resume_id = awards.resume_id),
     "certificates",(select json_arrayagg(json_object("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) from certificates where basics.resume_id = certificates.resume_id),
     "publications",(select json_arrayagg(json_object("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) from publications where basics.resume_id = publications.resume_id),
     "skills",(select json_arrayagg(json_object("name", skills.name, "level", skills.level, "keywords", skills.keywords)) from skills where basics.resume_id = skills.resume_id),
     "languages",(select json_arrayagg(json_object("language", languages.language, "fluency", languages.fluency)) from languages where basics.resume_id = languages.resume_id),
     "interests",(select json_arrayagg(json_object("name", interests.name, "keywords", interests.keywords)) from interests where basics.resume_id = interests.resume_id),
     "refreneces",(select json_arrayagg(json_object("name", references.name, "refrenece", references.reference)) from `references` where basics.resume_id = `references`.resume_id),
     "projects",(select json_arrayagg(json_object("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) from projects where basics.resume_id = projects.resume_id))
                    from basics left join profiles on basics.resume_id = profiles.resume_id 
                                             inner join work on basics.resume_id = work.resume_id
                                             left join volunteer on basics.resume_id = volunteer.resume_id
                                             left join education on basics.resume_id = education.resume_id
                                             left join awards on basics.resume_id = awards.resume_id
                                             left join certificates on basics.resume_id = awards.resume_id
                                             left join publications on basics.resume_id = publications.resume_id
                                             left join skills on basics.resume_id = publications.resume_id
                                             left join languages on basics.resume_id = languages.resume_id
                                             left join interests on basics.resume_id = interests.resume_id
                                             left join `references` on basics.resume_id = `references`.resume_id
                                             left join projects on basics.resume_id = projects.resume_id group by basics.resume_id;