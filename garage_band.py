import re


class Musician:
    pass

    member_list = []

    def __init__(self, name, band_name, instrument):
        """creates a musician instance using subclass
        based on instrument belo"""
        self.name = name
        self.band = band_name
        self.instrument = instrument
        Musician.member_list.append([name, band_name, instrument])

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'I am a {self.instrument} named {self.name}'

    @classmethod
    def to_list(cls):
        """returns list of members from each band"""
        return cls.member_list

    def get_instrument():
        """returns instrument based on musician instance"""
        return Musician.instrument

    def play_solo():
        """calls on each musician to play a solo"""
        return f"{Musician.name} is playing/singing a solo!"


class Band(Musician):
    pass

    all = []

    def __init__(self, name, musicians=[]):
        """"creates a band instance using the subclasses below"""
        self.name = name
        self.members = musicians
        self.__class__.all.append(self)

    def __repr__(self):
        """returns the name of the band"""
        return f'The name of the band is {self.name}'

    @classmethod
    def create_from_data(data):
        split = re.findall(r"\S.*", data)
        print(split)

        title = split[0]
        members = []
        for i in range(1, len(split)):
            current = split[i].split(',')

            if current[1] == 'Vocalist':
                members.append(Vocalist(current[0]))
            if current[1] == 'Guitarist':
                members.append(Guitarist(current[0]))
            if current[1] == 'Bassist':
                members.append(Bassist(current[0]))
            if current[1] == 'Drummer':
                members.append(Drummer(current[0]))
            else:
                members.append(Musician(current[0]))

        return Band(title, members)


class Vocalist(Musician):
    pass

    def __repr__(self):
        return self.name

    def __str__(self):
        return 'I am a vocalist named' + {self.name}
    # def play_solo(self):
    #     return 'vocal solo'


class Guitarist(Musician):
    pass

    # def __init__(self, name)
    # super().__init__(name, 'guitarist')

    # def play_solo(self):
    #     return 'guitar solo'


class Bassist(Musician):
    pass

    # def __init__(self, name)
    # super().__init__(name, 'bassist')

    # def play_solo(self):
    #     return 'bass solo'


class Drummer(Musician):
    pass

    # def __init__(self, name)
    # super().__init__(name, 'drummer')

    # def play_solo(self):
    #     return 'drum solo'


if __name__ == "__main__":

    band_test = """
    Jinjer
    Tati,Vocalist
    Vlad,Drummer
    Eugene,Bassist
    Roman,Guitarist
    """
    print(band_test)
