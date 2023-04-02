import requests

url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

headers = {'content-type': 'text/xml'}

print("List of Countries by Name")

body = """<?xml version="1.0" encoding="utf-8"?>
            <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                <soap12:Body>
                    <ListOfCountryNamesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    </ListOfCountryNamesByName>
                </soap12:Body>
            </soap12:Envelope>"""

response = requests.post(url,data=body,headers=headers)
print(response.text)
