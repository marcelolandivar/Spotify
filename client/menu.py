import curses
import curses.panel

from .alingment import Alignment
from .panel import Panel

NEW_LINE = 10
CARRIAGE_RETURN = 13


class Menu(Panel):
    """
    The Menu class inherits from the Panel base class, and the class initializer
    gets a few arguments: the title, the dimensions,
    the alignment setting which is LEFT by default, and the items.
    The items argument is a list of MenuItems objects.
    """
    def __init__(self, title, dimensions, align=Alignment.LEFT, items=[]):
        # Super is used to initialize the Panel class
        super().__init__(title, dimensions)
        self._align = align
        self.items =items

    def get_selected(self):
        items = [x for x in self.items if x.selected]
        return None if not items else items[0]

    def _select(self, expr):
        """
        Get the index of the current selected item, then run it in expr which
        will determine the next current item index. If the new index is less
        than 0 then it means we reach the top of the list, and if the new index
        is greater than the current index and the new index is grater or equal
        than the number of menu items on the lists then it is at the bottom.
        """
        current = self.get_selected()
        index = self.items.index(current)
        new_index = expr(index)

        if new_index < 0:
            return

        if new_index > index and new_index >= len(self.items):
            return

        self.items[index].selected = False
        self.items[new_index].selected = True

    def next(self):
        self._select(lambda index: index + 1)

    def previous(self):
        self._select(lambda index: index - 1)

    def _initialize_items(self):
        longest_label_item = max(self.items, key=len)

        for item in self.items:
            if item != longest_label_item:
                padding = (len(longest_label_item) - len(item)) * ' '
                item.label = (f'{item}{padding}' if self._align == Alignment.LEFT else f'{padding}{item}')

            if not self.get_selected():
                self.items[0].selected = True

    def init(self):
        self._initialize_items()

    def handle_events(self, key):
        """"
        Handle the events of up, down and enter key for changing the selection
        based on the created functions.
        """
        if key == curses.KEY_UP:
            self.previous()
        elif key == curses.KEY_DOWN:
            self.next()
        elif key == curses.KEY_ENTER or key == NEW_LINE or key == CARRIAGE_RETURN:
            selected_item = self.get_selected()
            return selected_item

    def __iter__(self):
        return iter(self.items)

    def update(self):
        """
        Set x and y coordinates to 2 which is where the menu will be shown.
         We loop through the menu items and call the addstr method to print
         the item on the screen with the position and style.
        """
        pos_x = 2
        pos_y = 2

        for item in self.items:
            self._win.addst(pos_y, pos_x, item.label,
                            curses.A_REVERSE if item.selected else curses.A_NORMAL)
            pos_y += 1

        self._win.refresh()






