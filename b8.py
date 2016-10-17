import xml.etree.ElementTree as ET



tree= ET.parse('parsing_table.xml')

root=tree.getroot()

term=[]

non_term=[]

lsprod=[]

rsprod=[]

n=0    #no of states



for child in root:

   if(child.tag=="states"):

      n=int(child.text)

   elif(child.tag=="term"):

      term.append(child.text)

   elif(child.tag=="nterm"):

      non_term.append(child.text)

   elif(child.tag=="productions"):

        for ch in child:

          lsprod.append(ch[0].text)

          rsprod.append(ch[1].text)

   elif(child.tag=="actiontable"):

      action=[[] for x in range(n)]

      i=0

      for ch in child:

         for c in ch:

           action[i].append(c.text)

         i=i+1

 

   elif(child.tag=="gototable"):

      goto=[[] for x in range(n)] 

      i=0

      for ch in child:

         for c in ch:

            goto[i].append(c.text)

         i=i+1





nterm=len(term)

nnterm=len(non_term)

nprod=len(lsprod)



print("Terminals:    "),;print(term)

print("Non Terminals:    "),;print(non_term)



print("Grammar Productions are as follows:   ")

for i in range(nprod):

   print(lsprod[i]+" -> "+rsprod[i])





print("\nAction Table:  ")

for i in range(n):

  print("")

  for j in range(nterm):

     print(action[i][j]+"   "),

print("")

print("Goto Table:    ")

for i in range(n):

  print(" ")

  for j in range(nnterm):

    print(str(goto[i][j])+"   "),



while True:

  #print("\nEnter input String:  "),

  istr=raw_input("\nEnter input String:  ")

  iptr=0
  #istr = 'abab'

  stack=['$',0]

  while True:

    print("Stack :"),

    print(stack)

    stop=stack[len(stack)-1]

    isym=istr[iptr]

    isindex=term.index(isym)

    ac=action[stop][isindex]

    print("Action for stop="+str(stop)+" and input symbol index   "+str(isindex)+" is "+action[stop][isindex])

    if(ac=="Error"):

       print("Syntax Error!!!")

       break

    elif(ac=="Accept"):

       print("Correct Syntax!!")

       break

    elif("s" in ac):

       stack.append(isym)

       ns=ac.replace("s","")

       stack.append(int(ns))

       iptr=iptr+1

    elif("r" in ac):

       rrule=int(ac.replace("r",""))

       print("Reduce using rule  "+lsprod[rrule-1]+"  ->  "+rsprod[rrule-1])

       for i in range(2*len(rsprod[rrule-1])):

           stack.pop()

       print(stack)

       stack.append(lsprod[rrule-1])

       pstate=stack[len(stack)-2]

       ntindex=non_term.index(lsprod[rrule-1])

       nst=goto[pstate][ntindex]

       stack.append(int(nst))

       print(stack)


# parsing_table.xml
# <parsetable>

#     <states>12</states>

#     <term>i</term>

#     <term>+</term>

#     <term>*</term>

#     <term>(</term>

#     <term>)</term>

#     <term>$</term>

#     <nterm>E</nterm>

#     <nterm>T</nterm>

#     <nterm>F</nterm>

#     <productions>

#          <prod><l>E</l><r>E+T</r></prod>

#          <prod><l>E</l><r>T</r></prod>

#          <prod><l>T</l><r>T*F</r></prod>

#          <prod><l>T</l><r>F</r></prod>

#          <prod><l>F</l><r>(E)</r></prod>

#          <prod><l>F</l><r>i</r></prod>

#     </productions>

#     <actiontable>

#         <tr><td>s5</td><td>Error</td><td>Error</td><td>s4</td><td>Error</td><td>Error</td></tr>

#         <tr><td>Error</td><td>s6</td><td>Error</td><td>Error</td><td>Error</td><td>Accept</td></tr>

#         <tr><td>r2</td><td>r2</td><td>s7</td><td>r2</td><td>r2</td><td>r2</td></tr>

#         <tr><td>r4</td><td>r4</td><td>r4</td><td>r4</td><td>r4</td><td>r4</td></tr>

#         <tr><td>s5</td><td>Error</td><td>Error</td><td>s4</td><td>Error</td><td>Error</td></tr>

#         <tr><td>r6</td><td>r6</td><td>r6</td><td>r6</td><td>r6</td><td>r6</td></tr>

#         <tr><td>s5</td><td>Error</td><td>Error</td><td>s4</td><td>Error</td><td>Error</td></tr>

#         <tr><td>s5</td><td>Error</td><td>Error</td><td>s4</td><td>Error</td><td>Error</td></tr>

#         <tr><td>Error</td><td>s6</td><td>Error</td><td>Error</td><td>s11</td><td>Error</td></tr>

#         <tr><td>r1</td><td>r1</td><td>s7</td><td>r1</td><td>r1</td><td>r1</td></tr>

#         <tr><td>r3</td><td>r3</td><td>r3</td><td>r3</td><td>r3</td><td>r3</td></tr>

#         <tr><td>r5</td><td>r5</td><td>r5</td><td>r5</td><td>r5</td><td>r5</td></tr>

#     </actiontable>

#     <gototable>

#         <tr><td>1</td><td>2</td><td>3</td></tr>

