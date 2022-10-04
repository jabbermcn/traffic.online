import logging

import requests
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import TOKEN

dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message()
async def get_results(message: Message):
    headers = {
        'authority': 'api.traffic.online',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJ4NXQiOiJaVEl5WTJNeFlUSXpZV0poWXpnM016Um1abUl3TVdOaU56ZGlPVEkwWVdZd1pESmxNMk5rWVRZMVpEUTFOall4WWpreE5XVmxPRFF3WkRKbFpEbGtOdyIsImtpZCI6IlpUSXlZMk14WVRJellXSmhZemczTXpSbVptSXdNV05pTnpkaU9USTBZV1l3WkRKbE0yTmtZVFkxWkRRMU5qWXhZamt4TldWbE9EUXdaREpsWkRsa053X1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJUb3RvbW90eUBtYWlsLnJ1IiwiYXVkIjoiRDB6b243SjF0WXVnRE13QTZRQVdRMjhpazk0YSIsIm5iZiI6MTY2NDkwMDQ0NSwicm9sZSI6IlRyYW5zcG9ydENvbXBhbnlBZG1pbiIsImNvbXBhbnlfaWQiOiJhYzI1OTdjZS1mZTFiLTRkNTQtYTViOS0yOTZiNjUxMmU4MzciLCJ1c2VyX2lkIjoiNzFhYjk2MjYtMmEwOC00NzFiLWE0ZGUtNTRlMTBkN2FhNDI0IiwiYXpwIjoiRDB6b243SjF0WXVnRE13QTZRQVdRMjhpazk0YSIsInNjb3BlIjoidHJhZmZpY19hdXRoIiwiaXNzIjoiaHR0cHM6XC9cL3RyYWZmaWMub25saW5lOjQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6MTY2NDkwNDA0NSwiaWF0IjoxNjY0OTAwNDQ1LCJqdGkiOiI0YTJlZDRiNi1jYzIyLTRlYzAtYmY3Yi1lMTNiZTI2YzNiNDEifQ.KgWxoyUqk3s_V0c-GTsTkZaGPT0V2wmwqfb4RJXRG23wfq44KcnUEL2yBoqF7VPNrOyE3M681dvGZx46I8oSP6PkLzKwz8FOcnFr8UFj7FTiAo1Zu7Kd3Jpdbu8XQyEZNMMCYhZvt0mcGBxMMF-ST4jLqT8toGKduKWwY2Z2zZ_vhiuoyzOomt3YLhedPdS2L5BOkaH8x_eCfcYF1H8v6kq4YUN5LriqePaqqgZHR0Yt7YDZ8y4vaRmcPu2LLCHGoREE-uNwk6rV3gUtlo_W-jx7Icz1EgqMr4zgR2-QbD7rmD928Thyy0Pe05tvcOiUzaIIQWX5RgJd85235j1Jlw',
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
    response = requests.get(url, headers=headers).json()
    total_res = response['page_info']['total_results']
    if total_res != 0:
        await message.reply(f'It is some changes. Total_results value = {total_res}')
    else:
        await message.reply(f'No changes')


def main() -> None:
    bot = Bot(TOKEN, parse_mode="HTML")
    dp.run_polling(bot)


if __name__ == "__main__":
    main()
