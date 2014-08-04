#Transcode Pre-class Setup
Here are some instructions to install software that you will need to go through the [Transcode classwork](https://github.com/TranscodeSF/classwork) which you can download or clone the to your computer.  If you have difficulty with any of these steps, you can get help from a Transcode TA.


##For Everyone
Download or clone the [Transcode classwork](https://github.com/TranscodeSF/classwork)
on GitHub to your computer.


##For folks with Windows laptops
All of the following instructions were tried on Windows XP, but should apply equally to Windows Vista and Windows 7.


###Install Python 2.7:
Install Python 2.7.3 from this [link](http://www.python.org/ftp/python/2.7.3/python-2.7.3).msi

We recommend just picking all the default options and installing everything that it comes with.


###Install a PDF reader:
Some of the things you will read for Transcode will be in PDF format.  If you can click on this [link](http://www.greenteapress.com/thinkpython/thinkCSpy/thinkCSpy.pdf) and read the document then you are good to go: 

If you don’t have a PDF reader, you should do one of the following:

Option 1: Install [Chrome](https://www.google.com/chrome)
Option 2: Install [Adobe Acrobat](http://get.adobe.com/reader/)

After you have done one of those things, make sure you can click on the above link and see the document.


##For folks with Mac / OSX laptops

OSX can be a great development environment, but it requires a bit of setup to get running like a programmer.  Make sure you’re logged in to an administrator account on your computer, then do the following:


###Install the developer tools:
Apple provides the development tools for OSX free of charge at the [apple developer center](https://developer.apple.com/devcenter/mac/index.action).  You will need to first [make an account](https://developer.apple.com/programs/register/) which is free and then download and run the installers for:
* The latest version of XCode.  You may end up wanting to use the App Store to download this, in Lion or Mountain Lion if you happen to have those.
* In Lion or Mountain Lion, you will also need to separately download and install a package called Command Line Tools (choose the one appropriate to your OS).  In previous OSX, this is included with the XCode download.
Next, briefly launch XCode so you can accept the license.  Once you’ve done that, you can quit it.


###Install MacPorts:
MacPorts is a “package manager” for OSX -- it has pointers to a lot of useful programs, and knows how to fetch and install them when you ask it to, and manage the dependencies between them.  It’s generally useful to have around, and we’ll be using it later to install some other programs.

Go to this [link](http://www.macports.org/install.php), and find the “pkg installer” for your version of OSX.  Run it.  Once it finishes you should be set.  


###Install Python 2.7:
Finally, the Python that tends to come with OSX is a little old.  Go to [python.org](http://www.python.org/download/releases/2.7.3/) and click to download the installer for your version of OSX, then run it.  
At your terminal, run the command:
`python` 

You can type your Python code in here. Press control-D to get out of it.
