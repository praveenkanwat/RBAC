from main.entities.Resource import Resource
from main.entities.Action import Action
from main.entities.Role import Role
from getpass import getpass
import hashlib


def get_user_id():
    return input("User Id : ")


def get_user_name():
    return input("User Name : ")


def get_password():
    return hashlib.sha256(getpass().encode()).hexdigest()


def get_role():
    role = input("Enter the role : ")
    if role in Role.__members__:
        return Role[role]
    else:
        print("ERROR: enter valid role")
        return None


def get_roles_string(roles):
    return [e.name for e in roles]


def get_resource():
    resource = input("Enter the resource : ")
    if resource in Resource.__members__:
        return Resource[resource]
    else:
        print("ERROR: enter valid resource")
        return None


def get_action():
    action = input("Enter the action : ")
    if action in Action.__members__:
        return Action[action]
    else:
        print("ERROR: enter valid action")
        return None


def get_command(n):
    try:
        command = int(input("-> "))
        if 0 < command <= n:
            return command
        else:
            print("Enter a valid command")
            return
    except:
        print("Enter a valid command")
        return

