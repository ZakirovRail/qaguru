from time import sleep

import requests

url = "https://www.selenium.dev/images/sponsors/browserstack.png"

response = requests.get(url, allow_redirects=True)

with open("browserstack_with.png", 'wb') as file:
    file.write(response.content)

with open("browserstack2.png", 'wb') as file:
    file.write(response.content)



