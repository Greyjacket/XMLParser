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
    info = root.findall('./idinfo/citation/citeinfo')

    descript = root.findall('./idinfo/descript/')
    descript = descript[0].text

    boundings = root.findall('./idinfo/spdom/bounding')  

    westbc = boundings[0][0].text
    eastbc = boundings[0][1].text
    northbc = boundings[0][2].text
    southbc = boundings[0][3].text

    for stuff in info:
        origin = stuff.findall('origin')
        origin = origin[0].text
        title = stuff.findall('title')
        title = title[0].text

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

main()