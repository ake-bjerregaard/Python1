try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': "Me me",
    'url': 'URL to get it at.',
    'download_url': 'where to do',
    'author_email': 'email',
    'version': '0.1',
    'install_requires':['nose2'], #nose2?
    'packages':['ex47'],
    'scripts': [],
    'name': 'projectiname'
}

setup(**config)