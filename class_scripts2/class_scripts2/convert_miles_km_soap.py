from zeep import Client

client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
result = client.service.ConvertSpeed(
    200, 'kilometersPerhour', 'milesPerhour')
print (result)
