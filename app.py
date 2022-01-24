from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
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
mycursor.execute("show tables")
for i in mycursor:
    print(i)

# def work(response):
#     print("############################\n",response)
#===================================================================
response = dict()
api = dict()
async def homepage(request):
    apiresp = requests.get("http://127.0.0.1:8000/hello")
    print(apiresp)
    print("#===================================================================")
    print(type(apiresp))
    print("#===================================================================")
    #apiresp = {'id': 1, 'coverLetter': 'Some text', 'basics': {'name': 'Richard Hendriks', 'label': 'Programmer', 'image': 'https://i.pravatar.cc/150?img=8', 'email': 'richard.hendriks@mail.com', 'phone': '(912) 555-4321', 'url': 'http://richardhendricks.example.com', 'summary': 'Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!', 'location': {'address': '2712 Broadway St', 'postalCode': 'CA 94115', 'city': 'San Francisco', 'countryCode': 'US', 'region': 'California'}, 'profiles': [{'network': 'Twitter', 'username': 'neutralthoughts', 'url': 'https://twitter.com/neutralthoughts'}, {'network': 'SoundCloud', 'username': 'dandymusicnl', 'url': 'https://soundcloud.example.com/dandymusicnl'}]}, 'work': [{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']}], 'volunteer': [{'organization': 'CoderDojo', 'position': 'Teacher', 'url': 'http://coderdojo.example.com/', 'startDate': '2012-01-01', 'endDate': '2013-01-01', 'summary': 'Global movement of free coding clubs for young people.', 'highlights': ["Awarded 'Teacher of the Month'"]}], 'education': [{'institution': 'University of Oklahoma', 'url': 'https://www.ou.edu/', 'area': 'Information Technology', 'studyType': 'Bachelor', 'startDate': '2011-06-01', 'endDate': '2014-01-01', 'score': '4.0', 'courses': ['DB1101 - Basic SQL', 'CS2011 - Java Introduction']}], 'awards': [{'title': 'Digital Compression Pioneer Award', 'date': '2014-11-01', 'awarder': 'Techcrunch', 'summary': 'There is no spoon.'}], 'publications': [{'name': 'Video compression for 3d media', 'publisher': 'Hooli', 'releaseDate': '2014-10-01', 'url': 'http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data.'}, {'name': 'Video compression for 3d media part 2', 'publisher': 'Hooli', 'releaseDate': '2015-10-01', 'url': 'http://hooli.com', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data. Again!'}], 'skills': [{'name': 'Web Development', 'level': 'Master', 'keywords': ['HTML', 'CSS', 'Javascript']}, {'name': 'Compression', 'level': 'Master', 'keywords': ['Mpeg', 'MP4', 'GIF']}], 'languages': [{'language': 'English', 'fluency': 'Native speaker'}], 'interests': [{'name': 'Wildlife', 'keywords': ['Ferrets', 'Unicorns']}], 'references': [{'name': 'Erlich Bachman', 'reference': 'It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.'}], 'projects': [{'name': 'Miss Direction', 'description': 'A mapping engine that misguides you', 'highlights': ['Won award at AIHacks 2016', 'Built by all women team of newbie programmers', 'Using modern technologies such as GoogleMaps, Chrome Extension and Javascript'], 'keywords': ['GoogleMaps', 'Chrome Extension', 'Javascript'], 'startDate': '2016-08-24', 'endDate': '2016-08-24', 'url': 'missdirection.example.com', 'roles': ['Team lead', 'Designer'], 'entity': 'Smoogle', 'type': 'application'}], 'meta': {'canonical': 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json', 'version': 'v1.0.0', 'lastModified': '2017-12-24T15:53:00'}, '__translation__': {'awards': 'Prizes', 'volunteers': 'Volunteers', 'skills': 'Skills', 'references': 'References', 'publications': 'Publications', 'languages': 'Languages', 'interests': 'Interests', 'education': 'Education', 'summary': 'Summary', 'experience': 'Experience', 'at': 'at'}, 'enableSourceDataDownload': True}
    api = apiresp.json()
    print("HELLO")
    global response
    response = api
    # work(response)
    print(type(api))
    print("-------------")
    print(type(api))
    print("-------------")
    id = api['id']
    print(id)
    coverLetter = api['coverLetter']
    print(coverLetter)
    basics = api['basics']
    print("-------------")
    print(basics['profiles'])
    return JSONResponse({'hello':'world'})

async def nextpage(request):
    return PlainTextResponse('hello world')

async def app(request):
    return JSONResponse({'hello':'world'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/hello', nextpage),
    Route('/h', app),
])

#=======================================================================================================================
#print

