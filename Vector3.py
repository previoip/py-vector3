from Point import Point

class Vector3(Point):

    def normalize(self):
        self.__truediv__(self.len)
        return self
