def on_button_pressed_a():
    global temp
    temp += 1
    basic.show_number(temp)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(temp)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global temp
    temp += -1
    basic.show_number(temp)
input.on_button_pressed(Button.B, on_button_pressed_b)

temp = 0
temp = 26
isOpen = 0

def on_forever():
    global isOpen
    basic.show_number(input.temperature())
    if input.temperature() <= temp:
        if isOpen == 0:
            pins.servo_write_pin(AnalogPin.P1, 0)
            basic.pause(200)
            pins.servo_write_pin(AnalogPin.P2, 109)
            isOpen = 1
    else:
        if isOpen == 1:
            pins.servo_write_pin(AnalogPin.P1, 95)
            basic.pause(300)
            pins.servo_write_pin(AnalogPin.P2, 120)
            isOpen = 0
basic.forever(on_forever)
