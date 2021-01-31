import requests
import json

country_cases = 'Poland'
url = "https://covid-api.mmediagroup.fr/v1/cases?country={}".format(country_cases)
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
a = json.loads(response.text)

# -----------------------------------
# sprawdzanie kluczy
expected = ['confirmed', 'recovered', 'deaths', 'country']
current = []

for key, value in a.items():
    for k, v in value.items():
        if k in expected:
            current.append(k)
assert expected == current

# -----------------------------------
# sprawdzanie wartosci
for key, value in a.items():
    for k, v in value.items():
        if k == 'country':
            country = v
        if k == 'continent':
            continent = v

assert country_cases == country
assert country_cases == 'Poland'

# -----------------------------------
# sprawdzanie odpowiedzi
assert response.status_code == 200

# -----------------------------------
# sprawdzanie niepoprawnego zapytania
url = "https://covid-api.mmediagroup.fr/v1/a?country={}".format(country_cases)  # zmiana endpointu z cases na a
response = requests.request("GET", url)
assert response.status_code == 403
