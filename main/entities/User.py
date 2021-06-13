from main.entities.Role import Role


class User:

    def __init__(self, user_id: str, user_name: str, password: str):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.roles = set()

    def add_role(self, role: Role):

        if role in self.roles:
            raise Exception(f"User: {self.user_id} already have this role:{role}")
        self.roles.add(role)

    def remove_role(self, role: Role):
        if role in self.roles:
            self.roles.remove(role)
        else:
            raise Exception(f"User: {self.user_id} does not have this role:{role}")
