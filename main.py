def on_button_pressed_a():
    global start
    basic.clear_screen()
    if start == 0:
        basic.clear_screen()
        basic.show_string("" + str((randint(0, 9))))
        start = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    if start == 0:
        basic.clear_screen()
        basic.show_string("" + str((randint(0, 100))))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global start
    if start == 1:
        basic.clear_screen()
        basic.show_string("" + str((randint(0, 9))))
        start = 0
    else:
        soundExpression.yawn.play_until_done()
input.on_button_pressed(Button.B, on_button_pressed_b)

start = 0
basic.show_leds("""
    # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
""")
start = 0