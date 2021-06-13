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

# To schedule a meeting, use the below mentioned format -

zoom(link, date, time)

''' where -
        link : meeting link
        date : the date you want to schedule the meeting to join
        time : the time you want to join the meeting
        
Example : zoom("www.google.com","13-06-2021","13-35-00")'''


