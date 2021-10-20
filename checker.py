import requests
import json
from repo_updater import first_after

with open('json/repos.json', 'r') as f:
    data = f.read()

repos = json.loads(data)

with open('json/checks.json', 'r') as f:
    data = f.read()

checks = json.loads(data)
completed = {}

for period in repos:
    completed[period] = {}
    
    for repo in repos[period]:
        username = repo.split('/')[3]
        print(f"\nChecking {username}'s repo, {repo}")
        print(completed)
        completed[period][username] == ''

        for check in checks:
            found = False
            i = 0
            while (not found) and (i < len(check)):
                url = repo + 'blob/main/' + check[i]
                r = requests.get(url)
                url = r.url

                if 200 <= r.status_code < 300:
                    print(f'{chr(9989)} {check[i]} for {username}')
                    completed[period][username] = url
                    found = True
                else:
                    print(f"{chr(8230)} Didn't find repo {check[i]} for {username}")
                    i += 1
            if not found:
                print(f"{chr(10060)} {check[0]} not found for {username}")

with open('json/completed.json', 'w') as f:
    json.dump(completed, indent=4)
