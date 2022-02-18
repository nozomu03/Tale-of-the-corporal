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
    event('lounge_event1', 'where==\"휴게실\" and evented == False', event.random(1), event.only(), priority=20)


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
    prf "어... 그렇습니까? {w}아무튼 약이야 먹으면 부작용 오는 거 떄문에 잘 안 먹는다고 치더라도 군의관님이 하지 말라고 하신건 안 하시는 게 맞을 것 같습니다."
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
        main "(망할... {w}나같은 놈 떄문에...)"
        $stress_val += 5
        $sat_val -= 5
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
    #main "나도 알고 있어. {w}이전에는 하지 않았던 새로운 일이라고는 해도 전입온 지 두 달 넘게 지났는데 아직도 적응 못하고 후임들도 안 내는 빵꾸만 뻥뻥 터뜨려 대고 있따는 걸. {w}넌 내 분대장이기도 하고 또래 상담병이기도 하니까 그냥 솔직하게 이야기 할게. {w}갓 전입왔을 때 말했으니까 너도 알고 있겠지만은 내가 평소에 앓고 있는 병이 하나 있어. {w}그것 떄문에 "
    $event_result_val = renpy.random.randint(1, 100)
    "처음에는 건강 이야기. {w}그 이후에는 1중대 시절 이야기. {w}그 다음으로는 균영이의 이야기. {w}겉으로 보기에는 다가서기 힘들고 언제나 화나 있어 보이는 무서운 분대장이었던 균영이."
    main "이렇게 길게 이야기 해 본 적 있었나?"
    go "없었던 걸로 기억합니다. {w}그래도 이걸로 ㅇㅇㅇ 상병님에 대해서 이전보다는 조금 더 알게 된 것 같습니다."
    main "나도 너에 대해서 더 알게 된 것 같아서 기분 좋네."
    if event_result_val <= 30:
        "굳어 있던 마음이 조금은 풀리는 것 같았다. {w}그리운 얼굴들이 겹쳐 보였다. {w}지금은 떠나버린 간부님들이. {w}선임들이 나와 이야기를 나눌 때. {w}고민을 털어 놓고서 조언을 구했을 때와 같은. {w}따스함이 이 곳에서도 다시금 느껴졌다."
        $stress_minus += 10
        $sat_val += 7
    elif event_result_val < 70:
        "털어놓자 무겁게만 느껴졌던 매일이 조금은 가벼워진 것 같았다. {w}균영이는 지겨운 내 이야기를 끝까지 들어주었고. {w}이에 공감하는 척이라도 해 주었다. {w}누군가는 나를 타인을 나의 감정 쓰래기통으로 이용하고 있다고. {w}이기적이라 몰아붙일지도 모를 일이다." 
        "그러나. {w}이 맘 속에 품은 채 때를 지나 썩어가는 감정 더미와. {w}소중한 사람에게 꼭 전해야 했으나. {w}때가 늦어 건내지 못했던 감사의 잔여물들은 지금까지도 차곡차곡 쌓여 벗어 던질 수 없는 짐덩이가 되어버린 상태였다."
        main "(미안하다. {w}하지만 이렇게라도 하지 않으면... {w}진짜 미쳐버릴 거 같아...)"
    else:
        "균영이는 무표정히 컴퓨터 화면을 바라보고 있다."
        $SoundPlayer("typing.ogg", 2.0)
        go "아...{w} 정말 죄송합니다. {w}계속 해야할게 밀려들어 와서... {w}그래도 ㅇㅇㅇ 상병님꼐서는 언제나 노력하고 계시지 않습니까. {w}그 노력이 언젠가는 결실을 맺을거라고 저는 생각하고 있습니다."
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


