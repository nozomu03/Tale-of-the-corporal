define main = Character("ㅇㅇ", who_color = "#000000", what_color="#AE8B59")
define fcaptain = Character("ㅁㅁ", who_color = "#C29F6D", what_color="#000000")
define prf = Character("주안", who_color="#8572EE", what_color="#3CB371")
define OOI = Character("통신소대장", who_color="#EF9F5B", what_color="#0A6E0A")
define adjutant = Character("김율호", who_color="#906D3B", what_color="#FF8200")
define oh = Character("오준현", who_color="#147814", what_color="#50508C")
define gwon = Character("권인호", who_color="#FF8200", what_color="#898989")
define snipe = Character("저격반장", who_color="#DB631F", what_color="#B90000")
define grand = Character("할아버지", who_color = "#F0B469", what_color = "#FF8200")
define jeong = Character("정제영", who_color="#F5AF64", what_color="#5A5AFF")
define go = Character("고균영", who_color="#2828CD", what_color="#0A6E0A")
define gang = Character("강민준", who_color="#110E0E", what_color="#001E38")
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

    class Item:
        def __init__(self, name="", icon="", intro="", tip=""):
            self.name = name
            self.icon = icon
            self.intro = intro
            self.tip = tip

    class Inventory:
        item_list = []
        def __init__(self):
            self.item_list = []
            return

        def add(self, item):
            print(len(self.item_list))
            if len(self.item_list) >= 9:
                narrator("더 이상 가질 수 없어.")
                return
            self.item_list.append(item)
            return

        def delete(self, item):
            self.item_list.remove(item)
            return 

        def search(self, item):
            if item in self.item_list:
                return True
            else:
                return False
        
        def getall(self):
            return self.item_list

    class Buff:
        def __init__(self, type=0, name="N/A", effect = 30, intro = "N/A", icon="na_buff"):
            self.type = type
            self.name = name
            self.effect = effect
            self.intro = intro
            self.icon = icon

    class Bufftory:
        buff_list = []
        def __init__(self):
            self.buff_list = []

        def add(self, buff):
            self.buff_list.append(buff)
        
        def delete(self, buff):
            self.buff_list.remove(buff)

        def serach(self, buff):
            if buff in self.buff_list:
                return True
            else:
                return False

        def getall(self):
            return self.buff_list

    mouse_pos = ( )
    blur_val = False
    now_h = 12
    now_m = 30
    renpy.music.register_channel(name = "looping", mixer = None, loop = True)
    
    item_x = 0
    item_y = 0

    buff_y = 67

    now_name = "N/A"
    now_intro = "N/A"

    where = "N/A"

    mouse_y = 0

    taba = Item("루나틱 드래곤", "item_taba", "군 PX에서 구할 수 있는 6mg 담배 중 가장\n인기가 좋다.\n6.0mg/0.5mg.\n\n{size=10}=과도한 흡연은 질병의 원인이 될 수 있습니다={/size}", "끊어. 돈 낭비 건강 낭비 하지 말고.")
    main_inventory = Inventory()
    

    stress_minus = Buff(type=0, name="족쇄-과거의 이름으로", effect=30, intro="{size=20}사람은 경험의 반복에서 만들어집니다.\n본래의 중대에서 전출하게 된 계기가.\n또한 학창시절에 겪었던 핍박이 제대로 된 \n판단을 내리지 못하게 만드는 족쇄로\n기능하고있습니다.\n\n{size=15}스테러스가 영구히 30 증가합니다", icon="icon_chain")
    bufftory = Bufftory()

    stress_val = 80
    sat_val = 20

    now_buff = stress_minus

    event_result_val = 0

    events_executed = { }
    events_executed_yesterday = { }
