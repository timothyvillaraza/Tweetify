import billboard
import re

chart = billboard.ChartData('hot-100')


top_songs = {}


def get_top_artists():
    i = 0
    top_artists = {}
    while len(top_artists) < 25:
        entry = re.sub(r'\W+', '', chart[i].artist).upper()
        featureCount = entry.find("FEATURING")
        if featureCount != -1:
            top_artists[entry[:featureCount]] = 0
            featureCount += 9
            top_artists[entry[featureCount:]] = 0
            i += 2
        else:
            top_artists[entry] = 0
            i += 1

        # top_25_titles.append(entry)
        # entry = re.sub(r'\W+','',chart[i].artist).upper()
        # top_25_artists.append(entry)
        # print(entry)
        # print(chart[i].artist)
    #print(top_artists)
    return top_artists

def get_top_songs():
    i = 0
    while len(top_songs) < 25:
        entry = re.sub(r'\W+','',chart[i].title).upper()
        top_songs[entry] = 0
        i = i+1
    # print(top_songs)
    return top_songs

