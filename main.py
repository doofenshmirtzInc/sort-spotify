#!/usr/bin/env python3

import os
import sys
import spotipy
from wrappers import Playlist, Track
from spotipy.oauth2 import SpotifyOAuth
from secrets import SECRETS


if __name__ == "__main__":


    SCOPES = [
        'user-library-read',
        'user-library-modify',
        'playlist-modify-public',
        'playlist-modify-private',
        'playlist-read-private'
    ]


    SaverBot(AUTH(scopes, *SECRETS['discover'])).save_discover_tracks()
