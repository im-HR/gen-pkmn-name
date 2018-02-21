# Generate all the PKMN

This is a fun and easy to use script to generate small pronouncable usernames which are easy to remember.

## What is a PKMN?

```
λ py gen_pkmn_name.py
imotaliv
```
So basically a PKMN is a word created from vocals and konsonants in turn starting with a vocal.

## Usage

### Cli

```
λ py gen_pkmn_name.py -h
usage: gen_pkmn_name.py [-h] [-n NUMBER] [-l LENGTH] [-u UNIQUE] [-v]

Generate PKMN names.

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        a number of names to be printed
  -l LENGTH, --length LENGTH
                        the length of the names to be printed
  -u UNIQUE, --unique UNIQUE
                        max repitions of chars (higher, less unique)
  -v, --verbose         repeats the input values in a nice way
```

### Module

```python
import gen_pkmn_name as pkmn

print(pkmn.gen())

```

## API

### gen()

Input: 0 Params

Output: String (i.e. ```eleyunow```)

Takes zero parmeters and returns a PKMN with the following specs:
* 1 PKMN
* 8 characters
* Uniquity of 3

### gen(number, length, unique)

Input: 3 integer (i.e. ```gen(3, 8, 5)```)

Output: Array of strings (i.e. ```['afigesev', 'oyuroqeg', 'oqovaluc']```)

Takes three integer parameter and creates the PKMN with these specs.
