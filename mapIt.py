import webbrowser
import sys

place=''
count=1
if len(sys.argv)==1:
    place = input('please input place you are looking for\n')
    place=place.split()
    place='+'.join(place)
else:
    for names in sys.argv[1:]:
        if count==1:
            place=names
            count+=1
        else:
            place = str(place)+'+'+str(names)
            print(place)

site='https://www.google.com/maps/place/'+place
webbrowser.open(site)
input()
