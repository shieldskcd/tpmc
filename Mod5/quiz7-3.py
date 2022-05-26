## Wrong
#def check_username(username)
#    if len(username) > 4:
#        return "Successful!"
#    else:
#        return "Try another user name"

# Also wrong
#def check_username(username):
#    if len(username) > 4
#        return "Successful!"
#    else:
#        return "Try another username"

# Correct
def check_username(username):
    if len(username) > 4:
        return "Successful!"
    else:
        return "Try another user name"