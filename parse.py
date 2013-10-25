# for convenience we can import some packages
# that become available to the repl
import json

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
		else:
			print 'evaluating'
			"""
			prod = eval(
				compile(
					tree[1] + '(' + ','.join(tree[2:len(tree)-1]) + ')',
					'', 
					'exec'))
			"""
			print tree[1] + '(' + ','.join(tree[2:len(tree)-1]) + ')'
			return eval( tree[1] + '(' + ','.join(tree[2:len(tree)-1]) + ')' )
			#exec( tree[1] + '(' + ','.join(tree[2:len(tree)-1]) + ')' )

	elif type(tree) == int or (hasattr(tree, 'isdigit') and tree.isdigit()):
		return int(tree)
	
	else:
		print 'type is ' + str(type(tree))
		return tree

def tokenize(text):
	for token in text.split(' '):
		yield token

if __name__ == '__main__':
	while True:
		s = raw_input('(repl): ')
		print _eval(parse(tokenize(s))[0])

