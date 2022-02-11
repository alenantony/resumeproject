from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse, PlainTextResponse
import json
from validation import Resume
import mysql.connector
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	auth_plugin='mysql_native_password',
    database = "Resume_Project",
)

print(mydb)
mycursor = mydb.cursor()


def list_resume():
    list_of_resume = []
    query = '''select 
json_object("resume_id",basics.resume_id,"coverLetter",basics.coverLetter,"basics",json_object("name",basics.name,"label",basics.label,"image",basics.image,"email",basics.email,"phone",basics.phone,"location",json_object("address",basics.address,"postalCode",basics.postalCode,"city",basics.city,"countryCode",basics.countryCode,"region",basics.region),"profiles",(select json_arrayagg(json_object("network", profiles.network, "username", profiles.username, "url", profiles.url)) from profiles where profiles.resume_id = basics.resume_id)),
"work",(select json_arrayagg(json_object("companyName", work.companyName, "companyLocation", work.location, "workDescription", work.description, "workPosition", work.position,"companyUrl", work.url, "workStartDate", work.startDate, "workEndDate", work.endDate, "workSummary", work.summary, "workHighlights", work.highlights, "workKeywords", work.keywords)) from work where basics.resume_id = work.resume_id),
"volunteer",(select json_arrayagg(json_object("volunteerOrganization", volunteer.organization, "volunteerPosition", volunteer.position,"organizationUrl", volunteer.url, "volunteeringStartDate", volunteer.startDate, "volunteeringEndDate", volunteer.endDate, "volunteeringHighlights", volunteer.highlights))from volunteer where basics.resume_id = volunteer.resume_id),
"education",(select json_arrayagg(json_object("educationInstitution", education.institution, "institutionUrl", education.url, "educationArea", education.area,"educationStudyType", education.studyType, "educationStartDate", education.startDate, "educationEndDate", education.endDate, "educationScore", education.score,"educationCourses",(select json_arrayagg(courses) from education_courses where education.education_id = education_courses.education_id))) from education where basics.resume_id = education.resume_id),
"awards",(select json_arrayagg(json_object("awardTitle", awards.title, "awardedDate", awards.date, "awarder", awards.awarder, "awardSummary", awards.summary)) from awards where basics.resume_id = awards.resume_id),
"certificates",(select json_arrayagg(json_object("certificateName", certificates.name, "certificatesIssueDate", certificates.date, "certificateUrl", certificates.url, "certificateIssuer", certificates.issuer)) from certificates where basics.resume_id = certificates.resume_id),
"publications",(select json_arrayagg(json_object("publicationTitle", publications.name, "publisher", publications.publisher,"publishedDate", publications.releaseDate, "publishedUrl", publications.url, "publicationSummary", publications.summary)) from publications where basics.resume_id = publications.resume_id),
"skills",(select json_arrayagg(json_object("skillName", skills.name, "skillLevel", skills.level, "skillKeywords", skills.keywords)) from skills where basics.resume_id = skills.resume_id),
"languages",(select json_arrayagg(json_object("languageName", languages.language, "languagesFluency", languages.fluency)) from languages where basics.resume_id = languages.resume_id),
"interests",(select json_arrayagg(json_object("interestName", interests.name, "interestKeywords", interests.keywords)) from interests where basics.resume_id = interests.resume_id),
"reference",(select json_arrayagg(json_object("referrerName", references.name, "reference", references.reference)) from `references` where basics.resume_id = `references`.resume_id),
"projects",(select json_arrayagg(json_object("projectName", projects.name, "projectDescription", projects.description, "projectStartDate", projects.startDate, "projectEndDate", projects.endDate,"projectUrl", projects.url, "projectEntity", projects.entity, "projectType", projects.type, "projectHighlights", projects.highlights, "projectKeywords", projects.keywords, "projectRoles", projects.roles)) from projects where basics.resume_id = projects.resume_id)) as resume
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
                                                        group by basics.resume_id'''
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
        resume_data = json.loads(i[0])
        list_of_resume.append(resume_data)
    # print(list_of_resume)
    return list_of_resume
# END OF LIST ALL RESUME

