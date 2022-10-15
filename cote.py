import requests

cookies = {
    'csrftoken': 'riBxCn6pqRtwzcQuJBtehAeODt1QTkGk',
}

headers = {
    'authority': 'www.sevenrooms.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'dnt': '1',
    'referer': 'https://www.sevenrooms.com/reservations/cote',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

avail_times = []

month = "12"
for day in range(1,31):
    date = f'{month}-{day}-2022'
    for t in range(360, 24*60, 15):
        h = t // 60 
        m = t % 60

        print(f"Checking {h}:{m:02} on {date}")

        response = requests.get(f'https://www.sevenrooms.com/api-yoa/availability/widget/range?venue=cote&time_slot={h}:{m:02}&party_size=4&halo_size_interval=16&start_date={date}&num_days=1&channel=SEVENROOMS_WIDGET', cookies=cookies, headers=headers)

        data = response.json()

        if int(day) < 10 and len(str(day)) == 1:
            day = "0" + str(day)

        if data["data"]["availability"][f'2022-{month}-{day}']:
            for time in data["data"]["availability"][f'2022-{month}-{day}'][0]["times"]:
                if f'{h}:{m:02}' in time["time_iso"] and "is_held" in time:
                    print("Available!")
                    avail_times.append(f"2022-{month}-{day} - {h}:{m:02}")

print(avail_times)

        

