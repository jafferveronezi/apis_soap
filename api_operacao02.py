import requests

url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

headers = {'content-type': 'text/xml'}

print("Captial City for a Country")

body = """<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>US</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
            </soap:Envelope>"""
            
response = requests.post(url,data=body,headers=headers)
print(response.text)
