import requests

url="http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

headers = {'content-type': 'text/xml'}

print("Currency for a Country")

body = """<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>US</sCountryISOCode>
                    </CountryCurrency>
                </soap:Body>
            </soap:Envelope>"""
            
response = requests.post(url,data=body,headers=headers)
print(response.text)


