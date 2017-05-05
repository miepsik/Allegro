from lxml.cssselect import CSSSelector
from lxml.html import fromstring
from urllib.request import urlopen
from re import compile, sub
from socket import gaierror


class EmptyResult(Exception):
    pass


if __name__ == "__main__":
    URL = "https://github.com/allegro"  # github profile url
    REPO_LIST = "repo-list"  # div containing repo list class
    LAST_ELEMENT = "a"  # parent of plain text repo name
    ATTRIBUTE = "itemprop"  # attribute that allows to identify proper element
    ATTRIBUTE_VALUE = "codeRepository"  # value of that attribute
    try:
        page = fromstring(urlopen(URL).read())  # downloading source
        selectorText = '.' + REPO_LIST + " " + LAST_ELEMENT + "[" + ATTRIBUTE + "~=" + ATTRIBUTE_VALUE + "]"
        selector = CSSSelector(selectorText)  # creating css selector
        result = ""
        projectList = selector(page)
        if len(projectList) == 0:
            raise EmptyResult
        for e in projectList:  # get first result
            result = e.text
            break
        pattern = compile(r'\s+')  # remove white spaces
        result = sub(pattern, '', result)
        print(result)
    except gaierror:
        print("Check your internet connection")
    except EmptyResult:
        print("HTML schema probably has changed. Please update constants")
    except:
        print("Something went wrong")
