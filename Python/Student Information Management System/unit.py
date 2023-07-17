import random
import json
class Unit:
    def __init__(self,unit_id,unit_code,unit_name,unit_capacity):
        self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        return f"{self.unit_id},{self.unit_code},{self.unit_name},{self.unit_capacity}"
    
    def generate_user_id():
        return random.randint(1000000,9999999)