def call_resume(id):
    query = '''select 
json_object("resume_id",basics.resume_id,"coverLetter",basics.coverLetter,"basics",json_object("name",basics.name,"label",basics.label,"image",basics.image,"email",basics.email,"phone",basics.phone,"location",json_object("address",basics.address,"postalCode",basics.postalCode,"city",basics.city,"countryCode",basics.countryCode,"region",basics.region),"profiles",(select json_arrayagg(json_object("network", profiles.network, "username", profiles.username, "url", profiles.url)) from profiles where profiles.resume_id = basics.resume_id)),
"work",(select json_arrayagg(json_object("companyName", work.companyNAme, "companyLocation", work.location, "workDescription", work.description, "workPosition", work.position,"companyUrl", work.url, "workStartDate", work.startDate, "workEndDate", work.endDate, "workSummary", work.summary, "workHighlights", work.highlights, "workKeywords", work.keywords)) from work where basics.resume_id = work.resume_id),
"volunteer",(select json_arrayagg(json_object("volunteerOrganization", volunteer.organization, "volunteerPosition", volunteer.position,"organizationUrl", volunteer.url, "volunteeringStartDate", volunteer.startDate, "volunteeringEndDate", volunteer.endDate, "volunteeringHighlights", volunteer.highlights))from volunteer where basics.resume_id = volunteer.resume_id),
"education",(select json_arrayagg(json_object("educationInstitution", education.institution, "institutionUrl", education.url, "educationArea", education.area,"educationStudyType", education.studyType, "educationStartDate", education.startDate, "educationEndDate", education.endDate, "educationScore", education.score,"educationCourses",(select json_arrayagg(courses) from education_courses where education.education_id = education_courses.education_id))) from education where basics.resume_id = education.resume_id),
"awards",(select json_arrayagg(json_object("awardTitle", awards.title, "awardedDate", awards.date, "awarder", awards.awarder, "awardSummary", awards.summary)) from awards where basics.resume_id = awards.resume_id),
"certificates",(select json_arrayagg(json_object("certificateName", certificates.name, "certificatesIssueDate", certificates.date, "certificateUrl", certificates.url, "certificateIssuer", certificates.issuer)) from certificates where basics.resume_id = certificates.resume_id),
"publications",(select json_arrayagg(json_object("publicationTitle", publications.name, "publisher", publications.publisher,"publishedDate", publications.releaseDate, "publishedUrl", publications.url, "publicationSummary", publications.summary)) from publications where basics.resume_id = publications.resume_id),
"skills",(select json_arrayagg(json_object("skillName", skills.name, "skillLevel", skills.level, "skillKeywords", skills.keywords)) from skills where basics.resume_id = skills.resume_id),
"languages",(select json_arrayagg(json_object("languageName", languages.language, "languagesFluency", languages.fluency)) from languages where basics.resume_id = languages.resume_id),
"interests",(select json_arrayagg(json_object("interestName", interests.name, "interestKeywords", interests.keywords)) from interests where basics.resume_id = interests.resume_id),
"reference",(select json_arrayagg(json_object("referrerName", references.name, "reference", references.reference)) from `references` where basics.resume_id = `references`.resume_id),
"projects",(select json_arrayagg(json_object("projectName", projects.name, "projectDescription", projects.description, "projectStartDate", projects.startDate, "projectEndDate", projects.endDate,"projectUrl", projects.url, "projectEntity", projects.entity, "projectType", projects.type, "projectHighlights", projects.highlights, "projectKeywords", projects.keywords, "projectRoles", projects.roles)) from projects where basics.resume_id = projects.resume_id)) as resume
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
                                                        where basics.resume_id = %s
                                                        group by basics.resume_id'''
    value = (id,)
    mycursor.execute(query,value)
    result = mycursor.fetchall()
    print(result[0][0])
    resume = json.loads(result[0][0])
    return(resume)
# END OF CALL RESUME

