import urllib2
import time
import sqlite3
import time

##if pdf - '1', html or htm - '0', nothing - '-1'
def CheckUrl(url):
	suffix_4 = url[len(url)-4:]
	suffix_5 = url[len(url)-5:]
	if suffix_4 == '.htm' or suffix_5 == '.html':
		return 0
	
	return -1

##Search for href
def find_sub_string (m_text, m_subtext, index):
	for i in range(index,len(m_text)):
		for j in range(len(m_subtext)):
			if (m_subtext[j]!=m_text[i+j]):
				break
			if j == len(m_subtext)-1:
				return i+j+1
	return -1
      
def find_sub_string_back (m_text, m_subtext, index):
	for i in range(index,-1,-1):
		for j in range(len(m_subtext)-1,-1,-1):
			if (m_subtext[j]!=m_text[i-((len(m_subtext)-1)-j)]):
				break
			if j == 0:
				return i+1
	return -1

##Get url after href=
def GetUrl(text,index):
	url =""
	while (text[index]!="\""):
		index = index + 1 
	index  = index + 1	
	while (text[index]!="\""):
		url = url + text[index]
		index = index + 1
	return url, index
	
##Check list for exist url
def CheckListForExistUrl(l_url, url):
	for i in range (len(l_url)):
		if l_url[i] == url:
			return -1
	return 0

##Build url if not root or root is diferent from 'url_address'
def BuildUrl(url_root, url):
	if (len(url)==0 or len(url_root) == 0):
	  return ""
	new_url = ""
	for i in range(len(url)):
		if ord(url[i]) == 32:
			new_url = new_url + "%20"
			continue
		new_url = new_url + url[i]
	#print new_url
	url = new_url

	if url.find('://') == -1:
		if (url_root[len(url_root)-1:] == '/' and url[0]!='/') or (url_root[len(url_root)-1:] != '/' and url[0]=='/'):
			url = url_root + url
		elif (url[0]!='/' and url_root[len(url_root)-1:] != '/'):
			url = url_root + '/' + url
		elif (url[0] == '/' and url_root[len(url_root)-1:] == '/'):
			url = url_root[:len(url_root)-1] + url
		return url
	      
	if url.find(url_root) == -1:
		return ""
	
	return url
	
##Save file
def SaveFile(url):
	file_name = url.split('/')[-1]
	try:
		u = urllib2.urlopen(url)
	except:
		return
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		#status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		#status = status + chr(8)*(len(status)+1)
		#print status,

	f.close()

def createTables():
   conn=sqlite3.connect('dnes_bg.db')
   c = conn.cursor()
   try:
    sql = "create table if not exists user_comment (id integer, user text, comment text, comment_id integer)"
    c.execute(sql)
    sql = "create table if not exists article (id integer primary key, title text)"
    c.execute(sql)
    c.close()
   except:
     print "Can't create DB tables."
     return 1
   return 0

def fillDataBase(html_source):
  conn=sqlite3.connect('dnes_bg.db')
  c = conn.cursor()
  
  #title
  index = 0
  index = find_sub_string(html_source, '<div id="art_header"><h1 class="title">', index)
  if index == -1:
    print "throw fillDataBase 1"
    c.close()
    return
  
  title =""
  while (index < len(html_source) and html_source[index]!='<'):
    title+=html_source[index]
    index+=1
  
  print "title:" + title
  
  ##check if title exist
  result = None
  c.execute("SELECT count(*) FROM article WHERE title= '" + title + "'")
  result = c.fetchone()[0]
  if result != 0:
    c.close()
    return
   
     
  ##get last id
  c.execute('SELECT max(id) FROM article')
  title_id = c.fetchone()[0]
  print "id:" + str(title_id)
  if title_id == None:
    title_id = 0
  else:
    title_id+=1
  print "last row id: " + str(title_id)
  
  sql = "insert into article (id, title) values("+ str(title_id) +",'" + title + "')"

  c.execute(sql)
  
  
  id = 0
  while (index!=-1):
    ##comment user
    #<div class="comment_user">
    previous_index = index
    index = find_sub_string(html_source, '<div class="comment_user">', index)
    if index == -1:
      #print "trying to get next page link..."
      #time.sleep(1)
      index = find_sub_string(html_source, 'class="next"', previous_index)
      if (index == -1): ##if hasn't more comment pages
	print "Comment pages have been finished..."
	c.close()
	return
      
      index = find_sub_string_back(html_source, 'href="', index)
      
      ##get link to next page of comments
      link_to_next=""
      while (index<len(html_source) and html_source[index] != '"'):
	link_to_next += html_source[index]
	index+=1
      
      link_to_next = BuildUrl(url_address, link_to_next)
      print "link to next:" + link_to_next
      try:
		u = urllib2.urlopen(link_to_next)
      except:
		print "except: cant connect to next link:" + link_to_next
		time.sleep(3)
		c.close()
		return
      addUrl(link_to_next)
      #l_url.append(link_to_next)
      html_source = u.read()
      index = 0
      previous_index = 0
      print "continue"
      continue
   
      
    previous_index = index
    index = find_sub_string(html_source, '<b>', index)
    user_name = ""
    
    while(index<len(html_source) and html_source[index]!='<'):
      user_name+=html_source[index]
      index+=1
      
    print "user name: " + user_name
    index = find_sub_string(html_source, '<div class="comment_text">', index)
    if (index == -1):
      print "cant find comment of above user."
      c.close()
      return
    
    down_index = find_sub_string(html_source, '<div class=', index)
    
    if (down_index == -1):
      print "down index sucks"
      c.close()
      return 
    
    comment_text=""
    down_index = down_index - 11
    while(index<down_index):
      comment_text += html_source[index]
      index+=1
    print "comment text:" + comment_text
    id+=1
    c.execute("INSERT INTO user_comment VALUES (" + str(title_id) + ",'" + user_name + "','" + comment_text + "',"+str(id)+")")
    conn.commit()
    print "data is added:" + str(id)
    print "-------"
    ##comment text
    #<div class="comment_text">
    
    ##next page comments
    
    
    ##end
    #<a href="/politika/2015/02/18/sled-populizma-shte-doide-vremeto-za-plashtaniiata.254906,2" rel="" class="next">
    #<a href="javascript:void()" rel="" class="next nt_a">
  c.close()
  
