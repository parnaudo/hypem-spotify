import hypem
import datetime
import spotipy
import spotipy.util as util
import sys
scope = 'playlist-modify-public'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:

    sp = spotipy.Spotify(auth=token)
    user = sp.me()
    sp.user_playlist_create(user['id'], "TestPlaylist", public=True)
    # results = sp.current_user_saved_tracks()
    # for item in results['items']:
    #     track = item['track']
    #     print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username


sp = spotipy.Spotify()
def check_spotify(query_string):
	results = sp.search(q=query_string, limit=1)
	for i, t in enumerate(results['tracks']['items']):
		print t

count=0
while count < 1:
	playlist = hypem.get_favorites("bobotronic",count)
	for song in playlist:
		query_string = song.artist +" "+ song.title
		print "Query String:",query_string
		check_spotify(query_string)
		#print song.artist," : ",song.title," : ",datetime.datetime.fromtimestamp(song.dateposted)
	count+=1

