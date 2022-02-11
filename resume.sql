CREATE DATABASE Resume
    DEFAULT CHARACTER SET = 'utf8mb4';
CREATE TABLE basics(  
    resume_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name text,
    label text,
    image text,
    email text,
    phone text,
    url text,
    summary text,
    address text,
    postalCode text,
    city text,
    countryCode text,
    region text,
    coverLetter text
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE profiles(  
    profile_id int NOT NULL PRIMARY KEY AUTO_INCREMENT ,
    resume_id int NOT NULL,
    network text,
    username text,
    url text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE work(  
    work_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    name text,
    location text,
    description text,
    position text,
    url text,
    startDate text,
    endDate text,
    summary text,
    highlights text,
    keywords text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE volunteer(  
    vol_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    organization text,
    position text,
    url text,
    startDate text,
    endDate text,
    summary text,
    highlights text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE education(  
    education_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    institution text,
    url text,
    area text,
    studyType text,
    startDate text,
    endDate text,
    score text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE education_courses(  
    course_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    education_id int NOT NULL,
    courses text,
    FOREIGN KEY (education_id) REFERENCES education(education_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE awards(  
    awards_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    title text,
    date text,
    awarder text,
    summary text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE certificates(  
    certificate_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int,
    name text,
    date text,
    url text,
    issuer text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE publications(  
    publication_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    name text,
    publisher text,
    releaseDate text,
    url text,
    summary text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE skills(  
    skill_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    name text,
    level text,
    keywords text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE languages(  
    language_id int NOT NULL PRIMARY KEY,
    resume_id int NOT NULL,
    language text,
    fluency text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE interests(  
    interest_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    interests text,
    keywords text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE `references`(  
    reference_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    name text,
    reference text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';
CREATE TABLE projects(  
    project_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    resume_id int NOT NULL,
    name text,
    description text,
    startDate text,
    endDate text,
    url text,
    entity text,
    type text,
    highlights text,
    keywords text,
    roles text,
    FOREIGN KEY (resume_id) REFERENCES basics(resume_id)
) DEFAULT CHARSET UTF8 COMMENT '';


-- ============================================================================
-- ============================================================================
-- ============================================================================
-- ============================================================================
INSERT INTO basics VALUES(
    1, "Richard Hendriks", "Programmer", "https://i.pravatar.cc/150?img=8",
    "richard.hendriks@mail.com", "(912) 555-4321", "http://richardhendricks.example.com",
    "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!",
    "2712 Broadway St", "CA 94115", "San Francisco", "US", "California",
    "Some text"
);
INSERT INTO profiles values(
    1, 1, "Twitter", "neutralthoughts", "https://twitter.com/neutralthoughts"
);
INSERT INTO profiles values(
    2, 1, "SoundCloud", "dandymusicnl","https://soundcloud.example.com/dandymusicnl"
);

insert into education values(3, 3, "university", "fgfsg", "dsffd", "fdsdf", "fdsfd", "frsf", "4");
insert into education_courses values(5,3,"Data Retrieval");
insert into awards values(
    3, 3, "Digital Compression Pioneer Award", "2014-11-01", "Techcrunch", "There is no spoon."
);
insert into certificates values(
    3,3, "Best Performer", "2014-11-01", "www.alen.com", "company"
);
insert into publications values(
    4,1, "Video compression for 3d media part 2", "Hooli", "2015-10-01", "http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)",
    "Innovative middle-out compression algorithm that changes the way we store data. Again!"
);
insert into skills values(
    4,3, "Web Development", "Master","HTML, CSS, Javascript"
);
insert into skills values(
    2,1, "Compression", "Master","Mpeg, MP4, GIF"
);
insert into languages values(
    3,3, "English","Native speaker"
);
insert into interests values(
    3,3, "Wildlife", "Ferrets, Unicorns"
);
insert into `references` values(
    3,3, "Erlich Bachman", "It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company."
);
insert into projects values(
    3,3, "Miss Direction", "A mapping engine that misguides you","2016-08-24","2016-08-24","missdirection.example.com",
    "Smoogle", "application", 
    "Won award at AIHacks 2016,
	Built by all women team of newbie programmers,
	Using modern technologies such as GoogleMaps, Chrome Extension and Javascript",
    "GoogleMaps, Chrome Extension, Javascript",
    "Team lead, Designer"
);

-- -------------------------------------------------------------------------
SELECT JSON_ARRAYAGG(jSON_OBJECT(
    'id',basics.resume_id, 'name', basics.name, 'label', label, 'image', image, 'email', email, 'phone', phone, 'url', basics.url, 'summary', basics.summary,
    'address', address, 'postalCode', postalCode, 'city', city, 'countryCode', countryCode, 'region', region, 'coverLetter', coverLetter,
    'work',jSON_OBJECT('name', work.name)
    ))
FROM basics 
LEFT JOIN work on basics.resume_id = basics.resume_id WHERE basics.resume_id = 1;

SELECT * FROM awards JOIN 
SELECT * FROM basics;

select basics.*, jSON_OBJECT('work', JSON_ARRAYAGG(jSON_OBJECT('name', work.name))) as work
FROM basics
LEFT JOIN work on basics.resume_id = work.resume_id
 WHERE basics.resume_id=1;
 
-- [{"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Pied Piper", "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}, {"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Pied Piper", "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}, {"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Pied Piper", "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}, {"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Pied Piper", "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}]
-- [{"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Richard Hendriks", "work": {"name": "Pied Piper"}, "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}, {"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Richard Hendriks", "work": {"name": "Pied Piper"}, "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}, {"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Richard Hendriks", "work": {"name": "Pied Piper"}, "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}, {"id": 1, "url": "http://richardhendricks.example.com", "city": "San Francisco", "name": "Richard Hendriks", "work": {"name": "Pied Piper"}, "email": "richard.hendriks@mail.com", "image": "\"https://i.pravatar.cc/150?img=8\"", "label": "Programmer", "phone": "(912) 555-4321", "region": "California", "address": "2712 Broadway St", "summary": "Richard hails FROM Tulsa. He has earned degrees FROM the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything FROM quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!", "postalCode": "CA 94115", "countryCode": "US", "coverLetter": "Some text"}]


-- SELECT basics.*, 
--     profiles.*,
--     work.*,
--     volunteer.*,
--     education.*,
--     awards.*,
--     certificates.*,
--     publications.*,
--     skills.*,
--     languages.*,
--     interests.*,
--     `references`.*,
--     projects.*
-- FROM basics 
--     INNER JOIN profiles 
--     INNER JOIN work
--     INNER JOIN volunteer
--     INNER JOIN education
--     INNER JOIN awards
--     INNER JOIN certificates
--     INNER JOIN publications
--     INNER JOIN skills
--     INNER JOIN languages
--     INNER JOIN interests
--     INNER JOIN `references`
--     INNER JOIN projects
--     ON
--         (basics.resume_id = profiles.resume_id) AND 
--         (basics.resume_id = work.resume_id) AND
--         (basics.resume_id = volunteer.resume_id) AND
--         (basics.resume_id = education.resume_id) AND
--         (basics.resume_id = awards.resume_id) AND
--         (basics.resume_id = certificates.resume_id) AND
--         (basics.resume_id = publications.resume_id) AND
--         (basics.resume_id = skills.resume_id) AND
--         (basics.resume_id = languages.resume_id) AND
--         (basics.resume_id = interests.resume_id) AND
--         (basics.resume_id = `references`.resume_id) AND
--         (basics.resume_id = projects.resume_id)
-- WHERE basics.resume_id = 3;

SELECT jSON_OBJECT(
    'id', basics.resume_id,
    'coverLetter', basics.coverLetter,
    'basics', jSON_OBJECT(
        'name', basics.name,
        'label', basics.label,
        'image', basics.image,
        'email', basics.email,
        'phone', basics.phone,
        'url', basics.url,
        'summary', basics.summary,
        'address', basics.address,
        'postalCode', basics.postalCode,
        'city', basics.city,
        'countryCode', basics.countryCode,
        'region', basics.region     
    ),
    'work', JSON_ARRAYAGG(
        jSON_OBJECT(
            'name', work.name,
            'location', work.location,
            'description', work.description,
            'position', work.position,
            'url', work.url,
            'startDate', work.startDate,
            'endDate', work.endDate,
            'summary', work.summary,
            'highlights', work.highlights,
            'keywords', work.keywords
        )
    ),
    'volunteer', JSON_ARRAYAGG(
        jSON_OBJECT(
            'organization', volunteer.organization,
            'position', volunteer.position,
            'url', volunteer.url,
            'startDate', volunteer.startDate,
            'endDate', volunteer.endDate,
            'summary', volunteer.summary,
            'highlights', volunteer.highlights
        )
    ),
    'education', JSON_ARRAYAGG(
        jSON_OBJECT(
            'institution', education.institution,
            'url', education.url,
            'area', education.area,
            'studyType', education.studyType,
            'startDate', education.startDate,
            'endDate', education.endDate,
            'score', education.score
       )
    ),
    'awards', JSON_ARRAYAGG(
        jSON_OBJECT(
            'title', awards.title,
            'date', awards.date,
            'awarder', awards.awarder,
            'summary', awards.summary
        )
    ),
    'certificates', JSON_ARRAYAGG(
        jSON_OBJECT(
            'name', certificates.name,
            'date', certificates.date,
            'url', certificates.url,
            'issuer', certificates.issuer
        )
    ),
    'publications', JSON_ARRAYAGG(
        jSON_OBJECT(
            'name', publications.name,
            'publisher', publications.publisher,
            'releaseDate', publications.releaseDate,
            'url', publications.url,
            'summary', publications.summary
        )
    ),
    'skills', JSON_ARRAYAGG(
        jSON_OBJECT(
            'name', skills.name,
            'level', skills.level,
            'keywords', skills.keywords
        )
    ),
    'languages', JSON_ARRAYAGG(
        jSON_OBJECT(
            'language', languages.language,
            'fluency', languages.fluency
        )
    ),
    'interests', JSON_ARRAYAGG(
        jSON_OBJECT(
            'interests', interests.name,
            'keywords', interests.keywords
        )
    ),
    'references', JSON_ARRAYAGG(
        jSON_OBJECT(
            'name', `references`.name,
            'reference', `references`.reference
        )
    ),
    'projects', JSON_ARRAYAGG(
        jSON_OBJECT(
            'name', projects.name,
            'description', projects.description,
            'startDate', projects.startDate,
            'endDate', projects.endDate,
            'url', projects.url,
            'entity', projects.entity,
            'type', projects.type,
            'highlights', projects.highlights,
            'keywords', projects.keywords,
            'roles', projects.roles
        )
    )
) FROM basics
LEFT JOIN work ON basics.resume_id = work.resume_id
LEFT JOIN volunteer ON basics.resume_id = volunteer.resume_id
LEFT JOIN education ON basics.resume_id = education.resume_id
LEFT JOIN awards ON basics.resume_id = awards.resume_id
LEFT JOIN certificates ON basics.resume_id = certificates.resume_id
LEFT JOIN publications ON basics.resume_id = publications.resume_id
LEFT JOIN skills ON basics.resume_id = skills.resume_id
LEFT JOIN languages ON basics.resume_id = languages.resume_id
LEFT JOIN interests ON basics.resume_id = interests.resume_id
LEFT JOIN `references` ON basics.resume_id = `references`.resume_id
LEFT JOIN projects ON basics.resume_id = projects.resume_id
WHERE basics.resume_id = 1
GROUP BY basics.resume_id;

SELECT jSON_OBJECT( 'id', basics.resume_id, 'coverLetter', basics.coverLetter, 'basics', jSON_OBJECT( 'name', basics.name, 'label', basics.label, 'image', basics.image, 'email', basics.email, 'phone', basics.phone, 'url', basics.url, 'summary', basics.summary, 'address', basics.address, 'postalCode', basics.postalCode, 'city', basics.city, 'countryCode', basics.countryCode, 'region', basics.region ), 'work', JSON_ARRAYAGG( jSON_OBJECT( 'name', work.name, 'location', work.location, 'description', work.description, 'position', work.position, 'url', work.url, 'startDate', work.startDate, 'endDate', work.endDate, 'summary', work.summary, 'highlights', work.highlights, 'keywords', work.keywords ) ), 'volunteer', JSON_ARRAYAGG( jSON_OBJECT( 'organization', volunteer.organization, 'position', volunteer.position, 'url', volunteer.url, 'startDate', volunteer.startDate, 'endDate', volunteer.endDate, 'summary', volunteer.summary, 'highlights', volunteer.highlights ) ), 'education', JSON_ARRAYAGG( jSON_OBJECT( 'institution', education.institution, 'url', education.url, 'area', education.area, 'studyType', education.studyType, 'startDate', education.startDate, 'endDate', education.endDate, 'score', education.score ) ), 'awards', JSON_ARRAYAGG( jSON_OBJECT( 'title', awards.title, 'date', awards.date, 'awarder', awards.awarder, 'summary', awards.summary ) ), 'certificates', JSON_ARRAYAGG( jSON_OBJECT( 'name', certificates.name, 'date', certificates.date, 'url', certificates.url, 'issuer', certificates.issuer ) ), 'publications', JSON_ARRAYAGG( jSON_OBJECT( 'name', publications.name, 'publisher', publications.publisher, 'releaseDate', publications.releaseDate, 'url', publications.url, 'summary', publications.summary ) ), 'skills', JSON_ARRAYAGG( jSON_OBJECT( 'name', skills.name, 'level', skills.level, 'keywords', skills.keywords ) ), 'languages', JSON_ARRAYAGG( jSON_OBJECT( 'language', languages.language, 'fluency', languages.fluency ) ), 'interests', JSON_ARRAYAGG( jSON_OBJECT( 'interests', interests.name, 'keywords', interests.keywords ) ), 'references', JSON_ARRAYAGG( jSON_OBJECT( 'name', `references`.name, 'reference', `references`.reference ) ), 'projects', JSON_ARRAYAGG( jSON_OBJECT( 'name', projects.name, 'description', projects.description, 'startDate', projects.startDate, 'endDate', projects.endDate, 'url', projects.url, 'entity', projects.entity, 'type', projects.type, 'highlights', projects.highlights, 'keywords', projects.keywords, 'roles', projects.roles ) ) ) FROM basics LEFT JOIN work ON basics.resume_id = work.resume_id LEFT JOIN volunteer ON basics.resume_id = volunteer.resume_id LEFT JOIN education ON basics.resume_id = education.resume_id LEFT JOIN awards ON basics.resume_id = awards.resume_id LEFT JOIN certificates ON basics.resume_id = certificates.resume_id LEFT JOIN publications ON basics.resume_id = publications.resume_id LEFT JOIN skills ON basics.resume_id = skills.resume_id LEFT JOIN languages ON basics.resume_id = languages.resume_id LEFT JOIN interests ON basics.resume_id = interests.resume_id LEFT JOIN `references` ON basics.resume_id = `references`.resume_id LEFT JOIN projects ON basics.resume_id = projects.resume_id GROUP BY basics.resume_id;

select jSON_OBJECT('id',basics.resume_id, 
    'work',JSON_ARRAYAGG(jSON_OBJECT('name', work.name, 'location', work.location, 
            'description', work.description, 'position', work.position, 'url', work.url, 
            'startDate', work.startDate, 'endDate', work.endDate, 'summary', work.summary, 
            'highlights', work.highlights, 'keywords', work.keywords)
            ),
    'awards', JSON_ARRAYAGG(jSON_OBJECT(
        'title', awards.title
    )
            )) FROM basics
            LEFT JOIN work ON basics.resume_id = work.resume_id
            LEFT JOIN awards ON basics.resume_id = awards.resume_id WHERE basics.resume_id = 1;

select jSON_OBJECT('id',basics.resume_id, 
    'work', jSON_OBJECT('work_id', work.work_id),
    'awards', jSON_OBJECT('awards_id', awards.awards_id)
    ) 
    FROM basics
        LEFT JOIN work ON basics.resume_id = work.resume_id
        LEFT JOIN awards ON basics.resume_id = awards.resume_id WHERE basics.resume_id = 1;

SELECT jSON_OBJECT('id', basics.resume_id,
    'work', SELECT JSON_ARRAYAGG(
        
            jSON_OBJECT(
                'name', work.name
            ) FROM work WHERE work.resume_id = basics.resume_id
        )
    );
    
SELECT JSON_OBJECT('id', basics.resume_id, 'coverLetter', basics.coverLetter) as id,
    (SELECT JSON_OBJECT('basics',JSON_OBJECT('name',basics.name, 'label',basics.label, 'image',basics.image, 'email',basics.email, 'phone',basics.phone, 'url',basics.url, 'summary',basics.summary, 'location',JSON_OBJECT('address',basics.address, 'postalCode',basics.postalCode, 'city',basics.city, 'countryCode',countryCode, 'region',region)))) as basics,
     (SELECT JSON_OBJECT('profiles',JSON_ARRAYAGG(jSON_OBJECT("network", profiles.network, "username", profiles.username, "url", profiles.url))) FROM profiles WHERE profiles.resume_id = basics.resume_id) as profiles ,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) FROM work WHERE basics.resume_id = work.resume_id) as work,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))FROM volunteer WHERE basics.resume_id = volunteer.resume_id) as volunteer,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score)) FROM education WHERE basics.resume_id = education.resume_id) as education,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) FROM awards WHERE basics.resume_id = awards.resume_id) as awards,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) FROM certificates WHERE basics.resume_id = certificates.resume_id) as certificates,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) FROM publications WHERE basics.resume_id = publications.resume_id) as publications,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", skills.name, "level", skills.level, "keywords", skills.keywords)) FROM skills WHERE basics.resume_id = skills.resume_id) as skills,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("language", languages.language, "fluency", languages.fluency)) FROM languages WHERE basics.resume_id = languages.resume_id) as languages,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", interests.name, "keywords", interests.keywords)) FROM interests WHERE basics.resume_id = interests.resume_id) as interests,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", references.name, "refrenece", references.reference)) FROM `references` WHERE basics.resume_id = `references`.resume_id) as `references`,
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) FROM projects WHERE basics.resume_id = projects.resume_id) as projects
                    FROM basics LEFT JOIN profiles ON basics.resume_id = profiles.resume_id 
                                             INNER JOIN work ON basics.resume_id = work.resume_id
                                             LEFT JOIN volunteer ON basics.resume_id = volunteer.resume_id
                                             LEFT JOIN education ON basics.resume_id = education.resume_id
                                             LEFT JOIN awards ON basics.resume_id = awards.resume_id
                                             LEFT JOIN certificates ON basics.resume_id = awards.resume_id
                                             LEFT JOIN publications ON basics.resume_id = publications.resume_id
                                             LEFT JOIN skills ON basics.resume_id = publications.resume_id
                                             LEFT JOIN languages ON basics.resume_id = languages.resume_id
                                             LEFT JOIN interests ON basics.resume_id = interests.resume_id
                                             LEFT JOIN `references` ON basics.resume_id = `references`.resume_id
                                             LEFT JOIN projects ON basics.resume_id = projects.resume_id WHERE basics.resume_id = 1 GROUP BY basics.resume_id;