def build_resume(data):
    # basics
    coverLetter = data['coverLetter']
    basics = data['basics']
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
    query = "insert into basics(name, label, image, email, phone, url, \
                summary, address, postalCode, city, countryCode, region, coverLetter) \
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (name, label, image, email, phone, url, summary,
            address, postalCode, city, countryCode, region, coverLetter)
    mycursor.execute(query, value)
    mycursor.execute("SELECT MAX(resume_id) FROM basics")
    result = mycursor.fetchall()
    resume_id = result[0][0]

    # profiles
    profiles = basics['profiles']
    for i in profiles:
        network = i['network']
        profile_username = i['username']
        profile_url = i['url']
        query = "INSERT INTO profiles(resume_id, network, username, url) VALUES(%s, %s, %s, %s)"
        value = (resume_id, network, profile_username, profile_url)
        mycursor.execute(query, value)
        # mydb.commit()

    # work
    work = data['work']
    for i in work:
        companyName = i['companyName']
        location = i['companyLocation']
        description = i['workDescription']
        position = i['workPosition']
        url = i['companyUrl']
        startDate = i['workStartDate']
        endDate = i['workEndDate']
        summary = i['workSummary']
        highlights = i['workHighlights']
        keywords = i['workKeywords']
        query = "insert into work(resume_id, companyName, location, description, position, url, startDate, endDate, summary, highlights, keywords) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, companyName, location, description, position, 
                url, startDate, endDate, summary, highlights, keywords)
        mycursor.execute(query, value)
        # mydb.commit()
    
    # volunteer
    volunteer = data['volunteer']
    for i in volunteer:
        organization = i['volunteerOrganization']
        position = i['volunteerPosition']
        url = i['organizationUrl']
        startDate = i['volunteeringStartDate']
        endDate = i['volunteeringEndDate']
        summary = i['volunteerSummary']
        highlights = i['volunteeringHighlights']
        query = "insert into volunteer(resume_id, organization, position, url, startDate, endDate, summary, highlights) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, organization, position, url, startDate, endDate, summary, highlights)    
        mycursor.execute(query, value)   

    # education
    education = data['education']
    for i in education:
        institution = i['educationInstitution']
        url = i['institutionUrl']
        area = i['educationArea']    
        studyType = i['educationStudyType']
        startDate = i['educationStartDate']
        endDate = i['educationEndDate']
        score = i['educationScore']
        courses = i['educationCourses']
        query = "insert into education(resume_id, institution, url, \
                area, studyType, startDate, endDate, score) \
                values(%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, institution, url, area, studyType, startDate, endDate, score)
        mycursor.execute(query, value)
        mycursor.execute("SELECT MAX(education_id) FROM education")
        result = mycursor.fetchall()
        education_id = result[0][0]
        for item in courses:
            query = "insert into education_courses(education_id,courses) values(%s,%s)"
            value = (education_id,item)
            mycursor.execute(query, value)
            # mydb.commit()

    #awards
    awards = data['awards']
    for i in awards:
        title = i['awardTitle']
        date = i['awardedDate']
        awarder = i['awarder']
        summary = i['awardSummary']
        query = "insert into awards(resume_id, title, date, awarder, summary) values(%s, %s, %s, %s, %s)"
        value = (resume_id, title, date, awarder, summary)
        mycursor.execute(query, value)
        # mydb.commit()

    # certificates
    certificates = data['certificates']
    for i in certificates:
        name = i['certificateName']
        date = i['certificatesIssueDate']
        url = i['certificateUrl']
        issuer = i['certificateIssuer']
        query = "insert into certificates(resume_id, name, date, url, issuer) values(%s, %s, %s, %s, %s)"
        value = (resume_id, name, date, url, issuer)
        mycursor.execute(query, value)
        # mydb.commit()

    # publications
    publications = data['publications']
    for i in publications:
        name = i['publicationTitle']
        publisher = i['publisher']
        releaseDate = i['publishedDate']
        url = i['publishedUrl']
        summary = i['publicationSummary']
        query = "insert into publications(resume_id, name, publisher, releaseDate, url, summary) values(%s, %s, %s, %s, %s, %s)"
        value = (resume_id, name, publisher, releaseDate, url, summary)
        mycursor.execute(query, value)
        # mydb.commit()

    # skills
    skills = data['skills']
    for i in skills:
        name = i['skillName']
        level = i['skillLevel']
        keywords = i['skillKeywords']
        query = "insert into skills(resume_id, name, level, keywords) values(%s, %s, %s, %s)"
        value = (resume_id, name, level, keywords)
        mycursor.execute(query, value)
        # mydb.commit      
    
    # languages
    languages = data['languages']
    for i in languages:
        language = i['languageName']
        fluency = i['languagesFluency']
        query = "insert into languages(resume_id, language, fluency) values(%s, %s, %s)"
        value = (resume_id, language, fluency)
        mycursor.execute(query, value)


    # interests
    interests = data['interests']
    for i in interests:
        name = i['interestName']
        keywords = i['interestKeywords']
        query = "insert into interests(resume_id, name, keywords) values(%s, %s, %s)"
        value = (resume_id, name, keywords)
        mycursor.execute(query, value)        
    # mydb.commit

    # references
    references = data['reference']
    for i in references:
        name = i['referrerName']
        reference = i['reference']
        query = "insert into `references`(resume_id, name, reference) values(%s, %s, %s)"
        value = (resume_id, name, reference)
        mycursor.execute(query, value)

    # projects
    projects = data['projects']
    for i in projects:
        name = i['projectName']
        description = i['projectDescription']
        highlights = i['projectHighlights']
        keywords = i['projectKeywords']
        startDate = i['projectStartDate']
        endDate = i['projectEndDate']
        url = i['projectUrl']
        roles = i['projectRoles']
        entity = i['projectEntity']
        type = i['projectType']
        query = "insert into projects(resume_id, name, description, startDate, endDate, url, entity, type, highlights, keywords, roles) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, name, description, startDate, endDate, url, entity, type, highlights, keywords, roles)
        mycursor.execute(query, value)
    mydb.commit()
    # END OF BUILD RESUME

