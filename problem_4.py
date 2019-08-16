class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
    
    def __repr__(self):
        return f'name: {self.name} groups: {self.groups} users: {self.users}'

    def add_group(self, group):
        self.groups.append(group)
        print(f'{self.name} has groups {self.groups}')

    def add_user(self, user):
        self.users.append(user)
        print(f'{self.name} has users {self.users}')

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    groups = group.get_groups()
    if user in users:
        return True
    else:
        for sub_group in groups:
            return is_user_in_group(user, sub_group)
    return False
    
    

# test case 1
print('Test case 1:')
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

print('\nAdd sub_child_user to sub_child.')
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

print('Is sub_child_user in sub_child? {}'.format(is_user_in_group(sub_child_user, sub_child))) 

# test case 2
print('\nTest case 2:')
print('\nAdd sub_child group to child.')
child.add_group(sub_child)
print('Is sub_child_user in child? {}'.format(is_user_in_group(sub_child_user, child))) 

# test case 3
print('\nTest case 3:')
print('\nAdd child group to parent.')
parent.add_group(child)
print('Is sub_child_user in parent? {}'.format(is_user_in_group(sub_child_user, parent)))