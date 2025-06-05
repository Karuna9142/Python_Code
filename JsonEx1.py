import json
file = open("posts.json","r")
x = file.read()
finaldata = json.loads(x)

#print(finaldata);
for a in finaldata:
    print(a['title'],a['userid'])
