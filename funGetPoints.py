import pandas as pd
import requests
from geopy import geocoders
from geopy.extra.rate_limiter import RateLimiter

import time
import sqlite3


def getPoints(term1,term2):
    start_time = time.time()

    searchTerm = f"{term1}{term2}"
    sqlTerm=f"{term1}{term2}"
    fileEmpty = False
    List = []
    List = searchTerm.split(",")
    print(List)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    d = conn.cursor()
    for i in List:
        print(i)
        # get the count of tables with the name

        sql_cmd = ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}' '''.format(
                sqlTerm)

        c.execute(sql_cmd)

        # if the count is 1, then table exists
        if c.fetchone()[0] == 1:
            print('Table exists.')
            sql_cmd = "SELECT * FROM {}".format(
                sqlTerm)
            d.execute(sql_cmd)
            print(d.fetchall())
        else:
            print("table doesnt exist.")
            beginYear = 1850
            endYear = 1860
            pg = 1
            endpg = 4
            # too much data? I'm just grabbing the first few pages right now
            stop = False
            allData = []
            locs = {}
            pd.set_option('display.max_colwidth', -1)
            while not stop:
                # http://chroniclingamerica.loc.gov/search/pages/results/?andtext={searchTerms}&page={startPage?}&ortext={chronam:booleanOrText?}&year={chronam:year?}&date1={chronam:date?}&date2={chronam:date?}&phrasetext={chronam:phraseText?}&proxText={chronam:proxText?}&proximityValue={chronam:proximityValue?}&format=json"
                url = "http://chroniclingamerica.loc.gov/search/pages/results/?phrasetext={0}&dateFilterType=yearRange&date1={1}&date2={2}&page={3}&format=json".format(
                    searchTerm, beginYear, endYear, pg)
                call = requests.get(url)
                data = call.json()
                df = pd.DataFrame(data["items"])
                #             nf=pd.DataFrame()
                #             americanPanda=pd.DataFrame()
                # only want city and date for this application
                #             nf['date']=pd.to_datetime(df['date'])
                #             nf['citystate']=df['city'].map(lambda a:a[0])+', '+df['state'].map(lambda a: a[0])
                c.execute('CREATE TABLE IF NOT EXISTS {tab} (date text, city text)'.format(tab=sqlTerm))
                newDate = pd.to_datetime(df['date'])
                newLocation = df['city'].map(lambda a: a[0]) + ', ' + df['county'].map(lambda a: a[0]) + ', ' + df[
                    'state'].map(lambda a: a[0])
                countMain = 0
                for one in newDate:
                    value1 = str(newDate[countMain])
                    value2 = str(newLocation[countMain])


                    sql_cmd = f"INSERT INTO {sqlTerm} VALUES ({value1},{value2})"

                    c.execute(f"INSERT INTO {sqlTerm} VALUES (?,?)",(value1, value2))

                    countMain = countMain + 1
                #             loopCount=len(americanPanda.columns)
                #             secondPanda=pd.DataFrame()
                #             pdfList=[]
                #             textList=[]
                #             for count, url in enumerate(df['url'], start=1):
                #                 print(count)
                #                 call = requests.get(url)
                #                 data = call.json()
                #                 forframe = pd.DataFrame(data)
                #                 forframe.index= [0,1,2]
                #                 forpanda=pd.DataFrame()
                #                 pdfframe=forframe['pdf']
                #                 textframe=forframe['text']
                #                 pdfList.append((pdfframe[0]))
                #                 textList.append((textframe[0]))
                #             americanPanda['keywords']=i
                #             print(americanPanda)
                print("=============")
                conn.commit()

                sql_cmd = "SELECT * FROM {}".format(
                    sqlTerm)

                c.execute(sql_cmd)

                #             americanPanda.to_pickle(i+'.pkl')
                if pg == endpg:
                    stop = True
                else:
                    pg += 1
        print("--- %s seconds ---" % (time.time() - start_time))
        print(c.fetchall())
getPoints("girl","boy")