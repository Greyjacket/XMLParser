# -*- coding: utf-8 -*-
import xml.etree.cElementTree as et
import pandas as pd
import glob, os

def main():

    dfcols = ['Title', 'Descript', 'Origin', 'Westbc', 'Eastbc', 'Northbc', 'Southbc', 'Keywords']
    df_xml = pd.DataFrame(columns=dfcols)
    
    """ main """
    for file in glob.glob("*.xml"):
        tree = et.parse(file)
        root = tree.getroot()
        df_xml_temp = pd.DataFrame(columns=dfcols)
        keywords = ""
        descript = ""
        westbc = ""
        eastbc = ""
        northbc = ""
        southbc = ""
        descript = ""
        origin = ""
        title = ""

        descript = root.findall('./idinfo/descript/')
        descript = descript[0].text

        boundings = root.findall('./idinfo/spdom/bounding')  

        westbc = boundings[0][0].text
        eastbc = boundings[0][1].text
        northbc = boundings[0][2].text
        southbc = boundings[0][3].text

        info = root.findall('./idinfo/citation/citeinfo')

        for stuff in info:
            origin = stuff.findall('origin')
            origin = origin[0].text
            title = stuff.findall('title')
            title = title[0].text

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

        df_xml_temp = pd.DataFrame({'Title':[title], 'Descript':[descript], 'Origin':[origin], 'Keywords':[keywords], 'Westbc': westbc, 'Eastbc': eastbc, 'Northbc': northbc, 'Southbc': southbc})
        df_xml = df_xml.append(df_xml_temp)

    df_xml.to_csv("test.csv", encoding='utf-8', columns=dfcols)

main()