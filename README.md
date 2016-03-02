# menoo
*interactive cli menu module for python*

### summary

Creating interactive cli utilities has never been easier! With **menu** you can, within **four** lines of code,
create your own arrow-keys controlled any-purpose menu.

### example

```python
from menoo import Menu

def print_choice(i):
    print i

menu = Menu(title='do you want to build a snowman?')
menu.add_option('yes', print_choice)
menu.add_option('no', print_choice)
menu.start()
```

### usage

`Menu(title='', cursor='>>', fullscreen=False)` instantiates a new Menu object, but **does not** start it yet,
with the following optional parameters:

1. `title` - displayed above the list of options
2. `cursor` - displayed near the selected option
3. `fullscreen` - will clear screen prior to rendering the menu

`Menu.add_option(text, handler)` adds a new entry to the list of options

1. `text` - the text to display
2. `handler` - a function which receives a single integer as its first positional argument, representing the index of
the selected option. the function can vary between options.

`Menu.start()` starts the menu and enters the menu loop. blocks the program until an option has been chosen

`Menu.stop()` will stop the menu loop on its next iteration

### getting it

`$ pip install menoo`
