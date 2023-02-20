from com.ibm.json.java import JSONObject, JSONArray

# create a JSON object
jsonObject = JSONObject()
jsonObject.put("equipment", mbo.getString("ASSETNUM"))
jsonObject.put("description", mbo.getString("DESCRIPTION"))

# Invoking an URL
url = "https://www.example.com/"
userid = None
passwd = None

# Invoke URL
response = service.httppostasjson(url, userid, passwd, None, jsonObject)

status = response.getStatusLine().getStatusCode()
obj = JSONArray.parse(response.getEntity().getContent())

if status == 200:
	# OK
else:
	# error
