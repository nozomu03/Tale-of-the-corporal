label go_px1:
    "일요일의 px는 3시가 되면 문을 닫는다."
    "오늘 먹을 간식을 미리 사두는 게 좋겠지."
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_black with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_px with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at center with dissolve
    "간식들을 골랐다."
    $SoundPlayer("pos.ogg", 1.0)
    $SoundPlayer("pos.ogg", 1.0)
    $SoundPlayer("pos.ogg", 1.0)
    main "아, 루나틱 드래곤 한 갑 주세요."
    "PX병" "루나틱 드래곤 한 갑이요." 
    $SoundPlayer("pos.ogg", 1.0)
    extend " 7200원 결제하겠습니다."
    main "네."
    hide main_cloth
    $SoundPlayer("door.ogg", 2.0)
    scene bg_bath with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at center with dissolve
    $now_m += 5
    
    return


label go_control:
    "[where]로 발걸음을 옮겼다."
    if where == "소대 사무실":
        call patron_event
    elif where == "본부 행정반":
        call hq_office
    elif where == "CSCO 행정반":
        call csco_office
    elif where == "세탁실":
        call washing_event
    elif where == "휴게실":
        call lounge_event
    elif where == "사지방":
        call pc_event
    return

label patron_event:
    return
label hq_office:
    return
label csco_office:
    return
label washing_event:
    return
label lounge_event:
    return
label pc_event: