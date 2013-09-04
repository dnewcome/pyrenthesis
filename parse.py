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
	if type(tree) == list:
		if tree[1] == '+':
			sum = 0
			for arg in tree[2:len(tree)-1]:
				sum += eval(arg)	
			return sum

	elif type(tree) == int or tree.isdigit():
		return int(tree)

def tokenize(text):
	for token in text.split(' '):
		yield token

if __name__ == '__main__':
	while True:
		s = raw_input('(): ')
		print eval(parse(tokenize(s))[0])

