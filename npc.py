import items

class NPC():
    def __init__(self):
        raise NotImplementedError("Do No Create Raw NPC Objects!")

    def __str__(self):
        return self.name


class Jeff(NPC):
    def __init__(self):
        self.name = "Jeff"
        self.inventory = []
        self.text = """
        
        Jeff The Wizard Bear: Jeff.
        
        """
        self.happy_text = """
        
        Jeff The Wizard Bear: Jeff!! 
        
        JeffJeffJeffJeffJeff!!!!
        
        """

class TinyTickles(NPC):
    def __init__(self):
        self.name = "Tiny Tickles"
        self.inventory = []
        self.text = """
        
        Tiny Tickles: Bleurgh blurgh!
        
        """
        self.happy_text = """
        
        Tiny Tickles: WEEEEE OOOOOOH blerugh luergh bluergh - swish swish ooooooh!
        
        """


class Snort(NPC):
    def __init__(self):
        self.name = "Snort"
        self.inventory = []
        self.text = """
        
        Snort the Snort: Aw man, I wish I had my scarf, it's chilly and the fashion show is coming up soon!
        
        """
        self.happy_text = """
        
        Snort the Snort: Oh gee, thanks so much, you found my scarf for me!! snuffsnuff
        
        """


class Waddles(NPC):
    def __init__(self):
        self.name = "Waddles"
        self.inventory = []
        self.text = """
        
        Waddles the Penguin: Qwack wack wack...
        
        """
        self.happy_text = """
        
        Waddles the Penguin: Wack?! Wack wack?!! Qwack wack wack wack!!
        
        """


class Hoots(NPC):
    def __init__(self):
        self.name = "Professor Hoots"
        self.inventory = []
        self.text = """
        
        Professor Hoots: Goodness me, I can't believe I put down my scrolls, where have they got to?!
        
        """
        self.happy_text = """
        
        Professor Hoots: Thank you, thank you, thank you!!! Off to teach a class now!!
        
        """


class Lawrence(NPC):
    def __init__(self):
        self.name = "Lawrence"
        self.inventory = [items.WaddlesTapShoes()]
        self.text = """
        
        Lawrence the Hedgehog: Tapity tap, oh goodness, these gloves make far too much noise!
        
        """
        self.happy_text = """
        
        Lawrence the Hedgehog: It makes much more sense that Waddles use them on his feet... anyway, see you!
        
        """


class Dizzy(NPC):
    def __init__(self):
        self.name = "Dizzy"
        self.inventory = [items.SnortScarf()]
        self.text = """
        
        Dizzy the Disco Dancing Lamb: This scarf is just too small for me! Urgh!
        
        """
        self.happy_text = """
        
        Dizzy the Disco Danging Lamb: Ohh, my dances are far too energetic to wear a choreographer's scarf anyway!
        
        """


class Osian(NPC):
    def __init__(self):
        self.name = "Osian"
        self.inventory = [items.HootsScrolls()]
        self.text = """
        
        Osian the Dragon: Put your left arm in... your left arm out... in out in out... shake it all... what??
        
        """
        self.happy_text = """
        
        Osian: At least Professor Hoots will make more use them than me!
        
        """


class Bertie(NPC):
    def __init__(self):
        self.name = "Bertie"
        self.inventory = [items.TinyTickleSwordHat()]
        self.text = """
        
        Bertie the Fox: Swish and flick!! Oh this wand and hat don't work very well...?
        
        """
        self.happy_text = """
        
        Bertie The Fox: Oh, it belongs to Tiny Tickles? Maybe he'll be in my next production as Captain Yawny-Face!
        
        """


class BabyBunny(NPC):
    def __init__(self):
        self.name = "Baby Bunny"
        self.inventory = [items.JeffBlankey()]
        self.text = """
        
        Baby Bunny: Skeebabadoo ughhh ???
        
        """
        self.happy_text = """
        
        Baby Bunny: Ohhhhhhh, Jeff!!! Blankey squisssssshhhhh!
        
        """



