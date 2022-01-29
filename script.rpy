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
    show cap_working at right 
    with dissolve
    $SoundPlayer("knock.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    show main_atten at center with dissolve
    $FaceChange("main_salute", 1.0, 1.0, "main_atten")
    main "북진! {w}상병 [main] 지휘통제실에 용무 있어 왔습니다. {w}용무는 상황근무 교대입니다."
    fcaptain "왔니?"
    $FaceChange("main_atten", 1.0, 1.0, "main_salute")
    main "고생하십니다, 중대장님. {w}미안. {w}좀 늦었지?"
    show prf_nom at left with dissolve
    prf "아닙니다. {w}아직 50분 안 됐습니다. {w}딱 맞춰 오신 겁니다."
    main "특이사항은?"
    prf "없습니다. {w}아까 저녁 때 말씀하셨던 CCTV도 사관님께서 조치해주셨습니다."
    main "오키. {w}고생했다. {w}비문낭 이리 주고 가 봐."
    prf "여기 있습니다."
    main "CEOI 개수... {w}맞고... {w}약호자재랑 음어자재도 이상 없네. {w}암구호는?"
    prf "내일 암구호는 인수인계 파일에 적어놨고 {w}그 다음 건 내일 통신소대장님께서 출근하시는 대로 프린트해 주실 겁니다. {w}아. {w}이거 하나 드시겠습니까? {w}아까 고균영 상병이 주고 갔습니다."
    main "넌 왜 안 먹고?"
    prf "이 시간에 카페인 먹으면 저 진짜 내일 죽습니다. {w}잠 못 자서."
    main "그래. {w}두고 가면 내가 야간 근무 때 요긴하게 쓸게."
    prf "고생하십쇼."
    main "그래. {w}수고했다."
    $FaceChange("prf_salute", 0.0, 1.0, "prf_nom")
    prf "북진! {w}중대장님. {w}생활관 복귀해도 되겠습니까?"
    fcaptain "그래. {w}주말에 고생했어. {w}푹 쉬어."
    $FaceChange("prf_nom", 0.0, 1.0, "prf_salute")
    hide prf_nom
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    main "부관은 어디 갔습니까?"
    fcaptain "잠깐 담배."
    main "그나저나 일찍 출근하셨습니다?"
    fcaptain "중대장이 할 일이 좀 있어서 저녁 때부터 나와 있었어."
    main "고생하십니다..."
    fcaptain "[main]이도 고생해야지?"
    hide cap_working
    show main_atten at right with moveinleft
    "상황병 컴퓨터를 바라보았다. {w}근무를 서지 않았떤 삼 일 동안 확인하지 않은 인수인계 사항을 점검했다."
    main "(\'네, 여러분. {w}균영이에요. {w}근무 끝나고 나면 자기가 사용했던 자리는 자기가 청소하는 양심 있는 본부중대원이 됩시다. {w}인간적으로 간부님들도 보는 공간인데 먹은 쓰레기 버리고 가는 건 아니죠.{w}자기가 버린 게 아니라도 치워주는 배려심 넘치는 여러분이니 믿고 있겠습니다\'? {w}아 씨... {w}이거 내 이야긴거 같은데...)"
    "저번 근무 때 깜빡하고 선반에 올려놓은 채 치우지 않은 스트링 치즈 껍데기가 불현듯 머리에 스쳤다."
    $SoundPlayer("buzzer.ogg", .8)
    $SoundPlayer("teleclick.ogg", 1.0)
    main "\[통신보안. {w}ㅇㅇ대대 상황근무자 상병 [main]입니다.\]"
    "목소리" "\[2중대 탄약고 근무자 병장 박륜입니다. {w}현 시간 부 군단본청 상사 권한성. {w}상사 권한성 탄약고 초소 입영하십니다. {w}입영 목적은 당직 근무자 순찰입니다.\]"
    main "\[군단본청 상사 권한성. {w}목적은 순찰 맞습니까?\]"
    "목소리" "\[그렇습니다.\]"
    main "\[예, 감사합니다.\]"
    $SoundPlayer("teleclick.ogg", 1.0)
    fcaptain "뭐야, 순찰자야?"
    main "네. {w}군단본청 권한성 상사라고 합니다."
    $SoundPlayer("typing.ogg", 3.0)
    $SoundPlayer("click.ogg", 1.0)
    main "부대일지 남겼습니다."
    "외출, 외박, 휴가, 외진, 전역. {w}이 네가지 경우를 제외한다면 공적인 업무가 없는 이상 부대 바깥으로 나가는 게 불가능에 가까운 병사들과 달리 간부들은 평시라면 일과시간이 끝나면 퇴근하게 된다."
    "병사 입장에서는 단순히 \'짜증나는 것\' 내지는 \'귀찮은 것\'으로 취급되는 신속대응조나 당직근무를 광적으로 기피하는 간부가 존재하는 것이 이 때문도 있는 것이다."
    "오늘은 토요일. {w}본래라면 출근을 하지 않아도 상관없을 휴일. {w}평일에도 짜증날 근무를 토요일이라는 황금같은 시간에 서게 되었기에. {w}근무 교대가 이루어지는 이 때쯤 으레 이뤄지는 당직근무자 화상 회의도, 뜬금없이 걸려오는 전화도. {w}사전 약속도 없이 불시에 날아오는 무전도 없이 시간은 고요히 흘러갔다."
    $SoundPlayer("door.ogg")
    $SoundPlayer("door.ogg")
    $SoundPlayer("walk_slow.ogg", 2.0)
    show sergeant_working at left with dissolve
    adjutant "오, [main]. {w}오늘 근무야?"
    main "예, 그렇습니다. {w}밖에 많이 추운가 봅니다?"
    adjutant "응. {w}아직 본격적으로 겨울 시작하지도 않았는데 벌써 이렇게 춥네."
    main "이 맘 때면 딱 저 신병휴가 복귀할 때 즈음이었는데 작년에도 이렇게 추웠지 않았었습니까?"
    adjutant "그렇긴 한데... {w}왜 여기만 지구 온난화가 반대로 오는 것 같지?"
    hide sergeant_working
    hide main_atten
    "인트라넷에 접속해 국방일보를 살펴보았다. {w}즐겨보던 작가의 새 칼럼이 기고된 것을 확인하고 천천히 읽어 나갔다."
    show cap_working at center with dissolve
    fcaptain "[main]아. {w}너 디오라마에 관심이 있었니?"
    show main_atten at right with dissolve
    main "예. {w}제대로 된 정식 디오라마를 만들어 본 적은 없지만 용돈 모아서 비행기나 전차 프라모델을 만들곤 했습니다."
    fcaptain "그렇구나... {w}몰랐네."
    "상황 근무 도중의 병사는 훈련 상황. {w}혹은 실상황이 벌어지지 않는 이상 할 일이 그렇게 많지 않았다. {w}칼럼을 전부 읽은 후 멍하니 CCTV 화면을 바라보고 있었다."
    "전번 근무자가 밥을 먹는 동안 대신 근무를 서 주던 때까지는 기름이 섞여들어간 물처럼 무지개색으로 번들거리던 화면도 지금은 깨끗히 밤의 순찰로를 비추고 있다."
    fcaptain "근무자 신고 갔다 올게."
    main "맨 강당에서 하십니까?"
    fcaptain "응."
    main "실시사항 기입해 두겠습니다."
    fcaptain "부탁해~"
    hide cap_working
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    "등받이에 기댄 채 나도 모르는 사이 무너진 자세를 바로잡았다. {w}첫 근무 때처럼 갑작스레 찾아온 저혈압으로 간부님들꼐 걱정을 끼치지 않으려면 이런 사소한 것도 전부 신경써야 했다."
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("alert.ogg", 2.0)
    "육군 레이더 체계 수신기가 경보음을 토해냈다."
    main "확인하겠습니다!"
    $SoundPlayer("click.ogg", 2.0)
    adjutant "뭐야?"
    main "수신율 점검입니다. {w}바로 응신하겠습니다."
    $SoundPlayer("dial.wav", 1.0)
    $SoundPlayer("phone.wav", 2.0)
    "목소리" "통신보안. {w}군단 AOC 근무자 일병 ＠＠＠입니다."
    main "통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다. {w}ㅇㅇ대대 육군 레이더 체계 수신율 점검 응신입니다."
    "목소리" "ㅇㅇ대대 확인되었습니다. {w}고생하십시오."
    $SoundPlayer("teleclick.ogg", 1.0)
    #adjutant "이렇게 어중간한 시간에 갑자기 왠 수신율 점검?"
    #main "그러게 말입니다. {w}훈련 상활 걸 거 같은데 대기합니까?"
    #adjutant "그-{w=.3}{nw}"
    #"부관님의 말씀이 끝나기도 전이었다."
    #$SoundPlayer("broadcast.wav", 2.0)
    #"녹음된 목소리" "\[문자형 전파체계 신규 문자 수신 알림입니다.\]"
    #show sergeant_working at left with dissolve
    #adjutant "보고드립니다! {w}"
    "."
    return

