init python:
    event('study_event1', 'af_do == \"공부\" and now_week==2 and now_day == 5 and evented == False', event.random(.3), priority=40)
    event('study_event2', 'af_do == \"공부\" and now_week==2 and now_day == 5 and evented == False', event.random(.3), priority=20)

label study_event1:
    $SoundPlayer("pen.ogg", 2.0)
    $renpy.pause(2.0)
    $SoundPlayer("door.ogg", 2.0)
    show gang_nom at left with dissolve
    gang "고생하십니다."
    $SoundPlayer("door.ogg", 2.0)
    main "응."
    gang "주말인데 왠일로 컴퓨터 안 하고 계십니까?"
    main "곧 훈련이잖아."
    gang "훈련...{w} 육지검 말입니까?"
    main "본부중대에선 처음이니까."
    gang "아... 작년에는 1중대에 계셨으니 말입니까?"
    main "어. {w}전투준비태세 때 상황근무는 처음 서 보니까."
    gang "육지검 때 뭐 합니까?"
    main "뭐 하냐라... {w}다른 훈련이랑 크게 다른 건 없어. {w}일단 전준태로 막사 싹 비우고."
    gang "예."
    main "작년에 1중대였을 때는 소산진지 점령하러 갔었는데 본부중대도 가나 모르겠다."
    gang "가지 않겠습니까?"
    main "그러려나..."
    gang "뭘 그렇게 보고 계십니까?"
    main "교범이랑 책자."
    gang "무슨 교범입니까?"
    main "임무수행계획이랑 전장통신망."
    gang "출동 안하시지 않습니까."
    main "검열관이 물어볼지도 모르니까."
    gang "물어도 봅니까?"
    main "몰랐어?"
    gang "여기 와서 저번에 안테나 친 것 빼고는 훈련이란 걸 해 본 적이 없습니다."
    main "그렇구만."
    gang "어떤 느낌입니까?"
    main "나도 모르는데? {w}1중대 기준으로라도 이야기해 줘?"
    gang "예."
    main "별 거 없어. {w}아침에 전준태 하는 거랑 훈련 끝나고 빼 놓은 짐 다시 집어넣는 거 빼고는 그렇게 힘들진 않아."
    gang "주로 뭐 합니까?"
    main "전준태로 짐 다 빼고 완전군장해서 상황 따라 움직여야지. {w}상황도 대대에서 하는 게 아니라 군단에서 내려오는 거라 그때그때 달라."
    gang "작년에는 어땠습니까?"
    main "작년... {w}소산진지 알지?"
    gang "저번에 전술전화기 야전선 정비했던 곳 말입니까?"
    main "응. {w}거기 가서 계속 대기했어. {w}밥 먹을 때만 빼고."
    gang "아무것도 안 하고 가만히 경계만 하는 것도 힘들 것 같습니다."
    main "중간중간 화생방 상황이나 이것저것 주고 검열관들이 돌아다니면서 계속 물어봐서 정신 없어."
    gang "뭘 물어봅니까?"
    main "그냥 지금까지 주어진 상황이나 암구호, 보유 장비랑 탄약... {w}통신병이면 무전을 넣어보라고 하는 경우도 있고. {w}지도 던져주면서 독도법으로 특정 위치를 표시해보라고 하는 경우도 있었다."
    gang "대답 못하면 어떻게 됩니까?"
    main "어떻게 되기는. {w}점수 왕창 깎아 먹는 거지. {w}훈련 끝나고 사후 강평할 때 이제 탈탈 털리는 거고."
    gang "그런 일 없이 다 외워 놔야겠습니다..."
    main "당연하지. {w}원래 이렇게 벼락치기하면 안 되고 항상 숙지하고 있어야 하는 거야."
    gang "으..."
    main "근데 왜 왔어?"
    if saturday1_list[0] == 4 or saturday1_list[0] == 5:
        gang "아, 저 두고 간 게 있어서 찾으러 왔습니다."
        play sound drawer_open
        main "오늘 야간이지?"
        gang "예."
        main "고생이 많구만."
        play sound drawer_close
        gang "ㅇㅇㅇ 상병님만 하겠습니까. {w}닷새 동안 매일 주간 근무라니...{w}전 죽었다 깨도 못할 겁니다."
    else:
        gang "근무 때 읽을 책 좀 미리 골라 놓으려고 했습니다."
        main "야간이야?"
        gang "예."
        main "하필 토요일 야긴이냐."
        gang "ㅇㅇㅇ 상병님은 근무 없으십니까?"
        main "야... {w}나 월요일부터 5일 내내 근무 섰다... {w}좀 쉬자..."
        gang "덕분에 훈련 잘 받고 왔습니다. {w}감사합니다."
    gang "먼저 가 보겠습니다. {w}고생하십시오."
    main "응~ {w}고생해~"
    hide gang_nom
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    "공부에 집중했다."
    $SoundPlayer("pen.ogg", 2.0)
    play sound pen
    $timeCheck(0, 15)
    scene bg_black with fade
    $stress_val -= 3
    $sat_val += 3
    stop sound
    play looping pen
    $renpy.pause(2.0)
    #$now_h = 17
    #$now_m = 20
    if saturday1_list[0] == 4 or saturday1_list[0] == 5:
        scene bg_office2
        show main_cloth
        with fade
    else:
        scene bg_library
        show main_cloth
        with fade
    stop looping
    $af_do = "_" + af_do
    return

