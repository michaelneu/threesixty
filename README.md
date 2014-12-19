# threesixty

First of all, threesixty is based on some parts of [jaraco.input], that's also, why threesixty is released under the MIT license. Nevertheless this library allows you to create XBOX 360 controller based user-interaction without worrying about how to interact with the controller itself. And it's really simple. 

## Installation
threesixty is currently Windows-only. You need to have `xinput1_3.dll` installed (which should be included in Windows 7/8 by default). Linux support is planned. 

After cloning the repository, you can go ahead and install it via
```sh
python setup.py install
```

## Basic usage
Using threesixty is indeed quite simple.
```python
import threesixty

controllers = threesixty.controllers()

def a_pressed(controller):
	print "A pressed"
	return False
    
def b_hold_down(controller):
	print "B is being pressed"
    
if len(controllers) > 0:
	controller = controllers[0]
    
    controller.on(threesixty.A, a_pressed)
    controller.on(threesixty.B, b_hold_down)
```

The root directory of the repository contains two simple examples which should explain, how threesixty works. 

## What threesixty isn't
- A game engine
	- threesixty was meant to be used for any application, but not in order to replace a real game engine. It allows you to use a controller, but that's it

- A perfect event handling system
	- It handles events, but doesn't use any library like [zope.event](https://github.com/zopefoundation/zope.event). threesixty uses a multithreaded callback system to fire its events. 



[jaraco.input]:http://pydoc.net/Python/jaraco.input/1.0.1/jaraco.input.win32.xinput/