def delete_record(id):
    query = ("DELETE FROM basics WHERE resume_id = %s")
    mycursor.execute(query, (id,))    
    mydb.commit()
    # END OF DELETE

def update_record(id, data):
    query = ("DELETE FROM basics WHERE resume_id = %s")
    mycursor.execute(query, (id,))    
    mydb.commit()
    # basics
    resume_id = id
    coverLetter = data['coverLetter']
    basics = data['basics']
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
    query = "insert into basics(resume_id, name, label, image, email, phone, url, \
                summary, address, postalCode, city, countryCode, region, coverLetter) \
                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (resume_id, name, label, image, email, phone, url, summary,
            address, postalCode, city, countryCode, region, coverLetter)
    mycursor.execute(query, value)


    # profiles
    profiles = basics['profiles']
    for i in profiles:
        network = i['network']
        profile_username = i['username']
        profile_url = i['url']
        query = "INSERT INTO profiles(resume_id, network, username, url) VALUES(%s, %s, %s, %s)"
        value = (resume_id, network, profile_username, profile_url)
        mycursor.execute(query, value)
        # mydb.commit()

    # work
    work = data['work']
    for i in work:
        companyName = i['companyName']
        location = i['companyLocation']
        description = i['workDescription']
        position = i['workPosition']
        url = i['companyUrl']
        startDate = i['workStartDate']
        endDate = i['workEndDate']
        summary = i['workSummary']
        highlights = i['workHighlights']
        keywords = i['workKeywords']
        query = "insert into work(resume_id, companyName, location, description, position, url, startDate, endDate, summary, highlights, keywords) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, companyName, location, description, position, 
                url, startDate, endDate, summary, highlights, keywords)
        mycursor.execute(query, value)
        # mydb.commit()
    
    # volunteer
    volunteer = data['volunteer']
    for i in volunteer:
        organization = i['volunteerOrganization']
        position = i['volunteerPosition']
        url = i['organizationUrl']
        startDate = i['volunteeringStartDate']
        endDate = i['volunteeringEndDate']
        summary = i['volunteerSummary']
        highlights = i['volunteeringHighlights']
        query = "insert into volunteer(resume_id, organization, position, url, startDate, endDate, summary, highlights) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, organization, position, url, startDate, endDate, summary, highlights)    
        mycursor.execute(query, value)   

    # education
    education = data['education']
    for i in education:
        institution = i['educationInstitution']
        url = i['institutionUrl']
        area = i['educationArea']    
        studyType = i['educationStudyType']
        startDate = i['educationStartDate']
        endDate = i['educationEndDate']
        score = i['educationScore']
        courses = i['educationCourses']
        query = "insert into education(resume_id, institution, url, \
                area, studyType, startDate, endDate, score) \
                values(%s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, institution, url, area, studyType, startDate, endDate, score)
        mycursor.execute(query, value)
        mycursor.execute("SELECT MAX(education_id) FROM education")
        result = mycursor.fetchall()
        education_id = result[0][0]
        for item in courses:
            query = "insert into education_courses(education_id,courses) values(%s,%s)"
            value = (education_id,item)
            mycursor.execute(query, value)
            # mydb.commit()

    #awards
    awards = data['awards']
    for i in awards:
        title = i['awardTitle']
        date = i['awardedDate']
        awarder = i['awarder']
        summary = i['awardSummary']
        query = "insert into awards(resume_id, title, date, awarder, summary) values(%s, %s, %s, %s, %s)"
        value = (resume_id, title, date, awarder, summary)
        mycursor.execute(query, value)
        # mydb.commit()

    # certificates
    certificates = data['certificates']
    for i in certificates:
        name = i['certificateName']
        date = i['certificatesIssueDate']
        url = i['certificateUrl']
        issuer = i['certificateIssuer']
        query = "insert into certificates(resume_id, name, date, url, issuer) values(%s, %s, %s, %s, %s)"
        value = (resume_id, name, date, url, issuer)
        mycursor.execute(query, value)
        # mydb.commit()

    # publications
    publications = data['publications']
    for i in publications:
        name = i['publicationTitle']
        publisher = i['publisher']
        releaseDate = i['publishedDate']
        url = i['publishedUrl']
        summary = i['publicationSummary']
        query = "insert into publications(resume_id, name, publisher, releaseDate, url, summary) values(%s, %s, %s, %s, %s, %s)"
        value = (resume_id, name, publisher, releaseDate, url, summary)
        mycursor.execute(query, value)
        # mydb.commit()

    # skills
    skills = data['skills']
    for i in skills:
        name = i['skillName']
        level = i['skillLevel']
        keywords = i['skillKeywords']
        query = "insert into skills(resume_id, name, level, keywords) values(%s, %s, %s, %s)"
        value = (resume_id, name, level, keywords)
        mycursor.execute(query, value)
        # mydb.commit      
    
    # languages
    languages = data['languages']
    for i in languages:
        language = i['languageName']
        fluency = i['languagesFluency']
        query = "insert into languages(resume_id, language, fluency) values(%s, %s, %s)"
        value = (resume_id, language, fluency)
        mycursor.execute(query, value)


    # interests
    interests = data['interests']
    for i in interests:
        name = i['interestName']
        keywords = i['interestKeywords']
        query = "insert into interests(resume_id, name, keywords) values(%s, %s, %s)"
        value = (resume_id, name, keywords)
        mycursor.execute(query, value)        
    # mydb.commit

    # references
    references = data['reference']
    for i in references:
        name = i['referrerName']
        reference = i['reference']
        query = "insert into `references`(resume_id, name, reference) values(%s, %s, %s)"
        value = (resume_id, name, reference)
        mycursor.execute(query, value)

    # projects
    projects = data['projects']
    for i in projects:
        name = i['projectName']
        description = i['projectDescription']
        highlights = i['projectHighlights']
        keywords = i['projectKeywords']
        startDate = i['projectStartDate']
        endDate = i['projectEndDate']
        url = i['projectUrl']
        roles = i['projectRoles']
        entity = i['projectEntity']
        type = i['projectType']
        query = "insert into projects(resume_id, name, description, startDate, endDate, url, entity, type, highlights, keywords, roles) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (resume_id, name, description, startDate, endDate, url, entity, type, highlights, keywords, roles)
        mycursor.execute(query, value)
    mydb.commit()


