#lex
import ply.lex as lex
from plygenCreator import action
tokens=('NUMBER','ID','DEF','TAB','RETURN','IF','ELIF','ELSE','PRINT','FOR','IN','RANGE','GREATERTHAN','MINUS','SPACE','COMMENT','AND','OR','NOT')
literals=['+','(',')',':',',','<','/','*','=','!','\'','"','%']

lineCount=0

def t_newline(t):
	r'\n+'
	global lineCount
	lineCount=lineCount+1

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t
def t_IF(t):
	r'if'
	return t
def t_FOR(t):
	r'for'
	return t
def t_DEF(t):
	r'def'
	return t
def t_TAB(t):
	r'\t'
	return t
def t_SPACE(t):
	r'\s'
	return t

def t_RETURN(t):
	r'return'
	return t
def t_ELIF(t):
	r'elif'
	return t
def t_PRINT(t):
	r'print'
	return t
def t_IN(t):
	r'in'
	return t
def t_RANGE(t):
	r'range'
	return t
def t_AND(t):
	r'and'
	return t
def t_OR(t):
	r'or'
	return t
def t_NOT(t):
	r'not'
	return t
def t_GREATERTHAN(t):
	r'>'
	return t
def t_MINUS(t):
	r'-'
	return t


def t_ID(t):
	r'[a-zA-Z_0-9][a-zA-Z_0-9]*'
	return t

def t_COMMENT(t):
	r'\'\'\'[if|while|do|for|print|elif|def|for|in|(|)|-|[a-zA-Z0-9]+]*\'\'\''
	return t


'''def p_empty(p):
	'empty :'
	pass'''

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer=lex.lex()
lexer.input("def computeGCD(x, y):\
	if x > y:\
		small = y\
	else:\
		small = x\
	for i in range(1, small+1):\
		if((x % i == 0) and (y % i == 0)):\
			gcd = i\
	return gcd\
a = 60\
b= 48\
print (computeGCD(60,48))")

#Tokenize
'''while True:
	tok = lexer.token()
	if not tok:
		break      # No more input
	print(tok.type)'''
import ply.yacc as yacc
def p_1(p):
	"Program  :  COMMENT Program"


def p_2(p):
	"Program :  DEF SPACE ID Expression  ':'  Funcbody Program"

	print(action[1])

def p_3(p):
	"Program :  DEF SPACE ID Expression  ')'   ':'  Funcbody Program"

	print(action[2])

def p_4(p):
	"Program :  DEF SPACE ID Expression  ':'  Program "

	print(action[3])

def p_5(p):
	"Program : DEF SPACE ID   ':'   Program"

	print(action[4])

def p_6(p):
	"Program  :  DEF SPACE ID Expression Funcbody "

	print(action[5])

def p_7(p):
	"Program : Statement"

	print(action[6])

def p_8(p):
	"Program : Assignment"

	print(action[7])

def p_9(p):
	"Program :  "

	print(action[8])

def p_10(p):
	"Funcbody  :  TAB Assignment Funcbody"

	print(action[9])

def p_11(p):
	"Funcbody :  TAB Condition Funcbody"

	print(action[10])

def p_12(p):
	"Funcbody :  TAB Statement Funcbody"

	print(action[11])

def p_13(p):
	"Funcbody :  TAB Loop Funcbody"

	print(action[12])

def p_14(p):
	"Funcbody :  TAB RETURN Idnum Funcbody"

	print(action[13])

def p_15(p):
	"Funcbody  :  Assignment "

	print(action[14])

def p_16(p):
	"Funcbody :  Condition "

	print(action[15])

def p_17(p):
	"Funcbody :  Statement "

	print(action[16])

def p_18(p):
	"Funcbody :  Loop "

	print(action[17])

def p_19(p):
	"Funcbody :  RETURN SPACE Idnum "

	print(action[18])

def p_20(p):
	"Funcbody :  "

	print(action[19])

def p_21(p):
	"Assignment  :  ID SPACE  '='  SPACE AssignmentExpression"

	print(action[20])

def p_22(p):
	"Assignment  :  ID SPACE  '='  '='  SPACE AssignmentExpression "

	print(action[21])

def p_23(p):
	"AssignmentExpression  :  NUMBER "

	print(action[22])

def p_24(p):
	"AssignmentExpression  :  NUMBER SPACE Op SPACE NUMBER "

	print(action[23])

def p_25(p):
	"AssignmentExpression  :  NUMBER SPACE Op SPACE ID "

	print(action[24])

def p_26(p):
	"AssignmentExpression  :  ID "

	print(action[25])

def p_27(p):
	"AssignmentExpression  :  ID SPACE Op SPACE ID "

	print(action[26])

def p_28(p):
	"Statement  :  PRINT Expression "

	print(action[27])

def p_29(p):
	"Statement  :  PRINT Expression  ':'   "

	print(action[28])

def p_30(p):
	"Statement  :  PRINT  '(' ID '(' Idnum ')'  ')'   "

	print(action[29])

def p_31(p):
	"Statement  :  PRINT  '(' ID '(' Idnum ',' Idnum ')'  ')' "

	print(action[30])

