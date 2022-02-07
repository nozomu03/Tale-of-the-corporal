define main = Character("ㅇㅇ", who_color = "#000000", what_color="#AE8B59")
define fcaptain = Character("ㅁㅁ", who_color = "#C29F6D", what_color="#000000")
define prf = Character("주안", who_color="#8572EE", what_color="#3CB371")
define OOI = Character("통신소대장", who_color="#EF9F5B", what_color="#0A6E0A")
define adjutant = Character("김율호", who_color="#906D3B", what_color="#FF8200")
define oh = Character("오준현", who_color="#147814", what_color="#50508C")
define right = Position(xalign=.9, yalign=1.0)
define center = Position(xalign=.5, yalign=1.0)
define left = Position(xalign=.1, yalign=1.0)

init python:
    def FaceChange(img="", loc=0 ,t=2.0, org_img=None):
        if loc == 0:
            renpy.show(img, [left])
        elif loc == 1:
            renpy.show(img, [center])
        elif loc == 2:
            renpy.show(img, [right])
        else:
            renpy.show(img, [Position(xalign=loc, yalign=1.0)])
        renpy.transition(Dissolve(t))
        if org_img != None:
            renpy.hide(org_img)

        renpy.pause(t, hard=True)


    def SoundPlayer(fn="", t=2.0, ch="sound"):
        renpy.music.play("/audio/"+ fn, channel=ch)
        renpy.pause(t)
        renpy.music.stop(channel='sound')
    
    renpy.music.register_channel(name = "looping", mixer = None, loop = True)
    
