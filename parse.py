# for convenience we can import some packages
# that become available to the repl
import json, re

# toplevel variable namespace
# todo: need concept of scope/envoronment
names = {} 

def last_item(stack):
	if stack:
		return stack[len(stack)-1]
	else:
		return None

def prev_item(stack):
	if stack and len(stack) >= 2:
		return stack[len(stack)-2]
	else:
		return None

def merge_item(stack):
	if len(stack) > 1:
		prev_item(stack).append(last_item(stack)) 
		stack.pop()

def parse(tokens):
	stack = []

	for token in tokens:
		if token == '(':
			item = []
			item.append(token)
			stack.append(item)
		elif token == ')':
			last_item(stack).append(token)
			merge_item(stack)
		else:
			last_item(stack).append(token)

	return stack[0]

def _eval(tree):
	if type(tree) == list:
		if tree[1] == '+':
			sum = 0
			for arg in tree[2:len(tree)-1]:
				sum += _eval(arg)
			return sum
			
		elif tree[1] == '*':
			prod = 1
			for arg in tree[2:len(tree)-1]:
				prod *= _eval(arg)	
			return prod 

		elif tree[1] == 'def':
			names[tree[2]] = tree[3]

		elif tree[1] == 'names':
			print names

		elif tree[1] == "'":
			# don't evaluate quoted expressions
			return tree[2];

		## use eval to execute python _expression_
		elif tree[1] == 'eval':
			return eval( tree[2] + '(' + ','.join(tree[3:len(tree)-1]) + ')' )

		## use eval to execute python _statement_ 
		elif tree[1] == 'exec':
			exec( tree[2] + '(' + ','.join(tree[3:len(tree)-1]) + ')' )

		## use eval to lisp function 
		elif tree[1] == 'call':
			expr = names[tree[2]]
			args = expr[1]
			body = expr[2]
			for i in range(1, len(args)-1):
				print('adding arg name:{0}', args[i])
				print('adding arg val:{0}', tree[2+i])
				names[args[i]] = tree[2+i]

			return _eval(body)

		else:
			print('looking up {0}',tree[1])
			return _eval(names[tree[1]])

	elif type(tree) == int or (hasattr(tree, 'isdigit') and tree.isdigit()):
		return int(tree)
	
	else:
		if tree in names:
			return _eval(names[tree])
		else:
			return tree

def tokenize(text):
	#for token in text.split(' '):
	for token in re.findall( r"\(|\)|[\w\.]+|\+|\*|'", text ):
		yield token

if __name__ == '__main__':
	while True:
		s = raw_input('(repl): ')
		print _eval(parse(tokenize(s)))

