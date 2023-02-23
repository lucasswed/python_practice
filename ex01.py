# Codewars exercise
# Name: Find the unknown digit <4kyu>
# Instructions:
# To give credit where credit is due:
# This problem was taken from the ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.
# You are helping an archaeologist decipher some runes.
# He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero.
# He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.
# The professor will give you a simple math expression, of the form [number][op][number]=[number]
# He has converted all of the runes he knows into digits.
# The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear.
# Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
# If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -).
# All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression.
# No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.
# Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one.
# If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.
# Complete the method to solve the expression to find the value of the unknown rune.
# The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.


# [number1][op][number2]=[number3]
# lhs = number1
# rhs = number2
# op = op
# result = number3


# verificar se ta no range, verificar 

# def fill_dict(expression, runes):
# 	flag = 0
# 	for c in runes:
# 		if c in "+-*" and flag == 0:
# 			expression["op"] += c
# 			flag = 2
# 		elif c == "=":
# 			flag = 3
# 		elif flag == 0:
# 			expression["lhs"] += c
# 		elif flag == 2:
#			 expression["rhs"] += c
# 		elif flag == 3:
# 			expression["result"] += c


def fill_dict(expression, runes):
	i = 0
	found_op = 0
	flag = 0
	
	while i < len(runes):
		if i == 0 and runes[i] == "-":
			expression["lhs"] += runes[i]
		elif runes[i] in "+-*" and found_op == 0:
			expression["op"] += runes[i]
			found_op = 1
			flag = 2
		elif runes[i] == "=":
			flag = 3
		elif flag == 0:
			expression["lhs"] += runes[i]
		elif flag == 2:
			expression["rhs"] += runes[i]
		elif flag == 3:
			expression["result"] += runes[i]
		i += 1


def substitute(string, to_sub, to_insert):
	to_return = ""
	for c in string:
		if c == to_sub:
			to_return += to_insert
		else:
			to_return += c
	return int(to_return)


def calculate(lhs, op, rhs):
	if op == '+':
		return lhs + rhs
	elif op == '-':
		return lhs - rhs
	elif op == '*':
		return lhs * rhs
	else:
		return "error"


def is_zero_left(expression):
	i = 0
	is_valid_lhs = 1
	is_valid_rhs = 1
	is_valid_ = 1
# -????? = False
# -4? = True
# ?  = True
# 1? = True
# ?1 = False
	if expression["lhs"][0] == '-':
			i += 1
	while i < len(expression["lhs"]):
		if (expression["rhs"][i - 1].isnum() or len(expression["rhs"]) == 1) and expression["lhs"][i] == '?':
			is_valid_lhs = 1
		elif expression["lhs"][i] == '?' and expression["lhs"][i + 1] != '?':
			is_valid_lhs = 0
			break
		i += 1
	i = 0
	if expression["rhs"][0] == '-':
		i += 1
	while i < len(expression["rhs"]):
		if expression["rhs"][i - 1].isnum() and expression["rhs"][i] == '?':
			is_valid_rhs = 1
		elif expression["rhs"][i] == '?' and expression["rhs"][i + 1] != '?':
			is_valid_rhs = 0
			break
		i += 1
	i = 0
	if expression["result"][0] == '-':
		i += 1
	while i < len(expression["result"]):
		if expression["result"][i] == '?':
			is_valid_result = 1
		elif expression["result"][i] == '?' and expression["result"][i + 1] != '?':
			is_valid_result = 0
			break
		i += 1
	if is_valid_lhs == 0 or is_valid_result == 0 or is_valid_rhs == 0:
		return True
	else:
		return False


def verifier(runes, i):
	if i in runes:
		return True
	else:
		return False


def solve_runes(runes):
	expression = {"lhs": "", "rhs": "", "op": "", "result": ""}
	fill_dict(expression, runes)
	i = 0
	#if (expression["lhs"][0] == '?') or (expression["rhs"][0] == '?') or (expression["result"][0] == '?'):
	#	i += 1
	if is_zero_left(expression) == False:
		i += 1
	while i <= 9:
		if verifier(runes, str(i)):
			i += 1
			continue
		new_lhs = substitute(expression["lhs"], '?', str(i))
		new_rhs = substitute(expression["rhs"], '?', str(i))
		new_result = substitute(expression["result"], '?', str(i))
		final = calculate(new_lhs, expression["op"], new_rhs)
		if final == "error":
			return -1
		if (final == new_result):
			if (new_lhs and new_rhs and new_result) in range(-1000000, 1000001):
				return i
		i += 1
	return -1


if __name__ == "__main__":
 	print(solve_runes("-6561+-?1772=-?8333"))
# if (new_lhs in range(-1000000, 1000001)) and (new_rhs in range(-1000000, 1000001)) and (new_result in range(-1000000, 1000001)):

# def is_zero_left(expression):
# 	i = 0
# 	is_valid_lhs = 1
# 	is_valid_rhs = 1
# 	is_valid_ = 1

	# while expression["lhs"][i]:
	# 	if expression["lhs"][i] == '-':
	# 		i += 1
# 		elif expression["lhs"][i] == '?':
# 			is_valid_lhs = 1
# 		elif expression["lhs"][i] != '?' and i > 1:
# 			is_valid_lhs = 0
# 			break
# 		i += 1
# 	i = 0
# 	while expression["rhs"][i]:
	# 	if expression["rhs"][i] == '-':
	# 		i += 1
# 		if expression["rhs"][i] == '?':
# 			is_valid_rhs = 1
# 		elif expression["rhs"][i] != '?' and i > 1:
# 			is_valid_rhs = 0
# 			break
# 		i += 1
# 	i = 0
# 	while expression["result"][i]:
	# 	if expression["result"][i] == '-':
	# 		i += 1
# 		if expression["result"][i] == '?':
# 			is_valid_result = 1
# 		elif expression["result"][i] != '?' and i > 1:
# 			is_valid_result = 0
# 			break
# 		i += 1
# 	if is_valid_lhs == 0 and is_valid_result == 0 and is_valid_rhs == 0:
# 		return True
# 	else:
# 		return False
# "-5?*-1=5?"