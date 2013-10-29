import parse, unittest

class TestParse(unittest.TestCase):
	def test_nominal(self):
		actual = parse.parse(['(', 'one', 'two', ')'])
		expected = ['(', 'one', 'two', ')']
		self.assertEqual(actual, expected)

	def test_nominal_tokenizer(self):
		actual = parse.parse(parse.tokenize("(one 'two)"))
		expected = ['(', 'one', "'", 'two', ')']
		self.assertEqual(actual, expected)

	# todo: support quoting without toplevel expression
	# todo: write 'print' function to output s-expression instead of AST 
	def test_nominal_tokenizer2(self):
		actual = parse.parse(parse.tokenize("('(one two))"))
		expected = ['(', "'", ['(', 'one', 'two', ')'], ')']
		self.assertEqual(actual, expected)

	def test_expr(self):
		actual = parse.parse(['(', '+', 1, 1, ')'])
		expected = ['(', '+', 1, 1, ')']
		self.assertEqual(actual, expected)

	def test_expr_eval(self):
		actual = parse._eval(parse.parse(['(', '+', 1, 1, ')']))
		expected = 2
		self.assertEqual(actual, expected)

	def test_nest_expr(self):
		actual = parse.parse(['(', '+', 1, '(', '+', 1, 1, ')', ')'])
		expected = ['(', '+', 1, ['(', '+', 1, 1, ')'], ')']
		self.assertEqual(actual, expected)

	def test_nest_expr_eval(self):
		actual = parse._eval(parse.parse(['(', '+', 1, '(', '+', 1, 1, ')', ')']))
		expected = 3
		self.assertEqual(actual, expected)

	def test_nest2_expr(self):
		actual = parse.parse(['(', '+', 1, '(', '+', 2, '(', '+', 3, 3, ')', ')', ')'])
		expected = ['(', '+', 1, ['(', '+', 2, ['(', '+', 3, 3, ')'], ')'], ')']
		self.assertEqual(actual, expected)

	def test_nest2_eval(self):
		actual = parse._eval(parse.parse(['(', '+', 1, '(', '+', 2, '(', '+', 3, 3, ')', ')', ')']))
		expected = 9
		self.assertEqual(actual, expected)

	def test_nest3_expr(self):
		actual = parse.parse(['(', '+', 1, '(', '+', 2, 2, ')', '(', '+', 3, 3, ')', ')'])
		expected = ['(', '+', 1, ['(', '+', 2, 2, ')'], ['(', '+', 3, 3, ')'], ')']
		self.assertEqual(actual, expected)

	def test_nest3_expr_eval(self):
		actual = parse._eval(parse.parse(['(', '+', 1, '(', '+', 2, 2, ')', '(', '+', 3, 3, ')', ')']))
		expected = 11
		self.assertEqual(actual, expected)

	def test_mul_expr_eval(self):
		actual = parse._eval(parse.parse(['(', '+', 1, '(', '+', 2, 2, ')', '(', '*', 3, 3, ')', ')']))
		expected = 14 
		self.assertEqual(actual, expected)

	def test_eval_json_expr(self):
		actual = parse._eval(parse.parse(['(', 'eval', 'json.loads', '"[1,2]"', ')']))
		expected = [1,2] 
		self.assertEqual(actual, expected)

	def test_eval_python_statement(self):
		actual = parse._eval(parse.parse(['(', 'exec', 'print', '"blah"', ')']))
		expected = None
		self.assertEqual(actual, expected)

	def test_mul_expr_eval(self):
		actual = parse._eval(parse.parse(parse.tokenize(
			'(+ 1(+ 2 2) (* 3 3 ) )'
		)))
		expected = 14 
		self.assertEqual(actual, expected)

	def test_def(self):
		parse._eval(parse.parse(parse.tokenize('(def foo "bar")')))
		actual = parse._eval(parse.parse(parse.tokenize('(foo)')))
		expected = 'bar'
		self.assertEqual(actual, expected)


class TestTokenize(unittest.TestCase):
	def test_nominal(self):
		tokens = []
		for token in parse.tokenize('one two'):
			tokens.append(token)
			
		actual1 = tokens[0] 
		actual2 = tokens[1] 

		self.assertEqual(actual1, 'one')
		self.assertEqual(actual2, 'two')
