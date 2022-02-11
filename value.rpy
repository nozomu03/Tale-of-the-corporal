define main = Character("ㅇㅇ", who_color = "#000000", what_color="#AE8B59")
define fcaptain = Character("ㅁㅁ", who_color = "#C29F6D", what_color="#000000")
define prf = Character("주안", who_color="#8572EE", what_color="#3CB371")
define OOI = Character("통신소대장", who_color="#EF9F5B", what_color="#0A6E0A")
define adjutant = Character("김율호", who_color="#906D3B", what_color="#FF8200")
define oh = Character("오준현", who_color="#147814", what_color="#50508C")
define gwon = Character("권인호", who_color="#FF8200", what_color="#898989")
define snipe = Character("저격반장", who_color="#DB631F", what_color="#B90000")
define right = Position(xalign=.9, yalign=1.0)
define center = Position(xalign=.5, yalign=1.0)
define left = Position(xalign=.1, yalign=1.0)

define config.gl2 = True
define centered = Character(None, kind = centered, what_color="#FFFFFF")

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

    def Smoking(img="main", loc=0, rep = 1, first=False):
        count = 0
        if first == True:
            renpy.sound.play("/audio/lighter.ogg")
            renpy.pause(4.0)
            FaceChange(img + "_taba", loc, 2.0, img + "_taba_nof")
        while count < rep:
            FaceChange(img + "_taba", loc, 1.0, img + "_tabahand")
            renpy.sound.play("/audio/smoke.ogg")
            FaceChange(img + "_tabahand", loc, 1.0, img + "_taba")
            renpy.pause(2.0)
            count += 1

    blur_val = False
    
    renpy.music.register_channel(name = "looping", mixer = None, loop = True)
    
