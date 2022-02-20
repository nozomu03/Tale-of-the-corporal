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
        if where == "사지방":
            "[where]으로 발걸음을 옮겼다."
        else:
            "[where]로 발걸음을 옮겼다."
        if where == "소대 사무실":
            call patron_event from _call_patron_event
        elif where == "본부 행정반":
            call hq_office from _call_hq_office
        elif where == "CSCO 행정반":
            call csco_office from _call_csco_office
        elif where == "세탁실":
            call washing_event from _call_washing_event
        elif where == "휴게실":        
            call lounge_event from _call_lounge_event
        elif where == "사지방":
            call pc_event from _call_pc_event
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
    call events_run_period from _call_events_run_period
    return
label hq_office:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_office with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth with dissolve
    $SoundPlayer("door.ogg", 2.0)
    call events_run_period from _call_events_run_period_1
    return
label csco_office:
    call events_run_period from _call_events_run_period_2
    return
label washing_event:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_washing with dissolve
    $SoundPlayer("door.ogg", 2.0) 
    show main_cloth at center with dissolve
    $SoundPlayer("door.ogg", 2.0)
    call events_run_period from _call_events_run_period_3
    return
label lounge_event:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_lounge with dissolve
    call events_run_period from _call_events_run_period_4
    return

label pc_event:
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_pcroom with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at center with dissolve 
    $SoundPlayer("door.ogg", 2.0)
    "사지방에는 아무도 없었다. {w}전면 무료화가 되었다고는 해도 누구나 휴대폰을 사용하고 있는 주말 개인정비 시간에 굳이 사지방을 찾는 사람은 드물다."
    $SoundPlayer("computer.wav", 4.0)
    "모니터에 바탕화면이 떴다. {w}키보드에, 마우스에 손을 얹는 것으로. {w}잡념이 사라지고. {w}잡음이 잦아들었다."
    show explain_scene with dissolve
    centered "학교에도 들어가지 않았을 정도로 어렸던 나날들의 한 켠. {w}아버지의 손에 이끌려 처음으로 접하였던 \'컴퓨터\'."
    extend "\n내 마음을 사로잡은 전자 두뇌는 그 어떤 때에도 내 곁을 떠나지 않고 친구로 남아주었다."
    extend "\n나이를 먹고, 점차 성장해가고. {w}그 과정에서 맞이했던 여러 부침과 상승 속에서 내 곁에 서 있던 자들도 저 너머로 돌아서던 와중에도 그것만큼은 지끔까지도 나와 함께하며 의지할 수 있는 수단이 되어 주었다."
    centered "중독자의 오명을 쓰면서까지 집착하고 매달리는 것은. {w}암울하였던 고교생활. {w}건강도, 올발랐던 희망도 잃어버린 3년의 시간. {w}땅바닥에 처박히는 것으로도 모자라 지하 저 나락까지 끌려내려가는 듯 했던 격랑 속에서 얻은 다른 이름의 중독으로부터 도피하기 위해서였다."
    hide explain_scene with Dissolve(.5)
    $now_h = 17
    $now_m = 20
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("click.ogg", 1.0)
    main "(지금 몇 시지?)"
    "컴퓨터의 전자 시계가 17시 20분을 알려왔다."
    main "(아... 애매한데...)"
    "조금만 더 시도한다면 배배 꼬인 채 해결되지 않은 기능 오류를 해결할 수 있을 것 같았다. {w}동시에, 곧 식사 출발 시간이다. {w}저격반장님께서 근무하고 있는 오늘, 저번처럼 늦게 식사하러 갔다가는 크게 혼날 게 뻔했다."
    menu:
        "생활관으로 돌아간다(+10m)":
            main "(아쉽지만 어쩔 수 없지.)"
            "업로드 버튼을 눌러 지금껏 짜 놓은 소스코드를 드라이브에 백업했다."
            "전원이 내려가면, 수행했던 모든 작업이 \'일어나지 않은 것\'이 되며 초기 상태로 돌아가는 사지방 컴퓨터. {w}저녁을 먹고 와서 다시 컴파일러와 IDE를 깔 생각을 하자 속이 쓰려왔으나 저격반장님과 균영이에게 혼나는 것보단 나으리라."
            hide main_cloth
            $SoundPlayer("door.ogg", 2.0)
            scene bg_hallway
            show main_cloth
            with dissolve
            $SoundPlayer("walk_slow.ogg", 2.0)
            $SoundPlayer("door.ogg", 2.0)
            scene bg_room with dissolve
            $SoundPlayer("door.ogg", 2.0)
            show main_cloth at center with dissolve
            "침대에 누워 휴대폰 화면을 들여다 보았다."
            $renpy.pause(2.0)
            $timeCheck(0, 10)
            $SoundPlayer("broadcast.wav", 2.0)
            go "\[아, 아. {w}통합중대 인원들. {w}식사 출발해 주시길 바랍니다.\]"
            show jeong_cloth at right with wipeup
            jeong "밥 먹으러 가자."
            main "빠르지 않나?"
            jeong "그러게... {w}평소보단 좀 빠르네. {w}그래도 안 늦었네?"
            main "응. {w}오늘은 그냥 일찍 나왔어."
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
            hide jeong_cloth
            hide go_nom
            hide main_cloth
            $SoundPlayer("walk_slow.ogg", 2.0)
            play looping dish_wash
            scene bg_resta_in with dissolve
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
            return

        "다시 시도한다(+10m/+20m)":
            main "(아주 조금... 아주 조금이면 돼...)"
            "전원이 내려가면, 수행했던 모든 작업이 \'일어나지 않은 것\'이 되며 초기 상태로 돌아가는 사지방 컴퓨터. {w}저녁을 먹고 와서 다시 컴파일러와 IDE를 깔 생각을 하는 것만으로도 속이 쓰렸다."
            call events_run_period from _call_events_run_period_8
            return
    return