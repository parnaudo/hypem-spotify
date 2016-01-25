import sys
import spotipy
import spotipy.util as util
import hypem
def check_spotify(query_string):
	results = sp.search(q=query_string, limit=1,type="track")
	try:
		return results['tracks']['items'][0]['id']
	except: 
		return None

def get_hypem_tracks(pages):
	tracks_to_add = []
	count=0
	while count <= pages:
		playlist = hypem.get_favorites("bobotronic",count)
		for song in playlist:
			query_string = song.artist +" "+ song.title
		#	print "Query String:",query_string
			spotify_result = check_spotify(query_string)
			if spotify_result is not None:
				print "found "+query_string
				tracks_to_add.append(spotify_result)
			else:
				print "Could not find "+query_string
			#print song.artist," : ",song.title," : ",datetime.datetime.fromtimestamp(song.dateposted)
		count+=1
	return tracks_to_add

scope = 'playlist-modify-public'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)
tracks_to_add = []
if token:

    sp = spotipy.Spotify(auth=token)
    user = sp.me()
    #sp.user_playlist_create(user['id'], "TestPlaylist", public=True)
    for playlist in sp.user_playlists(user['id'])['items']:
    	print playlist['id']
    	if playlist['id'] == "4ukrRdnArXibLTkVU1MY9s":
			tracks_to_add = get_hypem_tracks(1)
			sp.user_playlist_add_tracks(user['id'],playlist['id'],tracks_to_add)
			# results = sp.current_user_saved_tracks()
			# for song in results['items']:	
			# 	tracks_to_add.append(song['track']['id'])
			# print "tracks to add: ",tracks_to_add

else:
    print "Can't get token for", username