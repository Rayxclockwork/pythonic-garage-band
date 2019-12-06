class Band:
    pass

    all = []

    def __init__(self, name, musicians=[]):
        """"creates a band instance using the subclasses below"""
        self.band_name = name
        self.members = musicians
        self.__class__.all.append(self)

    def __repr__(self):
        """returns the name of the band"""
        return f'The name of the band is {self.name}'

    # @classmethod
    # def create_from_data(cls, data):


class Musician:
    pass

    member_list = []

    def __init__(self, name):
        """creates a musician instance using subclass
        based on instrument belo"""
        self.name = name
        # self.__class__.member_list.append(self)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'I am a {self.__class__.__name__} named {self.name}'

    @classmethod
    def to_list(cls):
        """returns list of members from each band"""
        return cls.member_list

    def get_instrument():
        """returns instrument based on musician instance"""
        return Musician.instrument

    def play_solo():
        """calls on each musician to play a solo"""
        return Musician.name


class Vocals(Musician):
    pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return 'I am a vocalist named' + {self.name}
    # def play_solo(self):
    #     return 'vocal solo'


class Guitar(Musician):
    pass

    # def __init__(self, name)
    # super().__init__(name, 'guitarist')

    # def play_solo(self):
    #     return 'guitar solo'


class Bass(Musician):
    pass

    # def __init__(self, name)
    # super().__init__(name, 'bassist')

    # def play_solo(self):
    #     return 'bass solo'


class Drums(Musician):
    pass

    # def __init__(self, name)
    # super().__init__(name, 'drummer')

    # def play_solo(self):
    #     return 'drum solo'


jinjer = Band('Jinjer', [tati, roman, eugene, vlad])
print(jinjer.members)
tati = Vocals('Tati')
roman = Guitar('Roman')
eugene = Bass('Eugene')
vlad = Drums('Vlad')
