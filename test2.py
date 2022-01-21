work = [{'name': 'Pied Piper', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']},
        {'name': 'Pied Piper1', 'location': 'Palo Alto, CA', 'description': 'Awesome compression company', 'position': 'CEO/President', 'url': 'http://piedpiper.example.com', 'startDate': '2013-12-01', 'endDate': '2014-12-01', 'summary': 'Pied Piper is a multi-platform technology based on a proprietary universal compression algorithm that has consistently fielded high Weisman Scores™ that are not merely competitive, but approach the theoretical limit of lossless compression.', 'highlights': ['Build an algorithm for artist to detect if their music was violating copy right infringement laws', 'Successfully won Techcrunch Disrupt', 'Optimized an algorithm that holds the current world record for Weisman Scores'], 'keywords': ['Javascript', 'React']}]

work_name, work_location, work_description, work_position = list(), list(), list(), list()
work_url, work_startDate, work_endDate, work_summary = list(), list(), list(), list()
work_hlights, work_keywords = list(), list()

for i in range(len(work)):
    work_name.append(work[i]['name'])
    work_location.append(work[i]['location'])
    work_description.append(work[i]['description'])
    work_position.append(work[i]['position'])
    work_url.append(work[i]['url'])
    work_startDate.append(work[i]['startDate'])
    work_endDate.append(work[i]['endDate'])
    work_summary.append(work[i]['summary'])
    work_hlights.append(work[i]['highlights'])
    work_keywords.append(work[i]['keywords'])

print(work_name)
print(work_location)
print(work_description)
print(work_position)
print(work_url)
print(work_startDate)
print(work_endDate)
print(work_summary)
print(work_hlights)
