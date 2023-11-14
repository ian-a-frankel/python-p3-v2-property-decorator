APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self._name = name
        self._breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25:
            self._name = new_name
        else:
            raise ValueError("Name must be string between 1 and 25 characters." )
        
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        if new_breed in APPROVED_BREEDS:
            self._breed = new_breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")
