from setuptools import setup

setup(
	name='gen_pkmn_name',
	version='0.1',
	packages=['gen_pkmn_name'],
	entry_points = {
        'console_scripts': ['gen_pkmn_name=gen_pkmn_name.command_line:main'],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://github.com/vardrop/gen-pkmn-name',
	author='vardrop',
	author_email='fesesoe@gmail.com'
)