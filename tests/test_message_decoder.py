from challengeML.src.message_decoder import MessageDecoder
import pytest

def test_merge_message_method_with_different_messages_in_result():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    result = []
    ship_message = MessageDecoder()
    
    #Act 
    ship_message.merge_message(result, mes_1)

    #Assert
    assert result[0] == "este"
    assert len(mes_1) == 3

def test_merge_message_method_with_same_messages_in_result_doesnt_modify_result():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    result = ["este"]
    ship_message = MessageDecoder()
    
    #Act 
    ship_message.merge_message(result, mes_1)

    #Assert
    assert result[0] == "este"
    assert len(result) == 1
    assert len(mes_1) == 3

def test_merge_message_method_with_empty_string_in_message_doesnt_modify_result():
    #Arrange
    mes_1 =  ["", "es", "un", "mensaje"]
    result = ["este"]
    ship_message = MessageDecoder()
    
    #Act 
    ship_message.merge_message(result, mes_1)

    #Assert
    assert result[0] == "este"
    assert len(result) == 1
    assert len(mes_1) == 3

def test_correct_offset_method_in_messages_without_offsets_doesnt_modify_messages():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    ship_message = MessageDecoder()

    #Act
    result = ship_message.correct_offset(mes_1, mes_2)

    assert len(mes_1) == 4
    assert len(mes_2) == 4

def test_correct_offset_method_in_msg_with_one_offset_in_first_msg_removes_them():
    #Arrange
    mes_1 =  ["", "este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    ship_message = MessageDecoder()

    #Act
    result = ship_message.correct_offset(mes_1, mes_2)

    assert len(mes_1) == 4
    assert len(mes_2) == 4
    assert mes_1[0] == "este"

def test_correct_offset_method_in_msg_with_one_offset_in_first_msg_removes_them():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    mes_2 =  ["", "este", "", "un", "mensaje"]
    ship_message = MessageDecoder()

    #Act
    result = ship_message.correct_offset(mes_1, mes_2)

    assert len(mes_1) == 4
    assert len(mes_2) == 4
    assert mes_2[0] == "este"


def test_get_messages_method_case_1():
    #Arrange
    mes_1 =  ["", "este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    mes_3 =  ["", "", "es", "", "mensaje"]
    ship_message = MessageDecoder()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == "este es un mensaje"

def test_get_messages_method_case_2():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    mes_3 =  ["", "", "es", "", "mensaje"]
    ship_message = MessageDecoder()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == "este es un mensaje"

def test_get_messages_method_case_without_offset():
    #Arrange
    mes_1 =  ["este", "es", "un", "mensaje"]
    mes_2 =  ["este", "", "un", "mensaje"]
    mes_3 =  ["", "es", "", "mensaje"]
    ship_message = MessageDecoder()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == "este es un mensaje"

def test_get_messages_method_case_with_offsets_in_all_messages():
    #Arrange
    mes_1 =  ["", "es", "un", "mensaje"]
    mes_2 =  ["", "", "un", "mensaje"]
    mes_3 =  ["", "es", "", "mensaje"]
    ship_message = MessageDecoder()
    messages = [mes_1, mes_2, mes_3]

    #Act
    result = ship_message.get_messages(messages)

    assert result == "es un mensaje"