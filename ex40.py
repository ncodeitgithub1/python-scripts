import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy borthday to you",
                   "I dont want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around teh family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
