input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    if (start == 0) {
        basic.clearScreen()
        basic.showString("" + (randint(0, 9)))
        start = 1
    }
})
input.onGesture(Gesture.Shake, function () {
    if (start == 0) {
        basic.clearScreen()
        basic.showString("" + (randint(0, 100)))
    }
})
input.onButtonPressed(Button.B, function () {
    if (start == 1) {
        basic.clearScreen()
        basic.showString("" + (randint(0, 9)))
        start = 0
    } else {
        soundExpression.yawn.playUntilDone()
    }
})
let start = 0
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . # . # .
    # . . . #
    `)
start = 0
music.playMelody("C5 B C5 B C5 B C5 B ", 120)
