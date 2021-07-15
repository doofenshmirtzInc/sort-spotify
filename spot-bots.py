"""
File: discover_weekly.py
Author: Jack McShane
Email: jackmcshane@protonmail.com
Github: https://github.com/jackrmcshane/
Description: a python script for saving my discover weekly playlist to a personal playlist
"""


import spotipy
from wrappers import AUTH, Playlist, Track
from spotipy.oauth2 import SpotifyOAuth





class SpotifyBot(object):
    def __init__(self, auth):
        super(SpotifyBot, self).__init__()
        self.auth = auth


    def get_liked_library():
        results = self.auth.spotify.current_user_saved_tracks()
        tracks = [item['track'] for item in results['items']]
        while results['next']:
            results = self.auth.spotify.next(results)
            tracks.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def get_user_playlists():
        results = self.auth.spotify.current_user_playlists()
        playlists = results['items']
        while results['next']:
            results = self.auth.spotify.next(results)
            playlists.extend(results['items'])

        return list(map(Playlist, playlists))


    def get_playlist_tracks(pid):
        results = self.auth.spotify.playlist_tracks(pid)
        tracks = [item['track'] for item in results['items']]
        while results['next']:
            results = self.auth.spotify.next(results)
            playlists.extend([item['track'] for item in results['items']])

        return list(map(Track, tracks))


    def save_tracks_to_playlist(pid, tracks):
        self.auth.spotify.user_playlist_add_tracks(self.auth.spotify.current_user(), pid, tracks)






class SorterBot(SpotifyBot):
    def __init__(self, auth):
        super(SorterBot, self).__init__(auth)


    def sort_liked_playlist():
        pass




class SaverBot(SpotifyBot):
    def __init__(self, auth):
        super(SaverBot, self).__init__(auth)

    def get_discover_tracks(pid):
        pass

    def save_discover_tracks(pid):
        pass

