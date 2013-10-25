import parse, unittest

class TestParse(unittest.TestCase):
	def test_nominal(self):
		actual = parse.parse(['(', 'one', 'two', ')'])
		expected = [['(', 'one', 'two', ')']]
		self.assertEqual(actual, expected)

	def test_expr(self):
		actual = parse.parse(['(', '+', 1, 1, ')'])
		expected = [['(', '+', 1, 1, ')']]
		self.assertEqual(actual, expected)

	def test_nest_expr(self):
		actual = parse.parse(['(', '+', 1, '(', '+', 1, 1, ')', ')'])
		expected = [['(', '+', 1, ['(', '+', 1, 1, ')'], ')']]
		self.assertEqual(actual, expected)

	def test_nest2_expr(self):
		actual = parse.parse(['(', '+', 1, '(', '+', 2, '(', '+', 3, 3, ')', ')', ')'])
		expected = [['(', '+', 1, ['(', '+', 2, ['(', '+', 3, 3, ')'], ')'], ')']]
		self.assertEqual(actual, expected)

	def test_nest3_expr(self):
		actual = parse.parse(['(', '+', 1, '(', '+', 2, 2, ')', '(', '+', 3, 3, ')', ')'])
		expected = [['(', '+', 1, ['(', '+', 2, 2, ')'], ['(', '+', 3, 3, ')'], ')']]
		self.assertEqual(actual, expected)

	def test_eval_nest3_expr(self):
		actual = parse._eval(parse.parse(['(', '+', 1, '(', '+', 2, 2, ')', '(', '+', 3, 3, ')', ')'])[0])
		expected = 11
		self.assertEqual(actual, expected)

	def test_eval_json_expr(self):
		actual = parse._eval(parse.parse(['(', 'json.loads', '"[1,2]"', ')'])[0])
		expected = [1,2] 
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
