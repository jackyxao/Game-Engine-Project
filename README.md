# **Game Engine Project**
### Main Authors: _Jacky Xao_, *Dustin Hu*
------
This is a revival of the dropped project from the Game Development Club from Milliken Mills High School.
We were essentially building the engine that would run a pixel rpg type game. 

The code originally is written in Python ver. 2.7.9 and uses pygame ver. 1.9.1
*UPDATE* I changed the syntax to work in python 3 (I use Python 3.6.1 and Pygame 1.9.3 now)
(~~Although I don't think it'll matter that much~~)
##### So far:
- we can import a map template file and create a corrisponding image with the correct tile images
- we can control a move a 'character' around the map using arrow keys
- we can walk through doors and 'teleport' to another map instance

##### Testing/running the engine
- Run one of the test scripts for now. Eventually there will be a proper interface...
```bat
$ python3 testXXX.py
```
- So far there is `testMap.py` and `testEngine.py`
##### To Do ~~(In general)~~:
- Make a plan.
- Make a proper mainloop
- Create event handlers to manage incoming events
- Add movement animations
- Do a better job at handling exceptions
- Compress all the seperate tile images into a single tileset image
- Rethink the whole 'object' idea
- If you want a battle system, then make one.

If you have any questions, ask either  [myself](https://github.com/jackyxao) or [Dustin Hu](https://github.com/Tenteki)
