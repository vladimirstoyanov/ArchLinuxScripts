#!/usr/bin/python

#ToDo: make HTTPS session instead HTTP

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

f = open("response.html", 'w')

f.write(response.read())
f.close()

print response.code
