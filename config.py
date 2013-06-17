# coding: utf-8

import os
from keyhac import *
from keyhacmacs import *

def configure(keymap):
    # editor
    editors = (
        "C:\Program Files\Sublime Text 2\sublime_text.exe",
        "notepad.exe",
        )

    for e in editors:
        if os.path.exists(e):
            keymap.editor = e
            break

    # font
    keymap.setFont("MeiryoKe_Gothic", 14)

    # theme
    keymap.setTheme("black")

    # keyhacmacs
    keyhacmacs.configure(keymap)
