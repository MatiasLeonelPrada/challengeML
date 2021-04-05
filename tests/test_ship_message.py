from challengeML.src.ship_message import ShipMessage
import pytest

def test_get_messages_method_case_1():
    #Arrange
    mes_1 =  ["", "este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    mes_3 =  ["", "", "es", "", "mensaje"]
    ship_message = ShipMessage()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == ["este", "es", "un", "mensaje"]

def test_get_messages_method_case_2():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    mes_3 =  ["", "", "es", "", "mensaje"]
    ship_message = ShipMessage()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == ["este", "es", "un", "mensaje"]

def test_get_messages_method_case_3():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    mes_3 =  ["", "es", "", "mensaje"]
    ship_message = ShipMessage()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == ["este", "es", "un", "mensaje"]