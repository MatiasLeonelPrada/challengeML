"""This module has the Trilateration algorithm implementation."""
import numpy as np


class NotValidSatellites(Exception):
    pass


class InvalidDistances(Exception):
    pass


class Trilateration:
    """Trilateration calculation class.

    Attributes:
        _satellites(list): name of the Satelite.

    Raises:
        NotValidSatellites: if number of satellites is
        different from 3.
    """
    def __init__(self, satellites):
        if len(satellites) != 3:
            raise NotValidSatellites
        self._satellites = satellites

    def get_location(self, distances):
        """Get ship position using trilateration with 3 distances.
        
        This solution was made using the intersection of the 3 circles
        and solving the system of two equations:
        Ax + By = C
        Dx + Ey = F

        and the solution is:
        x = EC - BF / EA - BD
        y = DC - AF / BD - EA

        Args:
            distances(list): list with 3 distances for every satellite.

        Raises:
            InvalidDistances: if the number of distances is
            different from 3.

        Returns:
            tuple with x and y position of the ship.
        """
        if len(distances) != 3:
            raise InvalidDistances
        positions = list()
        for satelite in self._satellites:
            positions.append(satelite.get_position())
        A = -2 * positions[0][0] + 2 * positions[1][0]
        B = -2 * positions[0][1] + 2 * positions[1][1]
        C = distances[0]**2 - distances[1]**2 - positions[0][0]**2 \
            + positions[1][0]**2 - positions[0][1]**2 + positions[1][1]**2
        D = -2 * positions[1][0] + 2 * positions[2][0]
        E = -2 * positions[1][1] + 2 * positions[2][1]
        F = distances[1]**2 - distances[2]**2 - positions[1][0]**2 \
            + positions[2][0]**2 - positions[1][1]**2 + positions[2][1]**2

        pos_x = np.divide(E * C - B * F, E * A - B * D)
        pos_y = np.divide(D * C - A * F, B * D - E * A)

        return (round(pos_x, 2), round(pos_y, 2))
