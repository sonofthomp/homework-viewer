import json
import requests
from repo_updater import first_after

with open('json/repos.json', 'r') as f:
    data = f.read()

repos = json.loads(data)

with open('json/checks.json', 'r') as f:
    data = f.read()

checks = json.loads(data)

for period in repos:
    for repo in repos[period]:
        name = repo.split('/')[3]
        print(f"\nChecking {name}'s repo, {repo}")

        for check in checks:
            found = False
            i = 0
            while (not found) and (i < len(check)):
                url = repo + check[i]
                r = requests.get(url)
                name = r.url.split('/')[3]

                if 200 <= r.status_code < 300:
                    print(f'{chr(9989)} {check[i]} for {name}')
                    found = True
                else:
                    print(f'{chr(8230)} {check[i]} not found for {name}')
                    i += 1
            if not found:
                print(f'{chr(10060)} could not find {check[0]} for {name}')
