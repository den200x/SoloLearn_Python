####simply concatenated the exsiting code from the learning path with a few changes indicated by comment 

##########################part I
def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:  #verb_dict is a dictionary which was created below
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)


############################part II
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc
##I used ''' and''' to enclose the part which was causing some problems for the program as just a string 
'''class Goblin(GameObject): 
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")''' ###this was moved to part III

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)
############################################################part III
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

goblin = Goblin("Gobbly")

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg

###this part was moved from part I of the original code
verb_dict = {
  "say": say,
  "examine": examine,
  "hit": hit
}

while True:
  get_input()
  
## not sure how to contiuniously run this with this Web Interface
##if you run this on your Python Shell, there shouldn't be any EOFError
