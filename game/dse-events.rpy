init python:
    test = "소대 사무실"
    event('meet_gang', 'where==\"소대 사무실\"', event.random(.3), event.only(), priority=20)
    event('meet_jeong', 'where==\"소대 사무실\"', event.random(.3), event.only(), priority=20)
    event('none', 'where==\"소대 사무실\"', priority = 100)
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
        $stress_val += 3

    return

label meet_jeong:
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    show jeong jeong_cloth at right
    jeong "에효... {w}내 팔자야... {w}뭐야, 언제부터 있었어?"
    main "방금 전부터."
    jeong "주말인데 왠일이야."
    main "그냥 심심해서."
    jeong "하... {w}비문병 줄까 물어봤을 때 받으면 안 됐었는데..."
    main "뭐야? {w}일 하러 온 거야?"
    jeong "어. {w}원래 금요일날 해 놨어야 했는데 까먹은 게 하나 있어서."
    main "고생하네."
    jeong "기왕 이렇게 된 거 나 한 번만 도와줄 수 있을까?"
    main "그래, 뭐 하면 되는데?"
    jeong "소대장님 직인 찍혀있는 "

label none:
    "[where]에는 아무도 없는 것 같다..."
    return
