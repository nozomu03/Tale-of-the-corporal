init python:
    test = "소대 사무실"
    event('meet_gang', 'where==\"소대 사무실\" and evented == False', event.random(.3), event.only(), priority=20)
    event('meet_jeong', 'where==\"소대 사무실\" and evented == False', event.random(.6), event.only(), priority=20)
    event('none', 'where==\"소대 사무실\" and evented == False', priority = 100)
    event('hq_event1', 'where==\"본부 행정반\" and evented == False', event.random(.3), event.only(), priority=20)
    event('sniper_hq', 'where==\"본부 행정반\" and evented == False', event.random(.5), event.only(), priority=20)
    event('none', 'where==\"본부 행정반\" and evented == False', priority = 100)
    event('washing_room1', 'where==\"세탁실\" and evented == False', event.random(.3), event.only(), priority=20)
    event('none', 'where==\"세탁실\" and evented == False', priority = 100)
    event('csco1', 'where==\"CSCO 행정반\" and evented == False', event.random(.2), event.only(), priority=20)
    event('none', 'where==\"CSCO 행정반\" and evented == False', priority = 100)
    event('lounge_event1', 'where==\"휴게실\" and evented == False', event.random(.3), event.only(), priority=20)
    event('pc_bad', 'where==\"사지방\" and evented == False', priority = 100)
    event('pc_good','where==\"사지방\" and evented == False', event.random(.5), event.only(), priority=20)
    event("day2_novel1", 'what==\"독서\" and evented == False', event.random(.6), event.only(), priority=20)
    event("day2_novel3", 'what==\"독서\" and evented == False', event.random(.4), event.only(), priority=20)
    event("day2_novel2", 'what==\"독서\" and evented == False', priority = 100)
    event("day2_study_specialty3", 'what==\"주특기 공부\" and evented == False', event.random(.7), event.only(), priority=20)
    event("day2_study_specialty2", 'what==\"주특기 공부\" and evented == False', event.random(.7), event.only(), priority=20)
    event("day2_study_specialty1", 'what==\"주특기 공부\" and evented == False', priority = 100)
    event("day2_study_major3", 'what==\"전공 공부\" and evented == False', event.random(.5), event.only(), priority=20)
    event("day2_study_major1", 'what==\"전공 공부\" and evented == False', event.random(.5), event.only(), priority=20)
    event("day2_study_major2", 'what==\"전공 공부\" and evented == False', priority = 100)

    event("pcroom1_good_event1", 'morn_do==\"사이버지식정보방\" and evented == False', event.random(.6), event.only(), priority = 20)
    event("pcroom1_normal_event1", 'morn_do==\"사이버지식정보방\" and evented == False', priority = 100)
    #event('meet_j')
    event("pcroom1_bad_event1", 'morn_do==\"사이버지식정보방\" and evented == False and what==\"딴짓\"', event.random(.7), event.only(), priority = 10)
    event("pcroom1_bad_event1", 'morn_do==\"사이버지식정보방\" and evented == False and what==\"게임\"', event.random(.7), event.only(), priority = 10)
#pcroom1_good_event2
    event("sat_tabaevent", 'where == "토요일_담배" and sat_val <=10 and evented == False', event.random(.6), event.only(), priority = 0)
  
    event("pcroom1_normal_event2", 'evented == False and af_do==\"사이버지식정보방\"', event.random(.6), event.only(), priority = 10)
    event("pcroom1_good_event2", 'evented == False and af_do==\"사이버지식정보방\"', event.random(.3), event.only(), priority = 10)
    event("pcroom1_none_event2", 'evented == False and af_do==\"사이버지식정보방\"', priority = 100)

    event("pcroom1_good_event3", 'evented == False and night_do==\"사이버지식정보방\"', event.random(.3), event.only(), priority = 10)
    event("pcroom1_none_event3", 'evented == False and night_do==\"사이버지식정보방\"', priority = 100)

label pc_bad:
    $timeCheck(0, 20)
    "막혔던 부분은 몇 차례나 코드를 고쳐도 해결되지 않았다."
    $SoundPlayer("phone2.wav", 1.0)
    main "\[통신보안?\]"
    go "\[통신보안이고 뭐고 지금 어디십니까? {w}식사 안 하십니까?\]"
    "시계를 쳐다봤다. {w}17시 40분. {w}어찌 변명도 못할 지각이다."
    main "\[아... {w}지금 바로 갈게.\]"
    play sound sigh
    go "\[하아...{w} 제가 저번에도 말씀드리지 않았습니까? {w}아니. {w}자세한 건 나중에 하고 빨리 식당으로 오십시오.\]"
    $SoundPlayer("teleclick.ogg", 1.0)
    $stress_val += 5
    $sat_val -= 2
    main "(망할... {w}일 났네...)"
    hide main_cloth
    $SoundPlayer("running.wav", 2.0)
    scene bg_resta_front
    show go_nom at right
    show snipe_working at center
    with dissolve
    $SoundPlayer("running.wav", 2.0)
    show main_cloth at left with moveinleft
    $FaceChange("main_cloth_sal", 0.0, .5, "main_cloth")
    main "북진."
    snipe "...{w}들어가서 밥 먹어."
    $FaceChange("main_cloth", 0.0, .5, "main_cloth_sal")
    "반장님의 목소리에는 평소 섞여있던 것을 웃도는 냉랭함만이 묻어 있었다."
    main "...예."
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    play looping dish_wash
    scene bg_resta_in
    show main_cloth
    with dissolve
    "밥을 다 먹고 퇴식하는 것이. {w}두려웠다."
    "그러나 두 사람을 기다리게 하는 것이 더 바보같은 일이란 것을 경험으로 체득한 나는 밥이 입으로 들어가는 지 코로 들어가는 지 모를 정도로 빠르게 식판을 비웠다."
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_resta_in2 
    show main_cloth 
    with dissolve
    $renpy.pause(1.0)
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    stop looping
    scene bg_resta_front
    show go_nom at right
    show snipe_working at center
    with dissolve
    show main_cloth at left with dissolve
    $FaceChange("main_cloth_sal", 0.0, .5, "main_cloth")
    main "북진."
    snipe "야, ㅇㅇㅇ."
    $FaceChange("main_cloth", 0.0, .5, "main_cloth_sal")
    main "상병 ㅇㅇㅇ."
    snipe "어디 있었냐?"
    "본능적으로 느껴졌다.{w} 솔직하게 대답해야한다는 것이."
    main "사이버지식정보방에 있었습니다."
    snipe "......."
    $SoundPlayer("sigh.wav", 1.0)
    snipe "대체 왜 그러냐?"
    main "죄송합니다."
    snipe "그놈의 \'죄송합니다\' 말고. {w}난 이유를 물었는데."
    main "....... {w}잠깐 정도는 괜찮겠지... {w}라고 안일하게 생각한 것 같습니다."
    snipe "그 안일... {w}{b}그만해라.{/b} {w}내 말 알아 들었지? {w}{b}마지막 경고다.{/b}"
    main "...예."
    hide snipe_working
    $SoundPlayer("walk_slow.ogg", 2.0)
    go "이ㅇㅇ 상병님."
    main "...어."
    go "조심해 주십쇼. {w}아시지 않습니까. {w}이렇게 되면 이ㅇㅇ 상병님 혼자서 혼나고 끝날 일이 아니란 걸. {w}같이 생활관 쓰시는 다른 선임분들도 피해보시고 저도 혼납니다. {w}잘 좀 부탁드립니다."
    main "...그래..."
    hide go_nom
    $SoundPlayer("walk_slow.ogg", 2.0)
    $FaceChange("main_cloth_ang", 0.0, 1.0, "main_nom")
    main "(시X... {w}빌어먹을...)"
    $stress_val += 5
    $sat_val -= 3
    $evented = True
    $now_h = 17
    $now_m = 50
    return

