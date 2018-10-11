import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()








class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


lyrics1 = ["New Lyrics", "How are the lyrics1 ", "Isnt it beautifual lyrics1"]
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

happy_bday1 = Song(lyrics1)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
happy_bday1.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
