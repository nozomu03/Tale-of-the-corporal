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
    if where in where_list:
        "이미 갔던 곳이야."
        call screen map_view
    else:
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
        else:
            "무슨 일이 벌어지고 있나요?"
    return

label patron_event:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_office2 with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at center with dissolve
    $SoundPlayer("door.ogg", 2.0)
    call events_run_period
    return
label hq_office:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_office with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth with dissolve
    $SoundPlayer("door.ogg", 2.0)
    call events_run_period
    return
label csco_office:
    scene bg_office3
    return
label washing_event:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_washing
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at center with dissolve
    $SoundPlayer("door.ogg", 2.0)
    call events_run_period
    return
label lounge_event:
    scene bg_lounge
    return
label pc_event: