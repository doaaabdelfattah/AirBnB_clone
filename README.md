

![Screenshot 2024-01-15 020847](https://github.com/nadashaban10/AirBnB_clone/assets/122872974/ee4cfe5c-8c4f-4fd1-8c94-129a17fc715c)


--------------------------------------------

# Describtion the AIRBNB clone project
---------------------------------------------
The Airbnb Clone project aims to replicate the core features of the Airbnb platform,
providing users with a platform to list their properties for short-term rentals
and enabling other users to discover and book accommodations for their travel needs.
---------------------------------------------
# Description of the command interpreter
The Airbnb Command Interpreter is a text-based interface designed to interact
with the Airbnb Clone project. Users can perform various actions,
such as searching for accommodations, making bookings, managing listings, and more
all through a series of command-line inputs.
----------------------------------------------
# How to use Console?

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```


# files and directories using >>>

1-models directory: will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
2-tests directory: will contain all unit tests.
3-console.py: file is the entry point of our command interpreter.
4-models/base_model.py: file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
5-models/engine: directory will contain all storage classes (using the same prototype). For the moment I will have only one: file_storage.py . ---
