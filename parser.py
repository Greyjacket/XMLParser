# -*- coding: utf-8 -*-
import xml.etree.cElementTree as et
import pandas as pd

def main():
    """ main """
    tree = et.parse("test1.xml")
    root = tree.getroot()
    dfcols = ['keywords']
    df_xml = pd.DataFrame(columns=dfcols)
    keywords = ""

    themes = root.findall('./idinfo/keywords/theme')

    for theme in themes:
        keys = theme.findall('themekey')

        for kw in keys:
            text = kw.text
            text = text.split()
            text = ' '.join(text)
            keywords = keywords + text + " "

    places = root.findall('./idinfo/keywords/place')

    for place in places:
        keys = place.findall('placekey')

        for kw in keys:            
            text = kw.text
            text = text.split()
            text = ' '.join(text)
            keywords = keywords + text + " "


    print(keywords)  

main()