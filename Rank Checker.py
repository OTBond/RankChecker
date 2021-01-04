import webbrowser, sys, pyperclip, requests, bs4
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

def openUrl(path):
    webbrowser.get(chrome_path).open(path)

def getRank(soup):
    tier = soup.find("div", class_='TierRank')
    lp = soup.find("span", class_='LeaguePoints')
    stuff = [tier, lp]
    
    Rank = ''
    Rank = Rank + stuff[0].getText() + ' '

    lp = stuff[1].getText()
    LP = ''
    for i in range(len(lp)):
        if 47 < ord(lp[i]) < 58:
            LP = LP + lp[i]

    return Rank + LP + " LP"
running = True
while running:

    user = input('Enter a username: ')
    link = 'https://na.op.gg/summoner/userName=' + user


    res = requests.get(link)

    Soup = bs4.BeautifulSoup(res.text, "html.parser")

    Rank = getRank(Soup)


    print(user + " is: " + Rank)

    if input("Press ENTER to close. Type Y to run again.").lower() != 'y':
        running = False
    
