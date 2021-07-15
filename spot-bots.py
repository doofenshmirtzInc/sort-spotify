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
        # get liked library songs
        # get playlists
        # get tracks for each playlist
        # for each track in liked library,
            # if track.artist is not a playlist
                # create playlist w/ artist name
                # add track to playlist
            # else
                # get corresponding playlist tracks
                # if current track in playlist tracks
                    # next
                # else
                    # add track to playlist
            # remove current track from liked library
        pass




class SaverBot(SpotifyBot):


    def __init__(self, auth):
        super(SaverBot, self).__init__(auth)
        self.discover_uri = 'spotify:playlist:37i9dQZEVXcDpi5Jo3ptNB'

    def get_discover_tracks(pid):
        self.discover_tracks = self.get_playlist_tracks(self.discover_uri)

    def save_discover_tracks(pid):
        # create new discovered playlist
        import time
        pname = '{}-Discover Weekly'.format('''time string''')
        descr = 'A previous Discover weekly playlist from spotify'
        new_playlist = self.auth.spotify.user_playlist_create(self.auth.spotify.current_user(), pname, public=False, description=descr)
        return new_playlist
        # save discover tracks to specified playlist (pid)
