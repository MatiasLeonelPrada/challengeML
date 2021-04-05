

class ShipMessage:
    def __init__(self):
        pass

    def get_last_element(self, lst):
        if len(lst) == 0:
            return ''
        else:
            return lst[-1]

    def merge_message(self, result, received_msg):
        if len(received_msg) > 0:
            if len(received_msg[0]) > 0:
                if self.get_last_element(result) != received_msg[0]:
                    result.append(received_msg[0])
            received_msg.pop(0)

    def correct_offset(self, mes_1, mes_2):
        if len(mes_1) != len(mes_2):
            if len(mes_1[0]) == 0:
                mes_1.pop(0)
            elif len(mes_2[0]) == 0:
                mes_2.pop(0)

    def get_messages(self, messages):
        result = list()
        mes_1 = messages[0]
        mes_2 = messages[1]
        mes_3 = messages[2]
        self.correct_offset(mes_1, mes_2)
        self.correct_offset(mes_1, mes_3)
        while len(mes_1) > 0:
            self.merge_message(result, mes_1)
            self.merge_message(result, mes_2)
            self.merge_message(result, mes_3)
        return result