import requests

nick = input("enter nickname: ")

url = "SOURCEBANS LINK/index.php?p=banlist&advSearch=" + nick + "&advType=name"
response = requests.get(url)

if response.status_code == 200:
    zawartosc = response.text
    profile_steam = re.findall(r'(https?://steamcommunity.com/profiles/\d+)', zawartosc)

    if profile_steam:
        print("Steam profile links found:")
        for link in profile_steam:
            print(link)
    else:
        print("Steam profile links not found.")
else:
    print("Error while downloading the page:", response.status_code)