#         <tr><td>0</td><td>0</td><td>0</td></tr>

#         <tr><td>0</td><td>0</td><td>0</td></tr>

#         <tr><td>0</td><td>0</td><td>0</td></tr>

#         <tr><td>8</td><td>2</td><td>3</td></tr>

#         <tr><td>0</td><td>0</td><td>0</td></tr>

#         <tr><td>0</td><td>9</td><td>3</td></tr>

#        <tr><td>0</td><td>0</td><td>10</td></tr>

#        <tr><td>0</td><td>0</td><td>0</td></tr>

#        <tr><td>0</td><td>0</td><td>0</td></tr>

#        <tr><td>0</td><td>0</td><td>0</td></tr>

#        <tr><td>0</td><td>0</td><td>0</td></tr>

#     </gototable>

# </parsetable>


# kbw@kbw-Lenovo-G50-80:~/BE/Execution A  group$ python b8.py 
# Terminals:     ['i', '+', '*', '(', ')', '$']
# Non Terminals:     ['E', 'T', 'F']
# Grammar Productions are as follows:   
# E -> E+T
# E -> T
# T -> T*F
# T -> F
# F -> (E)
# F -> i

# Action Table:  

# s5    Error    Error    s4    Error    Error    
# Error    s6    Error    Error    Error    Accept    
# r2    r2    s7    r2    r2    r2    
# r4    r4    r4    r4    r4    r4    
# s5    Error    Error    s4    Error    Error    
# r6    r6    r6    r6    r6    r6    
# s5    Error    Error    s4    Error    Error    
# s5    Error    Error    s4    Error    Error    
# Error    s6    Error    Error    s11    Error    
# r1    r1    s7    r1    r1    r1    
# r3    r3    r3    r3    r3    r3    
# r5    r5    r5    r5    r5    r5    
# Goto Table:    
 
# 1    2    3     
# 0    0    0     
# 0    0    0     
# 0    0    0     
# 8    2    3     
# 0    0    0     
# 0    9    3     
# 0    0    10     
# 0    0    0     
# 0    0    0     
# 0    0    0     
# 0    0    0    
# Enter input String:  i*(i+i)$
# Stack : ['$', 0]
# Action for stop=0 and input symbol index   0 is s5
# Stack : ['$', 0, 'i', 5]
# Action for stop=5 and input symbol index   2 is r6
# Reduce using rule  F  ->  i
# ['$', 0]
# ['$', 0, 'F', 3]
# Stack : ['$', 0, 'F', 3]
# Action for stop=3 and input symbol index   2 is r4
# Reduce using rule  T  ->  F
# ['$', 0]
# ['$', 0, 'T', 2]
# Stack : ['$', 0, 'T', 2]
# Action for stop=2 and input symbol index   2 is s7
# Stack : ['$', 0, 'T', 2, '*', 7]
# Action for stop=7 and input symbol index   3 is s4
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4]
# Action for stop=4 and input symbol index   0 is s5
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'i', 5]
# Action for stop=5 and input symbol index   1 is r6
# Reduce using rule  F  ->  i
# ['$', 0, 'T', 2, '*', 7, '(', 4]
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'F', 3]
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'F', 3]
# Action for stop=3 and input symbol index   1 is r4
# Reduce using rule  T  ->  F
# ['$', 0, 'T', 2, '*', 7, '(', 4]
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'T', 2]
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'T', 2]
# Action for stop=2 and input symbol index   1 is r2
# Reduce using rule  E  ->  T
# ['$', 0, 'T', 2, '*', 7, '(', 4]
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8]
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8]
# Action for stop=8 and input symbol index   1 is s6
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6]
# Action for stop=6 and input symbol index   0 is s5
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6, 'i', 5]
# Action for stop=5 and input symbol index   4 is r6
# Reduce using rule  F  ->  i
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6]
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6, 'F', 3]
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6, 'F', 3]
# Action for stop=3 and input symbol index   4 is r4
# Reduce using rule  T  ->  F
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6]
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6, 'T', 9]
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, '+', 6, 'T', 9]
# Action for stop=9 and input symbol index   4 is r1
# Reduce using rule  E  ->  E+T
# ['$', 0, 'T', 2, '*', 7, '(', 4]
# ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8]
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8]
# Action for stop=8 and input symbol index   4 is s11
# Stack : ['$', 0, 'T', 2, '*', 7, '(', 4, 'E', 8, ')', 11]
# Action for stop=11 and input symbol index   5 is r5
# Reduce using rule  F  ->  (E)
# ['$', 0, 'T', 2, '*', 7]
# ['$', 0, 'T', 2, '*', 7, 'F', 10]
# Stack : ['$', 0, 'T', 2, '*', 7, 'F', 10]
# Action for stop=10 and input symbol index   5 is r3
# Reduce using rule  T  ->  T*F
# ['$', 0]
# ['$', 0, 'T', 2]
# Stack : ['$', 0, 'T', 2]
# Action for stop=2 and input symbol index   5 is r2
# Reduce using rule  E  ->  T
# ['$', 0]
# ['$', 0, 'E', 1]
# Stack : ['$', 0, 'E', 1]
# Action for stop=1 and input symbol index   5 is Accept
# Correct Syntax!!

# Enter input String: 