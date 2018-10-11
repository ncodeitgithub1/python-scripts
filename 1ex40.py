import datetime
myname = 'Chaithanya'
myid = 'NCD0818H008'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around he family",
                        "with pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()