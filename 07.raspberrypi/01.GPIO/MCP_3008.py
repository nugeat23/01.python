import spidev
import time

delay = 0.5

pot_channel = 0     # MCP3008 채널 중 센서에 연결한 채널 설정

spi = spidev.SpiDev()

spi.open(0,0)

spi.max_speed_hz = 100000

def readadc(adcnum):
    if adcnum <0 or adcnum > 7:
        return -1

    r = spi.xfer2([1,8+adcnum<<4,0])
    data = ((r[1]&3)<<8) + r[2]

    return data

while True:
    pot_value = readadc(pot_channel)
    print("-------------------------")
    print(f'LDR value: {pot_value}')
    # print("LDR value: %d" %pot_value)
    time.sleep(delay)