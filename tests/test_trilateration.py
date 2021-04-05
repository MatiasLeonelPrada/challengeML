from challengeML.src.trilateration import Trilateration, NotValidSatellites, InvalidDistances
from challengeML.src.satelite import Satelite
import pytest

def test_trilateration_raise_exception_when_is_in_invalid_state():
    #Arrange
    satellites = [0]

    #Assert
    with pytest.raises(NotValidSatellites):
        Trilateration(satellites)

def test_get_position_method_raise_exc_when_distances_are_invalid():
    #Arrange
    sat1 = Satelite('test1', 0, 0)
    dist1 = 4.47
    sat2 = Satelite('test2', 3, 0)
    dist2 = 4.12
    sat3 = Satelite('test3', 5, 3)
    dist3 = 3.16
    trilateration = Trilateration([sat1, sat2, sat3])

    #Act
    with pytest.raises(InvalidDistances):
        trilateration.get_location([dist1, dist2])

def test_get_position_method_is_correct():
    #Arrange
    sat1 = Satelite('test1', 0, 0)
    dist1 = 4.47
    sat2 = Satelite('test2', 3, 0)
    dist2 = 4.12
    sat3 = Satelite('test3', 5, 3)
    dist3 = 3.16
    trilateration = Trilateration([sat1, sat2, sat3])

    #Act
    result = trilateration.get_location([dist1, dist2, dist3])

    #Assert
    assert (2.0, 4.0) == result
