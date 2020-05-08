from mycroft import MycroftSkill, intent_file_handler


class Universalskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('universalskill.intent')
    def handle_universalskill(self, message):
        self.speak_dialog('universalskill')


def create_skill():
    return Universalskill()

