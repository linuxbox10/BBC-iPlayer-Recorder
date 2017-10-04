#!/bin/sh

wget --quiet -O - http://www.bbc.co.uk/iplayer | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Recommended
wget --quiet -O - http://www.bbc.co.uk/iplayer/group/most-popular | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Most-Popular
wget --quiet -O - http://www.bbc.co.uk/bbcone | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-One
wget --quiet -O - http://www.bbc.co.uk/bbctwo | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Two
wget --quiet -O - http://www.bbc.co.uk/tv/bbcthree | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Three
wget --quiet -O - http://www.bbc.co.uk/bbcfour | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Four
wget --quiet -O - http://www.bbc.co.uk/tv/bbcnews | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-News
wget --quiet -O - http://www.bbc.co.uk/tv/cbeebies | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/CBeebies
wget --quiet -O - http://www.bbc.co.uk/tv/cbbc | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/CBBC
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/arts/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Arts
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/comedy/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Comedy
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/documentaries/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Documentaries
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/drama-and-soaps/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Dramas-and-Soaps
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/entertainment/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Entertainment
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/films/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Films
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/history/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-History
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/lifestyle/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Lifestyle
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/music/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Music
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/science-and-nature/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Science-and-Nature
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/sport/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Sport
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/audio-described/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Audio-Described
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/signed/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Signed
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/northern-ireland/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Northern-reland
wget --quiet -O - http://www.bbc.co.uk/iplayer/categories/scotland/highlights | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Scotland
wget --quiet -O - http://www.bbc.co.uk/tv/bbcparliament | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/BBC-Parliament
wget --quiet -O - http://www.bbc.co.uk/tv/s4c | grep -o '/iplayer/episode/[^"]*' > /usr/lib/enigma2/python/Plugins/Extensions/BBC-iPlayer-Recorder/tmp/S4C
exit