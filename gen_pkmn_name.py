from random import choice
from warnings import warn
import argparse

parser = argparse.ArgumentParser(description='Generate PKMN names.')
parser.add_argument('-n', '--number', type=int, default=1, help='a number of names to be printed')
parser.add_argument('-l', '--length', type=int, default=8, help='the length of the names to be printed')
parser.add_argument('-u', '--unique', type=int, default=3, help='max repitions of chars (higher, less unique)')
parser.add_argument('-v', '--verbose', action='store_true', help='repeats the input values in a nice way')
args = parser.parse_args()
defaults = {}
for key in vars(args):
	defaults[key] = parser.get_default(key)

vocals = ['a','e','i','o','u']
konson = ['b','c','d','f','g','h','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def main(number, length, unique):		
	names = []
	if number < 1:
		number = defaults.get('number')
	if length < 1:
		length = defaults.get('length')
	if unique < 1:
		unique = defaults.get('unique')
	if unique < length / 3:
		unique = length / 3
		warn('Uniquity to low for valid names. The uniquity was set to %i.' % unique)

	if args.verbose:
		print('~ Number: %i' % number)
		print('~ Length: %i' % length)
		print('~ Unique: %i' % unique)

	for x in range(1, number + 1):
		pkmn = ""
		for x in range(1, length + 1):
			kov = ""
			if x % 2 == 0:
				kov = konson
			else:
				kov = vocals
			char = choice(kov)
			if pkmn.count(char) >= unique:
				kov.remove(char)
			pkmn += choice(kov)
		names.append(pkmn)
	return names

def _gen_3_param(number, length, unique):
	return main(number, length, unique)

def _gen_0_param():
	name = main(0,0,0)
	for x in name:
		return x

def gen(*args):
	if len(args) == 3:
		return _gen_3_param(args[0], args[1], args[2])
	elif len(args) == 0:
		return _gen_0_param()
	else:
		raise TypeError("Method requires zero or three arguments")

if __name__ == "__main__":
    pkmn = gen(args.number, args.length, args.unique)
    for x in pkmn:
    	print(x)