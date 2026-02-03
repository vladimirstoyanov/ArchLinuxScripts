import requests
from bs4 import BeautifulSoup
import time
import os
import sys
import re

import subprocess

def speak(text: str,
          voice: str = None,
          speed: int = 0,
          pitch: int = 0,
          volume: int = 100,
          module: str = None,
          chunk_size: int = 0):  # optional for very long text
    """
    Speak using spd-say with -w to BLOCK until speech actually finishes.
    This ensures sequential playback in loops.
    """
    if not text.strip():
        return

    cmd = ["spd-say", "-w"]  # ← The magic flag: wait for completion

    if module:
        cmd.extend(["-o", module])
    if voice:
        cmd.extend(["-y", voice])
    if speed != 0:
        cmd.extend(["-r", str(speed)])
    if pitch != 0:
        cmd.extend(["-p", str(pitch)])
    if volume != 100:
        cmd.extend(["-i", str(volume)])

    if chunk_size > 0:
        # Split if text is huge (helps avoid rare queue stalls)
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        for chunk in chunks:
            full_cmd = cmd + [chunk]
            _run_spd(full_cmd)
    else:
        full_cmd = cmd + [text]
        _run_spd(full_cmd)


def _run_spd(cmd):
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Optional: tiny post-speak gap for natural flow
        # import time; time.sleep(0.3)
    except subprocess.CalledProcessError as e:
        print(f"spd-say failed (code {e.returncode}) – is speech-dispatcher running?")
    except FileNotFoundError:
        print("spd-say not found – check speech-dispatcher install.")

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

if __name__ == '__main__':
    slashdot = Slashdot ()
    index_article = 1
    for i in range (len (slashdot.listOfArticles)):
        print ("Reading " + slashdot.listOfArticles[i].title)
        time.sleep (1)
        speak (slashdot.listOfArticles[i].title)
        time.sleep (1)
        speak (slashdot.listOfArticles[i].content)
