# Digital electronics circuit project using Map Entered Variable(MEV) method of reduction for 4 variables

a=int(input("Please enter the number of min-terms that you are going to enter(max-16):"))
print("Enter the min-terms in ascending order : ",end="\n")
b=[]
for i in range(a):
	c=int(input())
	b.append(c)

print("Your question :  f(a,b,c,d) = ⵉ m(",end="")
for i in b:
	print(i,end=",")
print(end=")\n")
print("\n")

dec=list(range(16))
fun=[]
for i in dec:
	if i in b:
		fun.append(1)
	else:
		fun.append(0)
    
#print(fun)

final=[]
fun0=fun[0:4]
fun1=fun[4:8]
fun2=fun[8:12]
fun3=fun[12:16]

def kmap(x):
	if (x[0]==1 and x[1]==1) and (x[2]==1 and x[3]==1):
		final.append("1")
	elif (x[0]==1 and x[1]==0) and (x[2]==0 and x[3]==0):
		final.append("c'd'")
	elif (x[0]==0 and x[1]==1) and (x[2]==0 and x[3]==0):
		final.append("c'd")
	elif (x[0]==0 and x[1]==0) and (x[2]==1 and x[3]==0):
		final.append("cd'")
	elif (x[0]==0 and x[1]==0) and (x[2]==0 and x[3]==1):
		final.append("cd")
        
	elif (x[0]==1 and x[1]==1) and (x[2]==0 and x[3]==0):
		final.append("c'")
	elif (x[0]==0 and x[1]==0) and (x[2]==1 and x[3]==1):
		final.append("c")
	elif (x[0]==1 and x[1]==0) and (x[2]==1 and x[3]==0):
		final.append("d'")
	elif (x[0]==0 and x[1]==1) and (x[2]==0 and x[3]==1):
		final.append("d")
	elif (x[0]==1 and x[1]==0) and (x[2]==0 and x[3]==1):
		final.append("(c⊕ d)'")
	elif (x[0]==0 and x[1]==1) and (x[2]==1 and x[3]==0):
		final.append("(c⊕ d)")
         
	elif (x[0]==0 and x[1]==1) and (x[2]==1 and x[3]==1):
		final.append("(c+d)")
	elif (x[0]==1 and x[1]==1) and (x[2]==0 and x[3]==1):
		final.append("(c'+d)")
	elif (x[0]==1 and x[1]==0) and (x[2]==1 and x[3]==1):
		final.append("(c+d')")
	elif (x[0]==1 and x[1]==1) and (x[2]==1 and x[3]==0):
		final.append("(c'+d')")
    
	else:
		final.append("0")
kmap(fun0)
kmap(fun1)
kmap(fun2)
kmap(fun3)
#print(final)
print("   | b'   | b     ") 
print("----------------")
print(" a'|",final[0],"|",final[1],"|" )
print("----------------")
print(" a |",final[2],"|",final[3],"|" ,end="\n")
print("----------------")
print("\n \n")

tup=tuple(final)
#print(tup)

for i in range(4):
	if (final[i]!="0" and  final[i]!="1"):
		final[i]="0"
              
#print(final) 
step2=set(list(tup))
step2.discard("0")
step2.discard("1")
step3=list(step2)
#print("step3 =",step3)
   

