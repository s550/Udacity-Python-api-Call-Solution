# Client for the UINames.com service.
#
#
# Example output:
# My name is Tyler Hudson and the PIN on my card is 4840.

import requests


def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)
    # 1. Added variables to decode JSON from the response.
    nombre = r.json()["name"]
    password = r.json()["password"]
    lastname = r.json()["surname"]
    return "My name is {} {} and the PIN on my card is {}.".format(
        # 2. Had to use password for some reason pin wasnt available.
    nombre, lastname, password)

if __name__ == '__main__':
    print(SampleRecord())
