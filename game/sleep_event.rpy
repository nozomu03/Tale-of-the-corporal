init python:
    event('sleep_event1', ' now_week==2 and now_day == 5 and af_do==\"잠자기\" and evented == False', event.random(1.0), event.only(), priority=0)
    event('sleep_event2', ' now_week==2 and now_day == 5 and af_do==\"잠자기\" and evented == False', event.random(1.0), event.only(), priority=0)
    event('sleep_event3', ' now_week==2 and now_day == 5 and af_do==\"잠자기\" and evented == False', event.random(1.0), event.only(), priority=100)

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
    $evented = True
    $af_do = "_" + af_do
    return
  
label sleep_event2:
    main "으..."
    scene bg_hospital
    show hoyun_smi at center
    with fade
    hoyun "일어났냐."
    main "...김호윤... 병장님...?"
    hoyun "왜."
    main "정말 김호윤 병장님이십니까?"
    hoyun "...? {w}쓰읍... {w}이거 아무리 봐도 뇌진탕까지 겹친 거 같은데..."
    main "잘 못 들었습니다?"
    hoyun "아냐."
    show hoyun_smi at right with moveinleft
    $SoundPlayer("door.ogg", 2.0)
    extend "부소대장님. {w}ㅇㅇ이 정신 차렸습니다."
    $SoundPlayer("walk_slow.ogg", 2.0)
    show hoyun_smi at center
    show park_cross_hat at right
    with moveinright
    $renpy.pause(.3)
    $FaceChange("park_cross_smi", 2.0, .5, "park_corss_hat")
    park "여~ {w}ㅇㅇ~ {w}좀 괜찮냐~?"
    main "부소대장님..."
    "옅게 웃음을 짓고 있는 [park] 중사님."
    main "무슨 일이 있었던 겁니까?"
    park "뭐야, 기억 안 나?"
    main "예... {w}저는 그러니까..."
    park "혹한기 훈련 도중에 기절했잖아."
    main "기절... 말입니까?"
    hoyun "진짜 사람 놀래키는데는 재주가 있다니까."
    main "그러고보니 김호윤 병장님께서는 왜... 여기 계십니까...? {w}전역대기시지 않습니까?"
    hoyun "너 같으면 부사수가 훈련 받다가 쓰러졌다는데 싹 무시하고 룰루랄라 집에 갈 수 있겠냐? {w}내가 그런 사람으로 보여?"
    main "아닙니다."
    park "기억이 하나도 안 난다고?"
    main "그렇습니다."
    play sound sigh 
    park "그래도 정신 차려서 다행이다."
    main "감사합니다..."
    "꿈이라는 것을. {w}김호윤 병장님의 모습이 눈에 비쳤을 때부터 알고 있었다.{p}그러나, 마음 속에서부터 따뜻해져 오는 옛 정취의 파편은 눈을 감는다면. {w}고개를 흔든다면. {w}연못에 떨어진 돌맹이로부터 태어난 파문이 물에 비친 어렴풋한 형상을 지워내듯 산산히 흩어질 것만 같은 여린 것이어. {w}그저 똑바로 응시하는 것 밖에 할 수 없었다."
    "한 없이 닮게 베끼나, 결코 원품이 될 수 없는 거울 속의 상이라고 하여도. {w}찰나에 가까운 시간 속에서의 재회를 통해 직면한 문제들로부터 탈피하여 잠깐이나마 안락을 얻을 수 있었다."
    $stress_val -= 8
    $sat_val += 8
    $af_do = "_" + af_do
    $evented = True
    return

label sleep_event3:
    "안개가 낀다. {w}인지력에 먹구름이 드리우고, 기억에 결락이 생겨나기 시작한다. {w}꿈 없는 잠 속으로 빠져들며 이내 모든 감각이 빠른 속도로 옅어져 갔다."
    "소리도, 형체도, 광원도 존재하지 않는 방에 유폐된 것처럼 얼마나 넒게 펼쳐진지 모를 어둠에 잠겼다."
    "이곳에서 시간은 1분이 한 시간이, 때로는 1초가 되며 그 의미를 잃는다."
    "찰나. {w}어쩌면 수 시간.{w}그 이후에, 목소리가 들려왔다."
    $stress_val -= 3
    $sat_val += 3
    $af_do = "_" + af_do
    $evented=True
    return

