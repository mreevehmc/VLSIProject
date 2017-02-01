f = open('testvector.txt', 'r')
testvectors = [x.strip() for x in f.readlines()]
inputs = [s[0:11] for s in testvectors]
in_len = len(inputs)
outputs = [s[12:23] for s in testvectors]
out_len = len(outputs)

newline = 0;
print "const uint16_t PROGMEM input_vals[] = {"
all_inputs = ''
for a in inputs:
    all_inputs += hex(int(a,2)) + ', '
    newline += 1;
    if newline == 8:
        all_inputs += '\n'
        newline = 0
print all_inputs[:-2]
print "}"
    
print '\n'

newline = 0;
print "const uint16_t PROGMEM output_vals[] = {"
all_outputs = ''
for b in outputs:
    all_outputs += hex(int(b,2)) + ', '
    newline += 1;
    if newline == 8:
        all_outputs += '\n'
        newline = 0
print all_outputs[:-2]
print "}"

