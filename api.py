import argparse
import json
import datetime

import requests

team_name = "Хахатонщики"


def call_api(lat, lng, date):
    results_dict = {}
    
    API_KEY = "79a26ff8f69d41fcbdf9f0dbd7444f4e"
    date1 = date
    date2 = datetime.datetime.strptime(date1, "%Y-%m-%d") - datetime.timedelta(days=30)
    date2 = date2.date().strftime("%Y-%m-%d")
    url = f"https://api.weatherbit.io/v2.0/history/daily?lat={lat}&lon={lng}&start_date={date2}&end_date={date1}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results_dict = response.json()
    else:
        print(f'Ошибка: {response.status_code}')
        exit()
    return results_dict['data']



def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lat", type=float, help="Широта")
    parser.add_argument("--lng", type=float, help="Долгота")
    parser.add_argument("--date", type=str, help="Дата в формате YYYY-MM-DD")
    args = parser.parse_args()

    if not all([args.lat, args.lng, args.date]):
        print("Не все обязательные аргументы предоставлены.")
        parser.print_help()
        exit(1)

    results = call_api(args.lat, args.lng, args.date)
    save_json(results, f'{team_name}.json')
