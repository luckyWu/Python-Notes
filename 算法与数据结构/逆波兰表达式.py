RPN_str = '1 2 + 3 4 - *'
stack = []
for c in RPN_str.split():
  if c in '+-*':
    i2 = stack.pop()
    i1 = stack.pop()
    print (i1,c,i2)
    print (eval('%s'*3 % (i1,c,i2)))
    stack.append(eval('%s'*3 % (i1,c,i2)))
  else:
    stack.append(c)
print ('result', stack[0])