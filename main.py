f = open('archivo.txt','w')
for i in range(0,10):
  f.write('Line '+str(i+1)+'\n')
f.close()
