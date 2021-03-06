# SoundcloudTranscriptsMadeEasy
just as the title says: Soundcloud Transcript displays made easy, in html    
transcript, subtitles, captions, call it whatever you wish - this repo allows you to put these under a soundcloud track (potentially for a podcast)    
DEMO CODE: https://repl.it/@AnthonyAndroula/transferrablesndcld     
DEMO PAGE: https://transferrablesndcld.anthonyandroula.repl.co        
<img src='https://github.com/AnthonyAndroulakis/SoundcloudTranscriptsMadeEasy/blob/master/examples/screenshotpic.png' alt='screenshot'>     

# Motivation
While thinking of how to improve the display of a "soundcloud podcast", I noticed the cool-looking scrolling transcripts that YouTube, Khan Academy, and TED used. Such a design on a soundcloud track would (1) increase comprehension, (2) allow the audience to look at which words come next, and (3) allow the audience to read the transcript as they wish. So I set my eyes on achieving this. 

# Credit where credit is due
When I started this project, I knew next to nothing about html, css, and js. I started by stumbling across X-Raym codepen titled "SoundCloud Widget API - Subtitles and Interactive Transcripts" (https://codepen.io/X-Raym/pen/QdwEgJ). The main idea of my code is in his/her code. The bulk of what I did was change the design and presentation of this code to make it easier to implement.

# Quickstart (just tell me how to use this) 
(example implementation: https://repl.it/@AnthonyAndroula/transferrablesndcld)               
1) get python (https://www.python.org/)
2) create your transcript.csv file (an example can be found here: 
<a href="https://github.com/AnthonyAndroulakis/SoundcloudTranscriptsMadeEasy/blob/master/examples/transcript.en.csv">transcript.en.csv</a>)   
The general format of a transcript csv file is
```
TRACK; tracknumber    
DESCRIPTION; descriptiongoeshere    
LENGTH; hh:mm:ss:deciseconds    
hh:mm:ss:deciseconds; transcripttext1    
hh:mm:ss:deciseconds; transcripttext2    
hh:mm:ss:deciseconds; transcripttext3    
.     
.     
.     
```
  -----\*how to find track number:     
  -----1. go to the track on the soundcloud website (for example, https://soundcloud.com/varlam/haydn-1)   
  -----2. click the share button   
  -----3. click the Embed tab   
  -----4. copy the code in the code textbox   
  -----5. now analyze this text: you will find a part that looks a bit like api.soundcloud.com/tracks/139528931 (the last number is your track number)       
after you've created your tracknum.html file, upload it onto your website   
3) upload <a href="https://github.com/AnthonyAndroulakis/SoundcloudTranscriptsMadeEasy/blob/master/sndcldscript.js">sndcldscript.js</a> and <a href="https://github.com/AnthonyAndroulakis/SoundcloudTranscriptsMadeEasy/blob/master/sndcldstyle.css">sndcldstyle.css</a> onto your website (__must be in same directory as tracknum.html file__)    
4) okay so the fun part: wherever you want to place a transcript file, add the following line (change according to your tracknumber): `<iframe src="tracknumber.html" width="100%" height="444px" frameborder="0"></iframe>`

# Code formatting specifics
- note: do not place semicolons(;) in your transcripts. This will make parsetranscript.py mess up.
- How multiple soundcloud tracks are handled: soundcloud tracks and transcripts are put into iframes in order to minimize class, variable, and function conflicts. This also makes the code simpler to look at. However, iframes do have some downsides
I'd recommend doing a bit of iframe research before implementing my code directly.       
- How transcripts are displayed: I tried to make something inbetween TED's transcript and YouTube's transcript. I ended up making an invisible html table to put the time values and transcript text.      
- this code is changable. I've added a repl.it page so you can play around with the code and change it as you wish

# License
MIT License: https://github.com/AnthonyAndroulakis/SoundcloudTranscriptsMadeEasy/blob/master/LICENSE
