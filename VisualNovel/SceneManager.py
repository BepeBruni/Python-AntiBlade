from ursina import*
from TextManager import VisualText

class Scene(Button):
    def __init__(self, **kwargs):
        super().__init__()
        self.textList = []
        self.collider = 'box'
        self.currentIndex = 0
        self.on_click = self.nextText
        self.sprite = Sprite(scale = 4)
        self.text_origin = (-0.25,0.2)
        self.texting = True
        self.textAnimationIndex = 0
        self.textAnimationTick = 0
        self.objectText = Text(origin = (-.5,.5), position = (-.75, -.25), size = .040)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.sprite.texture = self.textList[self.currentIndex].sprite
        #self.text = self.textList[self.currentIndex].textTo
        if self.texting and self.textAnimationIndex < len(self.textList[self.currentIndex].textTo) + 1:
            self.textAnimationTick += 1
            if self.textAnimationTick == 4:
                textBuffer = self.textList[self.currentIndex].textTo
                print(self.textList[self.currentIndex].textTo)
                buffer = textBuffer[:self.textAnimationIndex]
                self.objectText.text = buffer + " "
                if self.textList[self.currentIndex].textTo[self.textAnimationIndex - 1]  == '<':
                    self.textAnimationIndex += 7
                self.textAnimationIndex += 1
                self.textAnimationTick = 0
        else:
            self.texting = False

    def nextText(self):
        self.currentIndex = self.textList[self.currentIndex].next
        self.texting = True
        self.textAnimationIndex =0


