import json
import pprint

with open('allstars.json' , 'r') as file:
    date = json.load(file)

printer = pprint.PrettyPrinter()

page = date.get('current_page')
data = date.get('data')
first_page= 'https://pickstar.com.au/api/our-stars?page=1   '

next_page = date.get('next_page')
if next_page:
    pass

print('Page Number' ,page)
for onedata in data:
    id = onedata.get('id')
    Full_Name = onedata.get('name')
    Based = onedata.get('based_in')
    Sports_club = onedata.get('sport_club')
    if Based:
        Country = Based.get('name')
    print('Full Name  :',Full_Name , ' : Country :', Country,'  : Sports Club :',Sports_club)