# LIST ALL RESUMES
async def list_all_resume(request):
    list_of_resume = list_resume()
    print("done")
    return JSONResponse(list_of_resume)

# GET DATA FROM SINGLE RESUME
async def resume_data(request):
    id = request.path_params['resume_id']
    resume_data = call_resume(id)
    return JSONResponse(resume_data)
    
# ADD A NEW RESUME
async def create_resume(request):
    data = await request.json()
    result = build_resume(data)
    return JSONResponse({"Resume":"Added"})

# UPDATE A RESUME
async def update_resume(request):
    id = request.path_params['resume_id']
    data = await request.json()
    result = update_record(id, data)
    return JSONResponse({"Resume Updated":id})

# DELETE A RESUME
async def delete_resume(request):
    id = request.path_params['resume_id']
    result = delete_record(id)
    return JSONResponse({"Resume Deleted":id})

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
    ]

routes = [
    Route("/resume", endpoint= list_all_resume, methods= ["GET"]),
    Route("/resume", endpoint= create_resume, methods= ["POST"]),
    Route("/resume/{resume_id:int}", endpoint=resume_data, methods= ["GET"]),
    Route("/resume/{resume_id:int}", endpoint= update_resume, methods= ["PUT"]),
    Route("/resume/{resume_id:int}", endpoint=delete_resume, methods= ["DELETE"])
]

app = Starlette(
    routes = routes, middleware= middleware
)