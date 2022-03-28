image bg_hallway_sepia = im.Sepia("bg_hallway.png")
define bg_qquari_sepia = im.Sepia("bg_qquari.png")
define main_gear_sepia = im.Sepia("main_gear.png")

image park_gear_ang_sepia = im.Sepia("park_gear_ang.png")
image gwon_nem_sepia = im.Sepia("gwon_nem.png")
image main_atten_sepia = im.Sepia("main_atten.png")
image bg_hospital_sepia = im.Sepia("bg_hospital.png")
image main_young_sepia = im.Sepia("main_young.png")
#define a = guiiamge
image crack_glass2 = "crack_glass.png"
image crack_glass3 = "crack_glass.png"
image blood2 = "blood.png"
image blood3 = "blood.png"
image blood4 = "blood.png"
image blood5 = "blood.png"
image blood6 = "blood.png"
image blood7 = "blood.png"
image blood8 = "blood.png"
image blood9 = "blood.png"
image blood10 = "blood.png"

transform bluring:
    blur 34.0
    linear 2.0 blur 10.0

layeredimage qquari:
    always:
        bg_qquari_sepia

    group chara:
        attribute main:
            align(.5, 1.0)
            main_gear_sepia

transform blur:        
    blur 100.0
    linear 4.0 blur 0.0

transform blur2:
    linear 1.0 blur 100
    linear 1.0 blur 0

transform blur3(xa=.5, ya=1.0):
    align(xa, ya)
    linear 1.0 blur 100
    linear 1.0 blur 0


transform chromatic_offset(child):
    crop_relative True
    Fixed(
        Transform(child, alpha=.0),   
        Transform(child, xalign=.0, xzoom=1.01, gl_color_mask=(False, False, True, True)),
        Transform(child, xalign=.5, xzoom=1.01, gl_color_mask=(False, True, False, True)),
        Transform(child, xalign=1.0, xzoom=1.01, gl_color_mask=(True, False, False, True)),
        fit_first=True)
    crop (.0, .0, 1.0, 1.0)

init python:
    def glitching(child):
        all_count = 0
        child = renpy.displayable(child)#이미지 생성
        dis_width, dis_height = renpy.render(child, 0, 0, 0, 0).get_size()#이미지 x y
        part_list = []#조각 리스트
        push_val = 0#조각을 좌우로 미는 정도
        all_part = [renpy.random.randint(0, dis_height) for i in range(30)]
        all_part.sort()#랜덤한 높이로 이미지 range 조각 내기        
        now_height = 0 #현재 
        part_sum_h = 0 #지금까지 조각낸 부분의 높이
        while part_sum_h < dis_height: #전부 다 조각내지 않는 한
            if all_part: #all_part이 비지 않았다면
                now_height = all_part.pop(0) - part_sum_h #all_part[0]
            else:
                #print all_count
                #print("BBB")
                now_height = dis_height - now_height #마지막 다리부분
            part = Transform(child, crop=(-push_val, part_sum_h, dis_width, now_height))
            part = chromatic_offset(Flatten(part))
            #Flatten 없으면 chromatic_offset이 이미지 위로 삐져나와서 겹침
            part_list.append(part)
            #조각 추가
            #print(str(all_count) + ":" + str(part_sum_h))
            part_sum_h += now_height
            if push_val: #push_val이 0이 아니면
                push_val = 0
            else: #push_val이 0이면
                push_val = renpy.random.randint(-50, 50)
            all_count += 1
        return Fixed(Transform(child, alpha=.0),
                VBox(*part_list),
                fit_first=True,                
                crop=(0, 0, 1.0, 1.0)
                )

screen itjusttest:
    add "bg_black"
    vbox:
        align(.5, .5)
        add "button"
        add "button2"
        add "button3"
#image temp(a=None):    