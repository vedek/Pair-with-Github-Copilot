
/*Bot needed to refresh page and click link 
I'm in need of a simple python or similar language bot that will click a specified element on a webpage after 
refreshing the page at a given time interval. If possible, I'd also like to vary the time interval between 
page refreshes or be able to set a random time interval between a given maximum and minimum.

For example, I'd like to refresh a page every 10 seconds and when the specified element is found, I want the
 bot to click on it instantly. After a delay of a second or two, I'd like the bot to resume page refreshes 
 every 10 seconds. No GUI is necessary as I am familiar with editing scripts so I can change the 
values for time intervals between refreshes for instance to suit my needs
*/

%python
%define a function, to open chrome browser, given url u, to refresh that page on the broswer every 10 seconds in a loop, infinitely
def open_chrome(u):
    import time
    import webbrowser
    while True:
        webbrowser.open(u)
        time.sleep(10)
        click_element(driver, u, eid)



    
    

%define a function to use a webdriver driver, to open a url u, click on the element with id eid
def click_element(driver, u, eid):
    driver.get(u)
    driver.find_element_by_id(eid).click()

