# coding : utf-8


class ImageFile:
    def __init__(self, name, ordination, size):
        self.name = name
        self.ordination = ordination
        self.size = size

    def get_name(cls):
        return cls.name

    def set_name(self, name):
        self.name = name

    def get_ordination(cls):
        return cls.ordination

    def set_ordination(self, ordination):
        self.ordination = ordination

    def get_size(cls):
        return cls.size

    def set_size(self, size):
        self.size = size

