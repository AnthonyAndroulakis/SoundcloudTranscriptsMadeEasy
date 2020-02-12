#parse csv transcript file into html
import sys

def run(filename): #example input: transcript.en.csv
	#first parse csv file for relevant data
	lines = open(filename).read().split('\n')
	tracknum = lines[0].split(';')[1].strip() #make tracknum id name in html and js
	description = lines[1].split(';')[1].strip()
	totallength = lines[2].split(';')[1].strip()
	totlenseg = [int(i) for i in totallength.split(':')]
	data = [i.split(';') for i in lines][3:]
	data = [i for i in data if len(i[0])!=0] #remove empty slots
	seconds = [[int(k) for k in j[0].split(':')][0]*3600+[int(k) for k in j[0].split(':')][1]*60+[int(k) for k in j[0].split(':')][2]+[int(k) for k in j[0].split(':')][3]*0.1 for j in data] #ignore first
	seconds.append(totlenseg[0]*3600+totlenseg[1]*60+totlenseg[2]*1+totlenseg[3]*0.1)
	words = [l[1] for l in data] #ignore first
	timeDisplay = [m[0][:-2] for m in data]
	timeDisplay.append(totallength)
	#check for any logic errors
	class TranscriptError(Exception):
    		pass

	if seconds[-1]<seconds[-2]:
		raise TranscriptError("LENGTH needs to be greater than last time mark.")

	#create txt file with html-version of transcript
	htmltext = '<iframe id="musicframe" width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/'+tracknum+'&amp;color=ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false"></iframe>'
	htmltext += '<br><br>'
	htmltext += '<div class="btntoggle"><button class="tablinks" onclick="openInfo(event, \'btndetails\')">Details</button><button id="defaultOpen" class="tablinks" onclick="openInfo(event, \'btntranscript\')">Transcript</button></div>'
	htmltext += '<div class="tabcontent" id="btndetails"><hr align="left">'+description+'</div>'
	htmltext += '<div class="tabcontent" id="btntranscript">'
	htmltext += '<hr align="left">'
	htmltext += '<div class="wavesurfer-transcript">'
	for i in range(len(data)):
		htmltext += '<div class="wavesurfer-marker" data-start="'+str(seconds[i])+'" data-end="'+str(seconds[i+1])+'"> <table><tr><td>'+timeDisplay[i]+'&nbsp;&nbsp;</td> <td>'+words[i]+'</td></tr></table></div>'
	htmltext += '</div>'
	htmltext += '<link rel="stylesheet" href="./sndcldstyle.css">'
	htmltext += '<script src="https://w.soundcloud.com/player/api.js"></script>'
	htmltext += '<script src="./sndcldscript.js"></script>'
	open(tracknum+'.html','w').write(htmltext)

run(sys.argv[1])
