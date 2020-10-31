from setuptools import setup

setup(
    name='rknotdocs',
    version='0.1',
    description="My sample package",
    long_description="",
    author='rskene',
    author_email='covidcharts1@gmail.com',
    license='none',
    zip_safe=False,
    install_requires=[
        'docutils',
        'jinja2',
        'nbconvert==5.6.1',
        'traitlets',
        'nbformat',
        'sphinx>=1.8',
        'sphinx-rtd-theme',
        # 'nbsphinx',
        'ipython',
          ],
)