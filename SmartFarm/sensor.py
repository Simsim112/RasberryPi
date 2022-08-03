import smbus
import time

bus = smbus.SMBus(2)
time.sleep(1)

def setup(Addr):
	global address
	address = Addr

def read(): #channel
	try:
		bus.write_byte(address, 0x40)
	except Exception as e:
		print("Address : %s" % address)
		print(e)
	return bus.read_byte(address)

if __name__ == "__main__":
	setup(0x48)
	while(True):
		print("ANI0 = ", read())
		print(" ")
		time.sleep(1.0)
