define main = Character("ㅇㅇ", who_color = "#000000", what_color="#AE8B59")
define fcaptain = Character("조예헌", who_color = "#C29F6D", what_color="#000000")
define prf = Character("주안", who_color="#8572EE", what_color="#3CB371")
define OOI = Character("통신소대장", who_color="#EF9F5B", what_color="#0A6E0A")
define adjutant = Character("김율호", who_color="#906D3B", what_color="#FF8200")
define oh = Character("오준현", who_color="#147814", what_color="#50508C")
define park = Character("박수윤", who_color = "#323232", what_color="#A0522D")
define gwon = Character("권인호", who_color="#FF8200", what_color="#898989")
define snipe = Character("저격반장", who_color="#DB631F", what_color="#B90000")
define grand = Character("할아버지", who_color = "#F0B469", what_color = "#FF8200")
define jeong = Character("정제영", who_color="#F5AF64", what_color="#5A5AFF")
define go = Character("고균영", who_color="#2828CD", what_color="#0A6E0A")
define gang = Character("강민준", who_color="#110E0E", what_color="#001E38")
define cap2 = Character("박류원", who_color="#1A1E1E", what_color="#09030A")
define son = Character("손한연", who_color="#828282", what_color="#3C3C8C")
define sang = Character("구상언", who_color="#6E6062", what_color="#343F39")
define tie = Character("정훈장교", who_color="#46649B", what_color = "#2E8B57")
define pl3 = Character("조원우", who_color="#0064FF", what_color="#D2E1FF")
define zoo = Character("주완영", who_color="#B3C6C6", what_color="#9E8181")
define young = Character("박영훈", who_color = "#CD853F", what_color = "#778899")
define past1 = Character("박호원", who_color = "#8c8c8c", what_color = "#B90000")
define wol = Character("정영월", who_color = "#3C4444", what_color = "#1E0A0A")
define jun = Character("김현준", who_color = "#262D2D", what_color = "#403C4C")
define zeen = Character("강진욱", who_color = "#7B708E", what_color = "#767074")
define hoyun = Character("김호윤", who_color = "#A17D7B", what_color = "#7D8186")
#1소대 통신병 -> 윤정현
#사수 통신병 -> 김호윤
#3소대장님 -> 작전장교님 = 조원우 
define right = Position(xalign=.9, yalign=1.0)
define center = Position(xalign=.5, yalign=1.0)
define center_true = Position(xalign=.5, yalign=.5)
define left = Position(xalign=.1, yalign=1.0)

define config.gl2 = True
define centered = Character(None, kind = centered, what_color="#FFFFFF")

default item_x = 0
default item_y = 0
default buff_y = 67
default now_name = "N/A"
default now_intro = "N/A"
default where = "N/A"
default evented = False
default mouse_y = 0
default taba = Item("루나틱 드래곤", "item_taba", "군 PX에서 구할 수 있는 6mg 담배 중 가장\n인기가 좋다.\n6.0mg/0.5mg.\n\n{size=10}=과도한 흡연은 질병의 원인이 될 수 있습니다={/size}", "끊어. 돈 낭비 건강 낭비 하지 말고.")
default main_inventory = Inventory()
default stress_minus = Buff(type=0, name="족쇄-과거의 이름으로", effect=30, intro="{size=20}사람은 경험의 반복에서 만들어집니다.\n본래의 중대에서 전출하게 된 계기가.\n또한 학창시절에 겪었던 핍박이 제대로 된 \n판단을 내리지 못하게 만드는 족쇄로\n기능하고있습니다.\n\n{size=15}스트레스가 영구히 30 증가합니다", icon="icon_chain")
default sat_debuff1 = Buff(type=1, name="번뇌탁-수욕정이풍부지", effect=20, intro="{size=10}{b}{i}\"판도라가 허락되지 않은 상자의 내용물을 탐하니, 갖은 죄악이 온 세상에 퍼지매 \n마지막으로 남은 것의 이름은 \'희망\'이라.{/b{/i}{/size}\"\n\n{size=20}이뤄질 수 없는 것을 희망하는 자는 불행합니다.{/size} \n\n{size=15}만족도가 영구히 20 감소합니다", icon="icon_wood")
default bufftory = Bufftory()
default stress_val = 80
default sat_val = 20
default now_buff = stress_minus
default event_result_val = 0
default now_h = 12
default now_m = 30
default events_executed = { }
default events_executed_yesterday = { }
default where_list = []
define bad_incount = 0
default message_list = []
default what = ""
#default what_list = ""
default what_all_list = []
#default random_x = -2
default saturday1_list = []
default go_px = False

