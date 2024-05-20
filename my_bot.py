"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
import random
answer_time = False
ez_or_hard = random.randint(1,4)
def should_i_respond(user_message, user_name):
  global ez_or_hard 
  global answer_time
  global answer
  global riddle_list
  global state
  answer = ""
  state = ""
  if "Borody bot" in user_message:
    state = "bot"
    return True
  elif answer_time is True:
    if "!hint" in user_message:
      state = "hint"
      return True
    elif "!sad" in user_message:
      state = "sad"
      return True
    else:
      print("got to answer time")
      answer = user_message
      state = "answer_bot"
      return True
    return True
  elif "!info" in user_message:
    state = "info"
    return True
  elif "!riddle" in user_message:
    riddle_list = ["what gets wet when drying?","What goes up but never goes down?","What gets bigger the more you take away?","I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?","There are five houses, each painted a different color. In each house lives a person with a different nationality. These five owners drink a certain type of beverage, smoke a certain brand of cigar, and keep a certain pet. No owners have the same pet, smoke the same cigar, or drink the same beverage.The question is, who owns the fish? Here are the clues: The Brit lives in the red houseThe Swede keeps dogs as pets The Dane drinks tea The green house is on the left of the white house The green house’s owner drinks coffee The person who smokes Pall Mall rears birds The owner of the yellow house smokes Dunhill The man living in the center house drinks milk The Norwegian lives in the first house The man who smokes blends lives next to the one who keeps cats The man who keeps horses lives next to the man who smokes Dunhill The owner who smokes BlueMaster drinks beer The German smokes Prince The Norwegian lives next to the blue house The man who smokes blend has a neighbor who drinks water"]
    state = "riddle_select"
    return True
  elif "!harder" in user_message:
    if ez_or_hard == 4:
      return "there are no harder riddles yet"
    else:
      ez_or_hard += 1
      state = "riddle_select"
      return True
  elif "!easier" in user_message:
    if ez_or_hard == 0:
      return "there are no easier riddles yet"
    else:
      ez_or_hard -= 1
      state = "riddle_select"
      return True
    

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message,user_name):
  global answer
  global answer_time
  if state == "bot":
    return f"Hello {user_name}, what do you want? for a list of commands type !info"
  elif state == "info":
    return "!riddle, will give you a riddle,from which you can keep answering until you get the correct answer. !harder or !easier will give you a harder or easier riddle, you can also type !hint for a hint and do !sad if you give up"
  elif state == "sad":
    if ez_or_hard == 0:
      answer_time = False
      return "the answer is a towel"
    elif ez_or_hard == 1:
      answer_time = False
      return "the answer is age"
    elif ez_or_hard == 2:
      return "the answer is a hole"
    elif ez_or_hard == 3:
      return "the answer is a map"
    elif ez_or_hard == 4:
      return "the answer is the german"
  elif state == "riddle_select":
    answer_time = True
    return riddle_list[ez_or_hard]
  elif state == "hint":
    if ez_or_hard == 0:
      return "you  use this after showering"
    elif ez_or_hard == 1:
      return "it happens to everyone"
    elif ez_or_hard == 2:
      return "you find these sometimes in cheese"
    elif ez_or_hard == 3:
      return "this is used for navigation"
    elif ez_or_hard == 4:
      return "my hint is to choose another riddle"
  elif state == "answer_bot":
    answer = user_message
    print("im at answer if statement")
    print(ez_or_hard)
    if ez_or_hard == 0:
      print("riddle 0 is selected")
      if answer == "towel" or answer == "a towel":
        answer_time = False
        return "your correct!"
      else:
        return "your wrong, try again!"
    elif ez_or_hard == 1:
      if answer == "age" or answer == "Age" or answer ==  "aging":
        answer_time = False
        return "your correct"
      else:
        return "your wrong, try again!"
    elif ez_or_hard == 2:
      if answer == "hole" or answer == "a hole":
        answer_time = False
        return "your correct!"
      else:
        return "your wrong, try again!"
    elif ez_or_hard == 3:
      if answer == "map" or answer == "a map":
        answer_time = False
        return "your correct!"
    elif ez_or_hard == 4:
      if answer == "german" or answer == "the german":
        answer_time = False
        return "your correct!"
      else:
        return "your wrong, try again!"
  else:
    return "I do not understand!"
 