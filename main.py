import matplotlib.pyplot as plt; import sys;
import requests; import json;

def parseName(name, shorten):
    if not shorten:
        return name
    newName = ""
    lis = name.split()
    for i in lis:
        newName += i[0]
    return newName

def main():
    shortening = True
    excluding = True
    if input("Would you like to shorten game names to an acronym? (y/n)") == "n":
        shortening = False
    if input("Would you like to exclude games with 0 playtime? [recommended] (y/n)") == "n":
        excluding = False

    try:
        id = input("enter steam ID:")
        res = requests.get("https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=28FE417B6906C45F07E57AE3177BCFC1&skip_unvetted_apps=false&steamid="+ id +"&format=json&include_played_free_games=1&include_appinfo=1")
        response = json.loads(res.text)
        gameNames = []
        gameHours = []
        for i in response["response"]["games"]:
            if (i["playtime_forever"] == 0 and excluding):
                continue
            gameNames.append(parseName(i["name"], shortening))
            gameHours.append(i["playtime_forever"] / 60)

        plt.bar(gameNames, gameHours, 1)
        plt.show()
    except:
        print("make sure you have the libraries: matplotlib.pyplot, requests and json installed bozo")

if __name__ == '__main__':
    sys.exit(main())