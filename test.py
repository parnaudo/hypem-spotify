import hypem
import datetime
import spotipy
import spotipy.util as util
import sys


sp = spotipy.Spotify()
def check_spotify(query_string):
	results = sp.search(q=query_string, limit=1,type="track")
	try:
		return results['tracks']['items'][0]['id']
	except: 
		return None



count=0
while count < 1:
	playlist = hypem.get_favorites("bobotronic",count)
	for song in playlist:
		query_string = song.artist +" "+ song.title
	#	print "Query String:",query_string
		spotify_result = check_spotify(query_string)
		if spotify_result is not None:
			print "found "+query_string
			print spotify_result
		else:
			print "Could not find "+query_string
		#print song.artist," : ",song.title," : ",datetime.datetime.fromtimestamp(song.dateposted)
	count+=1

