import requests

from bs4 import BeautifulSoup

class Article:
    def __init__ (self, title, content):
        self.title = title #<span id="title-  </span>
        self.content = content#<div class="body"
    def __str__(self):
        value = str(self.title)
        value += '\n'
        value +=str(self.content)
        value +='=============='
        return value

class Slashdot:
    def __init__ (self):
        self.url = "https://slashdot.org/"
        response = requests.get(self.url)
        self.listOfArticles = []
        if response.status_code == 200:
            self.parse(str(response.content))
        textsToReplace = {
            '\\n': '',
            '\\t': '',
            "\\'": ''
        }
        self.__editTexts(textsToReplace)
        self.__printArticles ()

    def __printArticles (self):
        for i in range (len (self.listOfArticles)):
            print (self.listOfArticles[i])

    def __editTexts (self, texts):
        for key, value in texts.items():
            print ("key: " + key + ", value: " + value)
            for i in range (len(self.listOfArticles)):
                self.listOfArticles[i].title = self.listOfArticles[i].title.replace(key, value)
                self.listOfArticles[i].content = self.listOfArticles[i].content.replace(key, value)


    def __getText (self, source, beginText, endText, index):
        begin_index = source.find (beginText, index)
        end_index = source.find(endText, begin_index)

        if (begin_index == -1 or end_index == -1 or begin_index>=end_index):
                return -1, ""
        content = source[begin_index: begin_index + (end_index - begin_index)]
        index = end_index
        soup = BeautifulSoup (content, 'html.parser')

        return index, soup.get_text()

    def parse (self, source):
        index = 0

        while (index !=-1):
            index, title = self.__getText (source, "<span id=\"title-", "</span>", index)
            if (index==-1):
                break

            index, content = self.__getText(source, "<div class=\"body\"", "</div>", index)
            if (index == -1):
                break

            article = Article (title, content)
            self.listOfArticles.append(article)



if __name__=="__main__":
        slashdot = Slashdot ()
