# 3M-ergo-mouse-macos-scroller
A python script for macOS to enable scrolling with the 3M ergonomic mouse [EM500GPS](https://www.3m.com/3M/en_US/p/dc/v000093833/) in any application.

## How to install
Make sure you have python installed. Open a terminal and run 
```zsh
pip install pynput
```
to install [pynput](https://github.com/moses-palmer/pynput), the awesome python package to monitor and simulate mouse and keyboard input.
Place the scrolling.py in a memorable place. Update the path in scrolling_launcher.plist to point to where you placed the scolling.py. Place scrolling_launcher.plist in 
` ~/Library/LaunchAgents/ `
Then open up a terminal and run 
```zsh
launchctl load -w ~/Library/LaunchAgents/scrolling_launcher.plist
```
After that, the python script should be run automatically at startup and scrolling with the mouse should be possible while the middle mouse button (the one at the back) is pressed.

A WORD OF WARNING: THIS PROGRAM WORKS WITH TOOLS THAT CAN MONITOR AND CONTROL YOUR KEYBOARD AND MOUSE. THIS IS A VERY SIMPLE PROGRAM THAT JUST EMULATES A SCROLLWHEEL IF THE MIDDLE MOUSE BUTTUN IS PRESSED AND THE MOUSE IS MOVED AT THE SAME TIME. YOU SHOULD HOWEVER BE CAREFUL WHAT YOU RUN ON YOUR SYSTEM, ESPECIALLY IF IT CAN MONITOR AND CONTROLL ALL YOUR KEYBOARD AND MOUSE INPUTS.
