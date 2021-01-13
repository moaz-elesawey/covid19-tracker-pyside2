## url => https://disease.sh/v3/covid-19/countries
import requests
from pprint import pprint
import json


URL = 'https://disease.sh/v3/covid-19/countries'

def get_countries_data(url=URL):
    print('[INFO] api called')
    _res = requests.get(url)
    _res_all = requests.get('https://disease.sh/v3/covid-19/all')
    _all = _res_all.json()

    _all_data = {
            'country_name': 'Worldwide',

            'cases': _all['cases'],
            'deaths': _all['deaths'],
            'recovered': _all['recovered'],

            'today_cases': _all['todayCases'],
            'today_deaths': _all['todayDeaths'],
            'today_recovered': _all['todayRecovered'],

            }

    _countries_data = _res.json()

    _modified_country_data = list(map(_make_our_data, _countries_data))

#     with open('_countries_data.json', 'w') as f:
#         f.write(json.dumps(_modified_country_data))

    _modified_country_data.insert(0, _all_data)



    return _modified_country_data

def _make_our_data(n):
    _data = {
            'id': n['countryInfo']['_id'],
            'country_code': n['countryInfo']['iso3'],
            'country_name': n['country'],
            'country_lat': n['countryInfo']['lat'],
            'country_lon': n['countryInfo']['long'],

            'cases': n['cases'],
            'deaths': n['deaths'],
            'recovered': n['recovered'],

            'today_cases': n['todayCases'],
            'today_deaths': n['todayDeaths'],
            'today_recovered': n['todayRecovered'],
        }
    return _data



if __name__ == '__main__':
    _modified_country_data = get_countries_data(URL)
    pprint(_modified_country_data[:10])

