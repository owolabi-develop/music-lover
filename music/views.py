
from django.shortcuts import render

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Create your views here.
from musiclover.settings import CLIENT_ID,CLIENT_SECRET
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))
from pprint import pprint
#main page........
def baseMusic(request):
   
    playlists = sp.user_playlists('spotify')
    
    
    
   
    return render(request,'music/base.html',{'article':playlists['items']})

#music search features....................
def music_search(request):
    artists_query = request.GET.get('musicQuery',None)
    results = sp.search(q=artists_query,type='artist')
    if results:
        artists = results['artists']['items'][0]
        uri = artists['uri']
        artists_tracks = sp.artist_top_tracks(artist_id=uri)
        artists_album = sp.artist_albums(artist_id=uri,album_type='single',limit=5)
        artists_data = sp.artist(artist_id=uri)
        
    else:
        return render(request,'music/search.html',{'track':'','artists_data':''})
      


    return render(request,'music/search.html',{'track':artists_tracks['tracks'][:5],'artists_data':artists_data,'album':artists_album['items']})
