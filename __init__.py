


from mycroft import MycroftSkill, intent_file_handler


class CheckTheProperty(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('property.the.check.intent')
    def handle_property_the_check(self, message):
        self.speak_dialog('property.the.check')


def create_skill():
    return CheckTheProperty()

