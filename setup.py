from setuptools import setup

filename = "poet/version.py"
exec(compile(open(filename, "rb").read(), filename, 'exec'))

setup(
    name='homebrew-pypi-poet',
    version=__version__,
    url='https://github.com/tdsmith/homebrew-pypi-poet',
    license='MIT',
    author='Tim D. Smith',
    author_email='poet@tim-smith.us',
    description='Writes Homebrew stanzas for pypi packages',
    packages=['poet'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.4'
    ],
    install_requires = ['jinja2', 'networkx', 'pip', 'tl.eggdeps'],
    entry_points = {'console_scripts': ['poet=poet:main']}
)
