input.onButtonPressed(Button.A, function () {
    temp += 1
    basic.showNumber(temp)
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(temp)
})
input.onButtonPressed(Button.B, function () {
    temp += -1
    basic.showNumber(temp)
})
let temp = 0
temp = 26
let isOpen = 0
basic.forever(function () {
    basic.showNumber(input.temperature())
    if (input.temperature() <= temp) {
        if (isOpen == 0) {
            pins.servoWritePin(AnalogPin.P1, 0)
            basic.pause(200)
            pins.servoWritePin(AnalogPin.P2, 109)
            isOpen = 1
        }
    } else {
        if (isOpen == 1) {
            pins.servoWritePin(AnalogPin.P1, 95)
            basic.pause(300)
            pins.servoWritePin(AnalogPin.P2, 120)
            isOpen = 0
        }
    }
})
