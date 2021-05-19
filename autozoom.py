import pyautogui as pyg, webbrowser as web, datetime,time as t, click

def openzoom(link):
    #setting up browser to chrome
    chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    web.register('chrome',None,web.BackgroundBrowser(chrome_path))
    browser=web.get('chrome')
    browser.open(link,new=2)
    
def zoom(link, date, time):
    date = [int(x) for x in date.split('-')]
    time = [int(x) for x in time.split('-')]
    python_format = datetime.datetime(date[2],date[1],date[0],time[0],time[1],time[2])
    time_left = python_format - datetime.datetime.now().replace(microsecond=0)
    time_left = time_left.total_seconds()
    print("Next meeting will start in around",time_left,'seconds')
    t.sleep(time_left)

    #to open zoom in browser
    openzoom(link)
    t.sleep(5)

    #these dimensions are for my lappy, will be different for yours
    #to click on open zoom
    pyg.click(x=737, y=222, clicks=1, interval=0, button='left')
    t.sleep(10)

    #to close the audio box
    pyg.click(x=921, y=234, clicks=1, interval=0, button='left')
    t.sleep(5)

    #and to click on continue
    pyg.click(x=838, y=435, clicks=1, interval=0, button='left')
    print("Meeting Launched\n")
    
weekday=datetime.datetime.now().weekday()
today=str(datetime.datetime.now().date())
reversing_today = [x for x in today.split('-')][::-1]
today = "-".join(reversing_today)
print(weekday,today)
#zoom('google.com','18-05-2021','18-10-00')
ai = "https://iare-ac-in.zoom.us/j/92836158713?pwd=NnZTZkVremRvd0pLUGNpdTZqZ1M1UT09"
lp = "https://iare-ac-in.zoom.us/j/98425928051?pwd=OFl4Qk1rVzBQZnZMNnRZTTJLeG0rQT09"
adb = "https://iare-ac-in.zoom.us/meeting/register/tJEkd-upqTsrEtFCM3ozv9UlLCYYwBf3Zq16"
iot = "https://iare-ac-in.zoom.us/j/95945210804?pwd=TjJhVFJ2NFprVzRnWElKeVh0aktPQT09"
dmdw = "https://iare-ac-in.zoom.us/j/96924410873?pwd=QmF2a2xWSXAyWjFtUFhvaVYyUUR0UT09"
sc = "https://iare-ac-in.zoom.us/j/99029418973?pwd=dHo5YWxYNXVjS1pXcmY2RFVadVZOUT09"
ss = "https://iare-ac-in.zoom.us/j/95189208348?pwd=Vi9sUXlIVFNkVnBIcEYxV21FeXdZdz09"
time_table = [[ai, lp, adb],
              [lp, ai, iot],
              [dmdw, ai, lp],
              [dmdw, iot, sc],
              [ss, dmdw,iot],
              [sc, ss, adb]]
zoom(time_table[weekday][0],today,"13-35-00")
zoom(time_table[weekday][1],today,"14-25-00")
zoom(time_table[weekday][2],today,"15-15-00")

