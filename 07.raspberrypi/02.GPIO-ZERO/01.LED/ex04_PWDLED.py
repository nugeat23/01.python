from gpiozero import PWMLED
from signal import pause

red = PWMLED(13)

red.pulse(fade_in_time=2,fade_out_time=2)

pause()