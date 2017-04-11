import pickle
d={'a':1,'b':2}
f=open('datafile.pkl','wb')
pickle.dump(d,f)
f.close()