label pc_good:
    "조급한 마음을 버리고 천천히 코드를 다시 살폈다."
    $timeCheck(0, 10)
    main "(어.)"
    "코드 뭉치 사이에 어처구니 없는 오타가 하나 섞여있었다."
    $SoundPlayer("typing.ogg", 3.0)
    main "(좋아... {w}이제... {w}작동해야 하는데.)"
    $SoundPlayer("enter.wav", 1.0)
    "프로그램은 문제 없이 작동했다."
    $stress_val -= 10
    main "(몇 시지? {w}...30분? {w}이런 씨...)"
    play sound running
    scene bg_hallway at run_trans
    "드라이브 업로드 버튼을 누르고 확인조차 하지 않은 채 내달렸다."
    stop sound
    scene bg_room with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at center with dissolve
    $renpy.pause(.3)
    $SoundPlayer("broadcast.wav", 2.0)
    go "\[아, 아. {w}통합중대 인원들. {w}식사 출발해 주시길 바랍니다.\]"
    show jeong_cloth at right with wipeup
    jeong "밥 먹으러 가자.{w} 오늘은 딱 맞췄네."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway 
    show go_nom at right 
    with dissolve
    show jeong_cloth at left
    show main_cloth at center
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    go "오, 오늘은 안 늦으셨습니다?"
    main "그러게. {w}오늘은 시간 맞췄네."
    go "그것 보십시오. {w}제가 할 수 있다 하지 않았습니까."
    $sat_val += 10
    hide jeong_cloth
    hide go_nom
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    play looping dish_wash
    scene bg_resta_in with dissolve
    show explain_scene with dissolve
    centered "아슬아슬하게 식사 집합에 늦지 않을 수 있었다."
    hide explain_scene with Dissolve(.5)
    go "그러고보니 ㅇㅇㅇ 상병님. {w}혹시 내일 뭐 할 일 있으십니까?"
    main "나? {w}내일 근문데. {w}말했었잖아."
    go "아 맞습니다... {w}내일이었습니다..."
    main "왜?"
    go "윤이가 금요일에 허리 다쳤던 것 때문에 의무대 진료 희망해서 말입니다. {w}다른 소대원들 전부 그날 일과 때 해야 할 거 있어서 ㅇㅇㅇ 상병님 소대 대기하시면 좀 같이 다녀와달라 하려고 했습니다."
    main "아... {w}어쩌지? {w}그날 딱 근무네..."
    go "어쩔 수 없지 않습니까. {w}제가 근무취침하기 전에 후딱 다녀와야 할 것 같습니다."
    main "괜히 미안하네."
    go "아닙니다. {w}근무가 당연히 더 우선이지 않겠습니까."
    $renpy.pause(1.0)
    jeong "그만 일어날까?"
    go "예."
    main "그래."
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_resta_in2
    show main_cloth
    show jeong_cloth at left
    show go_nom at right
    with dissolve
    $renpy.pause(1.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    stop looping
    scene bg_resta_front 
    show main_cloth
    show jeong_cloth at left
    show go_nom at right
    with dissolve
    go "그럼 있다 뵙겠습니다."
    jeong "나도 간다~"
    main "응. {w}고생해~"
    hide go_nom
    hide jeong_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    main "(하... {w}이렇게 또 하루가 끝나가는 건가...)"
    $evented = True
    $now_h = 17
    $now_m = 50
    return

label meet_gang:
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    show gang_nom at right with dissolve
    gang "계십니... {w=.3}아, ㅇㅇㅇ 상병님이셨습니까."
    main "뭐야, 주말인데 왠일로 사무실에 왔어."
    gang "지나가던 길에 불이 켜져 있길래 무슨 일 있나 싶어 와봤습니다. {w}ㅇㅇㅇ 상병님은 무슨 일이십니까."
    "사무실 소파에 앉아 가벼운 이야기를 나누었다."
    scene bg_black with blinds
    $event_result_val = renpy.random.randint(1, 100)
    scene bg_office2 
    show main_cloth at center
    if event_result_val <= 70:
        show gang_hap at right
        with blinds
        main "어, 미안하다. {w}주말에 계속 붙잡아 놨네."
        gang "아닙니다. {w}재밌었습니다. {w}고생하십시오."
        $stress_val -= 3
    elif event_result_val <= 90:
        show gang_kon at right
        main "뭐 그랬단 거지."
        gang "예... {w}고생하십시오."
        main "그래, 잘가."
    else:
        show gang_bad at right
        gang "저 혹시 죄송한데... {w}먼저 가 봐도 되겠습니까?"
        main "어? {w}아, 그래."
        gang "...고생하십시오."
        $stress_val += 5
    $renpy.pause(1.0)
    "나도 그만 갈까."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show main_cloth with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $timeCheck(0, 20)
    $evented = True

    return

label meet_jeong:
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    show jeong_cloth at right
    jeong "에효... {w}내 팔자야... {w}뭐야, 언제부터 있었어?"
    main "방금 전부터."
    jeong "주말인데 왠일이야."
    main "그냥 심심해서."
    jeong "하... {w}비문병 줄까 물어봤을 때 받으면 안 됐었는데..."
    main "뭐야? {w}일 하러 온 거야?"
    jeong "어. {w}원래 금요일날 해 놨어야 했는데 까먹은 게 하나 있어서."
    main "너도 고생하는구나..."
    $SoundPlayer("blanket.wav", 4.0)
    jeong "ㅇㅇ아."
    main "응?"
    jeong "나 지금 값 확인해야할 게 하나 있어서 지통실 다녀와야 할 거 같은데 컴퓨터 켜놓고 잠깐만 지켜줄래?"
    main "그래."
    jeong "{size=10}아 진짜 개같네... {w}그걸 왜 까먹어가지고..."
    $SoundPlayer("door.ogg", 2.0)
    hide jeong_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("computer.wav", 4.0)
    "컴퓨터의 전원을 올렸다."
    "화면이 들어오고, 육군 사이버 통합 보안 체계의 로그인 창이 팝업됐다."
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("click.ogg", .8)
    "늘상 붙잡고 씨름하던 웹사이트를 띄웠다."    
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("click.ogg", .8)
    "의자를 끌어내 그 위에 앉았다. {w}이렇게 로그인 된 창을 방치해 놓은 채 자리를 떴다가 간부님들에게 들켰다가는 또 진술서를 쓰게 될 지도 모를 일이다."
    "핸드폰 화면을 들여다보며 기다렸다."
    $renpy.pause(2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    show jeong_cloth at right with dissolve
    $SoundPlayer("door.ogg", 2.0)
    jeong "미안, 조금 늦었지?"
    main "아냐, 됐어. {w}신경쓰지 마."
    jeong "덕분에 살았다. {w}괜히 후임들한테 부탁했다가 껄끄러워질 뻔 했네."
    main "괜찮으니까 또 이런 일 생기면 그냥 바로 말해. {w}톡하거나 전화해도 되고."
    jeong "아냐, 내가 조심해서 이런 일 또 안 생기게 해야지."
    main "뭐 더 도와줄 거 있어?"
    jeong "이제 됐어. 고생해."
    main "응, 너도 고생해."
    $stress_val -= 8
    $sat_val += 5
    $SoundPlayer("door.ogg")
    hide main_cloth 
    $SoundPlayer("walk_slow.ogg")
    scene bg_hallway
    show main_cloth
    with dissolve
    $evented = True    
    $timeCheck(0, 20)   
    return

label none:
    if where == "CSCO 행정반":
        hide main_cloth
        $SoundPlayer("walk_slow.ogg", 2.0)
        scene bg_office3
        $SoundPlayer("door.ogg", 2.0)
        show main_cloth at center with dissolve
        $SoundPlayer("door.ogg", 2.0)
    elif where == "휴게실":
        $SoundPlayer("door.ogg", 2.0)
        show main_cloth with dissolve
        $SoundPlayer("door.ogg", 2.0)
    "[where]에는 아무도 없는 것 같다... {w}휴대폰을 만지며 시간을 때웠다."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show main_cloth
    with dissolve
    $timeCheck(0, 20)
    return

label hq_event1:
    main "아무도 없나?"
    show prf_cloth_nem at right with wipeup
    prf "누구십니까?"
    main "어 씨, 깜짝이야."
    $FaceChange("prf_cloth_nom", 2.0, 1.0, "prf_cloth_nem")
    prf "어우, 죄송합니다. {w}깜빡 졸았습니다."
    main "왜 하필 여기서 졸고 있어?"
    prf "애들 티비 본다 그래서 왔다가 식곤증으로 뻗은 것 같습니다. {w}죄송합니다."
    main "뭐... {w}그럴 수도 있지. {w}딱히 타박하려고 그런 건 아냐. {w}궁금해서."
    prf "뭐하고 계셨습니까?"
    main "그냥 왔다갔다."
    prf "혹시 할 거 있으십니까?"
    main "딱히 없는데."
    prf "사지방 안 가십니까?"
    main "좀 있다가."
    prf "오, 왠일이십니까? {w}매일 주말마다 사지방에 가서 잘 안 나오시지 않았습니까."
    main "그냥."
    prf "아~ {w}오늘 근무취침이라 이제 일어나신 겁니까?"
    main "아니? {w}점심도 먹었는데?"
    prf "하실 일 당장 없다 그러시지 않았습니까?"
    main "응."
    $FaceChange("prf_cloth_hap", 2.0, 1.0, "prf_cloth_nom")
    prf "그럼 저랑 같이 운동가십니까?"
    main "나 지금 다리 다쳤는데."
    prf "고균영 상병한테 들었습니다. {w}이제 꽤 괜찮아져서 체력단련이나 일과에 전혀 지장없다고 말씀하셨다고."
    $FaceChange("main_cloth_ser", 1.0, 1.0, "main_cloth")
    main "(아 씨... {w}고균영... {w}하....)"
    $FaceChange("prf_cloth_nom", 2.0, 1.0, "prf_cloth_nem")
    prf "뭐, 농담입니다."
    $FaceChange("main_cloth", 1.0, 1.0, "main_cloth_ser")
    main "식겁했네. {w}네가 그런 말 하면 농담인지 진담인지 구분 안된다고."
    prf "무릎은 좀 괜찮으십니까?"
    main "군의관님 말로는 무릎 꿇고 앉지 말고 쪼그려 앉지 말고 계단 한꺼번에 오르지 말고 약 꾸준히 먹으면 2~3달이면 낫는데."
    prf "그런데 매일 그러시지 않습니까. {w}약도 잘 안 드시지 않습니까."
    main "그렇지. {w}근데 내가 선수급으로 운동을 하는 것도 아니고 도리여 망부석에 가까우니까. {w}나가면 저절로 낫겠지."
    prf "조심하셔야 합니다. {w}무릎이랑 치아는 평생 간다는 말도 있지 않습니까."
    main "처음 들어보는데?"
    prf "제가 한 말이니까 말입니다."
    main "허."
    prf "ㅇㅇㅇ 상병님 원래 컴퓨터 쪽 일하시지 않았습니까?"
    main "일을 한 건 아니고, 배운거지. {w}혼자서 깔짝대거나."
    prf "운동해서 건강해지면 좋지만 선수도 아니면서 제몸 깎아먹기 식 운동은 자재하시는 편이 좋습니다."
    main "나 운동 그다지 열심히 안했는데."
    prf "어... 그렇습니까? {w}아무튼 약이야 먹으면 부작용 오는 거 때문에 잘 안 먹는다고 치더라도 군의관님이 하지 말라고 하신건 안 하시는 게 맞을 것 같습니다."
    main "그래, 고맙다. {w}내 몸 걱정해주는 건 너밖에 없네."
    prf "제가 또 대대 체력단련병이지 않겠습니까."
    "시시콜콜한 잡담들을 나누었다."
    main "나 간다."
    prf "고생하십시오."
    $SoundPlayer("door.ogg")
    scene bg_hallway 
    show main_cloth with dissolve
    $stress_val -= 5
    $sat_val += 5
    $timeCheck(0, 20)
    $evented = True

    return

label sniper_hq:
    main "아무도 안 계십니까?"
    snipe "나 있다."
    show snipe_working at right with dissolve
    $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
    main "북진."
    snipe "왜 왔어?"
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
    main "밖에서 보기에는 아무도 없는데 불이 켜져 있길래 끄러 왔습니다."
    snipe "내가 끄고 갈게. {w}마침 잘 됐네. {w}이리 와서 앉아 봐."
    main "예..."
    snipe "요즘 좀 어떠냐? {w}지낼만 하냐?"
    main "예. {w}다들 잘 대해 줘서 편히 지내고 있습니다."
    snipe "그래?"
    "저격반장님은 가볍게 숨을 내쉬더니 입을 여셨다."
    scene bg_black with blinds
    $event_result_val = renpy.random.randint(1, 100)
    scene bg_office
    show main_cloth at center
    show snipe_working at right
    with blinds
    snipe "알아 들었냐?"
    main "네. {w}더 분발토록 하겠습니다."
    main "그래."
    $FaceChange("main_salute", 1.0, .5, "main_cloth")
    main "북진. {w}고생하십시오."
    $FaceChange("main_cloth", 1.0, .5, "main_salute")
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    if event_result_val <= 50:
        show main_cloth 
        with dissolve
        $SoundPlayer("door.ogg", 2.0)
        "저격반장님은 역시 언제나 엄하셨다. {w}허나, 그 모든 언행이 중대원들을 생각하고, 더 나은 방향으로 인도하기 위한 것임은 이 잠깐의 대화를 통해서도 충분히 알 수 있었다."
        $stress_val -= 5
        $sat_val -= 5
    else:
        show main_cloth_ang
        with dissolve
        $SoundPlayer("door.ogg", 2.0)
        "알고 있었다. {w}저격반장님은 나를 더 좋게 이끌어 주기 위해서 혼을 내셨단 것을. {w}그러나..."
        $SoundPlayer("sigh.wav", 2.0)
        main "(x같네...)"
        "감정을 가다듬었다. {w}심호흡했다. {w}애써 생각했다. {w}이 또한 필요한 일이다. {w}멍청하고, 다른 누구보다 지금 서 있는 이 장소에 어울리지 않는 내가 동화되기 위해서는 엄히 서 꾸중하는 이 역시 있어야 한다. {w}고 되뇌이자 흐트러졌던 호흡도. {w}일그러져가던 생각도 바로잡혔다."
        main "(망할... {w}나같은 놈 때문에...)"
        $stress_val += 5
        $sat_val -= 10
    $timeCheck(0, 20)
    $evented = True
    return 
    
label washing_room1:
    $SoundPlayer("broadcast.wav", 2.0)
    "당직사령" "후후, 지휘통제실에서 당직사령이 전파합니다. {w}막사 내에 통신소대 통신병 인원 한 명만 지휘통제실로 와 주시면 감사하겠습니다. {w}다시 한 번 전파드립니다. {w}막사 내의 통신소대 통신병 인원 한 명만 지휘통제실로 와 주시면 감사하겠습니다."
    "본능적으로 몸이 반응했다."
    hide main_cloth
    $SoundPlayer("running.wav", 2.0)
    scene bg_zitong 
    show cap2_working
    with dissolve
    $SoundPlayer("knock.ogg", 1.0)
    main "본부중대 상병 ㅇㅇㅇ입니다. {w}잠시 들어가도 되겠습니까?"
    cap2 "어, 들어와."
    $SoundPlayer("door.ogg")
    show main_cloth at left with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $FaceChange("main_cloth_sal", 0.0, .5, "main_cloth")
    main "북진."
    cap2 "그래... {w}네가 왔구나?"
    $FaceChange("main_cloth", 0.0, .5, "main_cloth_sal")
    main "무엇이 안되고 있습니까?"
    show sol2_nom at right with dissolve
    "상황병" "탄약고 고가초소 전술 전화기가 안된다고 합니다."
    main "선은 확인해 보셨습니까?"
    cap2 "근무자들 말에 의하면 이상 없데."
    main "아... {w}아마도 전술전화기에 들어가는 건전지가 약아 다 된 것 같습니다."
    cap2 "언제 갈았는데?"
    main "상황병님?"
    $SoundPlayer("typing.ogg", 1.0)
    "상황병" "상황일지에는 지난 달 초에 교체했다고 나와 있습니다."
    cap2 "이상하다... {w}이렇게 빨리 닳나?"
    main "쓰다 남은 게 섞여 들어갔을 수도 있을 것 같습니다. {w}가서 후딱 교체해주고 오겠습니다. {w}혹시 건전지 있습니까?"
    cap2 "없는데..."
    main "그럼 소대에 있는걸로 갈아주면 됩니다. {w}다녀오겠습니다."
    cap2 "그래."
    $FaceChange("main_cloth_sal", 0.0, .5, "main_cloth")
    main "북진. {w}고생하십시오."
    $FaceChange("main_cloth", 0.0, .5, "main_cloth_sal")
    scene bg_black with blinds
    "상황병" "예, 이상 없이 잘 들립니다."
    main "네, 감사합니다."
    $SoundPlayer("teleclick.ogg", 1.0)    
    scene bg_tan
    show sol_nom at right 
    show main_cloth at center
    with blinds
    main "해결되었습니다. {w}대부분의 경우 안에 들어가는 건전지가 말썽인 경우가 많으니 중대에도 전파해 주시면 감사하겠습니다."
    "초병" "예, 감사합니다."
    scene bg_black with blinds
    $renpy.pause(2.0)
    scene bg_zitong
    show cap2_working at center
    show main_cloth at left
    show sol2_nom at right
    with blinds
    cap2 "이야, ㅇㅇ아. {w}덕분에 잘 된다. {w}주말에 갑자기 일 시켜서 미안."
    main "아닙니다. {w}통신소대원이니까 해야할 일이지 않겠습니까."
    cap2 "고생했다."
    $FaceChange("main_cloth_sal", 0.0, .5, "main_cloth")
    main "북진. {w}근무 고생하십시오."
    $FaceChange("main_cloth", 0.0, .5, "main_cloth_sal")
    $SoundPlayer("door.ogg")
    scene bg_hallway 
    show main_cloth
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    "혹시 모를 상황은 벌어지지 않았다. {w}전술 전화기에 들어가 있던 건전지 중 하나가 완전히 방전되어 있었고, 이를 소대 사무실에서 꺼내온 새 것으로 교체하자 방금 전까지의 불통이 거짓말이었던 것처럼 상황병의 목소리가 송수화기 너머에서 들려왔다."
    $stress_val -= 7
    $sat_val += 7
    $timeCheck(0, 20)
    $evented = True
    return

label csco1:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_room
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("blanket.wav", 4.0)
    "사 두었던 콜라를 집어 들었다."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway 
    show main_cloth
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_office3
    show main_cloth at left
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    main "균영아."
    go "부르셨습니까?"
    show go_nom at center with dissolve
    $SoundPlayer("put.ogg", 1.0)
    "가져온 콜라를 책상 위에 올렸다."
    main "마시면서 하라고."
    go "아, 감사합니다. {w}마침 목말랐는데 잘 마시겠습니다."
    $SoundPlayer("coke.wav", 1.0) 
    $SoundPlayer("drink.wav", 1.0)
    go "요즘은 좀 어떠십니까. {w}지낼만 하십니까?"
    main "그렇지."
    go "그래도 와 보니까 좋지 않습니까? {w}화기애애하고."
    main "그러게..."
    "머릿속을 스쳐 지나가는 과거의 이야기. {w}반목, 싸움, 결별."
    main "{size=15}적어도 맞을 일은 없어서 좋네.{/size}"
    go "몸은 괜찮아졌습니까?"
    main "며칠 전에도 말했지만 이제 일상생활에 지장은 없어. {w}조금만 조심하면 돼."
    go "그래도 아프시면 바로 말씀해 주셔야 합니다. {w}괜히 참으시지 말고."
    main "응. {w}알았어."
    #"입이, 떨어지지, 않았다. {w}준비했던 문장을 이루는 단어들이 머릿속을 복잡히 휘저었다."
    #"솔직히 말해 두려웠다. {w}내가 했떤 말실수. {w}6월달. {w}중대 격리 도중. {w}밥을 먹고 돌아오는 길의 철볼."
    #"내 한 마디 말 실수 탓에 내 군생활은 거대한 변혁을 맞이했고. {w}그대로 바닥으로 추락해 내려가기 시작했다. {w}똑같은 일이 벌어질지도 모른다."
    #main "(그래도... 해야겠지...)"
    #main "있잖아."
    #go "왜 그러십니까?"
    #"보가 무너졌다. {w}멈출 수도 없고. {w}멈춰서도 안 된다."
    #main "너도 알고 있겠지만 내가 그렇게 좋은 선임은 아니잖아."
    #go "......."
    #main "나도 알고 있어. {w}이전에는 하지 않았던 새로운 일이라고는 해도 전입온 지 두 달 넘게 지났는데 아직도 적응 못하고 후임들도 안 내는 빵꾸만 뻥뻥 터뜨려 대고 있따는 걸. {w}넌 내 분대장이기도 하고 또래 상담병이기도 하니까 그냥 솔직하게 이야기 할게. {w}갓 전입왔을 때 말했으니까 너도 알고 있겠지만은 내가 평소에 앓고 있는 병이 하나 있어. {w}그것 때문에 "
    $event_result_val = renpy.random.randint(1, 100)
    "처음에는 건강 이야기. {w}그 이후에는 1중대 시절 이야기. {w}그 다음으로는 균영이의 이야기. {w}겉으로 보기에는 다가서기 힘들고 언제나 화나 있어 보이는 무서운 분대장이었던 균영이."
    main "이렇게 길게 이야기 해 본 적 있었나?"
    go "없었던 걸로 기억합니다. {w}그래도 이걸로 ㅇㅇㅇ 상병님에 대해서 이전보다는 조금 더 알게 된 것 같습니다."
    main "나도 너에 대해서 더 알게 된 것 같아서 기분 좋네."
    if event_result_val <= 30:
        "굳어 있던 마음이 조금은 풀리는 것 같았다. {w}그리운 얼굴들이 겹쳐 보였다. {w}지금은 떠나버린 간부님들이. {w}선임들이 나와 이야기를 나눌 때. {w}고민을 털어 놓고서 조언을 구했을 때와 같은. {w}따스함이 이 곳에서도 다시금 느껴졌다."
        $stress_val -= 10
        $sat_val += 7
    elif event_result_val < 70:
        "털어놓자 무겁게만 느껴졌던 매일이 조금은 가벼워진 것 같았다. {w}균영이는 지겨운 내 이야기를 끝까지 들어주었고. {w}이에 공감하는 척이라도 해 주었다. {w}누군가는 나를 타인을 나의 감정 쓰래기통으로 이용하고 있다고. {w}이기적이라 몰아붙일지도 모를 일이다." 
        "그러나. {w}이 맘 속에 품은 채 때를 지나 썩어가는 감정 더미와. {w}소중한 사람에게 꼭 전해야 했으나. {w}때가 늦어 건내지 못했던 감사의 잔여물들은 지금까지도 차곡차곡 쌓여 벗어 던질 수 없는 짐덩이가 되어버린 상태였다."
        main "(미안하다. {w}하지만 이렇게라도 하지 않으면... {w}진짜 미쳐버릴 거 같아...)"
    else:
        "균영이는 무표정히 컴퓨터 화면을 바라보고 있다."
        $SoundPlayer("typing.ogg", 2.0)
        go "아...{w} 정말 죄송합니다. {w}계속 해야할게 밀려들어 와서... {w}그래도 ㅇㅇㅇ 상병님께서는 언제나 노력하고 계시지 않습니까. {w}그 노력이 언젠가는 결실을 맺을거라고 저는 생각하고 있습니다."
        main "그래, 고맙다."
    main "고생해라."
    go "고생하십시오. {w}화이팅입니다."
    hide main_cloth
    $SoundPlayer("door.ogg")
    scene bg_hallway 
    show main_cloth at center
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $timeCheck(0, 20)
    $evented = True
    return

label lounge_event1:
    play music guitar1
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth with dissolve
    $SoundPlayer("door.ogg", 2.0)
    "기타 소리."    
    show son_guitar at right with dissolve
    $renpy.pause(1.0)
    stop music
    son "안녕하세요."
    main "어, 한연 씨 기타 치셨어요?"
    son "옛날에요. {w}오랜만에 다시 잡아봤는데 기억이 잘 안 나네요."
    main "좀 더 쳐줄 수 있어요?"
    son "아까 전에 그거 처음부터 다시 쳐드릴게요 그럼."
    play music guitar1
    $renpy.pause(2.0)
    main "이거 혹시 제목이 뭔가요?"
    son "글쎄요... {w}어릴 때 하도 연습해서 손에 익은 거라 제목은 까먹어 버렸네요."
    $renpy.pause(30.0)
    stop music fadeout 1.0
    main "되게 잘 치시네요."
    son "아니에요. {w}아, 그러고보니 ㅇㅇ 씨도 옛날에 악기 했다고 하지 않았던가요?"
    main "예... {w}뭐. {w}바이올린 약간 했었어요."
    son "얼마나요?"
    main "제대로 했던 건... 초2때부터니까... 한 4년? 쯤 되네요."
    son "그 이후론 안 했어요?"
    main "가끔 음악 수업 수행평가 할 때 잡아본 이후론 거의요."
    son "바이올린이라... {w}멋있네요."
    main "인제는 하라고 해도 못할 걸요. {w}아마."
    "한연 씨와 악기 이야기를 나누었다."
    scene bg_lounge
    show main_cloth at center
    show son_guitar at right
    with blinds
    son "그럼 그 이후로는 쭉?"
    main "예... 뭐... {w}이런저런 핑계만 대면서 안 잡았었죠. {w}1중대 있었을 때 중대 단체 휴가 나갔다가 격리됐을 때 후임이 갖다 놓은 바이올린을 켜보긴 했지만... {w}오래 안 했으니까요."
    $SoundPlayer("blanket.wav", 4.0)
    son "일어나시려고요?"
    main "예."
    son "푹 쉬세요."
    main "한연 씨도요."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show main_cloth 
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    main "바이올린이라..."
    "초등학교 때. {w}다니던 피아노 학원의 선생님이 바이올린을 배우기 시작한 것을 계기로 나는 활을 잡았었다."
    "내 초등학교 때에서 바이올린이 차지한 지분은 결코 적지 않을 것이다."
    "하지만 그게 무슨 소용일까. {w}바이올린을 손에서 놓은 것은 나였고. {w}오랫동안 쓰지 않은 손의 근육은 뻣뻣히 굳었다. {w}재봉실 두께만큼의 재능조차 가지지 못한 내가 노력 비스무리한 것조차 하지 않았으니."
    "자연스럽게 옛날 같은 일을 하는 건. {w}...{w}무리겠지."
    "피식, 웃음이 나왔다."
    "그렇게 좋아하고. {w}자랑스러워했던 일인데. {w}졸업과 동시에 얄팍한 끈이 끊어지며 언제 그랬냐는 듯 나는 하드 케이스를 벽에 내팽게친 채 열어보지 않았다."
    "바니쉬가 발린. {w}나무색으로 반짝이던 바이올린의 본체도. {w}브릿지도, 지판도. {w}눈 앞에 놓인 보면대와 그 위에 놓인 악보도. {w}지휘봉이 휘둘러지는 그 순간을 기다리며 바라봤던 지휘자도."
    "나는 한 순간에 기억 한 구석에 처박은 채 떠올리지 않았다."
    "\'우상\'이. {w}\'닮고픈 모습\'이. {w}\'바램\'이. {w}없어졌기 때문에."
    "그랬던 \'나\'다. {w}그런 \'나\'다. {w}그럴 \'나\'이다."
    "훈련소에서부터 시작되어 벌써 1년. {w}국가에서 정의한. {w}의무라는 이름의 족쇄를 차고 하루하루를 살아왔다."
    "그러나 지금. {w}졸업했던 그 때와 마찬가지로. {w}내가 뒤쫒았던 그림자가. {w}뙤약볕 아래 서 있을 때 찾아 들어갈 수 있었던 그늘이. {w}그리고 언제나 내 앞에 서서 나아가며 내가 떨고 있을 때 슬쩍 내밀어지던 손이. {w}사라진. {w}아니, 그 모든 것을 잃어버린 이 날에."
    "시작되었을 때는 자그마한 얼룩이었던 것이. {w}내쫒을 수 있었던. {w}그저 꾸물이다 내가 미는 대로 떠밀리던 한낱 점에 불과했던 그것이. {w}이제 와서는 눈을 돌리기조차 힘들 거대한 늪이 되어 있었다."
    "다리를 휘감긴 채 서서히 빠져들면서도 헤엄쳐 빠져나올 생각조차 하지 않은 채 가만히 서서 밑바닥까지 삼켜져 가는 와중."
    "저항할 의지도. {w}노력도. {w}끌어내지 못할 만큼 너덜너덜해져."
    main "(x신 같은 새x... {w}이런 때까지도... {w}자기합리화냐.)"
    scene bg_black with dissolve
    $blur_val = True
    centered "{size=50}{color=#B90000}쓰래기처럼 살아온 나는."
    centered "{size=50}{color=#B90000}매일매일 습관처럼 죽고싶다는 말을 지분대는 나는."
    centered "{size=50}{color=#B90000}그런 용기 따위는 어디에도 없는 나는."
    centered "{size=50}{color=#B90000}어째서 태어나고."
    centered "{size=50}{color=#B90000}어째서 살아가는 걸까."
    $blur_val = False
    show why with vpunch
    play sound scream
    show blood at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood2 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood3 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood4 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood5 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood6 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood7 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood8 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood9 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood10 at Position(xpos=renpy.random.randint(200, 1000), ypos=renpy.random.randint(20, 700)) with vpunch
    $renpy.pause(.5)
    show blood_2 with vpunch
    $renpy.pause(1.0)
    stop sound
    $sat_val -= 10
    scene bg_hallway
    show main_cloth 
    with Dissolve(2.0)
    $timeCheck(0, 20)
    $evented = True
    return

label day2_novel1:
    $SoundPlayer("walk_slow.ogg", 2.0)
    show tie_nom at center with dissolve
    tie "뭐 읽어?"
    main "빨간머리 앤입니다."
    tie "요즘엔 그렇게 조그만 버전도 있나 보네. {w}어린이 용처럼 내용을 줄인 건가?"
    main "그건 아니라고 알고 있습니다. {w}이게 책 크기가 이런 만큼 글자도 작아서 이렇게 밝은 곳 아니면 거의 못 읽습니다."
    tie "눈 안 아파?"
    main "안경 안 끼고 있어서 괜찮습니다."
    tie "그러고 보니까 너 안경은 어쨌어?"
    main "제가 시력은 그럭저럭 괜찮은데 난시가 심한 거라 자꾸 움직이거나 멀리 떨어진 거 볼 때 아니면 괜찮습니다. {w}그리고 무엇보다 저번에 병영생활지도 했을 때 든 멍이 아직 안 없어져서 안경 쓰면 아픕니다."
    tie "맞다, 그건 어떻게 됐어? {w}괜찮데?"
    main "예. {w}괜찮습니다. {w}군의관님께 여쭸더니 그냥 가만히 내버려두면 낫는다고 합니다."
    tie "진짜 그때 엄청 놀랐는데."
    main "솔직히 저도 놀랐습니다."
    tie "야삽을 쓰다가 손이나 발 같은 데를 찍어서 다친 사람은 봤어도 군장에서 떨어진 야삽에 맞아서 귀에 멍이 들었다니. {w}들어 본 적도 없어."
    main "하하..."
    "아무런 통증도 없던 왼쪽 귀가 저릿거리기 시작했다."
    tie "어쩌다 그렇게 된 거야?"
    main "군장피가 벗겨졌길래 다시 끼우려고 군장을 내리다가 제대로 안 여며 놔서 안에 있는 야삽이 머리로 떨어지길래 피한 것까진 좋았는데..."
    tie "덜 피해서 귀에 맞았다?"
    main "예, 그렇습니다."
    tie "그게 뭐야. {w}피하면 피한 거고 못 피했으면 못 한 거지 덜 피할 수가 있나?"
    main "관물대와 침대 사이에서 내리고 있었어서 관물대에 머리 안 박으려고 살짝만 틀었는데 부족했나 봅니다."
    tie "그런 상황이면 보통 뒤로 빠지거나 앞으로 후딱 나가잖아."
    main "왜 거기서 옆으로 피한다는 발상을 했는지 저도 의문입니다. {w}진짜 귀가 찢어지는 줄 알았습니다."
    $FaceChange("tie_smi", 1.0, 1.0, "tie_nom")
    tie "너 그때 쓰러져서 지휘통제실에 들릴 만큼 크게 소리질렀던 거 알아? {w}진짜 나는 초소 근무자들이 실수로 공포탄이라도 격발한 줄 알았어."
    $FaceChange("main_unhat_sha", 2.0, 1.0, "main_unhat")
    main "진... 진짜입니까?"
    tie "그러니까 내가 곧바로 뛰어갔지. {w}뭐, 내가 갔을 때는 이미 본부중대장님이 조치를 취해주고 계셨지만. {w}아무 말도 못하고 끅, 끅 거리면서 바닥을 기고 있는데 진짜 뭔가 했다."
    main "으으..."
    tie "부끄러워? {w}사람이 살다 보면 그럴 수도 있지. {w}뭐 이런 거 가지고 부끄러워하고 그래."
    "책 글자 하나 하나에 집중하려 했다. {w}얼굴에서 전해지는 열기가 정신을 흐뜨러뜨리려 했지만. {w}이내 손가락에서 느껴지는 종이의 감촉과 문장에서 전해지는 감정이 다른 모든 자극을 차단하기 시작했다."
    $stress_val -= 5 
    $timeCheck(0, 2.0)
    $evented=True
    $what = "부상의 이유"
    $what_all_list.append(what)
    return 

label day2_novel2:
    $SoundPlayer("knock.ogg")
    $SoundPlayer("door.ogg", 2.0)
    show jeong_salute at center with dissolve
    jeong "북진. {w}병장 [jeong] 지휘통제실에 용무 있어 왔습니다."
    $FaceChange("jeong_nom", 1.0, .5, "jeong_salute")
    $SoundPlayer("walk_slow.ogg", 2.0)
    jeong "ㅇㅇ."
    main "엉?"
    jeong "대대 내부망 CEOI 종이 좀 빌려주라."
    main "갑자기?"
    jeong "이번에 간부님들 편제장비 시험 보시잖아. {w}예시로 들만한 실제 제원이 필요하데."
    main "아 그래서 대대망?"
    jeong "응. {w}군단 예하 부대가 전부 공유하는 무전망을 간부님들 연습하실 때 쓸 순 없잖아."
    main "상황간부님 허락은?"
    jeong "아까 중대장님이 전화해서 허가 받았어. {w}뭣하면 물어보지 그래?"
    main "정훈장교님?"
    show tie_nom at left with dissolve
    tie "어~ {w}아까 전에 본부중대장님께 전화 왔었어. {w}주면 돼."
    hide tie_nom 
    $SoundPlayer("blanket.wav", 4.0)
    "음어낭에서 종이를 꺼내 건냈다."
    main "고생하쇼."
    tie "너도 고생해~"
    $FaceChange("jeong_salute", 1.0, .5, "jeong_nom")
    jeong "북진. {w}용무 마치고 복귀하겠습니다."
    $FaceChange("jeong_nom", 1.0, .5, "jeong_salute")
    $renpy.pause(.5)
    hide jeong_nom
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    main "(편제장비라... {w}벌써 시간이 그렇게 됐나...)"
    "분기에 한 번 있는 간부님들의 자격 평가. {w}시간은 유수같이 흘러 어느덧 내가 본래 있었던 곳에서 떠난 지 3개월의 시간이 지나 버렸다."
    main "(이쯤되면 완전히... {w}바뀌어 버린 거겠지.)"
    "\'돌아가고 싶다\'. {w}동시에 \'도망치고 싶다\'. {w}내 옛 둥지는 내 심상 속에서 언제나 그리움의 온상이었으며. {w}전력으로 멀어져야 할 곪은 대지였다."
    "후회와, 아쉬움과, 참회와 동시에. {w}내 안에 잔류한 것. {w}품어서는 아니 될 허락되지 못한 감정."
    $FaceChange("main_ang", 2.0, 1.0, "main_atten")
    main "(하아... {w}개x신 같은 놈... {w}남탓하는 것 말고는... {w}할 줄 아는게 없지, 그래...)"
    $stress_val += 5
    $timeCheck(0, 20)
    $evented=True
    $what = "편제장비"
    $what_all_list.append(what)
    return 

label day2_novel3:
    $SoundPlayer("telering.wav", 1.5)
    $SoundPlayer("teleclick.ogg", 1.0)
    main "\[통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다.\]"
    pl3 "\[ㅇㅇ아. {w}나야 나.\]"
    $FaceChange("main_hap", 2.0, 1.0, "main_atten")
    main "\[소대장님!\]"
    pl3 "\[잘 지냈어?\]"
    main "\[예, 잘 지내고 있습니다. {w}소대장님께서도 잘 지내고 계십니까?\]"
    pl3 "\[나야 잘 지내지. {w}혹시 금요일날 어디가 5대기 투입했는지 알고 있어?\]"
    main "\[1중대 2소대입니다.\]"
    pl3 "\[지휘조장은?\]"
    main "\[2소대장입니다.\]"
    pl3 "\[오케, 알겠어.{w} 땡큐~ {w}고생해~\]"
    main "\[북진! {w}고생하십시오!\]"
    $SoundPlayer("teleclick.ogg", 1.0)
    show tie_nom at center with dissolve
    tie "누구 전화길래 그렇게 얼굴에 화색이 돌아?"
    main "3소대... {w}아니, ◇◇대대 작전장교님입니다."
    tie "아~ {w}너 원래 3소대였지?"
    main "예. {w}[pl3] 중위님 밑에서 9개월 정도 있었습니다."
    tie "표정이 활짝 필만 하구만. {w}무슨 이야기 했는데?"
    $FaceChange("main_unhat", 2.0, 1.0, "main_hap")
    main "금요일날 바뀐 5대기 투입한 소대랑 지휘조장 여쭤보셨습니다."
    tie "5대기? {w}◇◇대대에서 5대기를 왜 물어보지?"
    main "이번에 지휘검열 때문에 아닙니까? {w}ㅇㅇ대대가 작전 나가면 ◇◇대대가 5대기를 맡아주지 않습니까. {w}어쩌면 거기까지 훈련 내용에 포함되어 있을지도 모릅니다."
    tie "그런가? {w}그런 내용은 못 봤는데."
    main "어, 점검표 나왔습니까?"
    tie "나온 지 꽤 됐는데."
    main "보여주실 수 있습니까?" 
    tie "봐서 뭐하게?"
    main "이번 지휘검열 때 상황 근무를 처음으로 맡게 되서 불안합니다. {w}점검표를 보면 좀 괜찮아지지 않을까 싶어서 말입니다."
    tie "별 거 없어. {w}여기."
    "점검표를 훑어보았다."
    main "이번에도 소산진지 가는 겁니까?"
    tie "응. {w}근데 어차피 넌 근무라서 안 가잖아."
    main "1중대 사람들 고생 좀 할 것 같습니다. {w}작년 지휘검열 때는 1중대였으니까 저도 갔었는데... {w}어우, 그 때 생각만 하면 아찔합니다."
    tie "많이 힘들었어?"
    main "완전군장 한 것까지는 힘들고 말 정도였는데 꽈리고개를 넘고 공중강습 훈련장에서 갑자기 화생방 상황이 터졌었습니다."
    tie "켁. {w}작년 9월이면 덥기도 덥고 습도도 엄청 높았던 걸로 기억하는데."
    main "예... {w}화생방 보호의에 방독면에... {w}아으... {w}전투준비태세 점검이 끝나고 막사 돌아와서 씻는데 땀띠 때문에 한 2~3일은 고생했었습니다."
    tie "생각만 해도 고통스럽다, 야."
    main "그래도 이번엔 온도도 습도도 그렇게 안 높아서 다행입니다."
    tie "작년이 미쳤던 거지 뭐."
    main "하긴 그렇습니다. {w}저도 21년 살면서 그렇게 비 많이 오는 건 처음 봤습니다."
    tie "21년? {w}너 21살이야?"
    main "예."
    tie "와... {w}20살에 입대한 거네."
    main "할 게 없어서 말입니다. {w}20년 대구 코로나 범유행 기억나십니까?"
    tie "어, 기억 나."
    main "거기랑 제가 살던 곳이랑 꽤 가까워서 외부활동을 아예 못하게 되버리는 바람에 이 참에 후딱 군대 갔다와야겠다 싶어서 바로 입대했습니다."
    tie "입대하기 힘들었을텐데 용케 자리 찾았다?"
    main "그때는 몰랐습니다... {w}무선장비운용이 전투병과일지... {w}빨간색 글씨가 제 전공이라 관련있는 주특기인지..."
    tie "좀 천천히 알아보지 그랬어."
    main "그러게나 말입니다... {w}그때로 돌아가서 제 손목을 분질러 버리고 싶습니다."
    $evented=True 
    $timeCheck(0, 2.0)
    $stress_val -= 5
    $sat_val += 10
    $what_all_list.append(what)
    return

label day2_study_specialty1:
    $SoundPlayer("click.ogg", 1.0)
    main "(전술무전기는... 됐고... {w}위치전송 단말기... 위치전송 단말기가...)"
    $SoundPlayer("click.ogg", 1.0)
    main "......."
    $SoundPlayer("click.ogg", 1.0)
    $SoundPlayer("knock.ogg", 1.0)
    $SoundPlayer("door.ogg", 2.0)
    show go_uw_salute at center with dissolve
    go "북진. {w}상병 [go] 지휘통제실에 용무 있어 왔습니다."
    $FaceChange("go_uw_atten", 1.0, .5, "go_uw_salute")
    $SoundPlayer("walk_slow.ogg", 2.0)
    go "ㅇㅇㅇ 상병님."
    main "엉?"
    go "뭐하십니까?"
    main "교범 보는데."
    go "엇, 공부 중이셨습니까?"
    main "그렇지."
    go "무슨 교범입니까?"
    main "위치전송단말기. {w}복귀?"
    go "예. {w}윤이랑 저 의무대 복귀입니다."
    main "군의관님이 뭐라셔?"
    go "격한 운동 자제하고 2~3일 파스 붙이고 있으면 낫는답니다."
    main "크게 다친 건 아닌가 보네. {w}다행이다."
    go "근무 고생하십시오. {w}전 이제 씻으러 가 봐야겠습니다."
    main "그래, 잘 자."
    go "고생하십쇼~"
    $FaceChange("go_uw_salute", 1.0, .5, "go_uw_atten")
    go "북진! {w}상병 [go] 용무 마치고 복귀하겠습니다."
    $FaceChange("go_uw_atten", 1.0, .5, "go_uw_salute")
    $renpy.pause(.5)
    hide go_uw_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("click.ogg", 1.0)
    $SoundPlayer("click.ogg", 1.0)
    $renpy.pause(2.0)
    $timeCheck(0, 20)
    $evented = True
    $what_all_list.append(what)
    return

label day2_study_specialty2:
    $SoundPlayer("click.ogg", 1.0)
    main "(전술무전기는... 됐고... {w}위치전송 단말기... 위치전송 단말기가...)"
    $SoundPlayer("click.ogg", 1.0)
    main "......."
    "대대 내에서 위치전송단말기는 오랫동안 거의 쓰이지 않았다. {w}기껏해야 지휘통제실에 상황병 자리에 설치된 게 고작일까."
    "5대기 통신병이 지녀야 할 물품이긴 했지만 전원이 켜지는 일 없이 공격배낭 안쪽에 잠들어 있던 단말기를 돌연 실사용하라는 지침이 하달되었었다."
    "통신소대에 각 중대의 소대통신병들이 모여 들었던 위치단말기 사용법 교육. {w}나름 경청했음에도 투입 이후 많은 문제들에 직면해야만 했다."
    "근무 도중. {w}혹은 훈련 도중에 어떤 돌발상황이 생기더라도 남의 도움을 받지 않고 해결할 수 있을 정도의 지식을 쌓아 둔다면 그 때 같은 대참사는 터지지 않겠지."
    $SoundPlayer("click.ogg", 1.0)
    $SoundPlayer("click.ogg", 1.0)
    $renpy.pause(2.0)
    $stress_val -= 5
    $sat_val += 5
    $timeCheck(0, 20)
    $evented = True
    $what_all_list.append(what)
    return

label day2_study_specialty3:
    $SoundPlayer("telering.wav", 1.5)
    $SoundPlayer("teleclick.ogg", 1.0)
    main "\[통신보안 ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다.\]"
    gang "\[ㅇㅇㅇ 상병님? {w}저 민준입니다. {w}소대장님께서 저랑 근무교대하고 잠깐 사무실로 와달라 하시는데 지금 가면 되겠습니까?\]"
    main "\[소대장님께서?\]"
    gang "\[예.\]"
    main "\[뭐지... {w}어. {w}빨리 와.\]"
    main "정훈장교님?"
    show tie_nom at center with dissolve
    tie "왜 불러?"
    main "통신소대장이 절 호출해서 가 봐야 할 것 같습니다. {w}저 대신해서 민준이가 와서 근무 맡아 준다고 하는데 다녀와도 되겠습니까?"
    tie "어 그래. {w}민준이 오면 인수인계하고 후딱 갔다 와."
    $SoundPlayer("running.wav", 2.0)
    $SoundPlayer("knock.ogg", 1.0)
    $SoundPlayer("door.ogg", 2.0)
    show gang_salute at left with dissolve
    gang "북진. {w}일병 [gang] 지휘통제실에 용무 있어 왔습니다."
    tie "그래, 고생한다."
    $FaceChange("gang_atten", 0.0, .5, "gang_salute")
    hide tie_nom
    $SoundPlayer("walk_slow.ogg", 2.0)
    gang "저 왔습니다."
    main "무슨 일이야?"
    gang "잘... 모르겠습니다. {w}소대장님도 그냥 \'가서 ㅇㅇㅇ 데려와\' 라고 밖에 말씀 안하셨습니다."
    main "어디 계신데, 지금?"
    $event_result_val = renpy.random.randint(1, 100)
    #"[event_result_val]"
    if event_result_val <= 60:
        gang "사이버지식정보방입니다."
        $FaceChange("main_ang", 2.0, 1.0, "main_unhat")
        main "(x바... {w}x됐네...)"
        $FaceChange("main_unhat", 2.0, 1.0, "main_ang")
    else:
        gang "사무실에 계십니다."
        main "(사무실? {w}날 갑자기 왜?)"
    main "알았어. {w}특이사항은 없고, 잘 부탁해."
    gang "예, 고생하십시오."
    $FaceChange("main_unhat_salute", 2.0, .5, "main_unhat")
    main "북진. {w}다녀오겠습니다."
    hide main_unhat_salute
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show main_unhat
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("running.wav", 2.0)
    scene bg_black with blinds
    $renpy.pause(2.0)
    if event_result_val <= 70 and bufftory.search(sat_debuff1):
        scene bg_taba
        show main_tabahand at center
        with blinds
        main "(하... {w}x발...)"
        $Smoking("main", 1, 2)
        show explain_scene with dissolve
        centered "어제, 야간 연등 시간."
        extend "\n예전에 우연찮게 찾아냈던 보안 프로그램을 무력화 시키는 방법. {w}\악용하고자하는 마음이 없었다\'... {w}라고 단언할 수 없었다."
        extend "\n그러나, 그 시작은. {w}어제 진행하였던 작업은. {w}컴퓨터를 재부팅할 때마다. {w}보안 프로그램과 복원 프로그램을 완전히 삭제했음에도 다시금 설치되는 상황에 대한 순수한 호기심에서 출발한 일이었다."
        extend "\n꺼지지 않은 컴퓨터. {w}남아있는 작업 파일. {w}지워지지 않은 방문 기록과 다운로드 기록."
        centered "작업할 일이 있어 사이버지식정보방에 들어간 소대장님께서는 내가 사용했던 컴퓨터를 발견하고, 어제자 당직부관에게 연락해 연등시간에 사용했던 사람을 파악한 것이었다."
        extend"\n어디까지나 경고. {w}남아있는 증거만으로는 내게 그랬다는 것을 특정해낼 수 없었다. "
        extend "\n연등시간 이전에. {w}혹은 연등 시긴이 끝나고 누군가가 몰래 했을 가능성이 있기에 경고하는 것으로 일단 마무리 되었다."
        centered "그러나. {w}문제는 이 사실이 다른 사람들. {w}특히 균영이의 귀에 들어갔을 때의 후폭풍이다."
        extend "\n...할 수 있는 건... {w}마음을 비우고 기다리는 것 뿐이다."
        hide explain_scene
        $Smoking("main", 1, 2)
        main "빌어먹을..."
        show explain_scene with dissolve
        centered "무엇을 탓해야 할지는 명확했다. {w}해서는 안 될 일이라는 것을 알고도 잘못을 저지른 내 자신만을 원망하면 될 문제이다."
        extend "\n각오하고 있었던 일이다. {w}발각되고, 욕 먹고. {w}징계를 받게 될지도 모른다는 것을 알고 있었다."
        extend "\n후회는 없다. {w}만약에 내게 보안 체계 무력화라는 목표를 가지고, 임하지 않았더라면. {p}}나는 비루히나마 이어져 지금을 쥐지는 것조차 이루지 못한 채 진즉에 파절되어 흩어졌을 것이다."
        extend "\n그만큼, 하루하루는 내게 적대적이었고. {w}벼랑에 몰려 아슬아슬한 균형잡기를 이어가는 상황이었다."
        extend "\n물론 이는 변명이고, 핑계이다. {w}그 누구도 인정해주지 않을 여담이다."
        extend "\n동시에, 분명히 있었던 일이고. {w}틀림없는 현실이었다."
        extend "\n내 잘못임은 분명하고. {w}이로 인해 모종의 처벌을 받게 된다 하여도 내게 불복할, 반항할 권리도, 명분도 없음을 알고 있었다."
        extend "\n그럼에도, 머리 속을 맴도는 이 감정은... {w}무엇일까."
        hide explain_scenes
        $Smoking("main", 1, 2)
        $SoundPlayer("putoff.wav", 2.0)
        $FaceChange("main_atten", 1.0, .5, "main_tabahand")
        $stress_val += 15
        $sat_val -= 10
        $renpy.pause(.5)
        hide main_atten
        $what = "사지방"
    else:
        scene bg_hallway with blinds
        main "북진. {w}용무 마치고 복귀하겠습니다."            
        OOI "그래."
        $SoundPlayer("door.ogg", 2.0)
        show main_unhat at center with dissolve
        $SoundPlayer("door.ogg", 2.0)
        main "(편제 전환이라... {w}이제 정말로... {w}끝인 건가...)"
        "어디까지나 \'장기 파견\' 명목으로 본부중대에서 생활하고 있었기에 내 편제는 아직 1중대 3소대였고. {w}내 개인화기 역시 1중대 재산이었다."
        "내일이 되면, 나는 더 이상 1중대 소대 통신병이 아닌. {w}대대본부 통신소대 소속 무선장비운용병이 돤다."
        "비취인가는 물론, 보통의 경우 자대배치를 받은 이후 거의 바뀌지 않는 소총마저 새로 지급받게 될 것이다."
        "더 이상... {w}1중대와는 어떠한 연관점도 없는 남이 되어 버림을 의미했다."
        "물론, 알고 있다. {w}내가 도망치기로 결심한 이상. {w}꼭 거쳐야 할 과정이라는 것을."
        "그럼에도. {w}동시에 드는. {w}두 번 다시 돌아오지 않을 호시절. {w}이제 와서는 아득하게만 느껴지는 과거의 기억들과, 그 속에 남겨진 여러 \'약속\'들."
        "그 모든 것들을 저버리고. {w}마치 그런 일이 처음부터 없었던 것 마냥 바래버리는 듯한 느낌이 지워지지 않았다."
        $evented = True
        $stress_val-= 5
        $sat_val-=5
        hide main_unhat
        $what = "편제 전환"

    $timeCheck(0, 20)
    $evented = True
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_zitong with dissolve
    $SoundPlayer("knock.ogg", 1.0)
    $SoundPlayer("door.ogg", 2.0)
    show main_unhat with dissolve
    $SoundPlayer("door.ogg", 2.0)    
    $FaceChange("main_unhat_salute", 1.0, .5, "main_unhat")
    main "북진. {w}상병 ㅇㅇㅇ. {w}다녀왔습니다."
    $FaceChange("main_unhat", 1.0, .5, "main_unhat_salute")
    $SoundPlayer("walk_slow.ogg", 2.0)
    show gang_atten at right with dissolve
    main "특이사항."
    gang "없습니다."
    main "고생했다."
    gang "고생하십니다. {w}별 일 없으셨습니까?"
    main "...응. {w}별 거 아녔어."
    $FaceChange("gang_salute", 2.0, .5, "gang_atten")
    gang "북진! {w}일병 [gang]. {w}용무 마치고 복귀하겠습니다."
    $FaceChange("gang_atten", 0.0, .5, "gang_salute")
    $SoundPlayer("door.ogg", 2.0)
    hide gang_atten
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    $evented = True
    $what_all_list.append(what)
    return

label day2_study_major1:
    $SoundPlayer("pen.ogg", 1.0)
    main "(잠깐만. {w}두 점 사이에 거리? {w}어떻게 구하더라?)"
    $SoundPlayer("walk_slow.ogg", 2.0)
    show zoo_smi at center with dissolve
    zoo "ㅇㅇ."
    main "상병 ㅇㅇㅇ. {w}부르셨습니까?"
    zoo "뭐하고 있어?"
    main "아, [zoo] 하사님! {w}고생하십니다. {w}공부하고 있었습니다."
    zoo "전공?"
    main "예, 전공 공부입니다."
    zoo "열심히 하네."
    main "감사합니다. {w}부대 일지 뭐라고 남기면 되겠습니까?"
    zoo "백신 예비조 복귀."
    $SoundPlayer("typing.ogg", 2.0)
    main "예. {w}기입했습니다."
    zoo "오늘도 근무야?"
    main "예... {w}어쩌다 보니 그렇게 됐습니다."
    zoo "요원화 훈련이 사람 잡네."
    main "괜찮습니다. {w}저 훈련받을 때도 선임분들께서 제가 해야할 것까지 대신 해주시지 않았습니까."
    zoo "하긴. {w}너 훈련 가는 바람에 5대기 통신병이 없어서 2소대에서 지원해주긴 했다."
    main "그때 기억나십니까? {w}[zoo] 하사님께서 훈련 잘 받고 오라고 부식으로 나온 감자칩 나눠주시지 않았습니까."
    zoo "맞다, 그랬었지. {w}그때 준혁이가... {w}그... {w}왜 그랬었잖아. {w}이거 줄 테니까... {w}뭐였더라?"
    main "\'이거 줄게. {w}이거 주고 5대기도 들어가줄게. {w} 그 대신에 맛있게 먹고 훈련 열심히 받아서 가슴에 독수리 꼭 달고 돌아와라\'였습니다."
    zoo "그걸 아직도 기억하고 있어? {w}정말 대단한 기억력인데?"
    main "저도 아직 기억하고 있는 게 좀 신기하긴 합니다."
    zoo "와... {w}그게 벌써 반년이 넘었네..."
    main "예. {w}그게 올해 1월달이었으니까 시간 진짜 빨리 흐르긴 했습니다."
    zoo "그러게... {w}근무 고생하고 안녕~"
    main "중대 내려가십니까?"
    zoo "응. {w}가서 복귀 신고 해야지."
    main "고생하십시오, [zoo] 하사님."
    zoo "너도~"
    hide zoo_smi
    $SoundPlayer("walk_slow.ogg")
    $SoundPlayer("door.ogg")
    $SoundPlayer("door.ogg")
    "어깨에, 감촉이 남아있다."
    "작업 도중, 훈련 도중. {w}여러 차례 넘어지고, 부상당하며 해진 섬유 너머에서 체온이 전달되었다."
    "지금으로부터 닿을 수 없으리 만큼 멀직히 떨어진 것처럼 느껴지는 가까운 때에. {w}두려움에 질듯 고개를 숙일 때마다 살며시 얹어졌듯이."
    "몇 남지 않은 연결고리들마저 하나 둘 부서져 내리는 이금에, 어깨에 머문 온기. {w}그 흔적은 빠르게 흩어지겠지만. {w}분명한 형상을 지닌 따스함을 남겼다."
    main "([zoo] 하사님...)"
    "어리석음에서 시작된 잘못으로 인해 모래 위의 성탑은 파도라 말하지도 못할 하찮은 물줄기와 만나자 삽시간에 무너져 내렸다."
    "도망자. {w}어찌보면 선의를 배신한 사람. {w}그럼에도. {w}그 사실을 들었음에도. {w}진실을 보았음에도. {w}한결같은 은의를 베풀어주시기에."
    "한 번도 만족시켜드리지 못하고. {w}언제나 내게 내려진 기대를 저버리기를 반복하던 나. {w}하루하루를 두려움 속에서 살며. {w}나를 향한 제각각의 시선으로부터 도망가고자 궁리하던 사람."
    "한 시의 쉼도 없이 매 차례 몸집을 불리던 달빛의 그림자를 진실된 빛으로 지워내주던 이들."
    "비록 그 분들 중 대부분은 약속된 기간이 끝남과 함께 떠나가게 되었으나."
    "선임 분들이. {w}[zoo] {s}상병{/s}하사님이. {w} 간부님이 계셨기에. {w}노력할 수 있었고. {w}깎아지르는 절벽을 수 차례 넘어설 수 있었다."
    "변변한 사과 한 마디도 건내지 않은 채 도망나올 정도로 나를 둘러싼 허물이 커졌던 때도. {w}그 벗겨지지 않은 허물이 드리운 그늘이 아직 남은 지금에도."
    "나는 버텨 섰다. {w}폭풍에 휩싸인 것 마냥 굉굉히 흔들리면서도 아슬하게나마 꺾이지 않은 채."
    "지금껏 지탱해준 모든 것 중에 단 하나라도 도중에 잃어버렸거나, 처음부터 손에 쥐지 못했더라면."
    "어떻게 되었을지는 자명한 사실이다."
    $SoundPlayer("pen.ogg", 2.0)
    $SoundPlayer("pen.ogg", 2.0)
    $SoundPlayer("paper.ogg", 1.0)
    $SoundPlayer("pen.ogg", 2.0)
    $stress_val -= 5
    $sat_val += 5
    $timeCheck(0, 20)
    $evented = True
    $what = "전문하사"
    $what_all_list.append(what)
    return

label day2_study_major2:
    $SoundPlayer("pen.ogg", 1.0)
    main "(뭔가 이상한데... {w}이게 왜 안 풀리지?)"
    $SoundPlayer("telering.wav", 1.5)
    $SoundPlayer("teleclick.ogg", 1.0)
    main "\[통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다.\]"
    young "\[ㅇㅇㅇ 상병님? {w}저 영훈입니다.\]"
    main "\[어, 무슨 일이야.\]"
    young "\[지금 지철이가 얼굴을 데이는 바람에 저랑 같이 의무대 출발합니다.\]"
    main "\[괜찮데? {w}많이 안 다쳤어?\]"
    young "\[튀김 튀기다가 기름 튄 거라서 그렇게까지 심하진 않습니다.\]"
    main "\[그래, 빨리 갔다 와. {w}갔다 와서도 전화 주고.\]"
    young "\[예. {w}있다 복귀해서 다시 전화드리겠습니다.\]"
    $SoundPlayer("teleclick.ogg", 1.0)    
    $SoundPlayer("pen.ogg", 2.0)
    $SoundPlayer("pen.ogg", 2.0)
    $SoundPlayer("paper.ogg", 1.0)
    $SoundPlayer("pen.ogg", 2.0)
    $timeCheck(0, 20)
    $evented = True
    $what = "데였다"
    $what_all_list.append(what)
    return

label day2_study_major3:
    $SoundPlayer("pen.ogg", 1.0)
    main "(삼차원에서 두 점 사이의 거리? {w}어떻게 구하더라?)"
    "교과서에 부록으로 실려 있는 문제들을 하나 하나 풀어갔다."
    $SoundPlayer("pen.ogg", 2.0)
    $SoundPlayer("pen.ogg", 2.0)
    $renpy.pause(2.0)
    $timeCheck(0, 20)
    main "(82점이라... {w}나쁘진 않네.)"
    $stress_val -= 5
    $evented = True
    $what_all_list.append(what)
    return

label pcroom1_good_event1: #0
    $SoundPlayer("door.ogg", 2.0)
    show cap_working at right with dissolve
    if what == "게임" or what == "딴짓":
        "소리 없이 재빨리, 창을 닫았다."
    show main_cloth at center with wipeup
    $renpy.pause(.3)
    $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
    main "북진."
    fcaptain "안녕~ {w}주말인데 여기서 뭐하고 있어?"
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
    if what == "게임 개발" or what == "게임" or what == "딴짓":
        main "게임 만들고 있었습니다."
        fcaptain "게임?"
    elif what == "모델링":
        main "잠깐 모델링 공부 중이었습니다."
        fcaptain "3d 모델링?"
    main "예."
    fcaptain "한 번 볼 수 있을까?"
    if what == "게임 개발":
        "IDE 창을 최소화하고 테스트 모드로 게임을 실행했다."
        fcaptain "직접 만든거야?"
        main "그림이랑 오디오 쪽 빼고는 대부분 제가 직접 작업했습니다."
    if what == "게임" or what == "딴짓":
        "미리 켜둔 IDE 창 덕분에 바탕화면이 드러나 의심을 사는 일은 없었다."
        "테스트 모드로 게임을 실행했다"
    elif what == "모델링":
        "만든 모델이 전체적으로 잘 보이도록 화면을 조작했다."
        fcaptain "K2 소총이네? 직접 만든거야?"
        main "예. "
    fcaptain "잘 만들었네..."
    main "감사합니다."
    fcaptain "자기 개발도 좋지만 밥은 꼬박꼬박 시간 맞춰서 먹으러 가야 한다?"
    main "알겠습니다!"
    fcaptain "그래, ㅇㅇ이는 잘하니까 중대장이 이렇게 굳이 말할 필요도 없겠지."
    "눈동자가. {w}가만히 나를 응시한다. {w}그 어떤 천칭으로 저울질 되어도. {w}그 어떤 고난으로 시험받아도 변치 않을 결연한 의지가 가득한 눈동자에 내 모습이 비치였다."
    $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
    main "북진! {w}근무 고생하십시오!"
    fcaptain "잘 쉬어라 ㅇㅇ아."
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
    hide cap_working
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    "나는 구원받은 것이나 다름없다. {w}처음으로 이천에 발을 디뎠던 날. {w}중대장님께서 내게 미소 지어주시지 않았더라면 이야기는 여기까지 이어지지도 못한 채 파탄났을 것이다."
    main "(중대장님... {w}지금에서는 중대장님과 떨어지게 되었습니다만... {w}중대장님께서 베풀어주신 그 모든 것 덕분에 지금껏 살아남았습니다. {w}언젠가 제 군생활이 끝날 때까지. {w}어쩌면 그 넘어서에도.)"
    main "(중대장님은 저의 우상이시며, 아버지와 같은 분이십니다.)"
    if what == "게임 개발":
        "화면을 바라보았다. {w}지난 주 일요일. {w}끝내 해결하지 못한 채 근무 투입했던 난점."
        "지금이라면. {w}중대장님께 칭찬 받은 지금이라면. {w}아무리 머리를 굴려 보아도 해결하지 못한 오류를 풀어낼 수 있을 것 같았다."
        $SoundPlayer("typing.ogg", 2.0)
        play sound typing
        $stress_val -= 5
        $sat_val += 5
    elif what == "모델링":
        "모델을 저장하고 새 파일을 생성했다."
        main "(이번에는...)"
        "큐브이 길이를 늘리고, 다리가 될 부분을 만들기 시작했다."
        play sound click
        $stress_val -= 5
        $sat_val += 5
    else:
        play sound tinnitus
        $FaceChange("main_cloth_ser", 1.0, .5, "main_cloth")
        "그런 우상을 속였다는 사실이 가슴을 무겁게 옥죄어 왔다.{p}그리고, 동시에. {w}가슴 속에 피어오른 것은 내게 허락되지 않은 감정."
        "소등 이후의 막사, 그 끝모르게 퍼져나가는 어둠이 내 몸을 뒤치여. {w}하루가 더 없이 길었던 때. {w}자그마한 그늘마저 꼼꼼히 채우는 새론 광채를 두려워 하여 차라리 이 두 눈이 불타 멀어버기를 기도했던 때"
        "그 격랑은 이미 물러났으나. {w}한 편에 분명한 흉터를 남기었고.{p}아문 상처가 때때로 쓰라리듯. {w}익숙한 괴로움이 몸을 스쳐 지나갔다." 
        $renpy.transition(dissolve)
        call eye_screen
        main "(하지만... {w}어쩔 수 없다고...)"
        "목소리" "{color=#FF0000}정말 그렇게 생각해?"
        scene bg_pcroom at blur2 
        show main_cloth_ser at blur3
        with Dissolve(2.0)
        play looping heartbeat
        "이어 찾아오는 현기증."
        $SoundPlayer("sigh.wav", 1.0)
        main "(x같네... {w}진짜...)"
        $timeCheck(0, 10)
        $FaceChange("main_cloth", 1.0, 1.0, "main_cloth_ser")
        stop looping
        "고개를 흔들어 털어냈다. {w}중대장님은 나가셨다. {w}한 번 순찰을 돌았으니 다음 순찰까지는 여유가 있을 것이다."
        $SoundPlayer("enter.wav", 1.0)
        "종료한 {nw}"
        if what=="게임":
            extend "게임 프로그램을 다시 실행시켰다."
        elif what=="딴짓":
            extend "웹 브라우저를 다시 실행시켰다."
    scene bg_black with fade    
    $renpy.pause(1.0)
    stop sound
    if what == "게임" or what == "딴짓":
        $stress_val -= 15
        $sat_val += 20
        $timeCheck(2, 20)
    else:
        $timeCheck(2, 30)
    $evented=True
    $saturday1_list.append(0)
    $where = ""
    return

label pcroom1_normal_event1: #1
    if what == "게임 개발":
        $SoundPlayer("typing.ogg", 2.0)
        "쉽게 해결되지 않는 오류를 바로잡는 마지막 방법."
        play sound typing
        "소스코드 일부를 삭제하고 천천히 다시 짜 넣었다. {w}아무리 디버깅을 해도 원인을 알아낼 수 없는 오류라 해도 손쉽게 해결할 수 있는 마지막 수단."
        "공들여 쌓아온 탑 일부를 제 손으로 무너뜨리는 일. {w}두 걸음 나아가기 위한 한 걸음의 후퇴이다."
        stop sound
        $SoundPlayer("typing.ogg", 2.0)
        $SoundPlayer("click.ogg", 1.0)
        "예상대로 원인모를 오류는 사라져 있었다. {w} 다음 부분으로 넘어가 개발을 이어갔다."
        play sound typing
        scene bg_black with fade
        $SoundPlayer("typing.ogg", 2.0)
    elif what == "모델링":
        $SoundPlayer("click.ogg", 2.0)
        "배경으로 깔아둔 청사진을 따라 정육면체를 가공했다. {w}잘라내고, 늘이고, 줄여가며 모양을 만들었다."
        play sound mousework        
        scene bg_black with Fade(1.0, 3.0, 1.0, color="#000000")
    else:
        "1주일 만의 자유는 확실히 달콤했다.{p}지난 5일 간의 고생을 보상받는 느낌이었다." 
        "그에 더해, 해서는 안 될 일을 하는 데에서 오는 배덕감. {p}알량하다, 라고도 말할 수 있는 내 실력을 갈고닦아 하나의 체계에 일부나마 무력화시켰다는 데에서 오는 환희."
        "짓눌릴 것만 같던 압박감으로부터 해방되었다."
        $stress_val -= 5  
        $sat_val += 10
    $saturday1_list.append(1)
    $timeCheck(2, 30)
    $evented=True
    $where = ""
    stop sound
    return

label pcroom1_bad_event1:
    $SoundPlayer("door.ogg", 2.0)
    #show jun_working_sang at right with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)        
    show jun_working_sang at Position(xalign=.4, yalign=1.0)
    hide main_cloth
    show main_cloth_sup at center
    with vpunch
    jun "뭐하냐?"
    "조건반사적으로 손이 움직이려 했다."
    if what == "딴짓": #code 3
        extend "\n멈추었다. {w}경우에 따라서라면... {w}충분히 넘어갈 수 있는 상황이다."
        $FaceChange("main_cloth", 1.0, .5, "main_cloth_sup")
        main "잠깐... {w}웹서핑 중이었습니다."
        jun "나와 볼래? {w}확인할 게 있어서 그래."
        main "...예."
        hide main_cloth
        hide jun_working_sang
        show main_cloth at center
        show jun_working_sang at Position(xalign=.4, yalign=1.0)
        $SoundPlayer("typing.ogg", 2.0)        
        jun "이야~ {w}참..."
        main "......."
        jun "ㅇㅇ아."
        main "상병 ㅇㅇㅇ."
        jun "사지방이 뭐하는 곳이냐?"
        main "공부하라고 있는 곳입니다."
        jun "그런데 넌 뭐했어?"
        main "......."
        jun "경고다. {w}조금 있다가 다시 올 거야. {w}또 걸리기면 알아서 해라."
        main "예..."
        $saturday1_list.append(3)
        $stress_val += 10
        $sat_val -= 10
        hide jun_working_sang
        $SoundPlayer("walk_slow.ogg", 2.0)
        $SoundPlayer("door.ogg", 2.0)
        main "(...위험했다... {w}게임 같은 걸 했다면... 바로 끝장이었을 거야...)"
        play sound mousework
        scene bg_black with fade    
        $renpy.pause(1.0)
        stop sound
    elif what == "게임":
        $SoundPlayer("enter.wav", 1.0)
        jun "꺼봤자 소용없어. {w}다 봤으니까."
        $FaceChange("main_cloth_ang", 1.0, .5, "main_cloth_sup")
        main "(망할...)"
        jun "ㅇㅇ아."
        main "상병 ㅇㅇㅇ."        
        jun "비켜."
        main "....예."
        hide main_cloth_ang
        hide jun_working_sang
        show main_cloth 
        show jun_working_sang at Position(xalign=.4, yalign=1.0)
        $SoundPlayer("typing.ogg", 2.0)
        jun "이야... 아주 그냥... {w}네 세상이었구나?"
        main "......."
        jun "어떻게 할래?"
        main "잘 못 들었습니다?"
        jun "이거 어쩔 거냐고."
        main "그건..."
        jun "일단 일어나. {w}컴퓨터 꺼."
        $SoundPlayer("click.ogg", 2.0)
        main "껐습니다."
        jun "그리고{nw}"
        $event_result_val = renpy.random.randint(1, 100)
        $print(event_result_val)
        if event_result_val >= 60: #code 4
            extend ", 나가."
            main "...알겠습니다."
            jun "사지방 다시 오기만 해 봐."
            main "예."
            jun "나라서 운 좋은 줄 알아. {w}알겠어?"
            "당직사령님께. {w}혹은 소대장님께 보고된다는 최악의 상황은 일단 면했다."
            "그렇지만..."
            $stress_val += 10 
            $sat_val -= 10
            $saturday1_list.append(4)
        else: #code 5
            extend "..."
            jun "이건 어쩔 수 없다. {w}월요일날 통신소대장님 출근하시는 대로 보고드릴 테니까 그렇게 알아. {w}나가 봐."
            main "...예."
            $stress_val += 15
            $sat_val -= 20
            $saturday1_list.append(5)
            jun "사지방 다시 오기만 해 봐."
        $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
        main "북진. {w}고생하십시오."
        $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
        $renpy.pause(1.0)
        hide main_cloth
        $SoundPlayer("walk_slow.ogg", 2.0)
        $SoundPlayer("door.ogg", 2.0)
        $evented = True
        $timeCheck(0, 30) 
        scene bg_hallway_end2
        show main_cloth_ang at right
        with dissolve
        main "......."
        hide main_cloth_ang
        play looping walk_slow
        scene bg_taba_dawn with Fade(1.0, 2.0, 1.0, color="#000000")
        show main_cloth_taba_nof with dissolve
        stop looping
        $Smoking(img="main_cloth", loc=1, rep = 2, first=True)
        main "(일 났구만...)"
        $Smoking(img="main_cloth", loc=1, rep = 3)
        scene bg_black 
        hide screen time
        with Fade(1.0, 2.0, 1.0, color="#000000")
        $renpy.pause(2.0)  
        $where = ""
    return
##만약 잠자기/휴대폰의 경우는 코드 6
label sat_tabaevent:
    "희끄무레, 안개가 끼기 시작했다."
    scene bg_taba:
        blur 10
    show hoyun_sil at right:
        blur 10
    show main_cloth_tabahand
    with blur_transition
    "안개 틈 사이로 한 사람이 서 있다. {w}얼굴은 보이지 않는다. {w}확인할 수 있는 것은 어렴풋한 형체 뿐."
    "그것만으로도 저 인형이 무엇인지 알아보는데는 문제가 없었다."
    "목소리" "잉?"
    main "......."
    "목소리" "뭐야, 너 담배 폈었어?"
    main "예... {w}어쩌다 보니까... 이렇게 됐습니다."
    "살짝 미소를 지은 채 나를 바라보셨다."
    "언제나 그려셨다."
    "과묵히 앉아 먼저 말하지 않는다면 침묵을 유지하시던 분."
    "무섭게만 느껴졌던 김호윤 병장님은 부사수로 들어온 날 위해 통신병으로서 알아야 할 여러 지식들을 담담히 알려주셨다."
    "귓가에 들려오던 웃음소리, 감탄사. {w}후반기 교육을 받지 않고 곧바로 자대 배치를 받은 탓에 아무것도 모르는 신병이었던 나를 누구보다 가까이 두고 가르치던 이."
    main "김호윤 병장님..."
    "이제에서는 만날 수 없는. {w}군인으로 선 내가 진정으로 만족하며, 하루하루 충실감을 느끼던 날과 이어지는 열쇠조각."
    "미화된 기억이라 한다 하여도 그 날들의 나는 이렇게 매일매일을 부침과,{w} 충동과.{w} 격정과.{w} 부정 속에서 허우적거리지는 않았다."
    "적어도, 그 시절의 나는. {w}국가에서 부과한 18개월이란 짧지 않은 시간 동안 그저 증오하거나, 원망하거나. {w}때로는 끝모를 무력함에. {w}바닥 모를 공포감에 번민하지 않고서."
    "지속되는 행불행의 교차를 눈 앞의 사람들과 함께 겸허히 맞이하며. {w}들뜨거나, 침울해하며 보낼 수 있을지도 모른다고."
    "내가 품은 가시들에 겹찔려 가면서까지 품어주며. {w}갓 일어선 갓난아기처럼 위태로이, 느릿히 내딛어지는 내 발걸음마저 인내하며 함께해 주었던 분들께서 느꼈었다."
    main "김호윤 병장님..."
    hoyun "불렀으면 말을 해야지."
    main "보고싶습니다..."
    "그렇게 또 한 번. {w}너무나 당연한 사실을 망각했었던 것이다."
    "문자 그대로 내가 가진 모든 것을 얄팍한 가능성에 베팅한 채 주어졌던 십 수 번의 기회를 모두 걷어찼던 건 나였다."
    "최악의 선택지를 고른 대가. {w}나는 다시 한 번 내쫒김과 도주 사이에서 도주를 선택하였고. {w}아물었다고. {w}완전히 흩어져 사라졌으리라 여겨졌던 그림자는 몸집을 되불려냈다."
    $FaceChange("main_cloth_cry", 1.0, 1.0, "main_cloth_tabahand")    
    main "다시 한 번 김호윤 병장님과 이야기하고 싶습니다."
    main "다시 한 번 통신병 교육을 받고 싶습니다."
    main "다시 한 번 함께 훈련하고 싶습니다."
    main "다시 한 번 함께 5대기에 투입하고 싶습니다."
    main "그리고... 마지막까지 전하지 못했던 한 마디 말을 전하고 싶습니다."
    hoyun "......."
    "눈 앞에 있는 것은 그저 그림자.{w}아무리 모습을 비슷히 갖춘다 하여도 결코 진실은 되지 못하는 한 편린."
    show hoyun_sil at Position(xalign=.6, yalign=1.0): 
        blur 10
    with dissolve
    "머리에 손이 얹어졌다."
    $SoundPlayer("blanket.wav", 3.0)
    "부옇게 흐려진 시야 너머, 따스한 손길과 미소가 눈에 들어왔다."
    main "김호윤 병장님..."
    hoyun "고생했다. {w}조금만 더 고생하자. {w}거의 다 했잖아?"
    "이것은 환상이다. {w}내 뇌가 짜낸 거짓이다."
    "그러나. {w}거울 속에 비친 상에 불과하다 하여도. {w}달이 태양이 빛을 빌어 밤땅을 어스름히 비추어 주듯이."
    "지금 눈 앞의 꿈무리는 내게 잠시나마 안녕을 가져다 주었다."
    hoyun "그리고 울지 좀 마. {w}울어도 바뀌는 건 없다고."
    main "예..."
    scene bg_taba
    show main_cloth_cry
    with blur_transition
    "꿈꿔왔던 이상은 나타났을 때와 마찬가지로 예고 없이 흩어졌다."
    "담뱃재가 바닥에 떨어졌다."
    $SoundPlayer("blanket.wav", 3.0)
    $FaceChange("main_cloth_tabahand", 1.0, 1.0, "main_cloth_cry")
    main "(김호윤 병장님... {w}잘 지내고 계십니까?)"
    $Smoking("main_cloth", 1.0, 1)
    $sat_val += 10
    $stress_val -= 5
    $evented = True
    $where = ""
    return

#saturday1_list
label pcroom1_good_event2: ##1일차 점심
    "도중에 막히는 일 없이 개발은 순조롭게 진행되었다.{p}모델링도 생각한 것 이상으로 잘 뽑혔고, 스토리도 어딘가에 걸리지 않은 채 유유히 흘러갔다."
    $SoundPlayer("door.ogg", 2.0)
    show son_cloth_nom at right with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    son "엇, [main] 씨. {w}뭐하세요?"
    main "게임 만들어요."
    son "무슨 게임이요?"
    main "비주얼 노벨이라고 옛날에 초등학교 때 컴퓨터실 가면 깔려있는 클릭해서 진행하는 게임 있잖아요. {w}그거 사촌뻘 되는거요."
    son "헤에~ {w}신기하네요. {w}게임을 하는 사람이야 수 없이 봤지만 게임 만드는 사람은 실제로 처음 봐요."
    main "그런가요?"
    son "예. {w}멋있어요."
    main "......."
    "동경, 에서 시작된 선택. {w}내가 게임 개발자라는 직업을 장래희망으로 삼게 된 결정적인 계기.{p}중학교 때 우연찮게 접했던 한 게임."
    son "ㅇㅇ씨는 그럼 이런 게임 많이 해 봤어요?"
    main "예? {w}아, 네. {w}그렇죠. {w}관련된 게임을 좀 해본 사람이면 이 안에 들어가 있는 요소들 어디서 따왔는지 바로 알 수 있을 걸요?"
    son "특별히 추천할 만한 게임 같은 건 없나요? {w}입문작으로다가."
    main "어떤 장르 좋아하세요? {w}이런 류는 스토리가 중심에 서니까요. {w}취향에 안 맞는 걸 추천해 드릴 순 없죠."
    son "장르... {w}장르라... {w}그렇네요... {w}굳이 따지자면 판타지물이려나요."
    main "그럼 이거 추천드릴게요."
    "휴대폰을 꺼내 스토어를 띄웠다."
    main "기억을 잃어가는 공주가 마법학교에 들어가면서 벌어지는 일인데 재밌어요."
    son "으음~ {w}한 번 해볼게요."
    hide son_cloth_nom 
    $SoundPlayer("walk_slow.ogg", 2.0)
    "한연 씨는 다른 자리에 앉아 휴대폰을 만지작거리기 시작했다."
    $SoundPlayer("typing.ogg", 2.0)
    scene bg_black with wipeleft
    $SoundPlayer("typing.ogg", 2.0)
    $renpy.pause(3.0)
    $sat_val += 5
    $stress_val -= 8
    $now_h = 17
    $now_m = 10
    $evented = True
    return

label pcroom1_normal_event2:
    "도중에 막히는 일 없이 개발은 순조롭게 진행되었다.{p}모델링도 생각한 것 이상으로 잘 뽑혔고, 스토리도 어딘가에 걸리지 않은 채 유유히 흘러갔다."
    $SoundPlayer("phone_beep.wav", .4)
    $message_list.append(Message(type=0, who="고균영", message = "ㅇㅇㅇ 상병님."))
    call screen test_screen with dissolve
    $message_list.append(Message(type=0, who="고균영", message = "혹시 어디십니까?"))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "안 바쁘시면 잠깐 저랑\n같이 탄약고 좀 가 주실\n수 있겠습니까?"))
    call screen test_screen 
    $message_list.append(Message(type=1, who="나", message = "ㅇㅇ 어디로 갈까"))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "어차피 사지방이시지 않습니까.\n제가 가겠습니다."))
    call screen test_screen 
    $message_list.append(Message(type=1, who="나", message = "ㅇㅋ"))
    call screen test_screen 
    "굳이 탄약고라고 꼬집어서 말했다는 건 CCTV나 전화기 같은 게 망가졌다는 뜻이다.{w} 굳이 내게 전우조가 되어달라 부탁한 건 이 기회에 내 과업 수행 능력을 확인해보고 모르는 부분을 알려주기 위해서겠지."
    "누군가는 균영이의 행동을 보고 건방지다던가, 쓸데 없는 참견이라고 말할 지도 모르겠지만 적어도 나에게는 필요한 일이었다."
    "본디 전투중대였던 1중대에서 소대 통신병으로 군생활의 절반이 넘는 기간 동안 복무한 내가 통신소대에서 제대로 된 일과를 수행한 기간은 길게 잡아도 3개월. {w}실질적으로는 그보다 더 짧을 것이다. {w}선임이라고는 하지만, 과업에 대한 숙련도나 이해도에서는 뒤쳐지는 상황."
    "나중에, 평일 일과 수행 도중에.{w} 혹은, 훈련 도중에. {w} 능력 부족으로 간부님들께 질책받는 것보다는 낫다."
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_hallway_end 
    show main_cloth at left
    with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    show go_cloth_cross at right with dissolve
    $renpy.pause(.5)
    $FaceChange("go_cloth_cross2", 2.0, .5, "go_cloth_cross")
    go "먼저 나와 계셨습니까."
    main "응."
    go "바로 가십니까?"
    main "그래, 출발하자."
    scene bg_hallway_end
    play looping walk_slow
    scene bg_black with wipeleft
    $renpy.pause(2.0)
    scene bg_tanout with wiperight
    stop looping
    show go_cloth_atten at right
    show main_cloth at center
    with dissolve
    go "제가 저번에 말씀드리지 않았습니까. {w}CCTV가 안되면 10에 9은 탄약고 내부 선 문제입니다. {w}기억하고 계십니까?"
    main "응."
    go "이번에는 제가 안 도와드릴 테니 혼자 한 번 해 보십시오."
    scene bg_tanout
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_tanout2
    show go_cloth_atten at right
    show main_cloth at center
    with dissolve
    "초병 α" "누구십니까?"
    go "통신소대 상병 ㅇㅇㅇ, 상병 고균영입니다. {w}CCTV 수리 때문에 왔습니다."
    scene bg_black with dissolve
    $SoundPlayer("gate.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_tan_inside
    show go_cloth_cross at right
    show main_cloth at center
    with dissolve
    main "어디보자..."
    "시간을 너무 오래 끌 순 없다. {w}이건 일종의 테스트. {w}빠르고 정확하게 끝내는게 중요하다."
    call screen cctv_board
    $SoundPlayer("walk_slow.ogg", 2.0)
    show sol_sil at left with dissolve
    "초병 α" "고쳤습니까?"
    go "예. {w}전원선이 뽑혔었네요."
    "초병 α" "주말에 쉬지도 못하고 죄송해요."
    go "아녜요. {w}통신소대에서 해야 할 일인데요."
    scene bg_tan_inside2
    show sol_sil at left
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("gate.ogg", 2.0)
    scene bg_tanout2 
    show main_cloth at center
    show go_cloth_atten at right
    with dissolve
    go "고생하세요~"
    "초병 α" "고생하셨습니다!"
    scene bg_tanout2
    play looping walk_slow
    scene bg_black with fade
    $renpy.pause(4.0)
    stop looping
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $timeCheck(0, 20)
    scene bg_pcroom
    show main_cloth at center
    with fade
    "석식 때까지는 아직 꽤나 긴 시간이 남아있다. {w}자리를 잡고 다시 컴퓨터를 켰다."
    $renpy.pause(3.0)
    $stress_val -= 5
    $sat_val += 5
    $now_h = 17
    $now_m = 10
    $evented = True
    return

label pcroom1_none_event2:
    play sound typing
    "찾는 이 하나 없는 조용한 사이버지식정보방에 타건음 한 줄기만이 고요하게 퍼져나간다."
    $renpy.pause(3.0)
    $sat_val += 2
    $stress_val -= 2
    $now_h = 17
    $now_m = 10
    $evented = True
    return

label pcroom1_good_event3:
    $SoundPlayer("typing.ogg", 2.0)
    "꼬인 실타래처럼 쉬이 해결되지 않을 것 같던 버그들이 점차 고쳐져나가기 시작한다."
    "그 어느 때보다 깔끔한 코드가 화면에 길게 이어지기 시작하고. {w}내가 의도했던 그대로 작동하는 완벽한 소스가 되었다."
    play looping typing
    $renpy.pause(2.0)
    stop looping
    $stress_val -= 10
    $sat_val += 5
    $evented= True
    $now_h = 20
    $now_m = 30
    return

label pcroom1_none_event3:
    play sound typing
    "찾는 이 하나 없는 조용한 사이버지식정보방에 타건음 한 줄기만이 고요하게 퍼져나간다."
    $renpy.pause(3.0)
    $sat_val += 2
    $stress_val -= 2
    $now_h = 20
    $now_m = 30
    $evented = True
    return