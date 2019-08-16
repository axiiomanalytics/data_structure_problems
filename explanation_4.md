To find if a user is in a group, I need to iterate through sub-groups of a group and compare target user to each user in a group.

The time complexity of is_user_in_group(user, group) is O(m*n) in which m is the number of sub-groups and n is the number of users. The space complexity is O(n).

