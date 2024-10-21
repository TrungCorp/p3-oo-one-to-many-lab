class Pet:
    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self,pet_type):
        if (pet_type not in Pet.PET_TYPES):
            raise Exception("error 1")
        self._pet_type = pet_type
        Pet.all.append(self)
    @property 
    def owner(self):
        return self._owner 
    @owner.setter
    def owner(self,owner):
        if(isinstance(owner,Owner)):
            self._owner = owner
            owner.pet_list.append(self)

class Owner:
    def __init__(self,name):
        self.name = name
        self.pet_list = []
        
    def pets(self):
        return self.pet_list
    def add_pet(self,pet):
        self.pet_list.append(pet)
        pet._owner = (self)
    def get_sorted_pets(self):
        obj_1 = sorted(self.pet_list, key=lambda pet: pet.name)
        return obj_1