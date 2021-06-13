from main.entities import Role, Action, Resource


class Permission:

    def __init__(self):
        self.permission_map = {}

    def add_permission(self, role: Role, resource: Resource, action: Action) -> None:
        if role not in self.permission_map:
            self.permission_map[role] = {}

        resource_action_map = self.permission_map.get(role)

        if resource not in resource_action_map:
            resource_action_map[resource] = set()

        action_set = resource_action_map.get(resource)
        if action in action_set:
            print(f"The given action : {action} for resource {resource} in role {role} already exists")
        action_set.add(action)
        print(f"Added action : {action} for resource {resource} in role {role}")

    def remove_permission(self, role: Role, resource: Resource, action: Action) -> None:
        if role not in self.permission_map:
            print("No such permission exists")
            return

        resource_action_map = self.permission_map.get(role)

        if resource not in resource_action_map:
            print("No such permission exists")
            return

        action_set = resource_action_map.get(resource)
        if action not in action_set:
            print("No such permission exists")
            return
        action_set.remove(action)
        print(f"Removed action : {action} for resource {resource} in role {role}")

    def check_permission(self, role: Role, resource: Resource, action: Action) -> bool:
        if resource is None or action is None:
            return True

        if role not in self.permission_map:
            return False

        resource_action_map = self.permission_map.get(role)

        if resource not in resource_action_map:
            return False

        return action in resource_action_map.get(resource)

    def check_permissions(self, roles: set(), resource: Resource, action: Action) -> bool:
        if resource is None or action is None:
            return True

        for role in roles:
            if self.check_permission(role, resource, action):
                return True

        return False


