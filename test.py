#a = {'id':1, 'key':[{"hello":25},{"ball":25}]}
#print(a['key'])

import json
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
# mycursor.execute("select json_object('institution', education.institution, 'courses', education_courses.courses) from education inner join education_courses on education.educationno = education_courses.educationno where education.educationno =1;")
# # ith chey ^
# myresult = mycursor.fetchall()
# print(myresult[0][0])

mycursor.execute("select json_object('id',id,'name', name) from basics where id = 920 union select json_object('language', language, 'fluency', fluency) from languages where id = 920")
result = mycursor.fetchall()
# print(result)
# print(type(result))
api = {'id': 1, 'coverLetter': 'Some text', 
        'basics': {'name': 'Richard Hendriks',	 
					'label': 'Programmer', 
                    'image': 'https://i.pravatar.cc/150?img=8', 
					'email': 'richard.hendriks@mail.com', 
                    'phone': '(912) 555-4321', 
					'url': 'http://richardhendricks.example.com', 
                    'summary': 'Richard hails from Tulsa. He has earned degrees from the University of Oklahoma and Stanford. (Go Sooners and Cardinal!) Before starting Pied Piper, he worked for Hooli as a part time software developer. While his work focuses on applied information theory, mostly optimizing lossless compression schema of both the length-limited and adaptive variants, his non-work interests range widely, everything from quantum computing to chaos theory. He could tell you about it, but THAT would NOT be a “length-limited” conversation!', 
                    'location': {'address': '2712 Broadway St', 
									'postalCode': 'CA 94115', 
									'city': 'San Francisco', 
									'countryCode': 'US', 
									'region': 'California'}, 
                    'profiles': [{'network': 'Twitter', 
									'username': 'neutralthoughts', 
									'url': 'https://twitter.com/neutralthoughts'}, 
                        		{'network': 'SoundCloud', 
								'username': 'dandymusicnl', 
								'url': 'https://soundcloud.example.com/dandymusicnl'}]}, 
        'work': [{'name': 'Pied Piper', 
					'location': 'Palo Alto, CA', 
					'description': 'Awesome compression company', 
					'position': 'CEO/President', 
					'url': 'http://piedpiper.example.com', 
					'startDate': '2013-12-01', 
					'endDate': '2014-12-01', 
					'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 
                    'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 
                    'keywords': ['Javascript', 'React']},
                    ], 
        'volunteer': [{'organization': 'CoderDojo', 
						'position': 'Teacher', 
						'url': 'http://coderdojo.example.com/', 
						'startDate': '2012-01-01', 
						'endDate': '2013-01-01', 
						'summary': 'Global movement of free coding clubs for young people.', 
						'highlights': ["Awarded 'Teacher of the Month'"]}], 
        'education': [{'institution': 'University of Oklahoma', 'url': 'https://www.ou.edu/', 'area': 'Information Technology', 'studyType': 'Bachelor', 'startDate': '2011-06-01', 'endDate': '2014-01-01', 'score': '4.0', 
                'courses': ['DB1101 - Basic SQL', 'CS2011 - Java Introduction']}], 
        'awards': [{'title': 'Digital Compression Pioneer Award', 'date': '2014-11-01', 'awarder': 'Techcrunch', 'summary': 'There is no spoon.'}], 
        'publications': [{'name': 'Video compression for 3d media', 'publisher': 'Hooli', 'releaseDate': '2014-10-01', 'url': 'http://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data.'}, {'name': 'Video compression for 3d media part 2', 'publisher': 'Hooli', 'releaseDate': '2015-10-01', 'url': 'http://hooli.com', 'summary': 'Innovative middle-out compression algorithm that changes the way we store data. Again!'}], 
        'skills': [{'name': 'Web Development', 'level': 'Master', 'keywords': ['HTML', 'CSS', 'Javascript']}, {'name': 'Compression', 'level': 'Master', 'keywords': ['Mpeg', 'MP4', 'GIF']}], 
        'languages': [{'language': 'English', 'fluency': 'Native speaker'}], 
        'interests': [{'name': 'Wildlife', 'keywords': ['Ferrets', 'Unicorns']}], 
        'references': [{'name': 'Erlich Bachman', 'reference': 'It is my pleasure to recommend Richard, his performance working as a consultant for Main St. Company proved that he will be a valuable addition to any company.'}], 
        'projects': [{'name': 'Miss Direction', 'description': 'A mapping engine that misguides you', 'highlights': ['Won award at AIHacks 2016', 'Built by all women team of newbie programmers', 'Using modern technologies such as GoogleMaps, Chrome Extension and Javascript'], 'keywords': ['GoogleMaps', 'Chrome Extension', 'Javascript'], 'startDate': '2016-08-24', 'endDate': '2016-08-24', 'url': 'missdirection.example.com', 'roles': ['Team lead', 'Designer'], 'entity': 'Smoogle', 'type': 'application'}], 'meta': {'canonical': 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/resume.json', 'version': 'v1.0.0', 'lastModified': '2017-12-24T15:53:00'}, '__translation__': {'awards': 'Prizes', 'volunteers': 'Volunteers', 'skills': 'Skills', 'references': 'References', 'publications': 'Publications', 'languages': 'Languages', 'interests': 'Interests', 'education': 'Education', 'summary': 'Summary', 'experience': 'Experience', 'at': 'at'}, 'enableSourceDataDownload': True}
# id, coverLetter
mycursor.execute('''SELECT id,coverLetter FROM basics where id = 920''')
rv = mycursor.fetchall()
row_headers = [x[0] for x in mycursor.description]
json_data=[]
for result in rv:
	json_data.append(dict(zip(row_headers, result)))
x = json.dumps(json_data[0])
# basics: name, label, image, email, phone, url, summary
mycursor.execute('''SELECT name, label, image, email, phone, url, summary FROM basics where id = 920''')
rv = mycursor.fetchall()
row_headers = [x[0] for x in mycursor.description]
json_data1 = []
for result in rv:
	json_data1.append(dict(zip(row_headers, result)))
x = json.dumps(json_data1[0])
# basics: location: 
mycursor.execute('''SELECT address, postalCode, city, countryCode, region FROM basics where id = 920''')
rv = mycursor.fetchall()
print("-------\n",rv)
row_headers = [x[0] for x in mycursor.description]
print("\n",row_headers,"\n")
json_data2 = []
json_data3 = dict()
for results in rv:
	print(row_headers,"-",results,"----\n")
	json_data2.append(dict(zip(row_headers, results)))
json_data3.update({"location": json_data2[0]})
print(json_data3,"\n^^^^^^^^^^\n")

json_data1[0].update(json_data3)
json_basics = {"basics":json_data1[0]}
# json_data[0].update({"basics":json_data1[0]})
# json_data[0].update(json_basics)
print(json_data[0])
print(type(json_data[0]))

mycursor.execute('''SELECT COUNT(profileno) from profiles where id = 920''')
count = mycursor.fetchall()[0][0]
print(count)
json_profiles = []
# for i in range(count):
mycursor.execute('''SELECT network, username, url from profiles where id = 920''')
rv = mycursor.fetchall()
print("#\n",rv,"\n")
row_headers = [x[0] for x in mycursor.description]
for results in rv:
	json_profiles.append(dict(zip(row_headers, results)))
print("############",json_profiles)
# profiles_data = {"profiles":json_profiles}
# print(profiles_data)
######################
json_data3.update({"profiles":json_profiles})
print(json_data3)
json_basics.update(json_data3)
print("\n!!!!!!!!!!!!!\n",json_basics)

# print("!!!!!!!!!!!!!!\n",json_basics,"\n",)
# json_data[0].update(json_basics)
# print(json_data[0])















# print(api,"\n")
# id = api['id']
# coverLetter = api['coverLetter']
# basics = api['basics']
# name = basics['name']
# label = basics['label']
# image = basics['image']
# email = basics['email']
# phone = basics['phone']
# url = basics['url']
# summary = basics['summary']
# location = basics['location']
# address = location['address']
# postalCode = location['postalCode']
# city = location['city']
# countryCode = location['countryCode']
# region = location['region']

# query = "insert into basics(id, name, label, image, email, phone, url, summary, address, postalCode, city, countryCode, region, coverLetter) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# value = (id, name, label, image, email, phone, url, summary,
#             address, postalCode, city, countryCode, region, coverLetter)
# mycursor.execute(query, value)
# mydb.commit()


# profiles = [{'network': 'Twitter', 'username': 'neutralthoughts', 'url': 'https://twitter.com/neutralthoughts'}, 
#             {'network': 'SoundCloud', 'username': 'dandymusicnl', 'url': 'https://soundcloud.example.com/dandymusicnl'}]
# network = list()
# profile_username = list()
# profile_url = list()
# for i in range(len(profiles)):
#     network.append(profiles[i]['network'])
#     profile_username.append(profiles[i]['username'])
#     profile_url.append(profiles[i]['url'])
# query = "insert into profiles(profileno, id, network, username, url) values(%s, %s, %s, %s, %s)"
# mycursor.execute("SELECT MAX(profileno) FROM profiles")
# myresult = mycursor.fetchall()
# if (myresult[0][0] == None):
#     profileno = 1
# else:
#     profileno = myresult[0][0]
# for i in range(len(profiles)):
#     value = (profileno, id, network[i], profile_username[i], profile_url[i])
#     mycursor.execute(query, value)
#     mydb.commit()
#     profileno += 1

# # print(network,"\n",username,"\n",url)

# work = list()
# work = api['work']
# work_name, work_location, work_description, work_position = list(), list(), list(), list()
# work_url, work_startDate, work_endDate, work_summary = list(), list(), list(), list()
# work_hlights, work_keywords = list(), list()
# for i in range(len(work)):
#         work_name.append(work[i]['name'])
#         work_location.append(work[i]['location'])
#         work_description.append(work[i]['description'])
#         work_position.append(work[i]['position'])
#         work_url.append(work[i]['url'])
#         work_startDate.append(work[i]['startDate'])
#         work_endDate.append(work[i]['endDate'])
#         work_summary.append(work[i]['summary'])
#         work_hlights.append(work[i]['highlights'])
#         work_keywords.append(work[i]['keywords'])
# print(work_hlights)
# mycursor.execute("SELECT MAX(workno) FROM work")
# myresult = mycursor.fetchall()
# print(myresult)
# if (myresult[0][0] == None):
#     workno = 1
# else:
#     workno = myresult[0][0]
# print(workno)
# for i in range(len(work)):
#     query = "insert into work(workno, id, name, location, description, position, url, startDate, endDate, summary) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     value = (workno, id, work_name[i], work_location[i], work_description[i], work_position[i], 
#             work_url[i], work_startDate[i], work_endDate[i], work_summary[i])
#     mycursor.execute(query, value)
#     mydb.commit()
#     mycursor.execute("SELECT MAX(highlightsno) FROM work")
#     highlightsno = mycursor.fetchall()
#     highlightsno += 1
#     print("___________",highlightsno)
#     for j in range(len(work_hlights)):
#         query = "insert into work_highlights(workno, id, highlightsno, highlights) values(%s, %s, %s, %s)"
#         value = (workno, id, highlightsno, work_hlights[j])
#         mycursor.execute(query, value)
#         mydb.commit()
    
        

            
#     workno += 1
# #work_highlights
# # len_work_hlights = len(work_hlights)
# for i in range(len(work_hlights)):
#     for j in range(len(work_hlights[i])):
#         work_hlights[i][j]
#         query = "insert into work_highlights(workno, id,)"

# print(len)
# print(work_hlights[0],"\n1111111")
# print(work_hlights[1])






# print("-------------------------------------------")
# query = """SELECT CONCAT(CONCAT("{ 'id' : ", id, ", 'coverLetter' : '", coverLetter ),CONCAT("', 'basics' : { 'location' : '",address,"' }"))FROM basics where id = 920;"""
# mycursor.execute(query)
# myresult = mycursor.fetchall()
# print(myresult)
# print(myresult[0][0])
# myresult[0][0].replace("\\","")
# print(myresult[0][0])


# query = "SELECT 'id:' as , 'name:' as name FROM basics where id =920;" 
# mycursor.execute(query)
# myresult = mycursor.fetchall()
# print(myresult)
# print("!!!!!!!!!!!!!!!!!!!!")

########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################

# mycursor.execute('''SELECT id,coverLetter FROM basics where id = 920''')
# rv = mycursor.fetchall()
# # print(rv)
# row_headers = [x[0] for x in mycursor.description]
# json_data=[]
# for result in rv:
# 	json_data.append(dict(zip(row_headers, result)))
# x = json.dumps(json_data[0])
# # print(x)
# # print(type(x))

# # print("!!!!!!!!!!!!!!!!!!!!")
# mycursor.execute('''SELECT name, label, image, email, phone, url, summary FROM basics where id = 920''')
# rv = mycursor.fetchall()
# print(rv)
# row_headers = [x[0] for x in mycursor.description]
# json_data1=[]
# for result in rv:
# 	json_data1.append(dict(zip(row_headers, result)))
# x = json.dumps(json_data1[0])
# print(x)
# print(type(x))

# json_data[0].update({"basics":json_data1[0]})

# y = json_data[0]
# json_data[0].update(json_data1[0])
# print(json_data[0])
# print(type(json_data[0]))



# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# print(api)