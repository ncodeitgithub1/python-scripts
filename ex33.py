import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
class Song(object):

     def __init__(self,lyrics):
         self.lyrics = lyrics

     def sing_me_a_song(self):
          for line in self.lyrics:
             print line



lyrics1 = ["New Lyrics", "HOw are the lyrics1", "Isnot it beautiful lyrics1"]
happy_bday = Song(["Happy birthday to you", "I dont want to get sued", "So i'll stop right there"])

happy_bday1 = Song(lyrics1)

bulls_on_parade = Song(["THey rally around the family", "with pockets full of shells"])

happy_bday.sing_me_a_song()
happy_bday1.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
    
