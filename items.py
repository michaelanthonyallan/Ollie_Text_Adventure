class QuestItem:
    def __init__(self):
        raise NotImplementedError("Do not create raw questItems")

    def __str__(self):
        return self.name


class JeffBlankey(QuestItem):
    def __init__(self):
        super().__init__()
        self.name = "Jeff's Blankey"
        self.description = "A special blankey for Jeff to wrap himself in for sleepies!"


class TinyTickleSwordHat(QuestItem):
    def __init__(self):
        self.name = "Tiny Tickles's Tricorn Hat and Sword"
        self.description = "These are for when Tiny Tickles wants to play as Captain Yawny-Face!"


class SnortScarf(QuestItem):
    def __init__(self):
        self.name = "Snort's Rainbow Scarf"
        self.description = "Snort's Rainbow Scarf keeps him warm AND fashionable!"


class WaddlesTapShoes(QuestItem):
    def __init__(self):
        self.name = "Waddles's Tap Shoes"
        self.description = "Waddles wont be able to tap without them!"


class HootsScrolls(QuestItem):
    def __init__(self):
        self.name = "Professor Hoots's Scrolls"
        self.description = "Professor Hoots's very important and very old scrolls. He's never seen without them!"
