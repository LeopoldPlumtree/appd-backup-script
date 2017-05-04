import requests, json


def get_applications():
    # Switch for XML or JSON output
    output = "json"

    # Switch for User Authorization
    userAuth = "Basic "

    # Switch for Hostname
    conturl = "192.168.43.45"

    # Switch For Port
    contport = "8090"

    # Define BaseURL for individual HTTP requests
    baseURL = 'https://{url}:{port}/controller/ConfigObjectImportExportServlet?applicationId='.format(url=conturl, port=contport)

    # Send Request to get list of applications
    try:
        response = requests.get(
            url="https://{url}/controller/rest/applications".format(url=conturl,
            params={"output": output},
            headers={"Authorization": userAuth, },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    # Convert JSON to Python List
    applicationlist = json.loads(response.text)

    # Create List of application IDs
    IDList = [i['id'] for i in applicationlist if 'id' in i]

    # Iterate over list and create a HTTP request backup file for each object
    for i in IDList:
        req = requests.get(url=baseURL + '{appid}'.format(appid=i), params={"output": output}, headers={"Authorization": userAuth})
        file = open('app-{}-backup.xml'.format(i), 'w')
        file.write(req.text)
        file.close()


get_applications()


