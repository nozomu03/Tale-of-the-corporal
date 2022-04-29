init python:
    event('first_saturday1', 'go_px == True and now_week==2 and now_day == 5 and evented == False', event.random(.5), event.only(), priority=0)

label first_saturday1:
    #"px 이벤트 테스트입니다."
    if now_h < 11:
        scene bg_bath
        show main_cloth at center
        with dissolve
        "이미 한 차례 사람이 빠질 시간이어서일까. {w}px 앞은 한산했다."
        $SoundPlayer("door.ogg", 2.0)
        scene bg_px with dissolve
        "판매원" "어서 오세요."
        show main_cloth at center with dissolve
        $SoundPlayer("door.ogg", 2.0)
        main "루나틱 드래곤 한 갑 주세요."
        "판매원" "루나틱 드래곤 한 갑이요."
        $SoundPlayer("pos.ogg", 1.0)
        "판매원" "4500원입니다."
        "목소리" "[main]~ {w}담배 끊은 거 아니었어~?"
        main "...?"
        $SoundPlayer("walk_slow.ogg", 2.0)
        show jo_working at right with dissolve
        $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
        main "북진. {w}고생하십니다!"
        pl3 "오랜만이야~"
        $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
        main "잘 지내셨습니까?"
        pl3 "나야 당연히 잘 지냈지. {w}너는?"
        main "본부중대에 있는 동기나 후임들...{w} 그리고 간부님들도 많이 배려해 주셔서 편히 지내고 있습니다."
        pl3 "다행이네 그건."
        main "그렇습니다."
        pl3 "ㅇㅇ아."
        main "부르셨습니까?"
        pl3 "오랜만에 만났는데 뭐 먹고 싶은 거 없어? {w}사줄게."
        main "괜찮습니다."
        pl3 "아냐, 하나 골라 봐."
        "작은 콜라 캔을 골랐다."
        pl3 "그거면 되겠어?"
        main "예. {w}충분합니다."
        $SoundPlayer("pos.ogg", 1.0)
        "판매원" "500원입니다."
        pl3 "여기. {w}주말 잘 쉬어~"
        $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
        main "북진! {w}근무 고생하십시오."
        $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
        "싱긋, 웃어주시는 소대장님. {w}입술을 달싹여, 속삭이듯 말씀하셨다."
        pl3 "(괜찮아, ㅇㅇ아. {w}괜찮으니까...)"
        $renpy.pause(.3)
        $FaceChange("main_cloth_smi", 1.0, 1.0, "main_cloth")
        main "감사합니다...{w=.5}{nw}"
        "울컥. {w}무엇인가가 목에 걸렸다."
        $FaceChange("main_cloth_sad", 1.0, .5, "main_c loth_smi")
        $renpy.pause(.5)
        $SoundPlayer("door.ogg", 2.0)
        scene bg_bath with dissolve
        show main_cloth_sad at center with dissolve
        $SoundPlayer("door.ogg", 2.0)
        "말을 마치자 마자 도망치듯 px를 빠져나왔다."
        "쥐어진 캔에 응결된 수증기들이 방울방울 맺혔다. {w}내용물의 냉기가 체온을 빠르게 빼앗아 간다."
        $FaceChange("main_cloth", 1.0, 1.0, "main_cloth_sad")
        main "(소대장님...)"
        "돌이켜본다면, 발단은 지극히 단순했다."
        "임기를 마친 간부님이 보직 교체와 함께 다른 부대로 이임하게 되는 일이 간혹 일어나곤 했다. {w}보통 같은 대대 내의 다른 중대. {w}멀리 간다 해도 인근 부대로 이동하는 경우가 잦은 부사관과는 다르게 장교 분들은 두 번 다시 만나지 못할 만큼 먼 곳으로 떠나는 경우가 잦았다."
        "소대장님이 떠난다, 는 이야기. {w}5대기 임무 수행 도중 통신장비 예방정비를 위해 찾은 행정반에서 우연찮게 들은 말. {w}분기가 지나고 나면. {w}소대장님께서는 ㅇㅇ대대를 떠나 ◇◇대대에서 작전장교 임무를 수행하게 될 것이란 사실을 나는 우연찮게 들어 알고 있었다."
        "같은 건물 내에 더부살이 중인 ◇◇대대라면 자주 만나 뵐 수 있으리라고.{p}언젠가 그 날이 온다면 이취임식을 하게 될 테니, 그 간 입어왔던 은의에 대한 보답은 하지 못할지라도 적어도 감사 정도를 표할 수 있으리라 여기며 이내 머릿속에서 지워버린 게 화근이 된 것이다."
        main "(...그래도 잘 지내시는 것 같아 다행입니다, 소대장님.)"
        "매체에서 접해온 군인과는 한 없이 동떨어져 있는 모습.{p}단련된 체력에 따른 신체 능력으로 하달된 명령을 지체없이 수행하는것도.{p}어떤 상황에서도 당황하지 않고 침착히 상황을 정리하고 보고하며, 통신병으로서 보고를 취합하고, 상급자의 지시를 전달하는 것도 아닌."
        "훈련에서도, 작업에서도, 병영생활에서도. {w}낙제점만을 간신히 면한 채 버둥거리던 지난 나날들을 이제와서는 그래도 좋은 시절이었다 회상하며 우울히 웃을 수 있는 이유의 군집 중심에는 소대장님이 서 계셨다."
        main "(감사하고... 있습니다... {w}언제까지나.)"
        $sat_val += 5
        $stress_val -= 5
        $timeCheck(0, 10)
        $evented = True
        $go_px = False
    return