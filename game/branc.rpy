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


label day2_checker:
    if what == "독서":
        main "(책이나 읽어야지.)"
        "가슴 주머니에 넣어 두었던 포켓북을 꺼냈다."
        call events_run_period
        return
    elif what == "주특기 공부":
        main "(이제 곧 호국훈련이네... {w}그때까지 주특기를 좀 더 숙달해 놓으면 균영이도 더 이상 뭐라 못하겠지.)"
        main "정훈장교님?"
        tie "왜?"
        main "전자도서관 들어가서 교범 봐도 되겠습니까?"
        tie "무슨 교범?"
        main "무전기랑 C4I 연동 통신체계 교범입니다."
        tie "상관은 없는데 나한테 권한이 있나 모르겠네."
        main "간부님 계정으로 로그인만 되어 있으면 왠만한 교범은 다 읽을 수 있는 걸로 알고 있습니다."
        tie "맘대로 해."
        call events_run_period
        return
    elif what == "전공 공부":
        main "(어디보자... {w}어디까지 했더라...)"
        "챙겨왔던 전공서적을 꺼내 펼쳤다."
        call events_run_period
        return

label saturday1:
    #$del what
    $del where_list
    $what = "N/A"
    if morn_do != "잠자기":
        $SoundPlayer("blanket.wav", 4.0)
        main "......."
        scene bg_room2 with dissolve
        show main_cloth at right with wipeup
        main "(다른 애들은 아직 자고 있나? {w}조용히 움직여야겠네.)"
        $SoundPlayer("door.ogg", 2.0)
        scene bg_hallway2
        show main_cloth at center with dissolve
        $SoundPlayer("door.ogg", 2.0)
        $SoundPlayer("walk_slow.ogg")
        scene bg_hallway_mid2 
        show main_cloth at center
        with dissolve
        #$SoundPlayer("door.ogg", 2.0)
        #hide main_cloth
        $SoundPlayer("walk_slow.ogg", 2.0)
        $SoundPlayer("door.ogg", 2.0)
        scene bg_office
        show main_cloth at center
        with dissolve
        "조용한 행정반. {w}이미 몇 명 다녀갔는지 휴대폰 보관함은 드문드문 비어 있었다."
        $SoundPlayer("pen.ogg", 2.0)
        $SoundPlayer("walk_slow.ogg", 2.0)
        scene bg_hallway_mid2
        show main_cloth at center 
        with dissolve
        $SoundPlayer("door.ogg", 2.0)
        $SoundPlayer("walk_slow.ogg", 2.0)
        scene bg_toilet 
        show main_cloth at right
        with dissolve
        play sound brush
        "머리 속에, 어슴푸레 안개더미가 남았다."
        main "(뭐였을까... {w}그건.)"
        "희끄무레하여 형상을 파악할 수 없는. {w}그럼에도 분명히 존재하는 무언가가 헤엄친다."
        "도중에 일어나지 않고 조금 더 잤더라면 제대로 볼 수 있었겠지만..."
        main "(이미 일어나 버린 이상 그 꿈을 다시 꿀 수 있는 것도 아닌데 잊어버리자.)"
        $renpy.pause(2.0)
        stop sound
        $SoundPlayer("gargle.ogg", 2.5)
        hide main
        $SoundPlayer("walk_slow.ogg", 2.0)
        scene bg_hallway_mid2 
        show main_cloth at center
        with dissolve
        $now_h = 7
        $now_m = 10
        show screen time with dissolve
        if morn_do == "사이버지식정보방":
            call saturday1_morn_pc
            if not saturday1_list[0] == 4 and not saturday1_list[0] == 5:
                scene bg_pcroom
                show main_cloth
                with dissolve
                main "(시간이 벌써 이렇게 됐나.)"
                "괜히 늦게 밥을 먹으러 가 혼나는 것보다 조금 일찍 나서는 편이 낫겠지.{p}자리를 정돈하고 일어났다."
                hide main_cloth
                $SoundPlayer("walk_slow.ogg", 2.0)
                $SoundPlayer("door.ogg", 2.0)
                $SoundPlayer("door.ogg", 2.0)
                $SoundPlayer("walk_slow.ogg", 2.0)
                scene bg_black with fade
                $renpy.pause(1.0)
                $SoundPlayer("door.ogg", 2.0)
                $SoundPlayer("door.ogg", 2.0)
                scene bg_room2 
                show main_cloth
                with dissolve
                $renpy.pause(1.0)
                hide main_cloth
                $SoundPlayer("sheet.ogg", 1.0)  
                $timeCheck(0, 10)
                "침대 위에서 데굴거리며 식사 출발 방송이 나오기를 기다렸다."  

        elif morn_do == "휴대폰":
            call saturday1_morn_phone
    else:
        scene bg_office2:
            im.Sepia("bg_office3.png")
        show park_cross:
            im.Sepia("park_cross.png")
            align(.5, 1.0)
        show main_atten:
            im.Sepia("main_atten.png")
            align(.9, 1.0)
        with dissolve
        main "잘 못 들었습니다?"
        park "아무튼 그렇게 됐다."
        main "제가 말씀이십니까?"
        park "그래.{w} 왜? {w}못하겠어?"
        main "아... 아닙니다."
        park "지금 확실히 말해 줘야 해. {w}일단 한 번 투입하면 평소처럼은 못 해주니까."
        main "한 번 해보겠습니다."
        park "정말이지? {w}후회 없지?"
        main "예. {w}없습니다."
        show explain_scene with dissolve
        centered "처음으로 5대기에 투입하기로 결정됐던 날."
        extend "\n지금껏 겪어보지 못한 전혀 새로운 것을 마주했을 때 으레 느껴지는 두려움 역시 있었지만."
        extend "\n그 때. {w}내게 가장 크게 느꼈던 감정은 \'기쁨\'. {w}혹은, \'안도감\'이었다."
        hide explain_scene
        main "(저번에 참관도 했었고... {w}김호윤 상병님도 계시고... {w}다른 선임 분들도 계시잖아. {w}할 수 있을 거야... {w}아니, 해 내야만 해.)"
        show explain_scene with dissolve
        centered "같이 전입 온 다른 동기들보다 뒤쳐졌기에 자연스럽게 퍼진 소문."
        extend "\n내게 쏟아지던 것은 제각각 다른 종류의 시선이었으나. {w}결과적으로는 모두 같은 의미를 내포하고 있었다."
        extend "\n5대기에 투입된다면 적어도 동기들과의 차이점 중 하나가 메워질 것이고. {w}나아가 평소와는 다른 모습을 보여준다면 내게 쏟아지는 의심 중 일부는 거둘 수 있으리라."
        extend " ...생각했었다."
        $SoundPlayer("broadcast.wav", 2.0)
        fcaptain "\[지휘통제실에서 전파합니다. {w}강습대대 인원들 아침식사. {w}아침식사 출발해주시길 바랍니다.\]"
        $SoundPlayer("blanket.wav", 4.0)
        scene bg_room2 with dissolve
        show main_cloth with wipeup
        main "(꿈인가...)"
        "가슴 속에 자그맣게. {w}그날 느꼈던 감정의 모조품이 어렸다."
        main "(보고싶은... 사람들.)"
        main "(그 분들 뵈기 부끄럽지 않도록... {w}더 분발해야겠지.)"
        $stress_val -= 2
        $sat_val += 2
    return

