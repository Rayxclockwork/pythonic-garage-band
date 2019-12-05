class Band:

    all = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        self.__class__.all.append(self)

    def __repr__(self):
        return f'The name of the band is {self.name}'

    @classmethod
    def create_from_data(cls, data):
        """Create a new band with members Musicians with given data.
        Data in a string in form
        Each line has 'name, instrument'
        First is band name, rest members


        Arguments:
            data{[type]} -- [description]
        """
        lines = data.split('\n')
        name_line = lines[0]
        line_parts = name_line.split('.')


class Musician:

    member_list = []

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        self.__class__.member_list.append(self)

    def __repr__(self):
        return self.name

    @classmethod
    def to_list(cls):
        return cls.member_list

    def get_instrument():
        return Musician.instrument

    def play_solo():
        return Musician.name


class Vocals:

    def __init__(self, name)
    super().__init__(name, 'vocalist')

    def play_solo(self):
        return 'vocal solo'


class Guitar:

    def __init__(self, name)
    super().__init__(name, 'guitarist')

    def play_solo(self):
        return 'guitar solo'


class Bass:

    def __init__(self, name)
    super().__init__(name, 'bassist')

    def play_solo(self):
        return 'bass solo'


class Drums:

    def __init__(self, name)
    super().__init__(name, 'drummer')

    def play_solo(self):
        return 'drum solo'
