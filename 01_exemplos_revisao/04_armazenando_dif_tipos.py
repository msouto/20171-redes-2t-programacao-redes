x,y,z=43,44,45
s='spam'
d={'a':1,'b':2}
l=[1,2,3]
arq=open('datafile.txt','w')
arq.write(s+'\n')
arq.write('%s,%s,%s\n' % (x,y,z))
arq.write(str(l)+'$'+str(d)+'\n')
arq.close()
