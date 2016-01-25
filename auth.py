import sys
import spotipy
import spotipy.util as util

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
    print user['id']
    #sp.user_playlist_create("1214778550", "TestPlaylist", public=True)
    # results = sp.current_user_saved_tracks()
    # for item in results['items']:
    #     track = item['track']
    #     print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username