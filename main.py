"""
File: main.py
Author: Jack McShane
Email: jackmcshane@protonmail.com
Github: https://github.com/jackrmcshane/
Description: This script sorts the user's 'likes songs' library into playlists by artist
"""



#!/usr/bin/env python3



import os
import spotipy
from secrets import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth




'''
steps in the process
1. authorization
2. get next song batch from 'Liked Songs' Library
3. for each track,
    - get artist name
    - check if playlist with that title
        - True: add song to playlist
        - False:
            - create playlist with artist name as title
            - add song to playlist
4. return to step 2


necessary scopes:
getting saved songs -> user-library-read
remove songs from saved -> user-library-modify
create playlist -> playlist-modify-public, playlist-modify-private
get list of current user playlists -> palylist-read-private

'''



SCOPES = [
    'user-library-read',
    'user-library-modify',
    'playlist-modify-public',
    'playlist-modify-private',
    'playlist-read-private'
]


def authenticate(cid, secret, redirect, scope):
    """TODO: Docstring for authenticate.
    :returns: an authenticated spotify object for accessing the Spotify Web API

    """
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=cid,
                client_secret=secret,
                redirect_uri=redirect,
                scope=scope
            ))



def collectLikedTracks(spotify):
    """TODO: Docstring for collectLikedTracks.

    :spotify: TODO
    :returns: TODO

    """
    results = spotify.current_user_saved_tracks() # the base limit for the request is 20
    # moving through the pagination, retrieving all songs
    tracks = [track['track'] for track in results['items']]
    while results['next']:
        results = spotify.next(results)
        # do your stuff with the next batch of results
        [tracks.append(track['track']) for track in results['items']]

    return tracks




def collectPlaylists(spotify):
    """TODO: Docstring for collectPlaylists.

    :spotify: TODO
    :returns: TODO

    """
    results = spotify.current_user_playlists() # has default limit of 50
    playlists = results['items']
    while results['next']:
        results = spotify.next(results)
        playlists.extend(results['items'])

    return playlists




# preemptive function declaration
def createPlaylist():
    """TODO: Docstring for createPlaylist.
    :returns: TODO

    """
    pass



def filter_tracks(spotify, tracks):
    """TODO: Docstring for filter_tracks.

    :spotify: TODO
    :tracks: TODO
    :returns: TODO

    """
    '''
    logic:
    *** might be better/easier if transpose tracks and playlists to dicts with names as keys ***
    1. bool created = False # tracks whether a new playlist has been made or not
    # if True, have to reload user playlists
    2. get playlists
    3. build list of playlist names
    4. for track in tracks
        - if created = True
            - reload playlists
        - get artist name
        - check if artist name in playlist_names list
            - True: add song to playlist
            - False:
                - create playlist
                - add song to playlist
                - set created = True

    '''
    created = False
    playlists = collectPlaylists(spotify)
    for track in tracks:
        # do stuff
        if created: playlists = collectPlaylists(spotify)
        # get artist name
        # check if artist name is a playlist



'''
request result structure:
liked(dict)
|
|\-> href(str)
|\-> items(list of tracks, each a dict)
        |-> a track(dict)
                |->added_at(str)
                |->track(dict)
|\-> limit(int)
|\-> next (str)
|\-> offset (int)
|\-> previous (None)
\-> total(int)
'''


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    spotify = authenticate(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES)
    tracks = collectLikedTracks(spotify)



if __name__ == "__main__":



    spotify = authenticate(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES)
    # tracks = collectLikedTracks(spotify)
    # filter_tracks(spotify, tracks)

    # print('tracks', len(tracks), type(tracks))
    # for key, val in tracks[0].items():
        # print(key, val)


    playlists = collectPlaylists(spotify)
    for p in playlists:
        print(p['name'])

    '''
    deleting a song from 'liked'
    - sp.current_user_saved_tracks_delete(tracks=None)
    where tracks is a list of track URIs, URLs, or IDs
    '''


    '''
    get list of user playlists
    sp.user_playlists(user, limit=50, offset=0)

    or
    sp.current_user_playlists()
    '''


    '''
    retrieving a playlist
    sp.playlist(playlist_id, fields=None)
    where fields is a list of which fields to return

    or perhaps
    sp.playlist_items(playlist_id, fields=None, limit=100, offset=0)

    or perhaps
    sp.playlist_tracks(playlist_id, fileds=None, limit=100, offset=0)
    '''


    '''
    create a playlist
    sp.user_playlist_create(user, name, public=True, collaborative=False, description='')
    '''


    '''
    add a song to a playlist
    sp.palylist_add_items(playlist_id, items, position=None)

    or perhaps
    sp.user_playlist_add_tracks(user, playlist_id, tracks, position=None)
    '''