#=======================================================================================================================
print("++++++++++++++++++++++++++++++++++++++++++++++++\n",response)
'''
api = {'id': 1, 'coverLetter': 'Some text', 
        'basics': {'name': 'Richard Hendriks', 'label': 'Programmer', 
                    'image': 'https://i.pravatar.cc/150?img=8', 'email': 'richard.hendriks@mail.com', 
                    'phone': '(912) 555-4321', 'url': 'http://richardhendricks.example.com', 
                    'summary': 'Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!', 
                    'location': {'address': '2712 Broadway St', 'postalCode': 'CA 94115', 'city': 'San Francisco', 'countryCode': 'US', 'region': 'California'}, 
                    'profiles': [{'network': 'Twitter', 'username': 'neutralthoughts', 'url': 'https://twitter.com/neutralthoughts'}, 
                        {'network': 'SoundCloud', 'username': 'dandymusicnl', 'url': 'https://soundcloud.example.com/dandymusicnl'}]}, 
        'work': [{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 
                    'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 
                    'keywords': ['Javascript', 'React']}], 
        'volunteer': [{'organization': 'CoderDojo', 'position': 'Teacher', 'url': 'http://coderdojo.example.com/', 'startDate': '2012-01-01', 'endDate': '2013-01-01', 'summary': 'Global movement of free coding clubs for young people.', 'highlights': ["Awarded 'Teacher of the Month'"]}], 
        'education': [{'institution': 'University of Oklahoma', 'url': 'https://www.ou.edu/', 'area': 'Information Technology', 'studyType': 'Bachelor', 'startDate': '2011-06-01', 'endDate': '2014-01-01', 'score': '4.0', 
                'courses': ['DB1101 - Basic SQL', 'CS2011 - Java Introduction']}], 
        'awards': [{'title': 'Digital Compression Pioneer Award', 'date': '2014-11-01', 'awarder': 'Techcrunch', 'summary': 'There is no spoon.'}], 
        'publications': [{'name': 'Video compression for 3d media', 'publisher': 'Hooli', 'releaseDate': '2014-10-01', 'url': 'http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data.'}, {'name': 'Video compression for 3d media part 2', 'publisher': 'Hooli', 'releaseDate': '2015-10-01', 'url': 'http://hooli.com', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data. Again!'}], 
        'institutionskills': [{'name': 'Web Development', 'level': 'Master', 'keywords': ['HTML', 'CSS', 'Javascript']}, {'name': 'Compression', 'level': 'Master', 'keywords': ['Mpeg', 'MP4', 'GIF']}], 
        'languages': [{'language': 'English', 'fluency': 'Native speaker'}], 
        'interests': [{'name': 'Wildlife', 'keywords': ['Ferrets', 'Unicorns']}], 
        'references': [{'name': 'Erlich Bachman', 'reference': 'It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.'}], 
        'projects': [{'name': 'Miss Direction', 'description': 'A mapping engine that misguides you', 'highlights': ['Won award at AIHacks 2016', 'Built by all women team of newbie programmers', 'Using modern technologies such as GoogleMaps, Chrome Extension and Javascript'], 'keywords': ['GoogleMaps', 'Chrome Extension', 'Javascript'], 'startDate': '2016-08-24', 'endDate': '2016-08-24', 'url': 'missdirection.example.com', 'roles': ['Team lead', 'Designer'], 'entity': 'Smoogle', 'type': 'application'}], 'meta': {'canonical': 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json', 'version': 'v1.0.0', 'lastModified': '2017-12-24T15:53:00'}, '__translation__': {'awards': 'Prizes', 'volunteers': 'Volunteers', 'skills': 'Skills', 'references': 'References', 'publications': 'Publications', 'languages': 'Languages', 'interests': 'Interests', 'education': 'Education', 'summary': 'Summary', 'experience': 'Experience', 'at': 'at'}, 'enableSourceDataDownload': True}
id = api['id']
print("=============================")
print(id)
coverLetter = api['coverLetter']
basics = api['basics']
print("-----------------------------------------")
print(basics)
print("-----------------------------------------")
name = basics['name']
label = basics['label']
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

print("-----------------------------------------")
print(name,"\n",label,"\n",email,"\n",phone,"\n",url,"\n",summary,
"\n-------\n",address,"\n",postalCode,"\n",city,"\n",countryCode,"\n",region,
"\n-----------------------------------------\n")

profiles = basics['profiles']
print(profiles)
print("-----------------------------------------")

network  = list()
username = list()
url = list()
for i in range(len(profiles)):
    network.append(profiles[i]['network'])
    username.append(profiles[i]['username'])
    url.append(profiles[i]['url'])

print(network,"\n",username,"\n",url)
print("-----------------------------------------")

work = api['work']
print(work)
print("-----------------------------------------")
workname = list()
worklocation = list()
workdescription = list()
workposition = list()
workurl = list()
workstartdate = list()
workenddate = list()
worksummary = list()
for i in range(len(work)):
    workname.append(work[i]['name'])
    worklocation.append(work[i]['location'])
    workdescription.append(work[i]['description'])
    workurl.append(work[i]['url'])
    workstartdate.append(work[i]['startDate'])
    workenddate.append(work[i]['endDate'])
    worksummary.append(work[i]['summary'])

print(workname)
print(worklocation)
print(workdescription)
print(workurl)
print(workstartdate)
print(workenddate)
print(worksummary)

samplevalue = (name,workname[0],worklocation[0],workdescription[0])
qq="insert into sample1 (sampleid, name, label, image) values(%s,%s,%s,%s)"
mycursor.execute(qq,samplevalue)
mydb.commit()

'''
#==============================================================================================



