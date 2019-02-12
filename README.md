
# logs analysis

Logs analysis is a tool written in **python** that prints our reports
from a database outputted in plain text stored in a Query_Output.txt file.

## Installation

To run this project, you will need a UNIX based server environment.
If you already have access to a server where the project can
be deployed note the **dependencies** section below.

### Install Virtual Box

Download virtual box [here](https://www.virtualbox.org/wiki/Downloads).
Ensure you download the correct version for your operating system.

### Install Vagrant

Vagrant will configure the previously installed Virtual Box and set up a shared directory
between your host computer and the virtual machine.

Download vagrant [here](https://www.vagrantup.com/downloads.html).
Ensure you download the correct version for your operating system.

### Download the Virtual Machine Configuration

Download the configuration files [here](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

This file might be stored in your downloads folder.
Move this file to a directory that you would like to work from.
UnZip the file and `cd` into the vagrant directory.

- Start the machine using the `vagrant up` command. The command will trigger the
installation of the Virtual Machine and all dependencies required for this project.

- Once the installation has completed, you can access
the virtual machine by typing the command `vagrant ssh`

## Dependencies

- PostgreSQL
- python3, python3-pip
  - `pip3 install --upgrade pip`
  - `pip3 install flask packaging oauth2client redis passlib flask-httpauth`
  - `pip3 install sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests`
- Git

### Required SQL Files

Download the required SQL file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

- UnZip the file in your `vagrant` directory.
- On your server navigate `cd` into the `/vagrant` directory
- Type `psql` to connect to the SQL server
- Load the SQL file into the SQL server using the command `psql -d news -f newsdata.sql`

To create the required views follow the steps below

- Copy the `create_views.sql` file into your working directory
- Run the `psql -d news -f create_views.sql` command
to create the views in the `news` database

## Usage

If you have got this far, well done!
We will now run the `logs_analysis.py` program on our server.

### Run the Program

```
python3 logs_analysis.py
```

### Required Database Views

**total_log:**

```
CREATE VIEW total_log AS
SELECT TO_CHAR(time,'FMMonth DD, YYYY') AS date, COUNT(*) as log_total
FROM log
GROUP BY date;
```

**error_log:**

```
CREATE VIEW error_log AS
SELECT TO_CHAR(time,'FMMonth DD, YYYY') AS date, COUNT(*) as error_total
FROM log
WHERE status not like '%200%'
GROUP BY date;
```

### Expected Output

**What are the most popular three articles of all time?**

"Candidate is jerk, alleges rival" -- 338647 views

"Bears love berries, alleges bear" -- 253801 views

"Bad things gone, say good people" -- 170098 views

**Who are the most popular article authors of all time?**

Ursula La Multa -- 507594 views

Rudolf von Treppenwitz -- 423457 views

Anonymous Contributor -- 170098 views

**On which days did more than '1%' of requests lead to errors?**

July 17, 2016 -- 2%
