#!/usr/bin/env python3

import os
import sys
import spotipy
from wrappers import Playlist, Track
from spotipy.oauth2 import SpotifyOAuth
from secrets import SECRETS




if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print('fuck u doin?')


    arg = sys.argv[1]
    if arg in ('-h', '--help'):
        print('help')
    if arg in ('-s', '--sort'):
        # sorting route
        pass
    if arg in ('-d', '--discover'):
        # discover route
        pass





    SCOPES = [
        'user-library-read',
        'user-library-modify',
        'playlist-modify-public',
        'playlist-modify-private',
        'playlist-read-private'
    ]