'''
async def app(request):
   return JSONResponse({"re":"vfv"})

async def homepage(request):
    apiresp = requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume/1")
    apiresp = {'id': 1, 'coverLetter': 'Some text', 'basics': {'name': 'Richard Hendriks', 'label': 'Programmer', 'image': 'https://i.pravatar.cc/150?img=8', 'email': 'richard.hendriks@mail.com', 'phone': '(912) 555-4321', 'url': 'http://richardhendricks.example.com', 'summary': 'Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!', 'location': {'address': '2712 Broadway St', 'postalCode': 'CA 94115', 'city': 'San Francisco', 'countryCode': 'US', 'region': 'California'}, 'profiles': [{'network': 'Twitter', 'username': 'neutralthoughts', 'url': 'https://twitter.com/neutralthoughts'}, {'network': 'SoundCloud', 'username': 'dandymusicnl', 'url': 'https://soundcloud.example.com/dandymusicnl'}]}, 'work': [{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']}], 'volunteer': [{'organization': 'CoderDojo', 'position': 'Teacher', 'url': 'http://coderdojo.example.com/', 'startDate': '2012-01-01', 'endDate': '2013-01-01', 'summary': 'Global movement of free coding clubs for young people.', 'highlights': ["Awarded 'Teacher of the Month'"]}], 'education': [{'institution': 'University of Oklahoma', 'url': 'https://www.ou.edu/', 'area': 'Information Technology', 'studyType': 'Bachelor', 'startDate': '2011-06-01', 'endDate': '2014-01-01', 'score': '4.0', 'courses': ['DB1101 - Basic SQL', 'CS2011 - Java Introduction']}], 'awards': [{'title': 'Digital Compression Pioneer Award', 'date': '2014-11-01', 'awarder': 'Techcrunch', 'summary': 'There is no spoon.'}], 'publications': [{'name': 'Video compression for 3d media', 'publisher': 'Hooli', 'releaseDate': '2014-10-01', 'url': 'http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data.'}, {'name': 'Video compression for 3d media part 2', 'publisher': 'Hooli', 'releaseDate': '2015-10-01', 'url': 'http://hooli.com', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data. Again!'}], 'skills': [{'name': 'Web Development', 'level': 'Master', 'keywords': ['HTML', 'CSS', 'Javascript']}, {'name': 'Compression', 'level': 'Master', 'keywords': ['Mpeg', 'MP4', 'GIF']}], 'languages': [{'language': 'English', 'fluency': 'Native speaker'}], 'interests': [{'name': 'Wildlife', 'keywords': ['Ferrets', 'Unicorns']}], 'references': [{'name': 'Erlich Bachman', 'reference': 'It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.'}], 'projects': [{'name': 'Miss Direction', 'description': 'A mapping engine that misguides you', 'highlights': ['Won award at AIHacks 2016', 'Built by all women team of newbie programmers', 'Using modern technologies such as GoogleMaps, Chrome Extension and Javascript'], 'keywords': ['GoogleMaps', 'Chrome Extension', 'Javascript'], 'startDate': '2016-08-24', 'endDate': '2016-08-24', 'url': 'missdirection.example.com', 'roles': ['Team lead', 'Designer'], 'entity': 'Smoogle', 'type': 'application'}], 'meta': {'canonical': 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json', 'version': 'v1.0.0', 'lastModified': '2017-12-24T15:53:00'}, '__translation__': {'awards': 'Prizes', 'volunteers': 'Volunteers', 'skills': 'Skills', 'references': 'References', 'publications': 'Publications', 'languages': 'Languages', 'interests': 'Interests', 'education': 'Education', 'summary': 'Summary', 'experience': 'Experience', 'at': 'at'}, 'enableSourceDataDownload': True}
    api = apiresp.json()
    print(api)
    print("-------------")
    print(type(api))
    print("-------------")
    id = api['id']
    print(id)
    coverLetter = api['coverLetter']
    print(coverLetter)
    basics = api['basics']
    print("-------------")
    print(basics['profiles'])
    return JSONResponse({'hello':'world'})

async def nextpage(request):
    return PlainTextResponse("Hello")

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/hello', nextpage),
    Route('/h', app),
])
'''