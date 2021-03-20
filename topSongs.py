import billboard
import re
chart = billboard.ChartData('hot-100')
top_25_titles = []
top_25_artists = []
i = 0;
while i < 25:
    entry = re.sub(r'\W+','',chart[i].title).upper()
    top_25_titles.append(entry)
    entry = re.sub(r'\W+','',chart[i].artist).upper()
    top_25_artists.append(entry)
    print(entry)
    #print(chart[i].artist)
    i+=1