#!/usr/bin/python

import mechanize

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()

browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]           
browser.open("http://m.facebook.com/")
browser.select_form(nr=0)

browser.form['email'] = 'your@email.com'
browser.form['pass'] = 'your pass'
response = browser.submit()

req = browser.click_link(text='Profile', nr=0)
browser.open(req)

req = browser.click_link(text='Friends', nr=0)
browser.open(req)

f = open("response.html", 'w')

f.write(browser.response().read())
##ToDo: scrap friends names
f.close()
