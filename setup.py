from setuptools import setup

files = ['images/*']

setup(name = "warren",
    version = "0.2.1",
    description = "A dropzone application for Freenet",
    url="http://example.com",
    author = "Ratchet",
    author_email = "klaus@sentinel.dyndns.info",
    packages = ['warren','warren.ui','warren.core'],
    package_data = {'warren' : files },
    scripts = ["Warren"],
    install_requires = ['configobj>=4.7.2'],
) 