SELECT JSON_OBJECT("id", basics.resume_id, "coverLetter",coverLetter) as b,
 (SELECT JSON_OBJECT( 'basics',JSON_OBJECT('name',basics.name, 'label',basics.label, 'image',basics.image, 'email',basics.email, 'phone',basics.phone, 'url',basics.url, 'summary',basics.summary, 'location',JSON_OBJECT('address',basics.address, 'postalCode',basics.postalCode, 'city',basics.city, 'countryCode',countryCode, 'region',region)))) as basics,
     (SELECT JSON_OBJECT('profiles',JSON_ARRAYAGG(jSON_OBJECT("network", profiles.network, "username", profiles.username, "url", profiles.url))) FROM profiles WHERE profiles.resume_id = basics.resume_id) as profiles,
     CONCAT("",
     CONCAT("work:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) FROM work WHERE basics.resume_id = work.resume_id)),
     CONCAT(",volunteer:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))FROM volunteer WHERE basics.resume_id = volunteer.resume_id)),
     CONCAT(",education:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score)) FROM education WHERE basics.resume_id = education.resume_id)),
     CONCAT(",awards:",
     (SELECT JSON_ARRAYAGG(DISTINCT jSON_OBJECT("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) FROM awards WHERE basics.resume_id = awards.resume_id)),
     CONCAT(",certificates:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) FROM certificates WHERE basics.resume_id = certificates.resume_id)),
     CONCAT(",publications:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) FROM publications WHERE basics.resume_id = publications.resume_id)),
     CONCAT(",skills:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", skills.name, "level", skills.level, "keywords", skills.keywords)) FROM skills WHERE basics.resume_id = skills.resume_id)),
     CONCAT(",languages:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("language", languages.language, "fluency", languages.fluency)) FROM languages WHERE basics.resume_id = languages.resume_id)),
     CONCAT(",interests:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", interests.name, "keywords", interests.keywords)) FROM interests WHERE basics.resume_id = interests.resume_id)),
     CONCAT(",references:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", references.name, "refrenece", references.reference)) FROM `references` WHERE basics.resume_id = `references`.resume_id)),
     CONCAT(",projects:",
     (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) FROM projects WHERE basics.resume_id = projects.resume_id))) as "twelve"
                    FROM basics LEFT JOIN profiles ON basics.resume_id = profiles.resume_id 
                                             INNER JOIN work ON basics.resume_id = work.resume_id
                                             LEFT JOIN volunteer ON basics.resume_id = volunteer.resume_id
                                             LEFT JOIN education ON basics.resume_id = education.resume_id
                                             LEFT JOIN awards ON basics.resume_id = awards.resume_id
                                             LEFT JOIN certificates ON basics.resume_id = awards.resume_id
                                             LEFT JOIN publications ON basics.resume_id = publications.resume_id
                                             LEFT JOIN skills ON basics.resume_id = publications.resume_id
                                             LEFT JOIN languages ON basics.resume_id = languages.resume_id
                                             LEFT JOIN interests ON basics.resume_id = interests.resume_id
                                             LEFT JOIN `references` ON basics.resume_id = `references`.resume_id
                                             LEFT JOIN projects ON basics.resume_id = projects.resume_id GROUP BY basics.resume_id;




