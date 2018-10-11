import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()
class song(object):
  def __init__(self, lyrics):
    self.lyrics=lyrics
  def sing_me_a_song(self):
      for line in self.lyrics:
          print line
happy_bday=song(["happy birthday to u",
                  "i dont want to get sad"])
bulls_on_parade=song(["tey rally"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