def slashOrWithoutSlash(url):
  if (url[len(url)-1:] == '/'):
    l_url.append(url[:len(url)-1])
  else:
    l_url.append(url+'/')
    
def addUrl(url):
  l_url.append(url)
  slashOrWithoutSlash(url)
  
  protocol_index = url.find('://')
  if (protocol_index==-1):
    l_url.append('http://' + url)
    slashOrWithoutSlash('http://' + url)
    
    www_index = url.find('www.')
    if (www_index==0):
      l_url.append(url[4:])
      slashOrWithoutSlash(url[4:])
      l_url.append('http://' + url[4:])
      slashOrWithoutSlash('http://' + url[4:])
    else:
      l_url.append('www.' + url)
      slashOrWithoutSlash('www.' + url)
      l_url.append('http://www.' + url)
      slashOrWithoutSlash('http://www.' + url)
  else:
    #get protocol name
    protocol = ""
    i=0
    while (i<len(url) and url[i]!=':'):
      protocol+=url[i]
      i+=1
  
    #append without protocol name
    l_url.append(url[len(protocol)+3:])
    slashOrWithoutSlash(url[len(protocol)+3:])
    #check for www and append other variants
    www_index = url.find('www.')
    if (www_index==len(protocol)+3):
      l_url.append(url[len(protocol)+7:])
      slashOrWithoutSlash(url[len(protocol)+7:])
      l_url.append(protocol+'://' + url[len(protocol)+7:])
      slashOrWithoutSlash(protocol+'://' + url[len(protocol)+7:])
    else:
      l_url.append('www.' + url[len(protocol)+3:])
      slashOrWithoutSlash('www.' + url[len(protocol)+3:])
      l_url.append(protocol+'://' + 'www.' + url[len(protocol)+3:])
      slashOrWithoutSlash(protocol+'://' + 'www.' + url[len(protocol)+3:])
    
    
    
def checkContentType(content_type):
  #text/html
  content = ""
  i=0
  while(i<len(content_type) and content_type[i]!=';'):
    content+=content_type[i]
    i+=1
  if (content == 'text/html'):
    return 1
  return 0

l_url = []
l_current = []
log = open('log_file.txt', 'w')
url_address = 'http://www.dnes.bg/'#raw_input("Url address:")
addUrl(url_address)
#l_url.append(url_address)
l_current.append(url_address)
if (createTables()):
  sys.exit(1)

num = 0
while len(l_current)>0:
	url = l_current[0]
	del l_current[0]
	num = num + 1
	#print "interation " + str(num)
	#log.write("======================= INTERATION " + str(num) + "=========================\n")
	#log.write("Length of list: " + str(len(l_url)) + "\n")
	
	try:
		u = urllib2.urlopen(url)
	except:
		print "fail:" + url
		continue
	      
	html = u.read()

	#log.write("In: " + url  + "\n")
	#time.sleep(1)
	print "=================="
	print "Get comments of " + str(url)
	print len(l_current)
	fillDataBase(html)
	#print "after that"
	if (checkContentType(u.info().getheader('Content-Type'))==0): ##if content-type != text/html
	  print "not text/html..."
	  #time.sleep(1)
	  continue
	#time.sleep(2)
	index = 0
	while(index != -1):
		index = find_sub_string (html, 'href=', index)
	 	
		if index!=-1:
			url, index = GetUrl(html,index)
			
			url = BuildUrl(url_address, url)
		
			#print "Url: " + url
			#time.sleep(1)
			
			if url == "":
				#log.write( "Link is ignored: " + url + "\n")
				#time.sleep(1)
				continue
				
			#ret = CheckUrl(url)
			
			#if ret == 0:
				
			if CheckListForExistUrl(l_url, url) == 0:
				#log.write( "Adding url: " + url + "\n")
				#print "added..."
				#time.sleep(1)
				addUrl(url)
				#l_url.append(url)
				l_current.append(url)
log.close()		