def mevmap(x,y):
	if ((x[0]=="1" and x[1]=="1" ) and (x[2]=="1" and x[3]=="1")) or ((x[0]=="@" and x[1]=="@" ) and (x[2]=="@" and x[3]=="@")):
		exp= y
		return(exp)
	elif ((x[0]=="1" and x[1]=="0") and (x[2]=="0" and x[3]=="0")) or ((x[0]=="@"and x[1]=="0") and (x[2]=="0" and x[3]=="0")):
		exp="(a'b')"+ y
		return(exp)
	elif ((x[0]=="0" and x[1]=="1") and (x[2]=="0" and x[3]=="0")) or ((x[0]=="0" and x[1]=="@" ) and (x[2]=="0" and x[3]=="0")):
		exp="(a'b)"+y 
		return(exp)
	elif ((x[0]=="0" and x[1]=="0") and (x[2]=="1"  and x[3]=="0")) or ((x[0]=="0" and x[1]=="0") and (x[2]=="@"  and x[3]=="0")):
		exp="(ab')"+y
		return(exp)
	elif ((x[0]=="0" and x[1]=="0" ) and (x[2]=="0" and x[3]=="1" )) or ((x[0]=="0" and x[1]=="0" ) and (x[2]=="0" and x[3]=="@" )):
		exp="(ab)"+y
		return(exp)
	elif ((x[0]=="1" and x[1]=="1" ) and (x[2]=="0" and x[3]=="0")) or ((x[0]=="@" and x[1]=="@" ) and (x[2]=="0" and x[3]=="0")):
		exp="(a')"+y
		return(exp)
	elif ((x[0]=="0" and x[1]=="0") and (x[2]=="1"  and x[3]=="1" )) or ((x[0]=="0" and x[1]=="0") and (x[2]== "@" and x[3]=="@" )):
		exp="(a)"+y
		return(exp)
	elif ((x[0]=="1" and x[1]=="0") and (x[2]=="1"  and x[3]=="0")) or ((x[0]=="@" and x[1]=="0") and (x[2]=="@"  and x[3]=="0")):
		exp="(b)'"+y
		return(exp)
	elif ((x[0]=="0" and x[1]=="1" ) and (x[2]=="0" and x[3]=="1" )) or ((x[0]=="0" and x[1]=="@" ) and (x[2]=="0" and x[3]=="@" )):
		exp="(b)"+y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="0") and (x[2]=="0" and x[3]=="1" )) or ((x[0]=="@"  and x[1]=="0") and (x[2]=="0" and x[3]=="@" )):
		exp="((a⊕ b)')"+y
		return(exp)
	elif ((x[0]=="0" and x[1]=="1" ) and (x[2]=="1"  and x[3]=="0")) or  ((x[0]=="0" and x[1]=="@" ) and (x[2]=="@"  and x[3]=="0")):
		exp="(a⊕ b)"+y
		return(exp)
            
	elif ((x[0]=="0" and x[1]=="1" ) and (x[2]=="1"  and x[3]=="1" )) or  ((x[0]=="0" and x[1]=="@" ) and (x[2]=="@"  and x[3]=="@")):
		exp="(a+b)"+y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="1") and (x[2]=="0" and x[3]=="1" )) or ((x[0]=="@" and x[1]=="@") and (x[2]=="0" and x[3]=="@" )):
		exp="(a'+b)"+y
		return(exp)
	elif ((x[0]=="1" and x[1]=="0" ) and (x[2]=="1"  and x[3]=="1")) or ((x[0]=="@" and x[1]=="0") and (x[2]=="@"  and x[3]=="@")):
		exp="(a+b')" +y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="1" ) and (x[2]=="1"  and x[3]=="0" )) or ((x[0]=="@"  and x[1]=="@" ) and (x[2]=="@"  and x[3]=="0" )):
		exp="(a'+b')"+y
		return(exp)
	elif ((x[0]=="@"  and x[1]=="1" ) and (x[2]=="@"  and x[3]=="1" )) or ((x[0]=="1"  and x[1]=="@" ) and (x[2]=="1"  and x[3]=="@" )): 
		exp=y
		return(exp)
	elif ((x[0]=="@"  and x[1]=="@" ) and (x[2]=="1"  and x[3]=="1" )) or ((x[0]=="1"  and x[1]=="1" ) and (x[2]=="@"  and x[3]=="@" )):
		exp= y
		return(y)
	elif ((x[0]=="0"  and x[1]=="1" ) and (x[2]=="0"  and x[3]=="@" )) or ((x[0]=="0"  and x[1]=="@" ) and (x[2]=="0"  and x[3]=="1" )):
		exp="(b)"+y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="@" ) and (x[2]=="0"  and x[3]=="0" )) or ((x[0]=="@"  and x[1]=="1" ) and (x[2]=="0"  and x[3]=="0" )):
		exp="(a')"+y
		return(exp)
	elif ((x[0]=="0"  and x[1]=="0" ) and (x[2]=="1"  and x[3]=="@" )) or ((x[0]=="0"  and x[1]=="0" ) and (x[2]=="@"  and x[3]=="1" )):
		exp="(a)"+y
		return(exp)
	elif ((x[0]=="@"  and x[1]=="1" ) and (x[2]=="0"  and x[3]=="1" )) or ((x[0]=="0"  and x[1]=="@" ) and (x[2]=="0"  and x[3]=="1" )):
		exp="(b)"+y
		return(exp)
	elif ((x[0]=="@"  and x[1]=="1" ) and (x[2]=="0"  and x[3]=="1" )) or ((x[0]=="0"  and x[1]=="1" ) and (x[2]=="@"  and x[3]=="1" )):
		exp="(b)"+y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="@" ) and (x[2]=="1"  and x[3]=="0" )):
		exp="(b')"+y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="@" ) and (x[2]=="0"  and x[3]=="1" )):
		exp="(a'+b)"+y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="0" ) and (x[2]=="@"  and x[3]=="0" )):
		exp="(b')"+y
		return(exp)
	elif ((x[0]=="0"  and x[1]=="@" ) and (x[2]=="1"  and x[3]=="0" )):
		exp="(ab')"+y
		return(exp)
	elif ((x[0]=="@"  and x[1]=="1" ) and (x[2]=="1"  and x[3]=="1" )):
		exp= y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="@" ) and (x[2]=="@"  and x[3]=="1" )):
		exp= y
		return(exp)
	elif ((x[0]=="1"  and x[1]=="0" ) and (x[2]=="0"  and x[3]=="@" )):
		exp="(a'b')"+y
		return(exp)
		
	
	else:
		pass

step1=mevmap(final,"")
#print("step1=",step1)
do = []
#print("do =",do)
if step1 != None:
	do.append(step1)
	
#reserve=list(tup)
#print("reserve =",reserve)

def this(vision,x):
	for i in range(len(vision)):
		if vision[i]==x:
			vision[i]="1"
		elif vision[i]=="1":
			vision[i]="@"
		else:
			vision[i]="0"
	#print("vision =",vision)
	just= mevmap(vision,x)
	return(just)
			
#print(reserve)
for j in range(len(step3)):	
	a=this(list(tup),step3[j])
	#print(step3[j])
	do.append(a)
		
justit=set(do)
justdoit=list(justit)
print("f(a,b,c,d) = ",end="")
for i in justdoit:
	print(i,end="")
	if i!=justdoit[-1]:
		print(" + ",end="")
print("\n")
		

	
	
	
	




     





       

    


        






