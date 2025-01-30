import RPi.GPIO as GPIO

BEAM_PIN = 27
LED_PIN = 17

score = 0;
ballcount = 0;

def break_beam_callback(channel):
    global score
    global ballcount
    if GPIO.input(BEAM_PIN):        #RISING
        print("beam unbroken")
        GPIO.output(LED_PIN, GPIO.LOW)     # TURN OFF LED
    else:
        print("beam broken")        #FALLING
        if (ballcount < 9):
            score = score + 1000
            ballcount += 1
            print(score)
            GPIO.output(LED_PIN, GPIO.HIGH)     # TURN ON LED

        if ballcount >= 9:
            print("GAME OVER")
            GPIO.cleanup()
        sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(FALSE)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

# RISING means unbroken, FALLING means broken, or GPIO.BOTH for both
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()