ALTER TABLE
work
CHANGE 


SELECT JSON_OBJECT("id", basics.resume_id, "coverLetter",coverLetter) as b, (SELECT JSON_OBJECT( 'basics',JSON_OBJECT('name',basics.name, 'label',basics.label, 'image',basics.image, 'email',basics.email, 'phone',basics.phone, 'url',basics.url, 'summary',basics.summary, 'location',JSON_OBJECT('address',basics.address, 'postalCode',basics.postalCode, 'city',basics.city, 'countryCode',countryCode, 'region',region)))) as basics, (SELECT JSON_OBJECT('profiles',JSON_ARRAYAGG(jSON_OBJECT("network", profiles.network, "username", profiles.username, "url", profiles.url))) FROM profiles WHERE profiles.resume_id = basics.resume_id) as profiles, CONCAT("", CONCAT("work:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) FROM work WHERE basics.resume_id = work.resume_id)), CONCAT(',"volunteer":', (SELECT JSON_ARRAYAGG(jSON_OBJECT("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))FROM volunteer WHERE basics.resume_id = volunteer.resume_id)), CONCAT(',"education":', (SELECT JSON_ARRAYAGG(jSON_OBJECT("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score)) FROM education WHERE basics.resume_id = education.resume_id)), CONCAT(',"awards":', (SELECT JSON_ARRAYAGG(jSON_OBJECT("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) FROM awards WHERE basics.resume_id = awards.resume_id)), CONCAT(',"certificates":', (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) FROM certificates WHERE basics.resume_id = certificates.resume_id)), CONCAT(",publications:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) FROM publications WHERE basics.resume_id = publications.resume_id)), CONCAT(",skills:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", skills.name, "level", skills.level, "keywords", skills.keywords)) FROM skills WHERE basics.resume_id = skills.resume_id)), CONCAT(",languages:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("language", languages.language, "fluency", languages.fluency)) FROM languages WHERE basics.resume_id = languages.resume_id)), CONCAT(",interests:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", interests.name, "keywords", interests.keywords)) FROM interests WHERE basics.resume_id = interests.resume_id)), CONCAT(",references:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", references.name, "refrenece", references.reference)) FROM `references` WHERE basics.resume_id = `references`.resume_id)), CONCAT(",projects:", (SELECT JSON_ARRAYAGG(jSON_OBJECT("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) FROM projects WHERE basics.resume_id = projects.resume_id))) as "twelve" FROM basics LEFT JOIN profiles ON basics.resume_id = profiles.resume_id INNER JOIN work ON basics.resume_id = work.resume_id LEFT JOIN volunteer ON basics.resume_id = volunteer.resume_id LEFT JOIN education ON basics.resume_id = education.resume_id LEFT JOIN awards ON basics.resume_id = awards.resume_id LEFT JOIN certificates ON basics.resume_id = awards.resume_id LEFT JOIN publications ON basics.resume_id = publications.resume_id LEFT JOIN skills ON basics.resume_id = publications.resume_id LEFT JOIN languages ON basics.resume_id = languages.resume_id LEFT JOIN interests ON basics.resume_id = interests.resume_id LEFT JOIN `references` ON basics.resume_id = `references`.resume_id LEFT JOIN projects ON basics.resume_id = projects.resume_id WHERE basics.resume_id = 1 GROUP BY basics.resume_id;

select 
     json_object("id",basics.resume_id,"coverLetter",basics.coverLetter,"basics",json_object("name",basics.name,"label",basics.label,"image",basics.image,"email",basics.email,"phone",basics.phone,"location",json_object("address",basics.address,"postalCode",basics.postalCode,"city",basics.city,"countryCode",basics.countryCode,"region",basics.region),"profiles",(select json_arrayagg(json_object("network", profiles.network, "username", profiles.username, "url", profiles.url)) from profiles where profiles.resume_id = basics.resume_id)),
     "work",(select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics.resume_id = work.resume_id),
     "volunteer",(select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics.resume_id = volunteer.resume_id),
     "education",(select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score,"courses",(select json_arrayagg(education_courses.courses) from education_courses where education.education_id = education_courses.education_id))) from education INNER JOIN education_courses on education_courses.education_id = education.education_id where basics.resume_id = education.resume_id),
     "awards",(select json_arrayagg(json_object("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) from awards where basics.resume_id = awards.resume_id),
     "certificates",(select json_arrayagg(json_object("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) from certificates where basics.resume_id = certificates.resume_id),
     "publications",(select json_arrayagg(json_object("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) from publications where basics.resume_id = publications.resume_id),
     "skills",(select json_arrayagg(json_object("name", skills.name, "level", skills.level, "keywords", skills.keywords)) from skills where basics.resume_id = skills.resume_id),
     "languages",(select json_arrayagg(json_object("language", languages.language, "fluency", languages.fluency)) from languages where basics.resume_id = languages.resume_id),
     "interests",(select json_arrayagg(json_object("name", interests.name, "keywords", interests.keywords)) from interests where basics.resume_id = interests.resume_id),
     "refreneces",(select json_arrayagg(json_object("name", references.name, "refrenece", references.reference)) from `references` where basics.resume_id = `references`.resume_id),
     "projects",(select json_arrayagg(json_object("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) from projects where basics.resume_id = projects.resume_id))
                    from basics left join profiles on basics.resume_id = profiles.resume_id 
                                left join work on basics.resume_id = work.resume_id
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

select 
json_object("id",basics.resume_id,"coverLetter",basics.coverLetter,"basics",json_object("name",basics.name,"label",basics.label,"image",basics.image,"email",basics.email,"phone",basics.phone,"location",json_object("address",basics.address,"postalCode",basics.postalCode,"city",basics.city,"countryCode",basics.countryCode,"region",basics.region),"profiles",(select json_arrayagg(json_object("network", profiles.network, "username", profiles.username, "url", profiles.url)) from profiles where profiles.resume_id = basics.resume_id)),
"work",(select json_arrayagg(json_object("name", work.name, "location", work.location, "description", work.description, "position", work.position,"url", work.url, "startDate", work.startDate, "endDate", work.endDate, "summary", work.summary, "highlights", work.highlights, "keywords", work.keywords)) from work where basics.resume_id = work.resume_id),
"volunteer",(select json_arrayagg(json_object("organization", volunteer.organization, "position", volunteer.position,"url", volunteer.url, "startDate", volunteer.startDate, "endDate", volunteer.endDate, "highlights", volunteer.highlights))from volunteer where basics.resume_id = volunteer.resume_id),
"education",(select json_arrayagg(json_object("institution", education.institution, "url", education.url, "area", education.area,"studyType", education.studyType, "startDate", education.startDate, "endDate", education.endDate, "score", education.score,"courses",(select json_arrayagg(courses) from education_courses where education.education_id = education_courses.education_id))) from education where basics.resume_id = education.resume_id),
"awards",(select json_arrayagg(json_object("title", awards.title, "date", awards.date, "awarder", awards.awarder, "summary", awards.summary)) from awards where basics.resume_id = awards.resume_id),
"certificates",(select json_arrayagg(json_object("name", certificates.name, "date", certificates.date, "url", certificates.url, "issuer", certificates.issuer)) from certificates where basics.resume_id = certificates.resume_id),
"publications",(select json_arrayagg(json_object("name", publications.name, "publisher", publications.publisher,"releaseDate", publications.releaseDate, "url", publications.url, "summary", publications.summary)) from publications where basics.resume_id = publications.resume_id),
"skills",(select json_arrayagg(json_object("name", skills.name, "level", skills.level, "keywords", skills.keywords)) from skills where basics.resume_id = skills.resume_id),
"languages",(select json_arrayagg(json_object("language", languages.language, "fluency", languages.fluency)) from languages where basics.resume_id = languages.resume_id),
"interests",(select json_arrayagg(json_object("name", interests.name, "keywords", interests.keywords)) from interests where basics.resume_id = interests.resume_id),
"refreneces",(select json_arrayagg(json_object("name", references.name, "refrenece", references.reference)) from `references` where basics.resume_id = `references`.resume_id),
"projects",(select json_arrayagg(json_object("name", projects.name, "description", projects.description, "startDate", projects.startDate, "endDate", projects.endDate,"url", projects.url, "entity", projects.entity, "type", projects.type, "highlights", projects.highlights, "keywords", projects.keywords, "roles", projects.roles)) from projects where basics.resume_id = projects.resume_id)) as resume
                from basics left join profiles on basics.resume_id = profiles.resume_id 
                                        left join work on basics.resume_id = work.resume_id
                                        left join volunteer on basics.resume_id = volunteer.resume_id
                                        left join education on basics.resume_id = education.resume_id
                                        left join education_courses on education_courses.education_id = education.education_id
                                        left join awards on basics.resume_id = awards.resume_id
                                        left join certificates on basics.resume_id = awards.resume_id
                                        left join publications on basics.resume_id = publications.resume_id
                                        left join skills on basics.resume_id = publications.resume_id
                                        left join languages on basics.resume_id = languages.resume_id
                                        left join interests on basics.resume_id = interests.resume_id
                                        left join `references` on basics.resume_id = `references`.resume_id
                                        left join projects 
                                                        on basics.resume_id = projects.resume_id 
                                                                       
                                                                                        group by basics.resume_id                    