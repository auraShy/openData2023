import requests

url1 =  "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2023-10-09T00%3A00%3A00UTC/fechafin/2023-10-10T00%3A00%3A00UTC/estacion/5641X"

def recogida_datos(url):
    
    querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkYXZpZGNhbXVuZXpAdW1hLmVzIiwianRpIjoiOWVmMjg1OTQtNDEwYS00MTljLTgyMTgtMTUzODcxNTgyMGE2IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2OTk3MDIyNDAsInVzZXJJZCI6IjllZjI4NTk0LTQxMGEtNDE5Yy04MjE4LTE1Mzg3MTU4MjBhNiIsInJvbGUiOiIifQ.aOBip8wkwms_HU3oL0ryt65Z7JG_3d0w9nIld8LN0rg"}

    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response
   

## Se obtiene la url de los datos:
response1 = recogida_datos(url1)
data = response1.json()
url_datos = data['datos']

## Se obtienen los datos climatológicos:
response2 = recogida_datos(url_datos)
print(response2.text)