label study_event2:
    $SoundPlayer("pen.ogg", 2.0)
    $renpy.pause(2.0)
    $SoundPlayer("phone_beep.wav", .4)
    $message_list.append(Message(type=0, who="고균영", message = "ㅇㅇㅇ 상병님."))
    call screen test_screen with dissolve
    $message_list.append(Message(type=0, who="고균영", message = "혹시 어디십니까?"))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "안 바쁘시면 잠깐 저랑\n같이 탄약고 좀 가 주실\n수 있겠습니까?"))
    call screen test_screen 
    $message_list.append(Message(type=1, who="나", message = "ㅇㅇ 어디로 갈까"))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "지금 어디십니까?\n사지방이십니까?"))
    call screen test_screen 
    $message_list.append(Message(type=1, who="나", message = "아니."))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "그럼 지통실 쪽으로\n와 주십시오."))
    call screen test_screen 
    $message_list.pop(0)
    $message_list.append(Message(type=1, who="나", message = "ㅇㅋ"))
    call screen test_screen 
    "굳이 탄약고라고 꼬집어서 말했다는 건 CCTV나 전화기 같은 게 망가졌다는 뜻이다.{w} 굳이 내게 전우조가 되어달라 부탁한 건 이 기회에 내 과업 수행 능력을 확인해보고 모르는 부분을 알려주기 위해서겠지."
    "누군가는 균영이의 행동을 보고 건방지다던가, 쓸데 없는 참견이라고 말할 지도 모르겠지만 적어도 나에게는 필요한 일이었다."
    "본디 전투중대였던 1중대에서 소대 통신병으로 군생활의 절반이 넘는 기간 동안 복무한 내가 통신소대에서 제대로 된 일과를 수행한 기간은 길게 잡아도 3개월. {w}실질적으로는 그보다 더 짧을 것이다. {w}선임이라고는 하지만, 과업에 대한 숙련도나 이해도에서는 뒤쳐지는 상황."
    "나중에, 평일 일과 수행 도중에.{w} 혹은, 훈련 도중에. {w} 능력 부족으로 간부님들께 질책받는 것보다는 낫다."
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    play sound walk_slow
    scene bg_hallway_mid
    show main_cloth at left
    with fade
    $SoundPlayer("walk_slow.ogg", 2.0)
    show go_cloth_cross at right with dissolve
    $renpy.pause(.5)
    $FaceChange("go_cloth_cross2", 2.0, .5, "go_cloth_cross")
    go "먼저 나와 계셨습니까."
    main "응."
    go "바로 가십니까?"
    main "그래, 출발하자."
    scene bg_hallway_mid
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
    if study_count == 0:
        call screen cctv_board
    else:
        call go_test_good
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
    $timeCheck(0, 15)
    if saturday1_list[0] == 4 or saturday1_list[0] == 5:
        scene bg_office2
    else:
        scene bg_library
    show main_cloth at center
    with fade
    $stress_val -= 5
    $sat_val += 5
    "석식 때까지는 아직 꽤나 긴 시간이 남아있다. {w}자리를 잡고 다시 교본을 들여다 봤다."    
    play looping pen
    $renpy.pause(2.0)
    stop looping
    #$now_h = 17
    #$now_m = 20
    $af_do = "_" + af_do
    #$evented = True
    return
