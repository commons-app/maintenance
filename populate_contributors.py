import json
import urllib2

GITHUB_GET_CONTRIBUTORS_API = "https://api.github.com/repos/commons-app/apps-android-commons/contributors"
response = urllib2.urlopen(GITHUB_GET_CONTRIBUTORS_API).read()
response_json = json.loads(response)
contributors = []
# Below is the format in which a table column element should be, to be considered for being rendered in a table
BASE_STRING = ' [<img src="image_url" width="100px;"/><br /><sub><b>user_name</b></sub>](profile_url) |'
i = 1
table_row = '|'
row_index = 0
for contributor in response_json:
    table_row = table_row + (
        BASE_STRING.replace("image_url", contributor['avatar_url']).replace("user_name", contributor['login'])).replace(
        "profile_url", contributor['url'])
    if i % 5 == 0:
        print table_row
        # Usually the first row is the header, here we dont need an header, so making the first row as header
        if row_index == 0:
            print '| :---: | :---: | :---: | :---: | :---: |'
        table_row = '|'
        row_index = row_index + 1
    i = i + 1
