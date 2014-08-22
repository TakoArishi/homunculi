from distutils.core import setup

setup(
    name='Homunculi',
    version='0.1.0',
    author='tako',
    author_email='gandrewnavas@gmail.com',
    packages=['homunc', 'homunc.test'],
    #scripts=[''],
    url='http://pypi.python.org/pypi/Homunculi/',
    license='LICENSE.txt',
    description='A Legend of the Wulin-related character sheet manager designed to interface with IRC bots.',
    long_description=open('README.md').read(),
    install_requires=[
        "flask == 0.10.1",
	"sqlalchemy == 0.9.7",
	"flask-sqlalchemy == 1.0",
    ],
)

