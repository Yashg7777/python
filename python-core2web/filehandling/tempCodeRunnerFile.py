
import employee,pickle

f1=open("empdata.txt","rb")

obj=pickle.load(f1)
obj.display()