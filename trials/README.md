# Remotely and interactively connect
```
ssh -Y pi@IP.addr.here.
```

# install

Install Pygame.

https://www.pygame.org/wiki/GettingStarted

```
python3 -m pip install -U pygame --user
```

Upgrade `pip` if needed
```
pip install -U pip
```

Test Install
```
python3 -m pygame.examples.aliens
```

# Setup gpio

connect pins to approrpiate breadboard circuit. User the GPIO for the raspberry pi

# Run
```
cd ~/Documents/pygame/skeeball

python3 main.py

#geany &  #IDE for rasp pi
```


# Research

https://realpython.com/pygame-a-primer/#background-and-setup

https://www.pygame.org/docs/tut/PygameIntro.html

https://www.raspberrypi.org/documentation/usage/gpio/python/README.md

https://gpiozero.readthedocs.io/en/stable/recipes.html
