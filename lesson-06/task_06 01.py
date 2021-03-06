from requests import get, utils
import requests
#x = utils.get_unicode_from_response(get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"))
log = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
log = log.text
print(log)
data = log.split("\n")
my_data = []
for i in range(1, len(data)):
    x = data[i].split()
    if len(x) > 6:
        my_tuple = (x[0], x[5].replace('"', ''), x[6])
        my_data.append(my_tuple)

for i in my_data:
    print(i)