label saturday1_morn_phone:
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_hallway_mid2 with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_hallway2
    show main_cloth at right
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    scene bg_room2 with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth at right with dissolve
    $renpy.pause(1.0)
    $SoundPlayer("sheet.ogg", 1.0)
    "침대에 누워 밥을 먹으러 갈 시간이 될 때까지 빈둥거렸다."
    $stress_val -= 3
    $sat_val += 3
    return

label saturday1_morn_pc:
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_hallway_end2
    show main_cloth at right 
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    scene bg_pcroom2
    show main_cloth at center 
    with dissolve
    #"testMessage"
    play sound switch
    $renpy.pause(.6)
    scene bg_pcroom
    show main_cloth at center
    stop sound
    "자리를 잡고 본체에 전원을 넣었다."
    $SoundPlayer("computer.wav", 4.0)
    "꼼꼼히. {w}주변을 살폈다."
    "사이버지식정보방 내부에 CCTV는 없다. {w}밖에서 안을 들여다 볼 수 있는 창문 같은 것도 없다. {w}사람. {w}나보다 먼저 들어온 이가 있는가. {w}문을 열고 살피는 이는 없는가. {w}꼼꼼히 확인한 후 본체로 손을 뻗었다."
    "어느 날. {w}단순한 발상에서 시작된 실험. {w}내 호기심에서 시작된 일련의 계획은 차근차근 진행되어 완성 직전에 다달았다. {w}조금만 더 시간을 투자한다면 결실을 맺을 수 있을 것이다."
    "실시간 감시 기능이  사라진.{w}반쪽짜리 사이버 보안 체계가 가동하며 모니터 속에 바탕화면이 떴다."
    main "(브런치를 먹으러 갈 때까지 뭘 하면 좋으려나?)"
    $evented = False
    menu:
        "게임 개발(+1h 40m)":
            $SoundPlayer("click.ogg", 2.0)
            $SoundPlayer("typing.ogg", 3.0)
            "요 근래 딴짓을 너무 많이 했다. {w}꼬리가 길면 밟힌다. {w}설령 들킨다 하여도 얼버무릴 수 있는 웹서핑 정도면 모를까 그 이상은 위험하다."
            $SoundPlayer("typing.ogg", 3.0)
            $what = "게임 개발"
            call events_run_period
        "모델링 연습(+1h 40m)":
            $SoundPlayer("click.ogg", 2.0)
            $SoundPlayer("typing.ogg", 3.0)
            "요 근래 딴짓을 너무 많이 했다. {w}꼬리가 길면 밟힌다. {w}설령 들킨다 하여도 얼버무릴 수 있는 웹서핑 정도면 모를까 그 이상은 위험하다."
            $SoundPlayer("click.ogg", 2.0)
            "모델링 프로그램을 실행시켰다."
            "화면 속의 입체공간. {w}정육면체에서 시작하여 점차 복잡한 형태로. {w}물체에 곡면이 생겨나며 물체는 형상을 갖추어 나갔다."
            $what = "모델링"
            call events_run_period
        "!!딴짓!!(+1h 40m)":
            $what = "딴짓"
            #$in_secret1 = True
            "의자 등받이에 기댔다."
            $SoundPlayer("click.ogg", 2.0)
            "웹 브라우저를 실행시키고 주변을 샆펴 아무도 없는 것을 확인했다."
            "소리를 최소한으로 줄인 후 동영상을 재생시켰다."
            call events_run_period
        "!!게임!!(+1h 40m)":
            $what = "게임"
            #$in_secret2 = True
            "주위를 살폈다. {w}방 안에 나 홀로 있음을 몇 번이고 철저히 확인했다."
            main "(...음.)"
            "웹 드라이브에 접속했다."
            "미리 업로드 해 두었던 파일을 내려받고 혹시 모를 일에 대비해 로그를 삭제했다."
            "찾기 힘든 외진 경로에 압축을 팔고 파일을 완전히 삭제했다."
            $SoundPlayer("click.ogg", 2.0)
            call events_run_period            
    return
#label study_major:
#    $what = "전공 공부"
#
#    return