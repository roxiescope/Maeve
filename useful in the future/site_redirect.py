import webbrowser


def openMint():
    url = 'https://mint.intuit.com/overview.event'

    # Windows
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)

    # TODO: add login ability
