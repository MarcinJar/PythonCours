import os 

os.system("clear")

def get_formatted_name(first_name: str, last_name: str, middle_name: str=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}" 
    else:
        full_name = f"{first_name} {last_name}"  

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)