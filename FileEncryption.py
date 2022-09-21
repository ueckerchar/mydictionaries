infile = open('info_security.txt','r')
for line in infile:
    txt = line

codes = {'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#','C' : '7','c' : '*','D' : '+','d' : 'l','E' : '2', 'e' : '3','F' : '7','f' : '0','G' : '6','g' : '<','H' : 'q','h' : 'x','I' : 'u','i' : '.','J' : '&','j' : ')','K' : '!','k' : '{','L' : ',','l' : '-','M' : '^','m' : '0','N' : '/','n' : 'v','O' : '&','o' : 's','P' : '#','p' : '?','Q' : 'i','q' : '<','R' : 'f','r' : ']','S' : '=','s' : '!','T' : 'b','t' : 'w','U' : '7','u' : 'c','V' : '|','v' : '8','W' : 'h','w' : 'k','X' : ';','x' : 'b','Y' : 'x','y' : 'p','Z' : '5','z' : 'r'}

DiffText = ''

for i in range(0, len(txt)):
    if txt[i] in codes.keys():
        DiffText += codes[txt[i]]
    else:
        DiffText += txt[i]

print(DiffText)

outfile = open('encrypted.txt','w')
outfile.write(DiffText + '\n')


outfile.close()