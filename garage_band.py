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

    def get_instrument
        return self.instrument

    def play_solo
        return self.name
