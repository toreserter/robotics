#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop():

    x = event.code
   # print( event)

    if x == 2:
	y = event.value
        print('left wheels fw' + str(y))

    elif x == 5:
	y = event.value
        print('right wheels fw' + str(y))

    elif x == 310:

        print('left wheels back')

    elif x == 311:

        print('right wheels back')

    elif x == 3:

        y = event.value

        if y > 0:

            print('pan right' + str(y))

        else:

                  print('pan left' + str(y))

    elif x == 0:

        y = event.value

        if y > 0:

            print 'left +', y

            move(y/40, 'right', False)

        elif y < 0:
                  print 'right +', (y*-1)
                  move((y*-1)/40, 'left', False)
    elif x == 1:
        y = event.value
        if y > 0:

            print 'back', y

        else:

                  print 'fwd', (y*-1)

    elif x == 4:

        y = event.value

        if y > 0:

            print('tilt fwd' + str(y))

        else:

                  print('tilt back' + str(y))

    elif x == 304:
	print('A')
    elif x == 305:
	print('B')
    elif x == 307:
	print('X')
    elif x == 308:
	print('Y')
    elif x == 16:
	y = event.value
	if y>0:
		print('RIGHT')
	else:
		print('LEFT')
    elif x == 17:
	y = event.value
	if y>0:
		print('BOTTOM')
	else:
		print('TOP')

    elif x == 314:

        print('quit')

        break

    elif x == 315:

        print('servo reset')
