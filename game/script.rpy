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
    prf "내일 암구호는 인수인계 파일에 적어놨고 {w}그 다음 건 내일 통신소대장님께서 퇴근하시기 전에 프린트해 주실 겁니다. {w}아. {w}이거 하나 드시겠습니까? {w}아까 고균영 상병이 주고 갔습니다."
    main "넌 왜 안 먹고?"
    prf "이 시간에 카페인 먹으면 저 진짜 내일 죽습니다. {w}잠 못 자서."
    main "그래. {w}두고 가면 내가 새벽 때 요긴하게 쓸게."
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
    "상황병 컴퓨터를 바라보았다. {w}근무를 서지 않았던 삼 일 동안 확인하지 않은 인수인계 사항을 점검했다."
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
    $SoundPlayer("knock.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    show sol_nom at left with dissolve
    $renpy.pause(1.0)
    $FaceChange("sol_salute", 0.0, 1.0, "sol_nom")
    "병사 α" "북진!"
    show cap_working at center with dissolve
    fcaptain "어~ {w}총기교대야?"
    $FaceChange("sol_nom", 0.0, 1.0, "sol_salute")
    "병사 α" "예, 그렇습니다."
    fcaptain "율호 하사."
    adjutant "예, 지금 열겠습니다."
    hide sol_nom
    hide cap_working
    $SoundPlayer("walk_slow.ogg")
    $SoundPlayer("lock_open.ogg", 1.0)
    $SoundPlayer("lock_open.ogg", 1.0)
    "지통실의 문을 열어놓은 채 잠시 기다렸다. {w}근무자 총기함에 총기를 시건하기 위해 병사들이 하나 둘 올라오다 이내 발걸음이 뚝 끊겼다."
    $SoundPlayer("lock_close.ogg", 1.0)
    $SoundPlayer("lock_close.ogg", 1.0)
    show cap_working
    fcaptain "근무자 신고 갔다 올게."
    main "맨 강당에서 하십니까?"
    fcaptain "응."
    main "부대일지 기입해 두겠습니다."
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
    show sergeant_working at center with dissolve
    adjutant "뭐야?"
    main "수신율 점검입니다. {w}바로 응신하겠습니다."
    $SoundPlayer("dial.wav", 1.0)
    $SoundPlayer("phone.wav", 2.0)
    "목소리" "통신보안. {w}군단 AOC 근무자 일병 ＠＠＠입니다."
    main "통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다. {w}ㅇㅇ대대 육군 레이더 체계 수신율 점검 응신입니다."
    "목소리" "ㅇㅇ대대 확인되었습니다. {w}고생하십시오."
    $SoundPlayer("teleclick.ogg", 1.0)
    adjutant "오늘은 되게 칼같이 하네. {w}평소에는 시간 안 지키고 아무떄나 걸었잖아."
    main "맞습니다. {w}예전에 한 번 전준태 하던 도중에 걸려오는 바람에 응신 못할 뻔 한 적도 한 번 있지 않았습니까."
    adjutant "응. {w}그때 너 진지 가 있는 사람들 무전 받는다고 전화 놓치고 나도 C4I 조치한다고 바빠서 사령님이 대신 전화해줬었잖아."
    main "아 진짜 그때 당시에는 짜증만 나고 되는 것 하나 없는 하루라고 생각했었는데 지금 와서 생각하니 그것도 나름 군생활 추억담이지 않겠습니까."
    adjutant "추억담이라... {w}너 전역 언제지?"
    main "80일 조금 안 되게 남았습니다."
    adjutant "이야... {w}거의 다 했네."
    main "그래도 아직 좀 남지 않았습니까. {w}더 열심히 하겠습니다."
    adjutant "잘 하고 있잖아. {w}늘 하던 대로만 하면 돼."
    main "([adjutant] 하사님... {w}저는 간부님들께서 생각하시는 것과는 다르게... {w}그렇게 좋은 사람이 아닙니다... {w}저는... {w}저는...)"
    main "좋게 봐 주셔서 감사합니다."
    "웃음을 지어 부끄러워함을 가장해 넘겼다."
    "모니터를 바라보았다."
    "육군 레이더 체계에도. {w}3군 통합 레이더 체계에도. {w}보고되지 않은 비행. {w}의문점을 남기는 비행은 잡히지 않고 있다."
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    show cap_working at left with dissolve
    adjutant "다녀오셨습니까?"
    fcaptain "예. {w}[main]아. {w}오늘 강조사항은 탄약고 근무자 실외온도 영하로 내려가면 보고하고 실내 근무 전환."
    play sound typing
    main "외곽 근무 온도 영하로 내려가면 초소 내에서 근무입니다."
    stop sound
    fcaptain "순찰자 접근 시 공무원증 확인 철저."
    play sound typing
    main "공무원증 확인 철저입니다."
    stop sound
    fcaptain "기본 근무자 복장 B형. {w}근무자간 복장 통일이 된 경우 추가 복장 착용 가능."
    play sound typing
    main "근무자간 통일 시 추가 복장 착용 가능입니다."
    stop sound
    fcaptain "응. {w}그거면 됐어."
    main "예. {w}바로 실시사항 올리겠습니다."
    $SoundPlayer("click.ogg", 2.0)
    adjutant "오늘은 금방 끝났습니다?"
    fcaptain "예. {w}이번에는 암구호도 제대로 알고 있고 문제 없었습니다."
    scene bg_black with blinds
    $renpy.pause(1.0)
    hide sergeant_working
    hide cap_working
    scene bg_zitong
    show main_unhat at right
    with blinds        
    $SoundPlayer("walk_slow.ogg")
    show sol_nom at center with dissolve
    "병사 α" "탄약고 투입입니다."
    main "불러주십니까?"
    play sound typing
    "병사 α" "사수에 상병 박현중, 부사수에 일병 윤정훈입니다."
    stop sound
    main "상병 박현중, 일병 윤정훈 맞습니까?"
    "병사 α" "맞습니다."
    main "예, 감사합니다. {w}고생하십시오."
    "병사 α" "고생하십시오."
    hide sol_nom 
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_black with blinds
    $renpy.pause(1.0)
    scene bg_zitong
    show cap_working at center
    with blinds
    $SoundPlayer("broadcast.wav", 2.0)
    fcaptain "\[지휘통제실에서 당직사령이 전파합니다. {w}육군 복무신조.\]"
    "목소리" "우리의 결의!" with vpunch
    fcaptain "\[우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.\]"
    "목소리" "우리는 국가와 국민에 충성을 다하는 대한민국 육군이다!" with vpunch
    fcaptain "\[하나, 우리는 자유민주주의를 수호하며 조국통일의 역군이 된다.\]"
    "목소리" "하나! {w}우리는 자유민주주의를 수호하며 조국통일의 역군이 된다!" with vpunch
    fcaptain "\[둘, 우리는 실전과 같은 훈련으로 지상전의 승리자가 된다.\]"
    "목소리" "둘!{w} 우리는 실전과 같은 훈련으로 지상전의 승리자가 된다!" with vpunch
    fcaptain "\[셋, 우리는 법규를 준수하며 상관의 명령에 복종한다.\]"
    "목소리" "셋!{w} 우리는 법규를 준수하며 상관의 명령에 복종한다!" with vpunch
    fcaptain "\[넷, 우리는 명예와 신의를 지키며 전우애로 굳게 단결한다.\]"
    "목소리" "넷!{w} 우리는 명예와 신의를 지키며 전우애로 굳게 단결한다!" with vpunch
    fcaptain "\[아, 여러분. {w}토요일 하루 고생 많았습니다. {w}주말에도 쉬지 않고 각자의 위치에서 노력하시는 여러분이 있기에 오늘 하루도 무사히 끝났습니다. {w}오늘은 토요일. {w}TV연등이 있는 날입니다.\]"
    fcaptain "\[22시까지 미비된 동작을 마치고 22:50분부터 23시까지, 23시 50분부터 00시까지 유동병력 허용하며 00시에는 취침에 들어갈 수 있도록 합니다. {w}TV연등 이외 연등 희망자는 연명부와 출입대장에 기입하시고 연등 종료 후 각층 당직사관에게 보고 후 생활관에 복귀하시길 바랍니다. {w}이상, 점호를 마치겠습니다.\]"
    "목소리" "편안한 밤 되십시오!!!" with vpunch
    hide cap_working
    show main_unhat at right with dissolve
    main "저, 부관님?"
    show sergeant_working at center with dissolve
    adjutant "어, 왜?"
    main "혹시 담배 한 까치만 피고 와도 되겠습니까?"
    adjutant "그래. {w}음어낭 이리 주고 갔다 와."
    $SoundPlayer("blanket.wav", 4.0)
    $FaceChange("main_atten", 2.0, 1.0, "main_unhat")
    show cap_working at left with dissolve
    $FaceChange("main_atten", 2.0, .5, "main_unhat")
    show main_atten at right with dissolve
    $FaceChange("main_salute", 2.0, .5, "main_atten")
    main "북진. {w}흡연 다녀오겠습니다."
    fcaptain "응~ {w}다녀 와."
    $FaceChange("main_atten", 2.0, .5, "main_salute")
    $renpy.pause(1.0)
    hide main_atten
    $SoundPlayer("walk_slow.ogg")
    $SoundPlayer("door.ogg")
    $SoundPlayer("door.ogg")
    scene bg_black with blinds
    $renpy.pause(1.0)
    scene bg_zitong
    show main_unhat at right
    show sergeant_working at center
    show cap_working at left
    with blinds
    $SoundPlayer("broadcast.wav", 2.0)
    "녹음된 목소리" "\[문자형 전파체계 신규 문자 수신 알림입니다.\]"
    play sound typing
    adjutant "보고드립니다. {w}참조점 32번 일대에서 미상 인원 2인이 근방 초소 근무자에 의해 식별. {w}수하를 실시하였으나 이에 불응하고 울타리 방향으로 도주. {w}한 명은 검은 모자에 갈색 티셔츠, 다른 한 명은 검은 티셔츠에 파란색 청바지 차림이라고 합니다."
    "부관님의 말씀과 대형 스크린에 띄워진 메모 프로그램을 바라보며 부대일지에 신속히 옮겨 적기 시작했다."
    play sound noise
    "목소리 α" "\[단륜간, 단륜간. {w}새부엌 송f신.\]"
    "전 직할대가 공유하는 무전망으로 ㅇㅇ대대를 호출하는 목소리가 흘러나왔다."
    $FaceChange("main_hand", 2.0, 1.0, "main_unhat")
    main "\[새부엌, 새부엌. {w}단륜간 송신.\]"
    play sound noise
    "목소리 α" "\[단륜간측 수신감도 어떠한지.\]"
    main "\[단륜간측 수신감도 삼삼, 수신감도 삼삼. {w}이상.\]"
    "목소리 α" "\[수신 양호.\]"
    main "(무전망으로 우릴 불렀다는건...)"
    play sound noise
    "목소리 α" "\[장검집, 장검집. {w}새부엌 송신.\]"
    "ㅇㅇ대대 신속대응조를 부르는 목소리. {w}아직 잠들지 않은 옛 후임의 목소리가 무전을 탔다."
    "목소리 β" "\[장검집 등장.\]"
    "목소리 α" "\[장검집측 수신감도 어떠한지.\]"
    play sound noise
    "목소리 β" "\[장검집측 수신감도 삼삼.{w} 수신감도 삼삼.{w} 새부엌측 수신감도 어떠한지.\]"
    stop sound
    $FaceChange("main_unhat", 2.0, .5, "main_hand")
    main "군단과 이어지는 무전망 개통 완료했습니다!"
    scene bg_black with blinds
    $renpy.pause(2.0)
    scene bg_zitong 
    show sergeant_working at center
    with blinds
    adjutant "[main]."
    show main_nem at right with dissolve
    main "부르...셨습...니까?"
    adjutant "괜찮아? {w}많이 피곤해?"
    main "괜찮습니다... {w}죄송합니다. {w}화장실 가서 찬물 한 번 뒤집어  쓰고 오겠-{w=.3}{nw}"
    play sound alert2
    hide main_nem  
    show main_unhat_sup at right
    main "으악!"
    $SoundPlayer("collapse.ogg", 1.0)
    $FaceChange("main_ita", 2.0, .5, "main_unhat_sup")
    show cap_working at left with dissolve
    fcaptain "[main]아, 괜찮아? {w}안 다쳤어?"
    $FaceChange("main_unhat_sha", 2.0, 1.0, "main_ita")
    "녹음된 목소리" "\[훈련상황 전파, 훈련상황 전파. {w}N18562호 미상항적. {w}N18562호 미상항적.\]"
    main "괘... 괜찮습니다."
    play sound typing
    "3군 통합 레이더 체계 홈페이지에 수신율 점검 내역을 올렸다."
    stop sound
    $SoundPlayer("click.ogg", 1.0)
    adjutant "그래도 잠은 확실히 깼지?"
    main "예..."
    "귀가, 얼굴이. {w}불타는 듯 뜨거웠다."
    scene bg_black with blinds
    $renpy.pause(2.0)
    scene bg_zitong 
    show main_unhat at right
    show sol2_nom at center
    with blinds
    "병사 α" "이[main] 상병님이십니까?"
    main "예."
    "병사 α" "2중대 일병 김윤하입니다. {w}교대하러 왔습니다."
    main "아, 네. {w}특이사항은 딱히 없고 위치전송 단말기는 오늘 주말이라서 주욱 안 될 것 같긴 한데 10시에 확인해보시고 보내지면 사령님께 보고드리면 될 것 같습니다."
    "병사 α" "그거 말곤 없습니까?"
    main "그렇습니다. {w}고생하세요."
    "병사 α" "고생하셨어요."
    $SoundPlayer("blanket.wav", 4.0)
    $FaceChange("main_atten", 2.0, 1.0, "main_unhat")
    show cap_working at left with dissolve
    $FaceChange("main_salute", 2.0, .5, "main_atten")
    main "북진! {w}중대장님. {w}퇴근해 보아도 되겠습니까?"
    fcaptain "응~ {w}고생 많았다. {w}가서 푹 쉬고~"
    $FaceChange("main_atten", 2.0, .5, "main_salute")
    $renpy.pause(1.0)
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0) 
    scene bg_ground 
    show main_atten at right
    with dissolve
    play sound wind
    "평화로운 주말 아침. {w}탑탑한 바람이 몸을 엤다."
    main "어으, 추워."
    $SoundPlayer("walk_slow.ogg")
    scene bg_resta_front 
    show oh_ang at right 
    show main_atten at center
    with dissolve
    oh "왜 이렇게 늦었어?"
    main "근무 중이었습니다."
    oh "근무 중이어도 이렇게 늦게 오는 게 맞아?"
    main "근무교대 시간이 7시 40분에서 50분 사이인데 아무리 서둘러도 지금 도착할 수 밖에 없지 않습니까."
    "알고 있었다. {w}죄송합니다. {w}앞으로 그러지 않겠습니다. {w}그 두 문장이면 쓸데없이 씨름할 일은 없다는 것을."
    "주말에 출근해 밤새도록 잠 한 번 제대로 자지 못하고 근무를 서다 찬 바람을 맞으며 인원들의 식사를 감독하는 일은 상당히 짜증나는 일이란 것을 경험으로 알고 있었다."
    "한참 전에 먹은 저녁식사 이후 아무것도 입에 대지 않은 채 에너지 음료를 급하게 들이킨 탓에 메슥거리는 속. {w}수면 부족으로 미친 듯이 떨려오는 눈꺼풀이며 나팔이 울려퍼지는 머릿속."
    "평소라면 생각하더라도, 입 밖으로 내지 않았을 말이 나도 모르는 사이에 흘러나왔다."
    oh "뭐?"
    main "아, 아닙니다. {w}죄송합니다. {w}빨리빨리 다니겠습니다."
    play sound sigh
    oh "하아... {w}ㅇㅇ아."
    main "상병 ㅇㅇㅇ."
    oh "뭐가 문제니?"
    main "죄송합니다!"
    oh "아니다. {w}고생했다. {w}손 씻고 밥 먹어라."
    $FaceChange("main_salute", 1.0, .5, "main_atten")
    "가볍게 고개를 끄덕이는 사관님."
    $FaceChange("main_atten", 1.0, .5, "main_salute")
    $SoundPlayer("walk_slow.ogg")
    play looping dish_wash
    scene bg_resta_in with dissolve
    "꾸역꾸역. {w}입 안에 음식을 밀어넣었다. {w}계속하여 나를 괴롭히는 속쓰림과 떨어진 혈압 탓에 이어지는 현기증은 혀가 아무런 맛도 느끼지 못하게 하였다."
    "주변을 돌아보았다. {w}설거지 소리. {w}저 멀리 문 너머에서 분주히 오가는 취사병들의 모습. {w}배식조들은 배식 임무를 마치고 남은 음식들을 부지런히 짬하우스로 옮기고 있었다."
    "가만히 앉아 식사를 하는 이는 나 혼자였다. {w}문득. {w}생각이 났다."
    scene bg_hallway_sepia
    show gwon_nem_sepia at center 
    show main_atten_sepia at right
    with fade
    main "고생하셨습니다, 권인호 상병님."
    gwon "응~ {w}[main]이구나. {w}일일명령하달 시작했니?"
    main "아직 아닙니다."
    gwon "어우, 다행이다. {w}후딱 신고하고 빨리 씻고 누워야지."
    main "고생하셨습니다."
    gwon "너도 일과 고생해. {w}있다 체단 끝나고 보자."
    main "안녕히 주무십시오."
    hide gwon_nem_sepia
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_resta_in2 with fade
    $SoundPlayer("metal.ogg", 1.0)
    $SoundPlayer("metal.ogg", .5)
    "퇴식구에 잔반을 버렸다."
    scene bg_black with fade
    $SoundPlayer("walk_slow.ogg", 2.0)
    stop looping
    $renpy.pause(2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg")
    scene bg_office
    show snipe_nom at right
    with fade
    show main_atten at center with dissolve
    $renpy.pause(1.0)
    $FaceChange("main_salute", 1.0, .5, "main_atten")
    main "북진."
    snipe "어."
    $FaceChange("main_atten", 1.0, .5, "main_salute")
    main "근무십니까?"    
    snipe "어."
    main "고생하십니다."
    $SoundPlayer("pen.ogg", 2.0)
    "사용일지에 서명하고 휴대폰을 꺼냈다."
    $FaceChange("main_salute", 1.0, .5, "main_atten")
    main "북진."
    snipe "ㅇㅇㅇ."
    $FaceChange("main_atten", 1.0, .5, "main_salute")
    main "예."
    snipe "사용일지랑 온도대장 서명 똑바로 해라."
    main "더 이상 실수하지 않습니다."
    snipe "그래."
    hide main_atten
    $SoundPlayer("walk_slow.ogg")
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway 
    show main_atten at right 
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    "무뚝뚝한 표정으로. {w}때로는 일그러진 모습으로 일관힌 채 불호령을 내리는 반장님. {w}그 분은 병사의 입장에서 다가서기 힘들고. {w}누구보다 엄하기만 한 존재이긴 하였으나 나는 알 수 있었다. {w}다친 채 추락하여 원래의 둥지로 돌아가지 못한 새를 거둬준 보금자리에서 첫 마디를 땠을 때가 있었기에."
    main "(하지만 그건 그거고... {w}무섭단 말이지.)"
    "울리는 발소리 하나 없는 복도. {w}형광등이 비추는 바닥. {w}진한 색의 실이 가득한 텍스 천장. {w}수 천 번은 마주했던 풍경이고. {w}또 앞으로 수 백먼은 마주하게 될 풍경."
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_daidai
    show main_atten at right
    with dissolve
    $renpy.pause(1.0)
    "벽에 걸린 액자를 들여다 보았다. {w}사진 속에서 웃고 있는 나. {w}그리고, 그리운 얼굴들. {w}그 아래 주욱 이어진 입가에 맴도는 이름들."
    "이 안에 위치한 모두가 자신의 자리에 서 최선을 다하고 있을 지금에. {w}나 홀로 길을 잃은 채 방황하고 있다. {w}객기를 부리며 지도도, 나침반도 챙기지 않은 채 망망대해로 나선 대가를 치루듯이. {w}나는 이름 모를 해역에서 표류하고 있다."
    "오가는 이 없는 복도. {w}천장에 매달린 형광등은 잠시도 한눈을 팔지 않은 채 규칙적으로. {w}깜빡, 깜빡. {w}하얀 숨을 토해내고 있다."
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_taba with fade
    $SoundPlayer("walk_slow.ogg", 2.0)
    show main_taba_nof at center with dissolve
    $Smoking(img="main", loc=1.0, rep=2, first = True)
    "탁한 연기가 눈가를 스쳤다. {w}목구멍이 타들어간다."
    main "(그러고 보니까... {w}언제였지.)"
    "전입 온 직후, 였던 것으로 기억한다."
    $Smoking(img="main", loc=1.0, rep=1)
    extend "\n부소대장님과의 면담을 마치고, 처음으로 찾은 흡연장. {w}담배를 물고, 불을 붙이는 것도. {w}그 연기를 빨아들이는 것조차도 서툴렀던 날."
    "아마도{w}, 그때{w}, 부소대장님은 {w}, 나에게 {w}, 돈 아깝게 {w}, 뭐하는 짓이냐. {w}라고 했었던가."
    "어지러움이 몰려온다. {w}백사장의 모래알처럼 버석거리고, 하나로 모이지 못한 채 낱낱이 유리되어 버린. {w}두 번 다시 한 편이 되지 못할 필름의 조각들은 썰물녘이 찾아온 해변가의 바닷물처럼 어디론가 쓸려나가 더 이상 남지 않았다."
    "남은 것은 현실. {w}차갑게 식은 철기둥의 감촉."
    $Smoking(img="main", loc=1.0, rep=1)
    "손에 쥔 담배가 서서히 줄어들어 간다."
    "담뱃재가 군화 위로 떨어져 내려 허연 얼룩을 만들어냈다."
    $Smoking(img="main", loc=1.0, rep=1)
    "감각이 잦아든다."
    $SoundPlayer("blanket.wav", 4.0)
    show main_sil at right with pixellate
    " 막연하게 퍼져나가던 이름모를. {w}형상없는 두려움에 가닥이 잡히고, 어린 아이가 장난 삼아 모든 색을 섞어 만들어 낸 색점토 모형 마냥 거무튀튀한 부정형의 일그러짐만을 내 보이던 그것이 그림자를 벗어내고 윤곽을 드러냈다."
    "모습을. {w}이름을 안다면 대처하는 것은 간단."
    "목소리" "네가 할 수 있을까? {w}다음 일주일. {w}과연?"
    $Smoking(img="main", loc=1.0, rep=1)
    main "할 수 있든, 없든. {w}해야만 해. {w}지금껏 그래 왔듯이."
    "목소리" "매일매일을 힘겨워하고. {w}꺾이려고 하는 주제에. {w}또 만용이라도 부리겠다는 거야? {w}그러다가 그 \'운\'이 끊기면 어쩌려고?"
    main "...그건..."
    "목소리" "지금이라도 말하는 게 어때?"
    extend "\'못하겠습니다\'." with vpunch
    extend "\'무리입니다\'." with vpunch
    extend "\'죄송합니다\'.{w} 를." with vpunch
    main "......."
    $Smoking(img="main", loc=1.0, rep=1)
    "목소리" "담배만 뻑뻑 피워대지 말고 뭐라도 말해 보라고, [main]."
    main "아직 한계가 온 건 아니야. {w}난... 이것보다 심한 수라장도 버텨냈다고."
    "목소리" "\'이것보다 심한\'? {w}야... {w}너 그거 설마 진심으로 한 말이냐? {w}그 땐 적어도 속내를 나눌만한 사람 한 둘이라도 있었지... {w}지금 여기서 너는 온전한 외톨이인데 정말로 지금이 옛날보다 낫다고 생각하는 건 아니지?"
    $Smoking(img="main", loc=1.0, rep=1)
    main "할 이야기는 그것 뿐이야?"
    "목소리" "더 이상 할 필요도 없을 것 같네. {w}그럼 한 번 고생해 봐. {w}어차피 오늘 하루 남았잖아? {w}천천히 고민하고... {w}또 실패해서... {w}몸부림치라고."
    main "그래... 격려 고맙다... {w}개XX야."
    hide main_sil with pixellate
    $Smoking(img="main", loc=1.0, rep=1)
    $SoundPlayer("putoff.wav", 2.0)
    $FaceChange("main_atten", 1.0, .5, "main_tabahand")
    $SoundPlayer("sigh.wav", 2.0)
    main "x같네 진짜..."
    "한 때 이 몸을 덮었던 근거없는 공포는 지금에 이르러선 물러갔다. {w}그 자리를 대신하여 엄습한 것은 자신. {w}스스로를 누구보다 잘 알고 있기에 세워진 장벽."
    "지난 경험이. {w}살아왔던 시간이. {w}내 발목을 붙잡아 끌며 전진하는 것을 방해했다. {w}과거 겪었던 일과 닮은, 혹은 동일한 시간이 내게 찾아올 떄마다. {w}나는 움츠러들 수 밖에 없었고 그에 따른 정당한 비판을 받아냈다."
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_black with Fade(2.0, 2.0, 0.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    centered "객관적으로 판단했을 때. {w}나로서는 이뤄낼 수 없는 목표. {w}그에 무리하게 도전하여 부딪히고, 파절되며. {w}고지로 올라서던 도중{p}추락하기를 반복하던 날들."    
    centered "나는 해낼 수 없다. {p}지금껏 해왔던 경험을 통해 증명된 사실. {w}그럼에도 나는 앞으로 나섰다. {w}가파른 절벽을 오르면서. {p}몇 번이고 넘어지고, 때로는 굴러 떨어지고. {w}상처로 뒤덮힌 몸을 악착같이 쥐어짜내며 능선을 등반했다."
    centered "내 옆에서. {w}앞에서. {w}또는 뒤에서. {w}끌어주고, 밀어주고, 같이 걸어주던. {p}그들이 곁에 있어 주었기에. {w}나는 정상에 위치한 \'무언가\'를 향해 발걸음을 옮기는 일을 포기하지 않을 수 있었다."
    centered "그러나 지금에 이르러, 그들 모두가 흩어지고. {w}나 역시 외따른 곳에 이른 지금."
    $blur_val = True
    centered "{size=50}{color=#B90000}내 도전은 의미가 없었다."
    centered "{size=50}{color=#B90000}대략 11개월에 걸친 나의 투쟁은 무위로 돌아갔고."
    centered "{size=50}{color=#B90000}그렇게 커다란 상처를 안은 채 끝 모를 바닥을 향한 추락이 시작되었다.{/color}{/size}"
    $blur_val = False
    show crack_glass at Position(xpos=240, ypos=300) with vpunch
    $SoundPlayer("shotcrash.ogg")
    show crack_glass2 at Position(xpos=911, ypos=360) with vpunch
    $SoundPlayer("shotcrash.ogg")
    show crack_glass3 at Position(xpos=475, ypos=573) with vpunch
    $SoundPlayer("shotcrash.ogg")
    play sound bleed
    scene bg_black with Fade(4.0, 1.0, 1.0, color="#B90000")
    stop sound
    show syms_logo with Dissolve(2.0)
    $renpy.pause(5.0)
    hide syms_logo with Dissolve(2.0)
    $renpy.pause(.3)
    centered "{size=50}=제공="
    show syms_slogan with Dissolve(1.0)
    $renpy.pause(1.0)
    show syms_logo2 with Dissolve(1.0)
    $renpy.pause(5.0)
    hide syms_slogan
    hide syms_logo2
    with dissolve
    centered "Indie Studio SYMS 장기 프로젝트"
    extend "\n{size=50}{font=SDMiSaeng.ttf}Unit 1. \'어느 상병의 이야기\'{/font}{/size}"
    scene bg_black with dissolve
    centered "꿈을 꾸었다."
    extend "\n그래, 그것은 틀림없는 꿈이었다."
    scene bg_hospital_sepia
    show main_young_sepia at center 
    with dissolve
    "내용은 기억나지 않는다. {w}그러나 병상에 누워 계신 할아버지는 어린 내 이마에 손을 얹은 채 분명히 어떤 말을 읊조리셨다."
    "내 기억 속에 남은 것은. {w}새하얀 병원 복도. {w}다르르, 하는 소리를 내며 할아버지의 뒤를 따르던 링거. {w}주사. {w}찡그려진 얼굴."
    "거의 대부분의 시간을 병원에서 보내시던 할아버지가 내 곁에서 떠나신지 벌써 10년도 넘어버렸다."
    "이제 와서는 남겨진 말도, 물건도 시간의 흐름에 바래어 본래의 모습을 일어버린 이금의 나날에 모습을 비추는 일이 거의 없던 할아버지께서 내게 무언가 전언을 남기기 위해 꿈속에 나타났던 것이다."
    "목소리" "ㅇ... 안... 나?"
    main "......."
    "목소리" "ㅇ... ...나? {w}식... ....때..."
    main "......."
    "먼 곳에서 아련히 들려오던 목소리가 현실감을 가진 채 귓가에 속삭여졌다."
    "목소리" "야~{w} 안 일어나냐? {w}점심 먹을 때 깨워달라 한 건 너잖아~ {w}먼저 간다~"
    main "어... {w}일어났어... {w}일어났어..."
    $SoundPlayer("blanket.wav", 4.0)
    scene bg_room
    show main_cloth at center
    show jeong_cloth at right
    with dissolve
    main "다른 애들은?"
    jeong "당연히 먼저 갔지."
    main "나 때문에 기다린 거야?"
    jeong "그래. {w}또 너 혼자가면 혼날 게 뻔하니까 기다려줬다."
    main "땡큐."
    jeong "가자. {w}늦겠다."
    $SoundPlayer("walk_slow.ogg")
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway 
    show go_cross at left
    with dissolve
    show jeong_cloth at right
    show main_cloth at center
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    go "식사 가십니까?"
    jeong "엉."
    go "ㅇㅇㅇ 상병님은 왜 일어나셨습니까?"
    main "밥 먹으려고."
    go "오우... {w}밥에 진심인 남자 뭐 그런 겁니까?"
    main "아마도?"
    go "같이 가십니까? {w}저도 아직 안 먹었습니다."
    jeong "그래."
    scene bg_resta_front 
    show snipe_working at right
    with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    show main_cloth at left
    show jeong_cloth at Position(xalign=.3, yalign=1.0)
    show go_nom_hat at center
    with dissolve
    $FaceChange("go_salute", 1.0, .5, "go_nom_hat")
    go "북진."
    snipe "밥 먹기 전에 손 깨끗하게 씻어라."
    $FaceChange("go_nom_hat", 1.0, .5, "go_salute")
    $SoundPlayer("walk_slow.ogg")
    play looping dish_wash
    scene bg_resta_in
    show go_nom at left
    show jeong_cloth at center
    show main_cloth at right 
    with dissolve
    go "어제 근무는 어땠습니까?"
    main "뭐... 별 거 없었어. {w}점호하고 상황조치훈련하고... 레이더 점검 응신하고..."
    go "별 일 없었나 봅니다?"
    main "응. {w}상황훈련 때 위치단말도 잘 되던데?"
    go "그거 드디어 됩니까?"
    main "응. {w}들어보니까 무전실 근무자가 퇴근할 때 무전기를 다 끄고 퇴근했었다더라."
    go "말이 됩니까? {w}그게?"
    main "나도 이상하다고 생각은 했는데 무전실 쪽 사람들은 선임들한테 인수인계 받을 때 그렇게 받았다고 하더라고."
    go "거기 무전기가 꺼지면 직할대망 전부가 불통인거 모른답니까?"
    main "그건 안 물어봤는데... {w}알고 있지 않을까? {w}기본적인 거니까."
    go "왠지 모를 거 같다는 생각이 강하게 듭니다..."
    "식기 세척기 소리에 갇힌 건물. {w}저 너머에서 이름 모를 일병 하나가 옷소매로 땀을 닦아내며 수세미로 식판을 닦아내고 있었다."
    "뚜껑 없는 세척기가 줄 지어진 식판을 집어 삼켜 거품을 깨끗히 닦아내면 카트 위에 차곡차곡 쌓아 밖의 건조기로 가져간다."
    "짬통에서 올라오는 음식물 쓰레기의 냄새. {w}세척기가 뿜어내는 찝찝한 증기. {w}해진 고무장갑을 뚫고 들어온 수돗물 탓에 퉁퉁 부르튼 손."
    main "저 사람들도 고생하네..."
    jeong "아 맞네. {w}넌 저거 해봤겠구나."
    go "그러고보니 기억납니다. {w}옛날에 스쳐가듯이 한 번 뵌 적 있는 것 같습니다."
    main "그랬나? {w}난 잘 기억이 안 나는데."
    jeong "저거 개짜증날 거 같은데."
    main "엉. {w}더럽고, 무겁고, 짜증나지."
    jeong "본부중대라서 다행이다... {w}나라면 저거 절대 못한다."
    main "막상 하면 해 볼만 해. {w}저거 하면 일과도 적당히 빼주고."
    go "일과를 뺴준다 말입니까?"
    main "훈련이나 병기본 평가 같은거 하고 있으면 어쩔 수 없지만 작업은 왠만해선 빼줬었어. {w}고생한다고."
    go "어우 그래도 전 하기 싫을 거 같습니다."
    main "근데 체력단련은 해야 해."
    go "가능합니까?"
    main "뜀걸음만 후딱 뛰고 다른 사람들 근력운동 할 때 살짝 빠지면 되지."
    jeong "그럼 땀범벅인 상태 그대로 밥 먹고 투입이야?"
    main "그런 셈이지."
    jeong "어으 소름끼쳐."
    go "주말이면 더 최악이지 않습니까?"
    main "개인정비시간이 줄어드니까 아무래도 그렇지? {w}아, 그래도 주말 식청조가 좋은 점 하나 있다."
    go "무엇입니까?"
    main "휴대폰. {w}주말에는 휴대폰을 일찍 받으니까 노래 들으면서 설거지 하거나 눈치껏 잠깐 잠깐 보거나 할 수 있어."
    go "어으."
    jeong "주말에도 세 끼 전부 같은 사람이 할 거 아냐."
    main "당연하지."
    jeong "으."
    main "다 먹었어?"
    go "전 다 먹었습니다."
    jeong "나도."
    main "일어날까?"
    jeong "엉."
    hide main_cloth
    hide jeong_cloth
    hide go_nom
    $SoundPlayer("walk_slow.ogg", 2.0)
    stop looping
    scene bg_resta_front
    show go_nom_hat at left
    show jeong_cloth at center
    show main_cloth at right
    with dissolve
    main "그럼 있다 보자."
    go "고생하십쇼."
    jeong "고생해."
    hide jeong_cloth
    hide go_nom_hat
    $SoundPlayer("walk_slow.ogg")
    "다른 이들은 먼저 생활관으로 향하였다."
    play sound wind
    main "...추워."
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_taba with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    show main_cloth_taba_nof at center with dissolve
    $Smoking(img="main_cloth", loc=1.0, rep=2, first = True)
    "잔류했던 졸음이 사라졌다. {w}더부룩한 속이 정리되며 머리가 개운해졌다."
    $Smoking(img="main_cloth", loc=1.0, rep=1)
    main "(일요일이라.)"
    show screen time
    show explain_scene 
    with dissolve
    centered "시간 시스템에 관하여"
    extend "\n앞으로 등장하는 선택지 중 일부는 게임 상에서의 시간을 소모하게 됩니다."
    extend "\n예를 한 번 들어 볼까요?"
    hide explain_scene with Dissolve(1.5)
    "이제 뭘 하면 좋을까?"
    menu:
        "px에 간다(+5m)":
            call go_px1 from _call_go_px1
    show explain_scene with dissolve
    centered "이와 같이 선택지 지문에 + 기호와 함께 시간이 표시되어 있는 경우 해당 이벤트를 진행한 이후 적혀있는 숫자만큼의 시간이 경과하게 됩니다."
    $main_inventory.add(taba)
    $bufftory.add(stress_minus)
    show screen inventory_button
    show screen map_view
    show screen buff_screen
    show screen status
    with dissolve
    #scene inven_back
    #show item_taba at Position(xpos=710, ypos=221)
    "어디로 갈까?"
    $evented = False
    $where_list.append(where)
    $where = "N/A"
    show explain_scene 
    show screen map_view
    with dissolve
    "어디로 갈까?"
    $evented = False
    $where_list.append(where)
    $where = "N/A"
    show explain_scene 
    show screen map_view
    with dissolve
    "어디로 갈까?"
    $evented = False
    $where_list.append(where)
    $where = "N/A"
    show explain_scene 
    show screen map_view
    with dissolve
    "어디로 갈까?"
    $evented = False
    $where_list.append(where)
    $where = "N/A"
    show explain_scene 
    show screen map_view
    with dissolve
    "어디로 갈까?"
    $evented = False
    $where_list.append(where)
    $where = "N/A"
    if len(where_list) > 5:
        $del where_list[5]
    show explain_scene 
    show screen map_view
    with dissolve
    "어디로 갈까?"
#   $SoundPlayer("buzzer.ogg", 1.0)
#   $SoundPlayer("teleclick.ogg", 1.0) 
   # "."
    #adjutant "이렇게 어중간한 시간에 갑자기 왠 수신율 점검?"
    #main "그러게 말입니다. {w}훈련 상활 걸 거 같은데 대기합니까?"
    #adjutant "그-{w=.3}{nw}"
    #"부관님의 말씀이 끝나기도 전이었다."
    scene bg_black with Dissolve(5.0)
    centered "오늘 하루 나는..."
    extend "\n[stress_val]만큼의 스트레스를 받았다."
    extend "\n[sat_val]만큼 만족했다."
    call status_check from _call_status_check
    call screen continued with Dissolve(1.0)
    "......."
    return

#(85, 35, 238, 216)