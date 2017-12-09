import random 
from time import sleep 
import subprocess
import piglow 

bashCommand = "play testsound.wav" 
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#process.communicate()
piglow.auto_update = True 

piglow.all(0)

sleep_period = 0.001

leds = ["01", "02", "03", "07", "08", "09", "13", "14", "15"]

def random_brightness(): 
	sleep(random.uniform(0,sleep_period)) 
	return random.randint(0,255)

#while True: 
led_to_switch = int(random.choice(leds)) 
piglow.led(1, random_brightness())
piglow.led(2, random_brightness())
piglow.led(3, random_brightness())
piglow.led(7, random_brightness()) 
piglow.led(9, random_brightness()) 
piglow.led(13, random_brightness()) 
piglow.led(14, random_brightness()) 
piglow.led(15, random_brightness())

process.communicate()
