from com.ibm.json.java import JSONObject, JSONArray

# Invoking an URL
url = "https://www.example.com/"
userid = None
passwd = None

# Invoke URL
response = service.httpgetasjson(url, userid, None, passwd)

status = response.getStatusLine().getStatusCode()
obj = JSONArray.parse(response.getEntity().getContent())

if status == 200:
    # OK
else:
    # error
