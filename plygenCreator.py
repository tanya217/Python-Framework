with open("lex.txt") as f:
    with open("plygen.py", "w+") as f1:
        for line in f:
            f1.write(line)

f1=open("plygen.py","a")
f1.write("import ply.yacc as yacc")
count=1
stri=""
literals=['+','(',')',':','\'','\"','=','<','/',',','*','!','%']
f3=open("newRules.txt","w")
noOfLines=0
with open("rules.txt") as f2:
    for line in f2:
        noOfLines=noOfLines+1
        for word in line:
            if(word in literals):
                word=" "+"\'"+word+"\'"+" "
                f3.write(word)
            else:
                f3.write(word)
f3=open("newRules.txt","r")
global action
action=[]
for line in f3:
    f1.write("\n")
    func_name="def p_"+str(count)+"(p):"
    f1.write(func_name)
    rhs_action=line.split("->")[1]
    rhs=rhs_action.split("``")[0]
    action.append(rhs_action.split("``")[1])
    lhs=line.split("->")[0]
    stri=stri+lhs+" "+':'+" "+ rhs
    f1.write("\n")
    f1.write("\t" +"\""+stri.rstrip("\n")+"\"")
    f1.write("\n")
    f1.write("\n")
    if(count!=1 and count!=noOfLines):
        #f1.write("\t"+"print(\"Syntax error at line\",lineCount)"+"\n")
        #f1.write("\t"+"print(data)"+"\n")
        f1.write("\t"+"print(action[%d])"%(count-1)+"\n")
        #f1.write("\t"+"print(%d)"%(count)+"\n")
    stri=""
    count=count+1
f3=open("yacc.txt","r")
for line in f3:
    f1.write(line)