default my_hand = CardHand()
default enermy_hand = CardHand()

default morn_do = "선택"
default af_do = "선택"
default night_do = "선택"

define circirisin = ImageDissolve("board_fin.png", 5.0, 8)
define testd = ImageDissolve("testimage.png", 5.0, 8)

#풍수지탄

#화발다풍우
#수욕정이풍부지
#풍찬노숙
#즐풍목우
#


style menu_choice_button is choice_button:
    background "gui/button/choice_idle_warn.png"
  


screen test_screen:
    modal True

screen ForceMouse:
    on "show":
        action MouseMove(x=640, y=360)


label SpriteSystem:
    show screen ForceMouse
    python:
        import pygame
        s_manager = SpriteManager(update = SpriteUpdate, event = PosSaver)
        s_pos = None
        s_val = None
        flash = Image("flash_test.png")
        s_val = s_manager.create(flash)
    #$checkEvent()
    #$getMousePosition()
    $renpy.mouse = [ ]
    python:
        s_val.x = 0
        s_val.y = 0
    show expression s_manager as s_manager
    call screen test_screen
    return

init python:
    dummy_val = False
    now_glitch = "main_ord"
    schedule_time = 0
    exclaim = False

    def ValDel():
        if 'where_list' in globals():
            del store.where_list
        return


    def SpriteUpdate(st):
        if s_pos is None:
            return .01
        print("sval: ")
        t_sprite_x, t_sprite_y = s_pos
        s_val.x = t_sprite_x - (config.screen_width * 1.125)
        s_val.y = t_sprite_y - (config.screen_width * .63)
        return .01

    def PosSaver(event, x, y, st):        
        store.s_pos = (x, y)
        print(s_pos)

    import time
    temp_text = ""
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
            if img + "_lighter" in renpy.get_showing_tags():
                print("문제 발생")
                FaceChange(img + "_taba", loc, 2.0, img + "_lighter")
            else:
                FaceChange(img + "_taba", loc, 2.0, img + "_taba_nof")
            first = False
        while count < rep:
            FaceChange(img + "_taba", loc, 1.0, img + "_tabahand")
            renpy.sound.play("/audio/smoke.ogg")
            FaceChange(img + "_tabahand", loc, 1.0, img + "_taba")
            renpy.pause(2.0)
            count += 1

    class Card:
        def __init__(self, img="", number=1):
            self.img = img
            self.number = number
            return

    class CardHand:
        card_list = []
        def __init__(self):
            self.card_list = []
            return
        
        def add(self, card):
            self.card_list.append(card)
            return

        def remove(self, card):
            global coreect_card
            print(str(coreect_card)  + ":" + str(card.number))
            if coreect_card == True:
                if card in self.card_list:
                    self.card_list.remove(card)    
                    coreect_card = False
                    now_card = card
                    return
            return

        def getAll(self):
            return self.card_list

        def getSome(self, _index):
            return self.card_list[_index]

        def burst(self):
            if len(self.card_list) >= 20:
                return True
            else:
                return False

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

        def search(self, buff):
            if buff in self.buff_list:
                return True
            else:
                return False

        def getall(self):
            return self.buff_list

    class Message:
        def __init__(self, type=0, who="N/A", message = "awa\ngawg"):
            self.type = type
            self.who = who
            self.message = message

    mouse_pos = ( )
    blur_val = False
    renpy.music.register_channel(name = "looping", mixer = None, loop = True)
    renpy.music.register_channel(name = "looping2", mixer = None, loop = True)


    def timeCheck(add_h=0, add_m=0):
        global now_h
        global now_m
        now_h += add_h
        now_m += add_m
        if now_m >=60:
            now_h += 1
            now_m -= 60

    def stressAndSat():
        global stress_val
        global sat_val
        global bufftory
        global now_h 
        global now_m 
        now_h = 06
        now_m = 30
        stress_val = 20
        sat_val = 20
        all_buff = bufftory.getall()
        for b in all_buff:
            if b.type == 0:
                stress_val += b.effect
            elif b.type == 1:
                sat_val -= b.effect


label status_check:
    if sat_val <= 25:
        $bufftory.add(sat_debuff1)
        centered "디버프 \'번뇌탁-수욕정이풍부지\'가 추가되었다."
    if stress_val >= 72:
        centered "이런 개같은 하루 하루를... {w}얼마나 더 보내야 끝이 날까."
        $bad_incount += 1
    return
