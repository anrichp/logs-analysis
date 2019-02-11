# logs analysis 
Logs analysis is a tool written in **python** that prints our reports from a database outputted in plain text stored in a Query_Output.txt file.

## Installation

To run this project, you will need a UNIX based server environment. 
If you already have access to a server where the project can be deployed note the **dependencies** section below.

### Install Virtual Box

Install virtual box (https://www.virtualbox.org/wiki/Downloads)[here]. Ensure you download the correct version for your operating system.

### Install Vagrant

Vagrant will configure the previously installed Virtual Box and set up a shared directory between your host computer and the virtual machine.

Install vagrant (https://www.vagrantup.com/downloads.html)[here]. Ensure you download the correct version for your operating system.

### Download the Virtual Machine Configuration

Download the configuration files (https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)[here]. 

This file will now be stored in your downloads folder. Move this file to a directory that you would like to work from. 
UnZip the file and `cd` into the vagrant directory.

- start the machine using the `vagrant up` command. This will trigger the installation of the Virtual Machine and all dependencies required for this project. 

- Once the installation has completed you can access the virtual machine by typing the command `vagrant ssh`

## Dependencies

- postgresql
- python3, python3-pip
	- `pip3 install --upgrade pip`
	- `pip3 install flask packaging oauth2client redis passlib flask-httpauth`
	- `pip3 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests`
- Git	