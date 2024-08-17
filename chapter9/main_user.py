import os

from user import User, Admin

os.system("clear")

marcin = User(first_name='marcin', last_name='Jarmułowski', age=32)
anna = User(first_name='anna', last_name='kowlaska', age=39)
jan = User(first_name='jan', last_name='nowak', age=57)

marcin.increment_login_attempts()
marcin.describe()
marcin.increment_login_attempts()
marcin.greet()
marcin.increment_login_attempts()
marcin.show_number_login_attepmpts()
marcin.reset_login_attepmpts()
marcin.show_number_login_attepmpts()
print("\n")

anna.increment_login_attempts()
anna.describe()
anna.greet()
anna.show_number_login_attepmpts()
anna.reset_login_attepmpts()
anna.show_number_login_attepmpts()
print("\n")

jan.increment_login_attempts()
jan.describe()
jan.greet()
jan.increment_login_attempts()
jan.increment_login_attempts()
jan.increment_login_attempts()
jan.increment_login_attempts()
jan.show_number_login_attepmpts()
jan.reset_login_attepmpts()
jan.show_number_login_attepmpts()
print("\n")

admin = Admin("Tomasz", "Nowak", 45, ["add user", "remove user", "show all users", "read content"])
admin.increment_login_attempts()
admin.describe()
admin.greet()
admin.show_number_login_attepmpts()
admin.privliges.show_privliges()
admin.reset_login_attepmpts()
admin.show_number_login_attepmpts()