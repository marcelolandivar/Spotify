from .menu_item import MenuItem

from pytify.core import search_artist
from pytify.core import get_artist_albums
from pytify.core import get_album_tracks
from pytify.core import play

from .empty_results_error import EmptyResultError

from pytify import authenticate
from pytify import read_config


class DataManager():
    def __init__(self):
        self._conf = read_config()
        self._auth = authenticate(self._conf)
