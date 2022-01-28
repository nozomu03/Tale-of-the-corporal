# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

# 여기에서부터 게임이 시작합니다.
label start:
    window hide
    scene bg_black
    centered "내가 원하는 건. {w}무엇이었을까."
    extend "\n어떤 것을 이루고자 그리도 노력했을까. {w}멈추는 일도, 흔들리는 일도 없이. {w}오로지 하나."
    extend "그 얼굴에 떠오른 미소를 보기 위해 제 몸을 채찍질하던 날들, 은. {w}과연 의미가 있었을까?"
    scene bg_room 
    show main_ord 
    with fade
    $SoundPlayer("blanket.wav", 4.0)
    "목소리 1" "근무 들어가니?"
    main "응."
    $FaceChange("main_atten", 1.0, 1.0, "main_ord")
    main "오늘 사령님 누구셨더라."
    "목소리 2" "1중대장님."
    main "갔다 올게."
    "목소리 1" "고생해~"
    hide main_atten
    $SoundPlayer("door.ogg")
    $SoundPlayer("walk_slow.ogg")
    scene bg_hallway
    show main_atten
    with dissolve
    $SoundPlayer("door.ogg")
    "주말 19시 40분. {w}생활관이 줄지어 있는 복도는 고요했다."
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)    
    scene bg_office
    show main_atten
    with dissolve
    "불 켜진 행정반. {w}컴퓨터도, 사람도. {w}살아있는 것은 없었다."
    $SoundPlayer("pen.ogg", 2.0)
    "휴대폰을 제출했다. {w}온도 일지와 휴대폰 사용 일지에 서명했다."
    "19시 43분."
    $SoundPlayer("walk_slow.ogg")
    scene bg_black
    with dissolve
    scene bg_zitong
    show cap_nom at right 
    with dissolve
    $SoundPlayer("knock.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    show main_atten at center with dissolve
    $FaceChange("main_salute", 1.0, 1.0, "main_atten")
    main "북진! {w}상병 [main] 지휘통제실에 용무 있어 왔습니다. {w}용무는 상황근무 교대입니다."
    fcaptain "왔니?"
    $FaceChange("main_atten", 1.0, 1.0, "main_salute")
    main "고생하십니다, 중대장님."
    "."
    return
