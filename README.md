# Role Based Access Control (RBAC) Application 

##Entities

### User
Parameters are user_id, user_name, password and roles.
Passwords are stored as sha256 hash. 
A default user admin is created with required permissions at start.

### Role
A role is to group users to provide a set of permissions.
 
### Resources
Resources are items which a user can take action on, i.e like databases, clusters, etc. 

### Action
Action is the type of activity that a user can perform on the resource, like read, write, etc.

### Permission
It keeps track of what role have access to which resource and allowed actions. 
It maps Role to map of Resource to Actions. 

## Execution 
### Utils 
Have some set of basic function that is required by the driver class

### Main 
This is the starting point of application. Run this to start the application.

### Driver
This class handles all the execution.  
The functions here are defined by what kind of Resource and Action is required to execute the function.
It also keeps track of all the users in a user map. 


## Miscellaneous 
Admin credentials
- username : `admin` 
- password : `admin`


