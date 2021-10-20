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
<<<<<<< HEAD
        username = repo.split('/')[3]
        print(f"\nChecking {username}'s repo, {repo}")
        print(completed)
        completed[period][username] == ''
=======
        print(f"\nChecking {name}'s repo, {repo}")
>>>>>>> fd9a9be5b37d9132ee77efc8594237b7cc8e328c

        for check in checks:
            found = False
            i = 0
            while (not found) and (i < len(check)):
                url = repo + 'blob/main/' + check[i]
                r = requests.get(url)
                url = r.url

                if 200 <= r.status_code < 300:
<<<<<<< HEAD
                    print(f'{chr(9989)} {check[i]} for {username}')
                    completed[period][username] = url
=======
                    print(f'{chr(9989)} {check[i]} for {url.split("/")[3]}')
>>>>>>> fd9a9be5b37d9132ee77efc8594237b7cc8e328c
                    found = True
                else:
                    print(f"{chr(8230)} Didn't find repo {check[i]} for {username}")
                    i += 1
<<<<<<< HEAD
            if not found:
                print(f"{chr(10060)} {check[0]} not found for {username}")

with open('json/completed.json', 'w') as f:
    json.dump(completed, indent=4)
=======
                print(f'{chr(10060)} could not find {check[0]} for {url.split("/")[3]}')
>>>>>>> fd9a9be5b37d9132ee77efc8594237b7cc8e328c
