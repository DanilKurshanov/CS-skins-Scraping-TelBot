from fake_useragent import UserAgent
import requests
import json

user_agent = UserAgent()


def collect_data(category_type=2):

    offset = 0
    batch_size = 60
    result = []
    flag = True

    while flag:

        for item in range(offset, offset + batch_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&type={category_type}&withStack=true'
            response = requests.get(
                url=url,
                headers={'user-agent': f'{user_agent.random}'})

            offset += batch_size

            data = response.json()

            if data != {'error': 2}:
                # print(data)

                items = data.get('items')

                for i in items:
                    if i.get('overprice') is not None and i.get('overprice') < -10:
                        item_full_name = i.get('fullName')
                        item_3d = i.get('3d')
                        item_price = i.get('price')
                        item_over_price = i.get('overprice')

                        result.append(
                            {
                                'full_name': item_full_name,
                                '3d': item_3d,
                                'overprice': item_over_price,
                                'item_price': item_price
                            }
                        )
            else:
                flag = False
                break

        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

def main():
    collect_data()

if __name__ == '__main__':
    main()