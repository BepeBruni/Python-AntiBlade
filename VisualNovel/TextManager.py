from ursina import*

class VisualText(Text):
    def __init__(self,**kwargs):
        super().__init__()
        self.next = 1
        self.textTo = '''teste'''
        self.sprite = ""
        self.disable = False
        self.hasChoice = False
        self.choiceList = []

        for key, value in kwargs.items():
            setattr(self, key, value)
