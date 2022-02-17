init python:
    test = "소대 사무실"
    event('meet_gang', 'where==\"소대 사무실\" and evented == False', event.random(.3), event.only(), priority=20)
    event('meet_jeong', 'where==\"소대 사무실\" and evented == False', event.random(.6), event.only(), priority=20)
    event('none', 'where==\"소대 사무실\" and evented == False', priority = 100)
    #event('meet_j')

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
    "[event_result_val]"
    scene bg_office2 
    show main_cloth at center
    with blinds
    if event_result_val <= 70:
        main "어, 미안하다. {w}주말에 계속 붙잡아 놨네."
        gang "아닙니다. {w}재밌었습니다. {w}고생하십시오."
        $stress_val -= 3
    elif event_result_val <= 90:
        main "뭐 그랬단 거지."
        gang "예... {w}고생하십시오."
        main "그래, 잘가."
    else:
        gang "저 혹시 죄송한데... {w}먼저 가 봐도 되겠습니까?"
        main "어? {w}아, 그래."
        gang "...고생하십시오."
        $stress_val += 3
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
    jeong "하... {w}비문병 줄까 물어봤을 때 받으면 안됐었는데..."
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
    main "나 지금 발 다쳤는데."
    prf "고균영 상병한테 들었습니다. {w}이제 거의 다 나아서 체력단련이나 일과에 전혀 지장없다고 말씀하셨다고."
    $FaceChange("main_cloth_ser", 1.0, 1.0, "main_cloth")
    

