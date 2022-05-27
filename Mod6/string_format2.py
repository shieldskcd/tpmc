name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
when = "today"

message = "Hello %s %s!" % (name, last_name)
message = f"Hello {name} {last_name}. What's up {when}?"
print(message)