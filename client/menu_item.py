from uuid import uuid1
# The uuid is used to identify information in computer systems.


class MenuItem:
    """
    The MenuItem initializer gets three arguments, the label item, the data
    which will contain the raw data returned by the Spotify REST API, and a
    flag stating whether the item is currently selected or not.
    """
    def __init__(self, label, data, selected=False):
        self.id = str(uuid1())
        self.data = data
        self.label = label

        def return_id():
            """
            This is the id for the item on Spotify, and the URI is the URI for
            the item on Spotify. The latter will be useful when we select
            and play a song.
            """
            return self.data['id'], self.data['uri']

        self.action = return_id
        self.selected = selected

    def __eq__(self, other):
        return self.id == other.id

    def __len__(self):
        """Returns the length of the menu item"""
        return len(self.label)

    def __str__(self):
        return self.label
