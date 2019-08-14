class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

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
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

print('Is sub_child_user in sub_child? {}'.format(is_user_in_group(sub_child_user, sub_child))) # return True

# test case 2

child.add_group(sub_child)
parent.add_group(child)
      
print('Is sub_child_user in child? {}'.format(is_user_in_group(sub_child_user, child))) # return True

# test case 3
print('Is sub_child_user in parent? {}'.format(is_user_in_group(sub_child_user, parent))) # return True