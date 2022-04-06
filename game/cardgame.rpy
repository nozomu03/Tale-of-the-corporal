default all_card = [0 for i in range(55)]
default while_count = 0
default first_index = 54
default now_card = None
default coreect_card = False
default my_card_use = False
default enermy_card_use = False

style card_text:
    size 50
    color "#000000"

init python:
    def card_reset():
        for i in range(54):
            all_card.append(i)
        all_card.pop(0)
        all_card.append(54)
        return




screen cardgame:
    $dummy_val = False
    $renpy.block_rollback()
    $_skipping = False
    $while_count = 0
    modal True
    hbox:
        xalign .5
        yalign .0
        add "hand_image" 
    vbox:
        xalign .9
        yalign .5
        text str(len(enermy_hand.getAll()))
        textbutton "{color=FF0000}차례 넘기기":
            action[
                Function(enermy_pattern),
                If(my_card_use == False, true = Function(my_add), false = NullAction()),
                SetVariable("my_card_use", False)
            ]
        text str(len(my_hand.getAll()))

    hbox:
        xalign .5
        yalign 1.0
        if len(my_hand.getAll()) > 7:
            for i in range(7):                
                if my_card_use == False:
                    imagebutton idle my_hand.getSome(i).img:
                        action Show("over_7")
                        xpadding 10
                else:
                    imagebutton idle my_hand.getSome(i).img:
                #    action [
                #        If(my_hand.getSome(i).number / 13 == now_card.number /13, true = [SetVariable("now_card", my_hand.getSome(i)), Function(my_hand.remove(my_hand.getSome(i)))], false = NullAction())
                #    ]
                        xpadding 10
        else:
            for i in my_hand.getAll():
                if my_card_use == False:
                    imagebutton idle i.img: 
                        action [
                            If(i.number <= 13 and now_card.number <= 13, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                            If(i.number <= 26 and now_card.number <= 26 and i.number > 13 and now_card.number >13, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                            If(i.number <= 39 and now_card.number <= 39 and i.number > 26 and now_card.number >26, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                            If(i.number <= 52 and now_card.number <= 52 and i.number > 39 and now_card.number >39, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                      
                            Function(my_hand.remove, i),
                        ]
                        xpadding 10
                else:
                    imagebutton idle i.img: 
                        xpadding 10
    hbox:       
        xalign .5
        yalign .5
        spacing 30
        add "card_bone"
        add now_card.img        

screen alpha_scene:
    add "bg_alpha"
    hbox:       
        xalign .5
        yalign .5
        spacing 30
        add "card_bone"
        add now_card.img        

    button action[Hide("alpha_scene"), Show("cardgame")]

transform small_imagebutton(x=0, y=0):
    pos(x, y)
    zoom .8

screen over_7:
    modal True
    add "cg_over7"
    $x = 38
    $y = 34
    for i in my_hand.getAll():
        if x<=1138:
            imagebutton idle i.img:                 
                action[
                    If(i.number <= 13 and now_card.number <= 13, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                    If(i.number <= 26 and now_card.number <= 26 and i.number > 13 and now_card.number >13, true = [SetVariable("coreect_card", True), SetVariable("my_card_use", True), Function(log_print, i.number)], false = Function(log_print1, i.number)),                        
                    If(i.number <= 39 and now_card.number <= 39 and i.number > 26 and now_card.number >26, true = [SetVariable("coreect_card", True), SetVariable("my_card_use", True), Function(log_print, i.number)], false = Function(log_print1, i.number)),                        
                    If(i.number <= 52 and now_card.number <= 52 and i.number > 39 and now_card.number >39, true = [SetVariable("coreect_card", True), SetVariable("my_card_use", True), Function(log_print, i.number)], false = Function(log_print1, i.number)),                      
                    Function(my_hand.remove, i),
                    Hide("over_7")
                ]
                at small_imagebutton(x, y)
                xpadding 10
            $x+=110
        else:
            $x=38
            $y+=98
    textbutton "{size=40}{color=#FFFFFF}X":
        align .9, .1
        action Hide("over_7")

init python:
    def log_print(i):
        print("성공: " + str(i) + ":" + str(now_card.number))
        return

init python:
    def log_print1(i):
        print("실패: " + str(i) + ":" + str(now_card.number))
        return
label troll():
    "응 아니야"
    return

label set_allcard:
    $while_count = 1
    init:        
        
        $while_count = 1
        while while_count <= 54:
            if while_count <= 13:
                if while_count % 13 == 0:
                    $renpy.image("spade_k", Fixed(Transform("card_bone"), Transform(Text("♤K"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 1:
                    $renpy.image("spade_a", Fixed(Transform("card_bone"), Transform(Text("♤A"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 11:
                    $renpy.image("spade_j", Fixed(Transform("card_bone"), Transform(Text("♤J"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 12:
                    $renpy.image("spade_q", Fixed(Transform("card_bone"), Transform(Text("♤Q"), xalign=.5, yalign=.5), fit_first=True))
                else:                    
                    $renpy.image("spade_" + str(while_count%13), Fixed(Transform("card_bone"), Transform(Text("♤"+ str(while_count%13)), xalign=.5, yalign=.5), fit_first=True))
            elif while_count <= 26:
                if while_count == 26:
                    $renpy.image("diamond_k", Fixed(Transform("card_bone"), Transform(Text("◇K"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count == 14:
                    $renpy.image("diamond_a", Fixed(Transform("card_bone"), Transform(Text("◇A"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count == 24:
                    $renpy.image("diamond_j", Fixed(Transform("card_bone"), Transform(Text("◇J"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count == 25:
                    $renpy.image("diamond_q", Fixed(Transform("card_bone"), Transform(Text("◇Q"), xalign=.5, yalign=.5), fit_first=True))
                else:                    
                    $renpy.image("diamond_" + str(while_count%13), Fixed(Transform("card_bone"), Transform(Text("◇"+ str(while_count%13)), xalign=.5, yalign=.5), fit_first=True))
            elif while_count <= 39:
                if while_count % 13 == 0:
                    $renpy.image("heart_k", Fixed(Transform("card_bone"), Transform(Text("♡K"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 1:
                    $renpy.image("heart_a", Fixed(Transform("card_bone"), Transform(Text("♡A"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 11:
                    $renpy.image("heart_j", Fixed(Transform("card_bone"), Transform(Text("♡J"), xalign=.5, yalign=.5), fit_first=True))

                elif while_count % 13 == 12:
                    $renpy.image("heart_q", Fixed(Transform("card_bone"), Transform(Text("♡Q"), xalign=.5, yalign=.5), fit_first=True))
                else:                    
                    $renpy.image("heart_" + str(while_count%13), Fixed(Transform("card_bone"), Transform(Text("♡"+ str(while_count%13)), xalign=.5, yalign=.5), fit_first=True))
            elif while_count <= 52:
                if while_count % 13 == 0:
                    $renpy.image("clover_k", Fixed(Transform("card_bone"), Transform(Text("♧K"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 1:
                    $renpy.image("clover_a", Fixed(Transform("card_bone"), Transform(Text("♧A"), xalign=.5, yalign=.5), fit_first=True))
                elif while_count % 13 == 11:
                    $renpy.image("clover_j", Fixed(Transform("card_bone"), Transform(Text("♧J"), xalign=.5, yalign=.5), fit_first=True))

                elif while_count % 13 == 12:
                    $renpy.image("clover_q", Fixed(Transform("card_bone"), Transform(Text("♧Q"), xalign=.5, yalign=.5), fit_first=True))
                else:                    
                    $renpy.image("clover_" + str(while_count%13), Fixed(Transform("card_bone"), Transform(Text("♧"+ str(while_count%13)), xalign=.5, yalign=.5), fit_first=True))
            else:
                if while_count == 53:
                    $renpy.image("black_joker", Fixed(Transform("card_bone"), Transform(Text("흑백 조커"), xalign=.5, yalign=.5), fit_first=True))
                else:
                    $renpy.image("color_joker", Fixed(Transform("card_bone"), Transform(Text("컬러 조커"), xalign=.5, yalign=.5), fit_first=True))
            $while_count +=1
    #show spade_5
    #show spade_a at center
    $while_count = 0
    while while_count <= 54:
        if while_count <= 13:
            if while_count % 13 == 0:
                $all_card[13]= Card("spade_k", 13)
            elif while_count % 13 == 1:
                $all_card[1]=Card("spade_a", 1)         
            elif while_count % 13 == 11:
                $all_card[11]=Card("spade_j", 11)               
            elif while_count % 13 == 12:
                $all_card[12]=Card("spade_q", 12)          
            else:                    
                $all_card[while_count%13]= Card("spade_" + str(while_count%13), while_count%13)
        elif while_count <= 26:
            if while_count % 13 == 0:
                $all_card[26]=Card("diamond_k", 26)
            elif while_count % 13 == 1:
                $all_card[14]=Card("diamond_a", 14)            
            elif while_count % 13 == 11:
                $all_card[24]=Card("diamond_j", 24)                
            elif while_count % 13 == 12:
                $all_card[25]=Card("diamond_q", 25)            
            else:                    
                $all_card[while_count%13 + 13]= Card("diamond_" + str(while_count%13), while_count%13 + 13)
        elif while_count <= 39:
            if while_count % 13 == 0:
                $all_card[39]=Card("heart_k", 39)
            elif while_count % 13 == 1:
                $all_card[27]=Card("heart_a", 27)            
            elif while_count % 13 == 11:
                $all_card[37]=Card("heart_j", 37)                
            elif while_count % 13 == 12:
                $all_card[38]=Card("heart_q", 38)            
            else:                    
                $all_card[while_count%13 + 26]= Card("heart_" + str(while_count%13), while_count%13 + 26)
        elif while_count <= 52:
            if while_count % 13 == 0:
                $all_card[52]=Card("clover_k", 52)
            elif while_count % 13 == 1:
                $all_card[40]=Card("clover_a", 40)            
            elif while_count % 13 == 11:
                $all_card[50]=Card("clover_j", 50)                
            elif while_count % 13 == 12:
                $all_card[51]=Card("clover_q", 51)            
            else:                    
                $all_card[while_count%13 + 39]= Card("clover_" + str(while_count%13), while_count%13 + 39)
        else:
            if while_count == 53:
                $all_card[53]=Card("black_joker", 53)
            else:
                $all_card[54]=Card("color_joker", 54)
                #$renpy.image("spade_" + str(while_count%13), Fixed(Transform("card_bone"), Transform(Text("♤"+ str(while_count%13)), xalign=.5, yalign=.5), fit_first=True))
        $while_count += 1
        #$del while_count
    return

label game_reset:
    $while_count = 0
    while while_count < 7:
        #print("now while: " + str(while_count))
        $my_hand.add(all_card.pop(renpy.random.randint(1, first_index)))
        $first_index -= 1
        $enermy_hand.add(all_card.pop(renpy.random.randint(1, first_index)))
        $first_index -= 1
        $while_count += 1
    $now_card = (all_card.pop(renpy.random.randint(1, first_index)))
    $first_index -= 1
    return

init python:
    def card_shuffle():
        global while_count
        global all_card
        while_count = 0
        while while_count <= 54:
            if while_count <= 13:
                if while_count % 13 == 0:
                    all_card[13]= Card("spade_k", 13)
                elif while_count % 13 == 1:
                    all_card[1]=Card("spade_a", 1)         
                elif while_count % 13 == 11:
                    all_card[11]=Card("spade_j", 11)               
                elif while_count % 13 == 12:
                    all_card[12]=Card("spade_q", 12)          
                else:                    
                    all_card[while_count%13]= Card("spade_" + str(while_count%13), while_count%13)
            elif while_count <= 26:
                if while_count % 13 == 0:
                    all_card[26]=Card("diamond_k", 26)
                elif while_count % 13 == 1:
                    all_card[14]=Card("diamond_a", 14)            
                elif while_count % 13 == 11:
                    all_card[24]=Card("diamond_j", 24)                
                elif while_count % 13 == 12:
                    all_card[25]=Card("diamond_q", 25)            
                else:                    
                    all_card[while_count%13 + 13]= Card("diamond_" + str(while_count%13), while_count%13 + 13)
            elif while_count <= 39:
                if while_count % 13 == 0:
                    all_card[39]=Card("heart_k", 39)
                elif while_count % 13 == 1:
                    all_card[27]=Card("heart_a", 27)            
                elif while_count % 13 == 11:
                    all_card[37]=Card("heart_j", 37)                
                elif while_count % 13 == 12:
                    all_card[38]=Card("heart_q", 38)            
                else:                    
                    all_card[while_count%13 + 26]= Card("heart_" + str(while_count%13), while_count%13 + 26)
            elif while_count <= 52:
                if while_count % 13 == 0:
                    all_card[52]=Card("clover_k", 52)
                elif while_count % 13 == 1:
                    all_card[40]=Card("clover_a", 40)            
                elif while_count % 13 == 11:
                    all_card[50]=Card("clover_j", 50)                
                elif while_count % 13 == 12:
                    all_card[51]=Card("clover_q", 51)            
                else:                    
                    all_card[while_count%13 + 39]= Card("clover_" + str(while_count%13), while_count%13 + 39)
            else:
                if while_count == 53:
                    all_card[53]=Card("black_joker", 53)
                else:
                    all_card[54]=Card("color_joker", 54)
            while_count += 1
        return

    def my_add():
        global first_index
        global all_card
        if first_index == 0:
            all_card = [0 for i in range(55)]
            first_index = 54
            card_shuffle()
            now_card = all_card.pop(renpy.random.randint(1, first_index))
            first_index -= 1
        else:
            my_hand.add(all_card.pop(renpy.random.randint(1, first_index)))
            first_index -= 1
        return
    def enermy_add():
        global first_index
        global all_card
        if first_index == 0:
            first_index = 54
            all_card = [0 for i in range(55)]
            card_shuffle()
            now_card = all_card.pop(renpy.random.randint(1, first_index))
            first_index -= 1
        else:
            enermy_hand.add(all_card.pop(renpy.random.randint(1, first_index)))
            first_index -= 1
        return

init python:
    def enermy_pattern():    
        global first_index
        global enermy_hand
        global while_count 
        global enermy_card_use
        global coreect_card
        while_count =0
        while while_count < len(enermy_hand.getAll()):
          #  print("hellO?")
            i = enermy_hand.getSome(while_count)
        
            if i.number <= 13 and now_card.number <= 13:
             #   print("a")
                coreect_card = True
                enermy_hand.remove(i)
                enermy_card_use = True
                return
            elif i.number <= 26 and now_card.number <= 26 and i.number > 13 and now_card.number >13:
              #  print("b")
                coreect_card = True
                enermy_hand.remove(i)
                enermy_card_use = True
                return
            elif i.number <= 39 and now_card.number <= 39 and i.number > 26 and now_card.number >26:
              #  print("c")
                coreect_card = True
                enermy_hand.remove(i)
                enermy_card_use = True
                return
            elif i.number <= 52 and now_card.number <= 52 and i.number > 39 and now_card.number >39:
                #print("d")
                coreect_card = True
                enermy_hand.remove(i)
                enermy_card_use = True
                return
            while_count += 1
        enermy_card_use = False
        if enermy_card_use == False:
            #rint("e")
            enermy_add()
        #if len(enermy_hand.getAll()) > 7:
        #    print(len(enermy_hand.getAll()))
        return
                #action [
                #    If(i.number <= 13 and now_card.number <= 13, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                #    If(i.number <= 26 and now_card.number <= 26 and i.number > 13 and now_card.number >13, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                #    If(i.number <= 39 and now_card.number <= 39 and i.number > 26 and now_card.number >26, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                        
                #    If(i.number <= 52 and now_card.number <= 52 and i.number > 39 and now_card.number >39, true = [SetVariable("coreect_card", True), Function(log_print, i.number), SetVariable("my_card_use", True)], false = Function(log_print1, i.number)),                      
                #    Function(my_hand.remove, i)
