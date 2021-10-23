def find_all(string, substr):
    i = 0
    sublen = len(substr)
    indexes = []

    while i < len(string) - sublen:
        if string[i:i+sublen] == substr:
            indexes.append(i)
        i += 1

    return indexes

def first_after(str, start, search):
    searchlen = len(search)

    while start < len(str):
        if str[start:start+searchlen] == search:
            return start
        start += 1

if __name__ == '__main__':
    import json
    import requests
    print('imported modules')
    repo_links = {}

    # Paste GitHub HTML into repos.html
    for period in [6, 7, 8]:
        repo_links[period] = []
        f = open(f'html/pd{period}.html', 'r').read()
        all_instances = find_all(f, "a data-skip-pjax")

        for index in all_instances:
            end = first_after(f, index, "tree")
            url = f'https://www.github.com{f[index+30:end]}'
            r = requests.get(url)
            url = r.url
            if url[-1] != '/':
                url += '/'
            url += 'blob/main/'
            repo_links[period].append(url)
            print(url)

    with open('json/repos.json', 'w') as f:
        json.dump(repo_links, f, indent=4)
