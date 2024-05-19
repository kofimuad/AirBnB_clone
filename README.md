# 0x00. AirBnB clone - The console

## Content

* Description of the project
* Description of the command interpreter
* How to start and How to use it
* Examples

## Description of Project
This project is the first piece of the back-end in a series
of steps to building our my own Airbnb clone.
This step would be the back bone for the rest of the other
steps in building this web application, like the
front-end and the database.

In this project we would create a console to represent our
front-end and we would make use of python's cmd Module.

In this project we would perform the following tasks:
- Create a base class called (BaseModel) that would take care 
of initialization, serialization and deserialization of future classes.
- Do our serialization and deserailizatoin:
Data from instances <-> Dictionary <-> JSON string <-> file.
- Create other classes that would inherit from the BaseModel class.
- Create the storage engine File storage.
- Create all unittest test to test and validate
all our classes and storage engine.
<br/>

# Description of the command intepreter
* This interpreter is somewhat like the
* shell but has specific and limited use cases:
-   Create a new instance ( New user or New place ).
-   Get an instance from a file or data base.
-   Do operations on instances.
-   Update attributes of an instance.
-   Destroy an instance.

<br/>

## How to start and how to use it
* **Execution**
	- Your shell should work like this in interactive mode:

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project(simple shell) in C)

```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

All tests should also pass in non-interactive mode:
```sh
$ echo "python3 -m unittest discover tests" | bash
```
<br/>

## Examples

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
``````
