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

	return stack 

def eval(tree):
	print 'eval'
	print tree
	if type(tree) == list:
		if tree[1] == '+':
			print 'adding'
			sum = 0
			for arg in tree[2:len(tree)-1]:
				sum += eval(arg)	
			return sum

	elif type(tree) == int:
		return tree

def tokenize(text):
	for token in text.split(' '):
		yield token

