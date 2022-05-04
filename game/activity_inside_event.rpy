label go_pc_branch:
    go "왜 그러셨습니까?"
    main "......."
    go "대답해 주십시오."
    main "...나도 몰라."
    go "그게 대답이 된다고 생각하십니까?"
    $event_result_val = renpy.random.randint(1, 100)
    main "(.......)"
    #"[event_result_val]"
    if event_result_val < 60:
        "속마음을, 털어놓을 수 없었다.{p}어째서 이 일련의 사태가 벌어지게 되었는지에 관한 이야기를.{w} 2018년도부터 시작되는 기나긴 이유를."
        go "애당초 무슨 배짱으로 하신 겁니까? {w}기록 다 남아서 금방 들킬 텐데. {w}아니, 그 전에 어떻게 설치하셨습니까? {w}USB는 쓰지도 못하고 드라이브도 다 감시하고 있는데."
        main "...뚫었어."
        go "뭘 말입니까?"
        main "보안체계."
        play sound sigh
        go "하아... {w}그게 가능한 사람이 왜 기술을 그딴 식으로만 쓰는 겁니까?"
        main "......."
        go "솔직하게 말해서 ㅇㅇㅇ 상병님께서 좋은 일로 본부중대로 온 건 아니지 않습니까. {w}처음 오셨던 날부터 제가 못살게 군 적 있습니까?"
        main "아니..."
        go "왜 그러십니까? {w}뭐가 문제입니까?"
        "뱉을 수 있는 말은 없었다. {w}그 만큼 내가 품고 있는 이 감정과 초요는 이해받을 수 없는 부류였다. {w}상식, 으로는 설명할 수 없는. {w}부자연의 극치.{p}그럼에도 털어낼 수 없고. {w}파도에 휘말린 채로 어디까지고 쓸려내려가야 하는.{p}오로지 나만이 가진 듯 보이는 조각."
        play sound sigh
        go "...됐습니다. {w}앞으로는 그러지 말아 주십시오. {w}여긴 바깥이랑은 다릅니다. {w}ㅇㅇㅇ 상병님이 잘못하고. {w}혼자 혼나고. {w}혼자 책임지고 끝나는 곳이 아닙니다. {w}저보다 더 잘 알지 않습니까."
        main "...응."
        $stress_val += 15
        $sat_val -= 10
    else:
        play sound sigh
        go "에흐... {w}죄송합니다. {w}ㅇㅇㅇ 상병님도 말 못할 사정 같은게 있지 않겠습니까."
        main "미안하다."
        go "아닙니다. {w}속상해서 그랬습니다. {w}...여긴 밖이랑 다릅니다. {w}ㅇㅇㅇ 상병님 혼자 잘못하고.{w} 혼자 책임지고. {w}혼자 처벌받는 곳이 아닙니다. {w}저보다 더 잘 아시지 않습니까?"
        main "...그래..."
        $stress_val += 8
        $sat_val -= 6
    go "고생하십쇼."
    main "...고생해라."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth_ang at center with dissolve
    main "(...시x.)"
    $timeCheck(0, 10)
    return
