import pyodbc
import json
import collections
import requests

connstr = 'DRIVER={SQL Server};SERVER=67.227.0.42;DATABASE=ServiceRequest; UID=SA;PWD=70SR30ssD'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()

cursor.execute("""
            SELECT SRNUMBER, FirstName, LastName, Name
 FROM MYLA311 """)

rows = cursor.fetchall()

objects_list = []
for row in rows:
     d = collections.OrderedDict()
     d['SRNUMBER']= row.SRNUMBER
     d['FirstName']= row.FirstName
     d['LastName']= row.LastName
     d['Name']= row.Name

objects_list.append(d)

output = {
    'ServiceRequest': objects_list
}

j = json.dumps(output)
objects_file = 'C:\Users\Administrator\Desktop\JSONOutput.txt'
f = open(objects_file,'w')



url = "https://posttestserver.com/post.php"
data = j
headers = {'Content-type': 'text/plain', 'Accept': '/'}
r = requests.post(url, data= json.dumps(output), headers=headers)

print j
print >> f, j

print json.dumps(output, sort_keys=True, indent=4)

conn.close()
