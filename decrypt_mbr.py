import idaapi 
start_ea = 0x7C19
encr_size = 0xCF
for ix in xrange(encr_size):
  byte_to_decr = idaapi.get_byte(start_ea + ix)
  to_rotate = (0xCF - ix) % 8
  byte_decr = (byte_to_decr >> to_rotate) | (byte_to_decr << (8 - to_rotate))
  idaapi.patch_byte(start_ea + ix, byte_decr)