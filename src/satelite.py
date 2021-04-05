"""This module has the Satelite Class implementation."""


class Satelite:
    """Satelite abstraction class.

    Attributes:
        _name(str): name of the Satelite.
        _pos_x(float): position in x coordinates of the Satelite.
        _pos_y(float): position in x coordinates of the Satelite.
    """

    def __init__(self, name, pos_x, pos_y):
        self._name = name
        self._pos_x = pos_x
        self._pos_y = pos_y

    def get_position(self):
        """Getter of the Satelite position.

        Returns:
            tuple with (x, y) position.
        """
        return (self._pos_x, self._pos_y)
