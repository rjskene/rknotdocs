from setuptools import setup

setup(
    name='rknotdocs',
    version='0.1',
    description="My sample package",
    long_description="",
    author='TODO',
    author_email='todo@example.org',
    license='TODO',
    zip_safe=False,
    install_requires=[
        'docutils',
        'jinja2',
        'nbconvert!=5.4',
        'traitlets',
        'nbformat',
        'sphinx>=1.8',
        'sphinx-rtd-theme',
          ],
)