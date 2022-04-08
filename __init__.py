from mycroft import MycroftSkill, intent_file_handler


class NightVision(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vision.night.intent')
    def handle_vision_night(self, message):
        self.speak_dialog('vision.night')


def create_skill():
    return NightVision()

