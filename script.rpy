# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

# 여기에서부터 게임이 시작합니다.
label start:
    centered "내가 원하는 건. {w}무엇이었을까."
    extend "\n어떤 것을 이루고자 그리도 노력했을까. {w}멈추는 일도, 흔들리는 일도 없이. {w}오로지 하나."
    extend "그 얼굴에 떠오른 미소를 보기 위해 제 몸을 채찍질하던 날들, 은. {w}과연 의미가 있었을까?"
    scene bg_room 
    show main_ord 
    with fade
    $SoundPlayer("blanket.ogg", 4.0)
    return
