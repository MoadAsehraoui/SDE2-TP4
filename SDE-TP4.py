def on_sound_loud():
    for index in range(5):
        led.plot(0, index)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
        MelodyOptions.FOREVER)
    if input.button_is_pressed(Button.AB):
        music.stop_melody(MelodyStopOptions.ALL)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_number(input.light_level())
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

nbr_inclinaison_gauche = 0
nbr_inclinaison_droit = 0
while input.is_gesture(Gesture.TILT_LEFT) or input.is_gesture(Gesture.TILT_RIGHT):
    if input.is_gesture(Gesture.TILT_RIGHT):
        basic.pause(100)
        basic.show_number(nbr_inclinaison_droit)
        nbr_inclinaison_droit += 1
        continue
    if input.is_gesture(Gesture.TILT_LEFT):
        basic.pause(100)
        basic.show_number(nbr_inclinaison_gauche)
        nbr_inclinaison_gauche += 1
images.icon_image(IconNames.SQUARE).show_image(0)
if input.logo_is_pressed():
    for _in in range(5):
        for jn in range(5):
            led.unplot(_in, jn)
    images.icon_image(IconNames.SMALL_SQUARE).show_image(0)

def on_forever():
    if input.compass_heading() == 0 or (input.compass_heading() == 360 or input.compass_heading() == 180):
        basic.show_number(input.sound_level())
    elif input.compass_heading() == 90 or input.compass_heading() == 270:
        basic.show_number(input.temperature())
        basic.show_number(input.light_level())
basic.forever(on_forever)
