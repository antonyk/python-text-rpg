from datetime import datetime, date, timedelta

class Living:

  def __init__(self, bday):
    # self.age = initial_age
    # self.aggressive = is_aggressive
    self.birthday = bday

  def get_age(self):
    now = datetime.now()
    print(self.birthday)
    print(now)
    
    age = now - self.birthday
    print(type(age))
    # print(age.years)
    timedelta
    return age

class Npc(Living):
  
  pass



adam = Living(datetime(2010, 11, 8, 0,0,0))

print(adam.get_age())


# class Desk:
#   def __init__(self, items = []):
#     self.items = items


# class Bottle:
#   def __init__(self, waterAmt, hasCap):
#     self.waterAmount = waterAmt
#     self.hasCap = hasCap



# bottle1 = Bottle(0, True)
# bottle2 = Bottle(0, False)
# bottle3 = Bottle(400, True)


# adamsDesk = Desk()
# adamsDesk.items.append(bottle1)
# adamsDesk.items.append(bottle2)
# adamsDesk.items.append(bottle3)


# for b in adamsDesk.items:
#   print(b.waterAmount)



"""
Phase 1:
20 minute days (like in Minecraft)

Phase 2:
months and years

4 seasons
12 months

1 month = 30 days
1 day = 

Goal:

1 game year = 1 real week
1 game month = 0.5 real days (12 hours, 12*60 minutes)
1 game day = 24 real minutes
1 game hour = 1 real minute


14 game months = 1 game year
30 game days = 1 game month

real time
1 week = 7 days = 168 hours = 10080 minutes

game time
10080 hours = 420 days = 14 months = 1 year


"""