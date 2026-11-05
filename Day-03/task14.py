# Creating permission sets
admin = {"read", "write", "delete", "update", "manage_users"}

editor = {"read", "write", "update"}

# Editor user permissions
user_permissions = editor

# Action requiring admin permission
required_permission = "delete"

# Checking permission
if required_permission in user_permissions:
    print("Access Granted")
else:
    print("Access Denied")

print("User Permissions:", user_permissions)
print("Required Permission:", required_permission)