import datetime
myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
         for line in self.lyrics:
            print line

happy_bdy = Song(["happy birthday to u"])
bulls_on_a_parade = Song(["they rally the family"])

happy_bdy.sing_me_a_song()

bulls_on_a_parade.sing_me_a_song()