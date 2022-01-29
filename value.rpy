define main = Character("ㅇㅇㅇ", who_color = "#000000", what_color="#AE8B59")
define fcaptain = Character("ㅁㅁㅁ", who_color = "#C29F6D", what_color="#000000")
define prf = Character("김조", who_clor="#8572EE", what_color="#3CB371")
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

    
