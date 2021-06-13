from main.entities.User import User
from main.entities.Permission import Permission
from main.driver.Utils import *


class Driver:
    def __init__(self, user: User = None):
        self.user_map = {}
        self.permission = Permission()
        self.user = user
        self.create_admin()
        self.user_logged_in_functions = [
            ("Create a new user", Resource.USER, Action.WRITE, self.create_new_user),
            ("Delete an user", Resource.USER, Action.DELETE, self.delete_user),
            ("Get all users", Resource.USER, Action.READ, self.get_all_users),
            ("Add role for a user", Resource.USER, Action.WRITE, self.add_role_to_user),
            ("Remove role for a user", Resource.USER, Action.DELETE, self.remove_role_of_user),
            ("Add permission for a Role", Resource.PERMISSION, Action.WRITE, self.add_permission_to_role),
            ("Remove permission for a Role", Resource.PERMISSION, Action.DELETE, self.remove_permission_for_role),
            ("Logout", None, None, self.logout)
        ]
        self.user_logged_out_functions = [
            "Login",
            "Exit Application"
        ]

    def start_application(self):
        while True:
            if self.user is None:
                print("Enter one of the following commands")
                for i, j in enumerate(self.user_logged_out_functions):
                    print(f"{i + 1}. {j}")
                command = get_command(2)
                if command == 1:
                    self.login()
                elif command == 2:
                    break
            else:
                print(f"Welcome {self.user.user_name}")
                self.get_logged_in_functions()

    def get_logged_in_functions(self):
        while True:
            if self.user is None:
                break
            print("--------------\nEnter one of the following commands")
            available = []
            for i in self.user_logged_in_functions:
                if self.permission.check_permissions(self.user.roles, i[1], i[2]):
                    available.append(i)
            for i, j in enumerate(available):
                print(f"{i + 1}. {j[0]}")
            command = get_command(len(available))
            print("--------------")
            option = available[command - 1]
            option[3]()

    def create_admin(self):
        print("Doing initial preparation")
        user = User("admin", "admin", hashlib.sha256("admin".encode()).hexdigest())
        user.add_role(Role.ADMIN)
        self.user_map[user.user_id] = user
        self.permission.add_permission(Role.ADMIN, Resource.PERMISSION, Action.READ)
        self.permission.add_permission(Role.ADMIN, Resource.PERMISSION, Action.WRITE)
        self.permission.add_permission(Role.ADMIN, Resource.PERMISSION, Action.DELETE)
        self.permission.add_permission(Role.ADMIN, Resource.USER, Action.READ)
        self.permission.add_permission(Role.ADMIN, Resource.USER, Action.WRITE)
        self.permission.add_permission(Role.ADMIN, Resource.USER, Action.DELETE)

    def login(self):
        user_id = get_user_id()
        password = get_password()
        if user_id in self.user_map and self.user_map[user_id].password == password:
            self.user = self.user_map[user_id]
        else:
            print("Invalid User Id or Password")

    def logout(self):
        self.user = None

    def create_new_user(self):
        print("Enter new user details")
        user_id = get_user_id()
        user_name = input("User Name : ")
        password = get_password()
        if user_id in self.user_map:
            print("User id already exists try something different")
            return

        new_user = User(user_id, user_name, password)
        self.user_map[user_id] = new_user
        print(f"Successfully created user : {user_id}")

    def delete_user(self):
        print("Enter the user detail to delete the user")
        user_id = get_user_id()
        if user_id == self.user.user_id:
            print("Cannot delete the same user")
            return
        elif user_id not in self.user_map:
            print("User does not exists")
            return

        self.user_map.pop(user_id)
        print(f"Successfully deleted user : {user_id}")

    def get_all_users(self):
        print("Here is the complete list of users")
        for u in self.user_map.values():
            print(f"User Id : {u.user_id}, user name : {u.user_name}, roles : {[a.name for a in u.roles]}")

    def add_role_to_user(self):
        user_id = get_user_id()
        if user_id not in self.user_map:
            print("Enter valid user id")
            return
        user = self.user_map[user_id]
        available_roles = set([e for e in Role]) - user.roles
        print(f"User {user.user_id} has these roles {get_roles_string(user.roles)}, "
              f"available roles to add {get_roles_string(available_roles)}")
        role = get_role()
        if role is None:
            return
        elif role in user.roles:
            print("Error role already exists for the user")
            return
        user.roles.add(role)
        print(f"Successfully added role : {role.name} to user : {user.user_id}")

    def remove_role_of_user(self):
        user_id = get_user_id()
        if user_id not in self.user_map:
            print("Enter valid user id")
            return
        user = self.user_map[user_id]
        print(f"User {user.user_id} has these roles {get_roles_string(user.roles)}")
        role = get_role()
        if role is None:
            return
        elif role not in user.roles:
            print("Error user does not have this role")
            return
        user.roles.remove(role)
        print(f"Successfully removed role : {role.name} from user : {user.user_id}")

    def add_permission_to_role(self):
        print("Add permissions for a role")
        role = get_role()
        if role is None:
            return
        resource = get_resource()
        if resource is None:
            return
        action = get_action()
        if action is None:
            return
        self.permission.add_permission(role, resource, action)

    def remove_permission_for_role(self):
        print("Remove permissions for a role")
        role = get_role()
        if role is None:
            return
        resource = get_resource()
        if resource is None:
            return
        action = get_action()
        if action is None:
            return
        self.permission.remove_permission(role, resource, action)
