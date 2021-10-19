import requests
import json
from repo_updater import first_after

with open('repos.json', 'r') as f:
    data = f.read()

repos = json.loads(data)

with open('checks.json', 'r') as f:
    data = f.read()

checks = json.loads(data)

for period in repos:
    for repo in repos[period]:
        print(f'\nChecking {name}\'s repo, {}')

        for check in checks:
            found = False
            i = 0
            while (not found) and (i < len(check)):
                url = repo + 'tree/main/' + check[i]
                r = requests.get(url)

                if 200 <= r.status_code < 300:
                    print(f'{chr(9989)} {check[i]} for {name}')
                    found = True
                else:
                    i += 1
