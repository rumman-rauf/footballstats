# Changed the date format from dd/mm/yyyy to mm/dd/yyyy so that I can use the Javascript Date object

import json
for league in ['ucl','epl','aleague','seriea','laliga','ligue1']:
    with open(f"{league}.json") as f:
        data = json.load(f)

    for i in data:
        time = i['Date'][-4:]
        date =  i['Date'][:-5].split('/')
        i['Date'] = f"{date[1]}/{date[0]}/{date[2]}{time}"

    with open(f'{league}.json', 'w') as f:
        json.dump(data, f, indent=2)
