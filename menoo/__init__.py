import blessings
import readchar


class Menu(object):

    keys = {'up': '\x1b[A',
            'down': '\x1b[B',
            'select': '\r'}

    def __init__(self, title='', cursor='>>', fullscreen=False):
        self._terminal = blessings.Terminal()

        self._title = title
        self._cursor = cursor
        self._fullscreen = fullscreen

        self._options = []
        self._selected = 0

        self._active = False

    def add_option(self, text, handler):
        option = Option(text, handler)
        self._options.append(option)

    def start(self):
        if len(self._options) == 0:
            raise Exception('At least a single option is needed in order to start the menu')

        self._initialize_view()

        self._active = True
        while self._active:
            self._refresh_view()
            self._read_key()

    def stop(self):
        self._active = False

    def _initialize_view(self):
        self._prepare()
        self._print_title()
        self._print_menu()

    def _prepare(self):
        if self._fullscreen:
            print self._terminal.clear

    def _print_title(self):
        print self._title

    def _print_menu(self):
        for i in xrange(len(self._options)):
            if self._selected == i:
                print '{0} {1}'.format(self._cursor, self._options[i].text)
            else:
                print self._options[i].text

    def _refresh_view(self):
        self._clear_view()
        self._print_menu()

    def _clear_view(self):
        move_cursor_up = (self._terminal.move_up * (len(self._options) + 1))
        print move_cursor_up + self._terminal.clear_eos

    def _read_key(self):
        keycode = readchar.readkey()

        if keycode == Menu.keys['up']:
            self._navigate_to_option(self._selected - 1)
        elif keycode == Menu.keys['down']:
            self._navigate_to_option(self._selected + 1)
        elif keycode == Menu.keys['select']:
            self._select_current_option()

    def _navigate_to_option(self, option_id):
        if option_id not in xrange(len(self._options)):
            if option_id < 0:
                option_id = 0
            else:
                option_id = len(self._options) - 1

        self._selected = option_id

    def _select_current_option(self):
        self._options[self._selected].handler(self._selected)
        self.stop()


class Option(object):

    def __init__(self, text, handler):
        self._text = text
        self._handler = handler

    @property
    def text(self):
        return self._text

    @property
    def handler(self):
        return self._handler
