import requests
from pprint import pprint


def get_total_results():
    headers = {
        'authority': 'api.traffic.online',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': str(input(f'Enter the authorization key: ')),
        'origin': 'https://traffic.online',
        'referer': 'https://traffic.online/suggestions/requests?body_type[]=awning&body_type[]=refrigerator&body_type[]=isothermal&body_type[]=full_metal&from_location_geo=59.939084%7C30.315879&from_location_geo_fias_id=c2deb16a-0330-4f05-821f-1d09c93331e6&from_location_geo_label=%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3&from_radius=100&max_cargo_tonnage=24&max_cargo_volume=110&min_cargo_tonnage=6&min_cargo_volume=4&min_price=1&page=1&per_page=20&transport_loading_types[]=rear&visibility=all',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    url = 'https://api.traffic.online/api/v1/request_view?type\\[\\]=shipping_request&type\\[\\]=delivery&type\\[\\]=city_delivery&from_radius=100&body_type\\[\\]=awning&body_type\\[\\]=refrigerator&body_type\\[\\]=isothermal&body_type\\[\\]=full_metal&page=1&per_page=20&from_location_geo=59.939084%7C30.315879&min_cargo_tonnage=6&max_cargo_tonnage=24&min_cargo_volume=4&max_cargo_volume=110&min_price=1&transport_loading_types\\[\\]=rear'
    try:
        response = requests.get(url, headers=headers).json()
        pprint(response)
        total_res = response['page_info']['total_results']
        if total_res == 0:
            print(f'No changes. Total_results value = {total_res}')
        else:
            print(f'It is some changes. Total_results value = {total_res}')
    except Exception as ex:
        print(ex)
        print(f'Something wrong')


get_total_results()
