
Example of packaging a python app as a .deb using dh-virtualenv
====================================================


Overview
--------

- [dh-virtualenv](http://dh-virtualenv.readthedocs.org/en/0.9/) is a very neat way of packaging python into debs with the key advantage that these apps are packaged as
a virtualenv so that the latest packages can be use without relying on the packages on the system... 
But these packages can also be used.
- The dh-virtualenv documentation mainly focuses on terminal scripts and I couldn't find a good example of packaging an app. 
- So I've included one here that adds a terminal command as well as a desktop shortcut and icon. 
- The example I've used is from a [previous blog post](http://blog.birving.com/2015/09/drag-and-drop-files-into-gui-using.html) 
on pyside dragging and dropping

Setup for ubuntu 14.04
-----------------------
- Install the python development packages

`bash
sudo apt-get install python-dev
`

- Create a [virtualenv](https://virtualenv.pypa.io/en/latest/) (so that the latest pip and setuptools  and activate
`bash
virtualenv virt-example
source ~/virt-example/bin/activate
`

- Install the latest dh-virtualenv from source as discussed in step 1 of the 
[dh-virtualenv instructions](http://dh-virtualenv.readthedocs.org/en/0.9/tutorial.html#step-1-install-dh-virtualenv)


Create an example debian package of the GUI
-------------------------------------------
In the folder containing the source

`bash
dpkg-buildpackage -us -uc -b
`

This should build a debian outside the folder

For a full discussion on the setup and files, see the corresponding [blog post](http://blog.birving.com).


Screenshots
-----------


Notes
------