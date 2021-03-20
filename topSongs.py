import billboard
import re

chart = billboard.ChartData('hot-100')
top_25_titles = []
top_25_artists = []
i = 0;
while i < 25:
    entry = re.sub(r'\W+','',chart[i].artist).upper()
    featureCount = entry.find("FEATURING")
    if featureCount != -1:
        print(entry[:featureCount])
        top_25_titles.append(entry[:featureCount])
        featureCount += 9
        print(entry[featureCount:])
        top_25_titles.append(entry[featureCount:])
        i+=2
    else:
        print(entry)
        top_25_titles.append(entry)
        i+=1
    #top_25_titles.append(entry)
    #entry = re.sub(r'\W+','',chart[i].artist).upper()
    #top_25_artists.append(entry)
    #print(entry)
    #print(chart[i].artist)