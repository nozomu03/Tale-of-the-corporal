init python:
    event('test_px', 'go_px == True and now_week==2 and now_day == 5 and evented == False', event.random(1.0), event.only(), priority=0)

label test_px:
    #"px 이벤트 테스트입니다."
    if now_h < 11:
        scene bg_bath
        show main_cloth at center
        with dissolve
        "브런치가 평소와는 달리 든든하게 나왔기 때문일까, px 앞은 한산했다."
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
        $renpy.pause(.5)
        $SoundPlayer("door.ogg", 2.0)
        scene bg_bath with dissolve
        show main_cloth at center with dissolve
        $SoundPlayer("door.ogg", 2.0)
        "쥐어진 캔에 응결된 수증기들이 방울방울 맺혔다. {w}내용물의 냉기가 체온을 빠르게 빼앗아 간다."
        main "(소대장님...)"
        "돌이켜본다면, 발단은 지극히 단순했다."
        "임기를 마친 간부님이 보직 교체와 함께 다른 부대로 이임하게 되는 일이 간혹 일어나곤 했다. {w}보통 같은 대대 내의 다른 중대. {w}멀리 간다 해도 인근 부대로 이동하는 경우가 잦은 부사관과는 다르게 장교 분들은 두 번 다시 만나지 못할 만큼 먼 곳으로 떠나는 경우가 잦았다."
        "소대장님이 떠난다, 는 이야기. {w}5대기 임무 수행 도중 통신장비 예방정비를 위해 찾은 행정반에서 우연찮게 들은 말. {w}분기가 지나고 나면. {w}소대장님께서는 ㅇㅇ대대를 떠나 ◇◇대대에서 작전장교 임무를 수행하게 될 것이란 사실을 나는 우연찮게 들어 알고 있었다."
        "같은 건물 내에 더부살이 중인 ◇◇대대라면 자주 만나 뵐 수 있으리라 여기며 이내 머릿속에서 지워버린 게 화근이 된 것이다."
        main "(그래도 잘 지내시는 것 같아 다행입니다, 소대장님.)"
        $sat_val += 5
        $stress_val -= 5
        $timeCheck(0, 10)
        $evented = True
    return