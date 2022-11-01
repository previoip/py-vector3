import traceback
from dataclasses import dataclass
from math import sqrt, isclose


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __post_init__(self):

        if isinstance(self.__dict__.get('x'), self.__class__):
            o = self.__dict__.get('x')
            self.__init__(o.x, o.y, o.z)
            return

        elif isinstance(self.__dict__.get('x'), (list, tuple)):
            o = self.__dict__.get('x')
            o = [o[i] if i<len(o) else 0 for i in range(3)]
            self.__init__(o[0], o[1], o[2])
            return

        elif isinstance(self.__dict__.get('x'), dict):
            o = self.__dict__.get('x')
            self.__init__(o.get('x', 0.0), o.get('y', 0.0), o.get('z', 0.0))
            return

        for name, field_type in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                try:
                    self.__dict__[name] = field_type(self.__dict__[name])
                except ValueError:
                    traceback.print_exc()
                    exit(1)

    def set(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        self.__post_init__()

    def to_list(self) -> list:
        return [self.x, self.y, self.z]

    def to_dict(self) -> dict:
        return {'x': self.x, 'y': self.y, 'z': self.z}

    @property
    def ls(self) -> list:
        return self.to_list()

    @property
    def len(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, o):
        if isinstance(o, self.__class__):
            return all([
                isclose(self.x, o.x),
                isclose(self.y, o.y),
                isclose(self.z, o.z)
            ])
        else:
            return False

    def __add__(self, o):
        if isinstance(o, self.__class__):
            self.x += o.x
            self.y += o.y
            self.z += o.z
        elif isinstance(o, (int, float)):
            self.x += o
            self.y += o
            self.z += o
        else:
            raise TypeError(f'unsupported ` + ` operand for \'Vector3\' and \'{type(o).__name__}\'')
        return self

    def __sub__(self, o):
        if isinstance(o, self.__class__):
            self.x -= o.x
            self.y -= o.y
            self.z -= o.z
        elif isinstance(o, (int, float)):
            self.x -= o
            self.y -= o
            self.z -= o
        else:
            raise TypeError(f'unsupported ` - ` operand for \'Vector3\' and \'{type(o).__name__}\'')
        return self

    def __mul__(self, o):
        if isinstance(o, self.__class__):
            return self.x * o.x + self.y * o.y + self.z * o.z
        elif isinstance(o, (int, float)):
            self.x *= o
            self.y *= o
            self.z *= o
        else:
            raise TypeError(f'unsupported ` * ` operand for \'Vector3\' and \'{type(o).__name__}\'')
        return self

    def __matmul__(self, o):
        if isinstance(o, self.__class__):
            self.x = (self.y * o.z) - (self.z * o.y)
            self.y = (self.z * o.x) - (self.x * o.z)
            self.z = (self.x * o.y) - (self.y * o.x)
            return self
        else:
            raise TypeError(f'unsupported ` @ ` operand for \'Vector3\' and \'{type(o).__name__}\'')

    def __truediv__(self, o):
        if isinstance(o, (int, float)):
            self.x /= o
            self.y /= o
            self.z /= o
        else:
            raise TypeError(f'unsupported ` / ` operand for \'Vector3\' and \'{type(o).__name__}\'')
        return self

    def __pos__(self):
        return self

    def __neg__(self):
        self.x *= -1
        self.y *= -1
        self.z *= -1
        return self

    def __invert__(self):
        return self.__neg__()

