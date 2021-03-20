import billboard
chart = billboard.ChartData('hot-100')
print(chart.title)
i = 0;
while i < 25:
    print(chart[i].title)
    #print(chart[i].artist)
    i+=1