def p_32(p):
	"Loop  :  FOR SPACE ID SPACE IN SPACE RANGE   '('   Idnum  ','  Idnum  ')'   ':'  LoopBody"

	print(action[31])

def p_33(p):
	"Loop  :  FOR SPACE ID SPACE IN SPACE RANGE   '('   Idnum  ','  Idnum Op Idnum  ')'   ':'  LoopBody"

	print(action[32])

def p_34(p):
	"Loop  :  FOR SPACE ID SPACE IN SPACE RANGE   '('   Idnum  ','  Idnum Op Idnum  ')'  ')'   ':'  LoopBody"

	print(action[33])

def p_35(p):
	"Loop  :  FOR SPACE ID SPACE IN SPACE RANGE  '('  Idnum  ','  Idnum ')'  LoopBody "

	print(action[34])

def p_36(p):
	"Loop  :  FOR SPACE ID SPACE IN SPACE RANGE   '('   Idnum  ','  Idnum Op Idnum  ')'   LoopBody"

	print(action[35])

def p_37(p):
	"LoopBody  :  TAB AssignmentExpression "

	print(action[36])

def p_38(p):
	"LoopBodyc :  TAB Condition "

	print(action[37])

def p_39(p):
	"LoopBody  :  AssignmentExpression "

	print(action[38])

def p_40(p):
	"Condition  :  IF SPACE CondStmt  ':'  CondBody"

	print(action[39])

def p_41(p):
	"Condition  :  IF SPACE CondStmt "

	print(action[40])

def p_42(p):
	"Condition  :  ELIF SPACE CondStmt  ':'  CondBody"

	print(action[41])

def p_43(p):
	"Condition  :  ELIF SPACE CondStmt "

	print(action[42])

def p_44(p):
	"Condition  :  ELSE  ':'  CondBody"

	print(action[43])

def p_45(p):
	"Condition  :  ELSE "

	print(action[44])

def p_46(p):
	"Condition  :  IF  '('  '(' Idnum Op Idnum relOp Idnum ')'  logOp  '(' Idnum Op Idnum relOp Idnum ')'  ')'  ':'  CondBody "

	print(action[45])

def p_47(p):
	"CondStmt  :  ID SPACE relOp SPACE Idnum"

	print(action[46])

def p_48(p):
	"CondBody  :  TAB Statement"

	print(action[47])

def p_49(p):
	"CondBody  :  TAB RETURN Idnum"

	print(action[48])

def p_50(p):
	"CondBody  :  TAB Loop"

	print(action[49])

def p_51(p):
	"CondBody : TAB Assignment CondBody "

	print(action[50])

def p_52(p):
	"CondBody :  Assignment CondBody"

	print(action[51])

def p_53(p):
	"CondBody  :  Statement"

	print(action[52])

def p_54(p):
	"CondBody  :  RETURN SPACE Idnum"

	print(action[53])

def p_55(p):
	"CondBody  :  Loop"

	print(action[54])

def p_56(p):
	"CondBody :  "

	print(action[55])

def p_57(p):
	"Expression :   '(' Idnum ','  SPACE Idnum ')' "

	print(action[56])

def p_58(p):
	"Expression :   '(' Idnum ','  Expression ')' "

	print(action[57])

def p_59(p):
	"Expression :    '('  '(' Idnum ','  Expression ')'   "

	print(action[58])

def p_60(p):
	"Expression  :    '(' Idnum ','  Expression ')'  ')'   "

	print(action[59])

def p_61(p):
	"Expression :  "

	print(action[60])

def p_62(p):
	"Idnum :  ID"

	print(action[61])

def p_63(p):
	"Idnum : NUMBER"

	print(action[62])

def p_64(p):
	"relOp  :    '='  '='   "

	print(action[63])

def p_65(p):
	"relOp  :    '<'  '='   "

	print(action[64])

def p_66(p):
	"relOp  :  GREATERTHAN  '='   "

	print(action[65])

def p_67(p):
	"relOp  :    '<'  "

	print(action[66])

def p_68(p):
	"relOp  :  GREATERTHAN "

	print(action[67])

def p_69(p):
	"relOp  :    '!'  '='   "

	print(action[68])

def p_70(p):
	"Op  :    '+'  "

	print(action[69])

def p_71(p):
	"Op  :  MINUS "

	print(action[70])

def p_72(p):
	"Op  :    '*'   "

	print(action[71])

def p_73(p):
	"Op  :    '/'   "

	print(action[72])

def p_74(p):
	"Op  :   '%'  "

	print(action[73])

def p_75(p):
	"logOp  :  AND "

	print(action[74])

def p_76(p):
	"logOp  :  OR "

	print(action[75])

def p_77(p):
	"logOp  :  NOT "

def p_error(p):
    if p:
        #print("Syntax error at line",lineCount)
        #print(data)
        print(action[0])
    else:
        #print("Syntax error at line",lineCount)
        #print(data)
        print(action[0])
parser=yacc.yacc()
with open("userProgram.py",'r') as f1:
  for line in f1:
    data=str(line)
    result=parser.parse(data)
