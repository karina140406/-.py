ascii_codes = "90 110 97 110 105 101 32 45 32 115 105 108 97 33"    
codes = ascii_codes.split()   
message = ''.join([chr(int(code)) for code in codes])    
print(message)  