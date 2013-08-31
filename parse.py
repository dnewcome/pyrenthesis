def parse(tokens):
	parsetree = []
	stack = []
	for token in tokens:
		if token == '(':
			stack.append([])
			stack[len(stack)-1].append(token)
		elif token == ')':
			stack[len(stack)-1].append(token)
			parsetree.append(stack.pop())
		else:
			stack[len(stack)-1].append(token)

	return parsetree 

def tokenize(text):
	for token in text.split(' '):
		yield token
