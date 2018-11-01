# cloudStorage
Two servers developed as part of the PTIN (Internet Technologies Project) course that allows to receive JSON requests and execute operations with a MySQL database.

### Main Server
The main server of the project, that receives messages from a set of possible intelligent nodes of a fictitious city and registers them inside the database.

If it receives an invalid node identifier or a non-existent type, it will create all the necessary data and register this new node inside the database.

### Login Main Server
Secondary project server, which handles the login and registration system for the Android application of the fictional city.

## Executing
Each server can be executed using the following command. The server's **IP address** and **port** can be specified as optional parameters.

`python file.py [ipAddress] [port]`