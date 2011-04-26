from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ['images/*']

setup(name = "warren",
    version = "0.2",
    description = "A dropzone application for Freenet",
    url="http://example.com",
    author = "Ratchet",
    author_email = "yeah@sure.net",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['warren','warren.ui','warren.core'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'warren' : files },
    #'runner' is in the root.
    scripts = ["Warren"],
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
