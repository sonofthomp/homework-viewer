from json import loads, dump
from requests import get
from datetime import datetime
from repo_updater import first_after

visual = False
with open('json/repos.json', 'r') as f:
    data = f.read()

repos = loads(data)

with open('json/checks.json', 'r') as f:
    data = f.read()

checks = loads(data)

with open('json/completed.json', 'r') as f:
    data = f.read()

completed = loads(data)

for check in checks:
    completed[check[0]] = {}

for period in repos:
    for repo in repos[period]:
        name = repo.split('/')[3]
        if visual:
            print(f"\nChecking {name}'s repo, {repo}")

        for check in checks:
            found = False
            i = 0
            while (not found) and (i < len(check)):
                url = repo + check[i]
                r = get(url)
                name = r.url.split('/')[3]

                if 200 <= r.status_code < 300:
                    completed[check[0]][name] = {'link': url, 'pd': period}
                    if visual:
                        print(f'{chr(9989)} {check[i]} for {name}')
                    found = True
                else:
                    if visual:
                        print(f'{chr(8230)} {repo + check[i]} not found for {name}')
                    i += 1
            if not found:
                completed[check[0]][name] = {'link': 'n/a', 'pd': period}
                if visual:
                    print(f'{chr(10060)} could not find {check[0]} for {name}')

with open('json/completed.json', 'w') as f:
    dump(completed, f, indent=4)

time = datetime.now()
with open('json/updated.txt', 'w') as f:
    f.write(time.strftime("%m/%d/%Y, %H:%M:%S"))
