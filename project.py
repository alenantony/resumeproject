from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
# from starlette.responses import PlainTextResponse
import mysql.connector, requests

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	auth_plugin='mysql_native_password',
    database = "project",
)

print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

response = dict()

async def homepage(request):
    # apiresp = requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume/1")
    global response
    # response = apiresp.json()
    # print(response)
    data(response)
    return JSONResponse(response)

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])

response = {'id':2800, 'coverLetter': 'Some text', 'basics': {'name': 'Richard Hendriks', 'label': 'Programmer', 'image': 'https://i.pravatar.cc/150?img=8', 'email': 'richard.hendriks@mail.com', 'phone': '(912) 555-4321', 'url': 'http://richardhendricks.example.com', 'summary': 'Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!', 'location': {'address': '2712 Broadway St', 'postalCode': 'CA 94115', 'city': 'San Francisco', 'countryCode': 'US', 'region': 'California'}, 'profiles': [{'network': 'Twitter', 'username': 'neutralthoughts', 'url': 'https://twitter.com/neutralthoughts'}, {'network': 'SoundCloud', 'username': 'dandymusicnl', 'url': 'https://soundcloud.example.com/dandymusicnl'}]}, 'work': [{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']}], 'volunteer': [{'organization': 'CoderDojo', 'position': 'Teacher', 'url': 'http://coderdojo.example.com/', 'startDate': '2012-01-01', 'endDate': '2013-01-01', 'summary': 'Global movement of free coding clubs for young people.', 'highlights': ["Awarded 'Teacher of the Month'"]}], 'education': [{'institution': 'University of Oklahoma', 'url': 'https://www.ou.edu/', 'area': 'Information Technology', 'studyType': 'Bachelor', 'startDate': '2011-06-01', 'endDate': '2014-01-01', 'score': '4.0', 'courses': ['DB1101 - Basic SQL', 'CS2011 - Java Introduction']}], 'awards': [{'title': 'Digital Compression Pioneer Award', 'date': '2014-11-01', 'awarder': 'Techcrunch', 'summary': 'There is no spoon.'}], 'publications': [{'name': 'Video compression for 3d media', 'publisher': 'Hooli', 'releaseDate': '2014-10-01', 'url': 'http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data.'}, {'name': 'Video compression for 3d media part 2', 'publisher': 'Hooli', 'releaseDate': '2015-10-01', 'url': 'http://hooli.com', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data. Again!'}], 'skills': [{'name': 'Web Development', 'level': 'Master', 'keywords': ['HTML', 'CSS', 'Javascript']}, {'name': 'Compression', 'level': 'Master', 'keywords': ['Mpeg', 'MP4', 'GIF']}], 'languages': [{'language': 'English', 'fluency': 'Native speaker'}], 'interests': [{'name': 'Wildlife', 'keywords': ['Ferrets', 'Unicorns']}], 'references': [{'name': 'Erlich Bachman', 'reference': 'It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.'}], 'projects': [{'name': 'Miss Direction', 'description': 'A mapping engine that misguides you', 'highlights': ['Won award at AIHacks 2016', 'Built by all women team of newbie programmers', 'Using modern technologies such as GoogleMaps, Chrome Extension and Javascript'], 'keywords': ['GoogleMaps', 'Chrome Extension', 'Javascript'], 'startDate': '2016-08-24', 'endDate': '2016-08-24', 'url': 'missdirection.example.com', 'roles': ['Team lead', 'Designer'], 'entity': 'Smoogle', 'type': 'application'}], 'meta': {'canonical': 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json', 'version': 'v1.0.0', 'lastModified': '2017-12-24T15:53:00'}, '__translation__': {'awards': 'Prizes', 'volunteers': 'Volunteers', 'skills': 'Skills', 'references': 'References', 'publications': 'Publications', 'languages': 'Languages', 'interests': 'Interests', 'education': 'Education', 'summary': 'Summary', 'experience': 'Experience', 'at': 'at'}, 'enableSourceDataDownload': True}
# response = {'id': 1, 'coverLetter': 'Some text', 'basics': {'name': 'Richard Hendriks', 'label': 'Programmer', 'image': 'https://i.pravatar.cc/150?img=8', 'email': 'richard.hendriks@mail.com', 'phone': '(912) 555-4321', 'url': 'http://richardhendricks.example.com', 'summary': 'Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!', 'location': {'address': '2712 Broadway St', 'postalCode': 'CA 94115', 'city': 'San Francisco', 'countryCode': 'US', 'region': 'California'}, 'profiles': [{'network': 'Twitter', 'username': 'neutralthoughts', 'url': 'https://twitter.com/neutralthoughts'}, {'network': 'SoundCloud', 'username': 'dandymusicnl', 'url': 'https://soundcloud.example.com/dandymusicnl'}]}, 'work': [{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']},{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']}], 'volunteer': [{'organization': 'CoderDojo', 'position': 'Teacher', 'url': 'http://coderdojo.example.com/', 'startDate': '2012-01-01', 'endDate': '2013-01-01', 'summary': 'Global movement of free coding clubs for young people.', 'highlights': ["Awarded 'Teacher of the Month'"]}], 'education': [{'institution': 'University of Oklahoma', 'url': 'https://www.ou.edu/', 'area': 'Information Technology', 'studyType': 'Bachelor', 'startDate': '2011-06-01', 'endDate': '2014-01-01', 'score': '4.0', 'courses': ['DB1101 - Basic SQL', 'CS2011 - Java Introduction']}], 'awards': [{'title': 'Digital Compression Pioneer Award', 'date': '2014-11-01', 'awarder': 'Techcrunch', 'summary': 'There is no spoon.'}], 'publications': [{'name': 'Video compression for 3d media', 'publisher': 'Hooli', 'releaseDate': '2014-10-01', 'url': 'http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data.'}, {'name': 'Video compression for 3d media part 2', 'publisher': 'Hooli', 'releaseDate': '2015-10-01', 'url': 'http://hooli.com', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data. Again!'}], 'skills': [{'name': 'Web Development', 'level': 'Master', 'keywords': ['HTML', 'CSS', 'Javascript']}, {'name': 'Compression', 'level': 'Master', 'keywords': ['Mpeg', 'MP4', 'GIF']}], 'languages': [{'language': 'English', 'fluency': 'Native speaker'}], 'interests': [{'name': 'Wildlife', 'keywords': ['Ferrets', 'Unicorns']}], 'references': [{'name': 'Erlich Bachman', 'reference': 'It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.'}], 'projects': [{'name': 'Miss Direction', 'description': 'A mapping engine that misguides you', 'highlights': ['Won award at AIHacks 2016', 'Built by all women team of newbie programmers', 'Using modern technologies such as GoogleMaps, Chrome Extension and Javascript'], 'keywords': ['GoogleMaps', 'Chrome Extension', 'Javascript'], 'startDate': '2016-08-24', 'endDate': '2016-08-24', 'url': 'missdirection.example.com', 'roles': ['Team lead', 'Designer'], 'entity': 'Smoogle', 'type': 'application'}], 'meta': {'canonical': 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json', 'version': 'v1.0.0', 'lastModified': '2017-12-24T15:53:00'}, '__translation__': {'awards': 'Prizes', 'volunteers': 'Volunteers', 'skills': 'Skills', 'references': 'References', 'publications': 'Publications', 'languages': 'Languages', 'interests': 'Interests', 'education': 'Education', 'summary': 'Summary', 'experience': 'Experience', 'at': 'at'}, 'enableSourceDataDownload': True}

def data(response):

    #basics
    id = response['id']
    coverLetter = response['coverLetter']
    basics = response['basics']
    name = basics['name']
    label = basics['label']
    image = basics['image']
    email = basics['email']
    phone = basics['phone']
    url = basics['url']
    summary = basics['summary']
    location = basics['location']
    address = location['address']
    postalCode = location['postalCode']
    city = location['city']
    countryCode = location['countryCode']
    region = location['region']
    query = "insert into basics(id, name, label, image, email, phone, url, summary, address, postalCode, city, countryCode, region, coverLetter) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (id, name, label, image, email, phone, url, summary,
            address, postalCode, city, countryCode, region, coverLetter)
    mycursor.execute(query, value)
    mydb.commit()

    #profiles
    profiles = basics['profiles']
    for i in profiles:
        network = i['network']
        profile_username = i['username']
        profile_url = i['url']
        mycursor.execute("SELECT MAX(profileno) FROM profiles")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            profileno = 1
        else:
            profileno = myresult[0][0] + 1
        query = "INSERT INTO profiles(profileno, id, network, username, url) VALUES(%s, %s, %s, %s, %s)"
        value = (profileno, id, network, profile_username, profile_url)
        mycursor.execute(query, value)
        mydb.commit()
    
    #work
    work = response['work']
    for i in work:
        name = i['name']
        location = i['location']
        description = i['description']
        position = i['position']
        url = i['url']
        startDate = i['startDate']
        endDate = i['endDate']
        summary = i['summary']
        highlights = i['highlights']
        keywords = i['keywords']
        mycursor.execute("SELECT MAX(workno) FROM work")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            workno = 1
        else:
            workno = myresult[0][0] + 1
        query = "insert into work(workno, id, name, location, description, position, url, startDate, endDate, summary) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (workno, id, name, location, description, position, 
                url, startDate, endDate, summary)
        mycursor.execute(query, value)
        mydb.commit()
        #work_highlights
        for item in highlights:
            mycursor.execute("SELECT MAX(highlightsno) FROM work_highlights")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                highlightsno = 1
            else:
                highlightsno = myresult[0][0] + 1
            query = "insert into work_highlights(workno, highlightsno, highlights) values(%s, %s, %s)"
            value = (workno, highlightsno, item)
            mycursor.execute(query, value)
            mydb.commit()
        #work_keywords
        for item in keywords:
            mycursor.execute("SELECT MAX(keywordsno) FROM work_keywords")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                keywordsno = 1
            else:
                keywordsno = myresult[0][0] + 1
            query = "insert into work_keywords(workno, keywordsno, keywords) values(%s, %s, %s)"
            value = (workno, keywordsno, item)
            mycursor.execute(query, value)
            mydb.commit()

    #volunteer
    volunteer = response['volunteer']
    for i in volunteer:
        organization = i['organization']
        position = i['position']
        url = i['url']
        startDate = i['startDate']
        endDate = i['endDate']
        summary = i['summary']
        highlights = i['highlights']
        mycursor.execute("SELECT MAX(volno) FROM volunteer")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            volno = 1
        else:
            volno = myresult[0][0] + 1
        query = "insert into volunteer(volno, id, organistaion, position, url, startDate, endDate, summary) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (volno, id, organization, position, url, startDate, endDate, summary)
        mycursor.execute(query, value)
        mydb.commit()
        #volunteer_highlights
        for item in highlights:
            mycursor.execute("SELECT MAX(highlightsno) FROM volunteer_highlights")
            highlightsno = mycursor.fetchall()
            highlightsno = highlightsno[0][0]
            if (highlightsno == None):
                highlightsno = 1
            else:
                highlightsno = myresult[0][0] + 1
            query = "insert into volunteer_highlights(highlightsno, volno, highlights) values(%s, %s, %s)"
            value = (highlightsno, volno, item)
            mycursor.execute(query, value)
            mydb.commit()

    #education
    education = response['education']
    for i in education:
        institution = i['institution']
        url = i['url']
        area = i['area']    
        studyType = i['studyType']
        startDate = i['startDate']
        endDate = i['endDate']
        score = i['score']
        courses = i['courses']
        mycursor.execute("SELECT MAX(educationno) FROM education")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            educationno = 1
        else:
            educationno = myresult[0][0] + 1
        query = "insert into education(educationno, id, institution, url, area, studyTape, startDate, endDate, score) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (educationno, id, institution, url, area, studyType, startDate, endDate, score)
        mycursor.execute(query, value)
        mydb.commit()
        #courses
        for item in courses:
            mycursor.execute("SELECT MAX(coursesno) FROM education_courses")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                coursesno = 1
            else: 
                coursesno = myresult[0][0] + 1
            query = "insert into education_courses(coursesno, educationno, courses) values(%s, %s, %s)"
            value = (coursesno, educationno, item)
            mycursor.execute(query, value)
            mydb.commit()

    #awards
    awards = response['awards']
    for i in awards:
        title = i['title']
        date = i['date']
        awarder = i['awarder']
        summary = i['summary']
        mycursor.execute("SELECT MAX(awardno) FROM awards")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            awardno = 1
        else:
            awardno = myresult[0][0] + 1
        query = "insert into awards(awardno, id, title, date, awarder, summary) values(%s, %s, %s, %s, %s, %s)"
        value = (awardno, id, title, date, awarder, summary)
        mycursor.execute(query, value)
        mydb.commit()
    
    #certificates
    try:
        certificates = response['certificates']
        for i in certificates:
            name = i['name']
            date = i['date']
            url = i['url']
            issuer = i['issuer']
            mycursor.execute("SELECT MAX(certificateno) FROM certifications")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                certificateno = 1
            else:
                certificateno = myresult[0][0] + 1
            query = "insert into certifications(certificateno, id, name, date, url, issuer) values(%s, %s, %s, %s, %s, %s)"
            value = (certificateno, id, name, date, url, issuer)
            mycursor.execute(query, value)
            mydb.commit()
    except:
        print("No Certifications")
    
    #publications
    publications = response['publications']
    for i in publications:
        name = i['name']
        publisher = i['publisher']
        releaseDate = i['releaseDate']
        url = i['url']
        summary = i['summary']
        mycursor.execute("SELECT MAX(publicationno) FROM publications")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            publicationno = 1
        else: 
            publicationno = myresult[0][0] + 1
        query = "insert into publications(publicationno, id, name, publisher, releaseDate, url, summary) values(%s, %s, %s, %s, %s, %s, %s)"
        value = (publicationno, id, name, publisher, releaseDate, url, summary)
        mycursor.execute(query, value)
        mydb.commit()

    #skills
    skills = response['skills']
    for i in skills:
        name = i['name']
        level = i['level']
        keywords = i['keywords']
        mycursor.execute("SELECT MAX(skillno) FROM skills")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            skillno = 1
        else:
            skillno = myresult[0][0] + 1
        query = "insert into skills(skillno, id, name, level) values(%s, %s, %s, %s)"
        value = (skillno, id, name, level)
        mycursor.execute(query, value)
        mydb.commit()
        #skills_keywords
        for item in keywords:
            mycursor.execute("SELECT MAX(keywordno) FROM skills_keywords")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                keywordno = 1
            else:
                keywordno = myresult[0][0] + 1
            query = "insert into skills_keywords(keywordno, skillno, keywords) values(%s, %s, %s)"
            value = (keywordno, skillno, item)
            mycursor.execute(query, value)
            mydb.commit()

    #languages
    languages = response['languages']
    for i in languages:
        language = i['language']
        fluency = i['fluency']
        mycursor.execute("SELECT MAX(languageno) FROM languages")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            languageno = 1
        else:
            languageno = myresult[0][0] + 1
        query = "insert into languages(languageno, id, language, fluency) values(%s, %s, %s, %s)"
        value = (languageno, id, language, fluency)
        mycursor.execute(query, value)
        mydb.commit()

    #interests
    interests = response['interests']
    for i in interests:
        name = i['name']
        keywords = i['keywords']
        mycursor.execute("SELECT MAX(interestno) FROM interests")
        myresult = mycursor.fetchall()
        if(myresult[0][0] == None):
            interestno = 1
        else:
            interestno = myresult[0][0] + 1
        query = "insert into interests(interestno, id, name) values(%s, %s, %s)"
        value = (interestno, id, name)
        mycursor.execute(query, value)
        mydb.commit()
        #interests_keywords
        for item in keywords:
            mycursor.execute("SELECT MAX(keywordno) FROM interests_keywords")
            myresult = mycursor.fetchall()
            if(myresult[0][0] == None):
                keywordno = 1
            else:
                keywordno = myresult[0][0] + 1
            query = "insert into interests_keywords(keywordno, interestno, keywords) values(%s, %s, %s)"
            value = (keywordno, interestno, item)
            mycursor.execute(query, value)
            mydb.commit()

    #references
    references = response['references']
    for i in references:
        name = i['name']
        reference = i['reference']
        mycursor.execute("SELECT MAX(referenceno) FROM REFERENCE")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            referenceno = 1
        else:
            referenceno = myresult[0][0] + 1
        query = "insert into REFERENCE(referenceno, id, name, reference) values(%s, %s, %s, %s)"
        value = (referenceno, id, name, reference)
        mycursor.execute(query, value)
        mydb.commit()

    #projects
    projects = response['projects']
    for i in projects:
        name = i['name']
        description = i['description']
        highlights = i['highlights']
        keywords = i['keywords']
        startDate = i['startDate']
        endDate = i['endDate']
        url = i['url']
        roles = i['roles']
        entity = i['entity']
        type = i['type']
        mycursor.execute("SELECT MAX(projectno) FROM projects")
        myresult = mycursor.fetchall()
        if (myresult[0][0] == None):
            projectno = 1
        else:
            projectno = myresult[0][0] + 1
        query = "insert into projects(projectno, id, name, description, startDate, endDate, url, entity, type) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (projectno, id, name, description, startDate, endDate, url, entity, type)
        mycursor.execute(query, value)
        mydb.commit()
        #projects_highlights
        for item in highlights:
            mycursor.execute("SELECT MAX(highlightsno) FROM project_highlights")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                highlightsno = 1
            else: 
                highlightsno = myresult[0][0] + 1
            query = "insert into project_highlights(highlightsno, projectno, highlights) values(%s, %s, %s)"
            value = (highlightsno, projectno, item)
            mycursor.execute(query, value)
            mydb.commit()
        #projects_keywords
        for item in keywords:
            mycursor.execute("SELECT MAX(keywordno) FROM projects_keywords")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                keywordno = 1
            else: 
                keywordno = myresult[0][0] + 1
            query = "insert into projects_keywords(keywordno, projectno, keywords) values(%s, %s, %s)"
            value = (keywordno, projectno, item)
            mycursor.execute(query, value)
            mydb.commit()
        #projects_roles    
        for item in roles:
            mycursor.execute("SELECT MAX(roleno) FROM projects_roles")
            myresult = mycursor.fetchall()
            if (myresult[0][0] == None):
                roleno = 1
            else: 
                roleno = myresult[0][0] + 1
            query = "insert into projects_roles(roleno, projectno, roles) values(%s, %s, %s)"
            value = (roleno, projectno, item)
            mycursor.execute(query, value)
            mydb.commit()
    # mycursor.execute("select json_object('id', basics.id, 'title', awards.title) from basics inner join awards on basics.id = awards.id where basics.id =9200;")
    # myresult = mycursor.fetchall()
    # print(myresult)



#################################################
#################################################
    mycursor.execute('''SELECT id, coverLetter FROM basics where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    json_data = []
    for items in results:
        json_data.append(dict(zip(row_headers, items)))



    #basics:
    mycursor.execute('''SELECT name, label, image, email, phone, url, summary FROM basics where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    basics1 = []
    for item in results:
        basics1.append(dict(zip(row_headers, item)))

    #basics:location:
    mycursor.execute('''SELECT address, postalCode, city, countryCode, region FROM basics where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    location = []
    for item in results:
        location.append(dict(zip(row_headers, item)))
    location = {"location":location[0]}
    basics1[0].update(location)

    #basics:profiles
    profiles = []
    mycursor.execute('''SELECT network, username, url from profiles where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        profiles.append(dict(zip(row_headers, item)))
    profiles = {"profiles":profiles}
    basics1[0].update(profiles)

    basics = {"basics":basics1[0]}
    # end of basics


    #work
    working = []
    mycursor.execute('''SELECT workno, name, location, description, position, url, startDate, endDate, summary from work where id = 1''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        working.append(dict(zip(row_headers, item)))
        print("===============================================\n\n")
        print(dict(zip(row_headers,item)))
        print("\n\n-----------------------------------------------")
        for i in working:
            highlights = []
            query = ('''SELECT highlights FROM work_highlights\
                                where workno = %s''')
                                #query change required when there is more than 1 work
                                #loop should switch between number of total work highlights
            value = i['workno']
            mycursor.execute(query, (value,))
            hresults = mycursor.fetchall()
            for highs in hresults:
                highlights.append(highs[0])
            # work_keywords
            keywords = []
            query = ('''SELECT keywords from work_keywords
                                where workno = %s''')
                                #query change required when there is more than 1 work
                                #loop should switch between number of total work keywords
            value = i['workno']
            mycursor.execute(query, (value,))
            kresults = mycursor.fetchall()
            for keys in kresults:
                keywords.append(keys[0])
        hlights = {"highlights":highlights}
        kwords = {"keywords":keywords}
        working[0].update(hlights)
        working[0].update(kwords)   
    # # # # print(highlights)
    # # # #     lights = {"highlights":highlights}
    # # # #     work.append(lights)
    # # # #     #work_highlights
    # # # #     work_highlights = []
    # # # #     mycursor.execute('''SELECT highlights from work_highlights where workno = 1''')
    # # # #     hresults = mycursor.fetchall()
    # # # #     row_headers = [x[0] for x in mycursor.description]
    # # # #     for highlights in hresults:
    # # # #         print(highlights[0])
    # # # #         print(type(highlights[0]))
    # # # #         work_highlights.append(highlights[0])
    # # # #     work.append({"highlights":work_highlights}) 
    # # # adf
    # # afe
    # ac
    work = {"work":working}
    # end of work

    # VOLUNTEER
    volunteers = []
    mycursor.execute('''SELECT organistaion, position, url, startDate, endDate, summary\
                        FROM volunteer where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        volunteers.append(dict(zip(row_headers, item)))
        # volunteer_highlights
        highlights = []
        mycursor.execute('''SELECT volunteer_highlights.highlights FROM volunteer\
                            LEFT JOIN volunteer_highlights\
                            ON volunteer.volno = volunteer_highlights.volno\
                            where volunteer.id = 920''')
                            #query change required when there is more than 1 volunteer
                            #loop should switch between number of total volunteer highlights
        hresults = mycursor.fetchall()
        for highs in hresults:
            highlights.append(highs[0])
        
        hlights = {"highlights":highlights}
        volunteers[0].update(hlights)
    volunteer = {"volunteer":volunteers}

    # END OF VOLUNTEER

    # EDUCATION
    educations = []
    mycursor.execute('''SELECT institution, url, area, studyTape, startDate, endDate, score\
                        FROM education where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        educations.append(dict(zip(row_headers, item)))
        # education_courses
        courses = []
        mycursor.execute('''SELECT education_courses.courses FROM education\
                            LEFT JOIN education_courses\
                            ON education.educationno = education_courses.educationno\
                            where education.id = 920''')
        eresults = mycursor.fetchall()
        for ecourses in eresults:
            courses.append(ecourses[0])
        ecourses = {"courses":courses}
        educations[0].update(ecourses)
    education = {"education":educations}

    # END OF EDUCATION


    # AWARDS
    awards = []
    mycursor.execute('''SELECT title, date, awarder, summary FROM awards\
                        WHERE id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        awards.append(dict(zip(row_headers, item)))
    awards = {"awards":awards}

    # END OF AWARDS


    # CERTIFICATIONS
    # END OF CERTIFICATIONS


    # PUBLICATIONS
    publications = []
    mycursor.execute('''SELECT name, publisher, releaseDate, url, summary\
                        FROM publications where id =920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        publications.append(dict(zip(row_headers, item)))

    publication = {"publications":publications}

    # END OF PUBLICATIONS

    # SKILLS
    skill = []
    mycursor.execute('''SELECT name, level \
                        FROM skills where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    number = 1
    for item in results:
        skill.append(dict(zip(row_headers, item)))

        # skills_keywords
        keywords = []
        mycursor.execute('''SELECT keywords from skills_keywords\
                    where skillno = 1''')
        # value = 1
        # mycursor.execute(query, value)
        sresults = mycursor.fetchall()
        for kskills in sresults:
            keywords.append(kskills[0])
        keyword = {"keywords":keywords}
        skill[0].update(keyword)
        
    skills = {"skills":skill}

    # END OF SKILLS

    # LANGUAGES
    language = []
    mycursor.execute('''SELECT language, fluency from languages where id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        language.append(dict(zip(row_headers, item)))
    languages = {"languages": language}

    # END OF LANGUAGES

    # INTERESTS
    interest = []
    mycursor.execute('''SELECT name from interests where id = 920''')
    result = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        interest.append(dict(zip(row_headers, item)))
        # interest_keywords
        keyword = []
        mycursor.execute('''SELECT interests_keywords.keywords FROM interests\
                            LEFT JOIN interests_keywords\
                            ON interests.interestno = interests_keywords.interestno\
                            where interests.id =920''')
        kresults = mycursor.fetchall()
        for keys in kresults:
            keyword.append(keys[0]) 
        kwords = {"keywords":keyword}
        interest[0].update(kwords)
    interests = {"interests":interest}    

    # END OF INTERESTS


    # REFERENCES
    reference = []
    mycursor.execute('''SELECT name, reference FROM REFERENCE\
                        WHERE id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    for item in results:
        reference.append(dict(zip(row_headers, item)))
    references ={"references":reference}

    # END OF REFERENCES


    # PROJECTS
    projects = []
    mycursor.execute('''SELECT name, description, startDate, endDate, url, entity, type \
                        FROM projects WHERE id = 920''')
    results = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
                                                                                                                        # print("\n\n\n----------------------------------------------------------------------------------\n\n\n")
                                                                                                                        # print(mycursor.description)
                                                                                                                        # print("\n\n\n----------------------------------------------------------------------------------\n\n\n")
                                                                                                                        # print("\n\n\n----------------------------------------------------------------------------------\n\n\n")
                                                                                                                        # for x in mycursor.description:
                                                                                                                        #     print(row_headers)
                                                                                                                        # print("\n\n\n----------------------------------------------------------------------------------\n\n\n")
    for item in results:
        projects.append(dict(zip(row_headers,item)))
        print("\n\n======================PROJECT=========================\n\n")
        print(dict(zip(row_headers,item)))
        print("\n\n-----------------------------------------------\n\n")


    # END OF PROJECTS





    json_data[0].update(basics)
    json_data[0].update(work)
    json_data[0].update(volunteer)
    json_data[0].update(education)
    json_data[0].update(awards)
    json_data[0].update(publication)
    json_data[0].update(skills)
    json_data[0].update(languages)
    json_data[0].update(interests)
    json_data[0].update(references)

    print(json_data[0])