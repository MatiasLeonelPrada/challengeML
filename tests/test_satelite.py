from challengeML.src.satelite import Satelite

def test_satellite_method_get_positions_works_correctly():
    #Arrange
    sat = Satelite('test', 10, 10)
    #Act
    result = sat.get_position()
    #Assert
    assert result == (10, 10)