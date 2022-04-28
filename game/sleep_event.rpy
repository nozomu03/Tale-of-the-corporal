init python:
    event('first_saturday1', ' now_week==2 and now_day == 5 and af_do==\"잠자기\" and evented == False', event.random(1.0), event.only(), priority=0)

label sleep_event1:
    centered "그것은 아마, 옛 꿈."
    extend "\n기저에 잠들어 두 번 다시 떠오를 일 없으리라 여겼던 잔향."
    extend "\n동시에. {w}헌 떄의 현재이자 나를 가두었던 감옥."
    scene bg_school_sepia 
    show main_atten_sepia at right 
    with fade
    main "(여긴...)"
    "햇수로 따진다면 기껏해야 1년 반. {w}작년 1월 녘까지 나는 거진 3년에 걸쳐 이곳에 머물렀다."
    "문은 굳게 잠겨있다. {w}위를 창문 너머로 보이는 복도는 불이 전부 꺼져 있었다."
    main "(꿈 한 번 살벌하네...)"
    "두 번 다시 돌아오고 싶지 않았던. {w}뇌리에서 지워지지 않는 쇠사슬의 땅."
    "목소리" "선배. {w}여기서 혼자 뭐 해요?"
    $SoundPlayer("walk_slow.ogg")
    show extra_sil at right with dissolve
    main "......."
    "목소리" "선배?"
    main "어? {w}어. {w}불렀어?"
    "목소리" "일찍 일어나서 왜 밖에 계세요? {w}사감 만나면 어쩌려고요."
    main "그러네... {w}실습실로 가자."
    "아침 식사 시간이 되기 전까지 기숙사동에서 교실동으로 건너가기 위한 하늘다리의 전자잠금장치는 학생이 가진 카드로는 열 수 없도록 굳게 잠긴다. {w}이로서 명백해졌다. {w}이건 현실이 아니다. {w}그저 한 없이 비슷하게 베껴 투영한. {w}자그만 파문에도 이내 지워질 수면 너머에 상일 뿐."  
    "그럼에도. {w}그 안에서 스며 나오는 악취는. {w}손아귀에 쥐면 곧장 바스러지며 흩어질 것만 같은 모래알의 감촉은.{p}놀라울 정도로 똑같이 느껴졌다."
    scene bg_black with fade
    "꿈에서 깨려, 눈을 감았다. {w}갑작스레 잠깐의 현기증이 찾아왔다."
    "\'행복\'이란 것을 어떻게든 찾아내기 위해서 발버둥치던. {w}그 과정에서 벌어진 주변 상황에는 눈길조차 주지 않은 채 달려나갔던."
    "그 때 쌓아올려진 경험들이 지금까지도 직, 간접적으로 영향을 미치고 있는 지금. {w}감정 역시 시간 아래에서 자유롭지 못하니 언젠가에 이르게 된다면 사라질 터이나. {w}적어도 지금까지는 그럴 낌세조차 보이지 않았다."
    $stress_val += 10
    $sat_val -= 5
    $evented = False
    $af_do = ""
    return
  
label sleep_event2:
    main "으..."
    scene bg_hospital
    show hoyun_smi at right
    with fade
    hoyun "일어났냐."
    main "...김호윤... 병장님...?"
    hoyun "왜."
    main "정말 김호윤 병장님이십니까?"
    hoyun "...? {w}쓰읍... {w}이거 아무리 봐도 뇌진탕까지 겹친 거 같은데..."
    main "잘 못 들었습니다?"
    hoyun "아냐."
    $SoundPlayer("door.ogg", 2.0)
    extend "부소대장님. {w}ㅇㅇ이 정신 차렸습니다."

    return