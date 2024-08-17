import os
from typing import Dict

os.system("clear")

def build_profile(first, last, **user_info) -> Dict:
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton', 
                             field='fizyka')
print(user_profile)
