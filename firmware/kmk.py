from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros
from kmk.modules.holdtap import HoldTap

import board

keyboard = KMKKeyboard()

# Define pins
keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11,
                     board.GP10, board.GP16, board.GP17, board.GP20, board.GP21)

keyboard.row_pins = (board.GP9, board.GP8, board.GP7, board.GP6, board.GP5,
                     board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Add modules
layers = Layers()
macros = Macros()
keyboard.modules = [layers, macros]

# Layer names
BASE = 0
PROD = 1
DEV = 2
GAME = 3
ART = 4

# Keymap
keyboard.keymap = [

    # 0: BASE LAYER (F1–F24)
    [
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,
        KC.F11, KC.F12, KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.F20,
        KC.F21, KC.F22, KC.F23, KC.F24, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.TRNS, KC.MO(PROD), KC.MO(DEV), KC.MO(GAME), KC.MO(ART), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ],

    # 1: PRODUCTIVITY LAYER
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Z), KC.LCTL(KC.LSFT(KC.Z)),  # Copy/Paste/Undo/Redo
        KC.WIN(KC.LSFT(KC.S)), KC.WIN(KC.DOT), KC.LALT(KC.TAB), KC.LCTL(KC.TAB),  # Snip, Emoji, AltTab
        KC.LCTL(KC.LSFT(KC.M)),  # Mute Mic
        KC.MACRO(0), KC.MACRO(1),  # Notepad, Terminal (macros below)
        *[KC.NO] * (100 - 11)
    ],

    # 2: DEV WORK LAYER
    [
        KC.LCTL(KC.LSFT(KC.B)), KC.F5, KC.LCTL(KC.SLASH),  # Build/Run, Comment
        KC.LCTL(KC.GRAVE), KC.LSFT(KC.LALT(KC.F)),         # Toggle terminal, Format
        KC.MACRO(2), KC.MACRO(3),  # Custom snippets, Git Pull/Push
        *[KC.NO] * (100 - 7)
    ],

    # 3: GAMING MACROS
    [
        KC.MACRO(4), KC.MACRO(5), KC.MACRO(6), KC.MACRO(7), KC.MACRO(8),
        *[KC.NO] * (100 - 5)
    ],

    # 4: CREATIVE / DESIGN LAYER
    [
        KC.LBRC, KC.RBRC,                 # Brush Size +/-
        KC.MACRO(9), KC.MACRO(10),        # Lock/Hide Layer
        KC.LCTL(KC.T), KC.LCTL(KC.J),     # Transform / Duplicate
        KC.F12, KC.B, KC.E,               # Render, Brush, Eraser
        *[KC.NO] * (100 - 9)
    ]
]

keyboard.macros = [
    # 0: Open Notepad (Windows Run shortcut)
    (0, [KC.WIN, KC.R], [KC.N, KC.O, KC.T, KC.E, KC.P, KC.A, KC.D, KC.ENTER]),

    # 1: Open Terminal
    (0, [KC.WIN, KC.R], [KC.C, KC.M, KC.D, KC.ENTER]),

    # 2: Insert Snippet
    (0, [], [KC.SLASH, KC.SLASH, KC.SPACE, KC.S, KC.N, KC.I, KC.P, KC.NEWLINE]),

    # 3: Git pull/push combo (as a placeholder, just types git pull)
    (0, [], [KC.G, KC.I, KC.T, KC.SPACE, KC.P, KC.U, KC.L, KC.L, KC.ENTER]),

    # 4: Quick Cast (simulate combo)
    (0, [], [KC.D, KC.D]),

    # 5: Double Tap Macro
    (0, [], [KC.SPACE, KC.SPACE]),

    # 6: Combo Tap
    (0, [], [KC.X, KC.W, KC.Y]),

    # 7: Inventory key
    (0, [], [KC.I]),

    # 8: Chat Command
    (0, [], [KC.SLASH, KC.D, KC.A, KC.N, KC.C, KC.E, KC.ENTER]),

    # 9: Lock Layer (e.g. L)
    (0, [], [KC.L]),

    #10: Hide Layer (e.g. H)
    (0, [], [KC.H]),
]

if __name__ == '__main__':
    keyboard.go()
