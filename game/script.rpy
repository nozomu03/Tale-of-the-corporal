# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

# 여기에서부터 게임이 시작합니다.


label start:
    #scene bg_room2
    #call SpriteSystem
    #image main_ord_glitch:
    #    At("main_ord", glitching)
    #    pause .2
    #    At("main_ord", chromatic_offset)
    #    pause .3
    #    At("main_ord", glitching)
    #    pause .2
    #    At("main_ord", chromatic_offset)
    #    pause .3
    #    At("main_ord", glitching)
    #    pause .2
    #    At("main_ord", chromatic_offset)
    #    pause .3
    #    At("main_ord", glitching)
    #    pause .2
    #    At("main_ord", chromatic_offset)
    #    pause .3
    #    pause 1.0
    #    repeat
    #show main_ord_glitch at center with dissolve
    #$renpy.pause(3000)
    #"테스트메세지"
   # show para_text("aaaaaa")
    window hide
    scene bg_black
    centered "내가 원하는 건. {w}무엇이었을까."
    extend "\n어떤 것을 이루고자 그리도 노력했을까. {w}멈추는 일도, 흔들리는 일도 없이. {w}오로지 하나."
    extend "그 얼굴에 떠오른 미소를 보기 위해 제 몸을 채찍질하던 날들, 은. {w}과연 의미가 있었을까?"
    scene bg_room 
    show main_ord 
    with blur_transition
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
    "등받이에 기댄 채 나도 모르는 사이 무너진 자세를 바로잡았다. {w}첫 근무 때처럼 갑작스레 찾아온 저혈압으로 간부님들께 걱정을 끼치지 않으려면 이런 사소한 것도 전부 신경써야 했다."
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("alert.ogg", 2.0)
    "육군 레이더 체계 수신기가 경보음을 토해냈다."
    main "확인하겠습니다!"
    $SoundPlayer("click.ogg", 2.0)
    show sergeant_working at center with dissolve
    adjutant "뭐야?"
    main "수신율 점검입니다. {w}바로 응신하겠습니다."
    $SoundPlayer("dial.ogg", 1.0)
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
    hide screen time
    $stressAndSat()
    centered "반복. {w}어제는 오늘과. {w}오늘은 내일과."
    extend "\n매일매일이 같은. {w}모든 것이 뻔히 예상되는. {w}그렇기에 조그마한 실금이라도 난다면. {w}반드시 파절로 이어지는."
    extend "\n그 속에서 상처 입고, 상처 주며 2년이라는 시간을 살아왔다. {w}몇 번이고 깨어질 위기를 넘어서며 악착같이 헤엄쳐 졸업장을 받아냈다."
    centered "그리고 지금에 이르러. {w}나는 등치를 증오하고, 돌발을 두려워하며 살아간다."
    extend "\n무엇에도 속하지 못한 채. {w}나를 거두어주려 내밀어진 손을 쳐내고 홀로 떨며 만사의 핏대를 세운 채 경계하며."
    extend "\n내게 감정을 품은 이도 이내 질려 무덤덤히, 혹은 적개심만이 남은 채."
    extend "\n다른 것을 잃어버리는 것이 일상 내지는 당연한 것인 양 느껴지는 무렵이다."
    $SoundPlayer("broadcast.wav", 2.0)
    "당직사령" "\[아, 기상. 기상.{w} ㅇㅇ대대 장병 여러분 기상. {w}기상. {w}오늘 점호는 연병장, 연병장에 실시하겠습니다. {w}ㅇㅇ대대 장병 여러분들은 07시까지 전투복으로 환복 후 집합하시길 바랍니다.\]"
    scene bg_room with dissolve
    show main_cloth with wipeup
    go "\[전투지원중대 행정반에서 당직 부사관 상병 [go]이 전파합니다. {w}통합중대 인원들 점호 복장 착용해서 07시까지 연병장으로 나가주시길 바랍니다.\]"
    $SoundPlayer("blanket.wav", 4.0)
    $FaceChange("main_atten", 1.0, 1.0, "main_cloth")
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show go_nom at right
    with dissolve
    show main_atten at center with dissolve
    go "일어나셨습니까?"
    main "어..."
    $SoundPlayer("walk_slow.ogg", 2.0)
    play sound ambient
    scene bg_ground
    show main_atten
    with dissolve
    "날씨는 더 없이 맑았다. {w}새파란 하늘에는 뭉게구름 몇 점만이 한가로이 노닌다."
    "연병장을 내려다 보았다. {w}서둘러 나온 몇몇 이들은 이미 사열대를 기준점 삼아 줄 지어 서 있었다."
    "기억 속 남은. {w}언젠가와 똑같은 풍경."
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_ground2
    show main_atten at center 
    with dissolve
    "흘낏, 옆을 봤다. {w}똑같은 옷과, 똑같은 모자를 쓴 이들의 군집. {w}새벽꿈에 아스름히 비치었던 때와는 달리 사열대 정면이 아닌 왼편에 서게 되었다."
    "눈에 익은 얼굴들이 드문드문 보인다. {w}두 번 다시 마주치고 싶지 않다고 생각했던 이의 얼굴도. {w}간혹 가다 떠오르는 그리운 이의 얼굴도."
    "이제 와 돌이키면 너무나도 하찮은 것에서 피어난 불씨는 내 몸뚱이 하나만이 아닌 건물 한 층의 절반을 불태우고 나서야 사그라들었다."
    "아무리 정교하게 복원한다 하여도 한 번 불에 탄 것은 과거의 모습으로 돌아갈 수 없다."
    "...내가 그러하듯이."
    $timeCheck(0, 25)
    $SoundPlayer("walk_slow.ogg", 2.0)
    show cap2_working at right with dissolve
    cap2 "아, 20xx년 9월 XX일 아침점호는 ㅇㅇ대대 당직사령이 직접 실시한다.{p}뒤로 돌아! {w}전방에 힘찬 함성 3초간 실시!"
    "목소리" "아아아아아!!" with vpunch
    cap2 "구령조정 3회 실시!"
    "목소리" "부대 차려! {w}열 중 쉬어! {w}뒤로 돌아!"
    cap2 "육군 복무 신조!"
    "목소리" "우리의 결의!" with vpunch
    cap2 "우리는 국가와 국민에 충성을 다하는...{w}{nw}"
    scene bg_black with blinds
    $renpy.pause(1.0)
    scene bg_ground2
    show main_atten at center
    show cap2_working at right
    with blinds
    $timeCheck(0, 5)
    cap2 "지금부터 국군 도수체조를 실시한다. {w}체조는 1번 다리 운동부터 12번 숨쉬기 운동까지 방송 반주에 맞춰 2회 반복 실시한다. {w}방송 반주가 나올 때까지 잠시 대기할 수 있도록."
    main "먼저 간다."
    show go_nom at left with dissolve
    go "예. {w}오늘도 고생하십시오."
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    show bg_resta_front 
    show main_atten 
    with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_resta_in 
    show main_unhat at center
    with dissolve
    "목소리" "ㅇㅇ."
    main "예."
    $SoundPlayer("walk_slow.ogg")
    show sang_smi at right with dissolve
    main "너였구나."
    sang "어때. {w}본부 생활은?"
    if sat_val >= 1:
        main "뭐... {w}나쁘진 않아.."
    else:
        main "뭐... {w}그냥 그렇지."
    sang "에효... {w}미안하다."
    main "아냐, 내가 말도 잘못하고... {w}생각도 잘못한 탓인 걸. {w}식청이야?"
    sang "응."
    main "고생하네."
    sang "넌 근무?"
    main "응."
    sang "그저께도 근무지 않았어?"
    main "이번에 오랜만에 요원화 훈련 하잖아. {w}본부중대 근무 인원 중 절반 이상이 21년도 전반기 군번이거든."
    sang "왜 그렇지? {w}아, 취사병?"
    main "어."
    "목소리" "{size=30}구상언 병장님! {w}물 다 채웠습니다!"
    sang "{size=30}어~ {w}전원 올려! {w}나도 지금 갈게!{/size} {w}가 봐야겠다. {w}근무 힘 내."
    main "너도."
    play looping dish_wash
    hide sang_smi 
    $SoundPlayer("walk_slow.ogg")
    "멀어져 가는 뒷모습을 바라보았다. {w}그것은, 엄연한 잘못이었다. {w}오판, 따위가 아니었다."
    "제아무리 튼튼하게 꿰매진 단추라 해도 어긋나게 채웠다면 미약한 힘으로도 터져 버리듯. {w}첫 발걸음부터 꼬여버려 아슬아슬하게 이어져온 줄타기는 감정에 휘둘려 무심코 내뱉아버린 한 마디에 의해 붕괴되었다."
    "오해를 풀 시간. {w}사과를 건낼 시간. {w}\'기다림\'이라는 선택지 역시 있었겠지만. {w}내게 내비쳐진 시선이 두려워 그 굴에서 도망친 나."
    "내게 내려져 마땅한 처벌을 담담히 받아들이지 못한 채 도주했기에. {w}박리되어 어정쩡히 동결된 관계는 선뜻 다가가기 힘든 복잡한 모습을 얻고 말았다."
    main "(고맙다... {w}진심으로.)"
    $renpy.pause(1.0)
    hide main_unhat
    $SoundPlayer("walk_slow.ogg")
    scene bg_resta_in2 
    show main_unhat at center
    with dissolve
    $SoundPlayer("metal.ogg", 1.0)
    $SoundPlayer("metal.ogg", .5)
    sang "잘 가."
    main "있다 점심 때 보자."
    sang "응."
    "얼굴이. {w}세척기의 증기에 파묻혀 지워졌다."
    hide main_unhat
    $SoundPlayer("walk_slow.ogg", 2.0)
    stop looping
    scene bg_resta_front
    show main_atten at center 
    with dissolve
    $timeCheck(0, 15)
    "멀리서 국군 도수체조 방송이 들려온다. {w}발걸음을 재촉했다."
    play sound running
    hide main_atten
    #show main_gaer at center with dissolve
    scene qquari main at blur with Dissolve(3.0)
    $renpy.pause(4.0)
    play looping gasp
    main "하아... 하아..."
    stop looping
    show park_gear_ang_sepia at right with dissolve
    park "ㅇㅇㅇ."
    main "상병... {w}ㅇㅇㅇ"
    park "고작 그거야? {w}보여 준다면서. {w}해보겠다면서. {w}40km... 꿋꿋히 완주해 보겠다면서!"
    main "아직... {w}아직... {w}괜찮습니다..."
    show explain_scene with dissolve
    centered "그날, 나는 행군을 완주하지 못하였다."
    extend "\n다시금 엄습해 온 어깨 통증은 날 무릎 꿇렸고, 결국 군장을 주임원사님 차에 싣고서 단독군장에 방독면만을 맨 상태로 행군을 마쳤다."
    extend "\n그로 인한 어떠한 불이익도 받지 않았으나 그 사실은 지금까지도 잔류하여 시시때떄로 이 마음을 혼탁케 해 왔다."
    $SoundPlayer("telering.wav", 1.5)
    $SoundPlayer("teleclick.ogg", 1.0)
    scene bg_zitong
    show main_unhat at right
    with dissolve
    main "\[통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다.\]" 
    "목소리" "\[군단 무전실 근무자 상병 ㅁㅁㅁ입니다. {w}직할대망 교전 가능하겠습니까?\]"
    main "\[예. {w}바로 준비하겠습니다."
    $FaceChange("main_hand", 2.0, 1.0, "main_unhat")
    extend " 준비 완료되었습니다. {w}먼저 무전 부탁드립니다.\]"
    "목소리" "\[보내겠습니다.\]"
    play looping noise
    "목소리" "\[단륜간, 단륜간. {w}새부엌 송신.\]"
    main "\[단륜간 등장.\]"
    "목소라" "\[단륜간 측 수신감도, 수신감도 어떠한지.\]"
    main "\[단륜간 측 수신감도 삼삼. {w}새부엌측 수신감도 어떠한지.\]"
    "목소리" "\[새부엌 측 수신감도 삼삼. {w}이상 교신 끝.\]"
    stop looping
    $FaceChange("main_unhat", 2.0, 1.0, "main_hand")
    "목소리" "\[관등성명 여쭈어 봐도 되겠습니까?\]"
    main "상병 ㅇㅇㅇ. {w}ㅇㅇㅇ입니다."
    "목소리" "군단 무전실 근무자 상병 ㅁㅁㅁ이었습니다."
    main "아, 저 혹시 오늘 음어자재 교신은 몇 시 쯤에 하십니까?"
    "목소리" "아... 전문 준비되는 대로 다시 전화 드리겠습니다."
    main "예, 고생하십시오."
    main "고생하십시오."
    $SoundPlayer("teleclick.ogg", 1.0)
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("enter.wav", 1.0)
    "돌이켜보면. {w}지금까지 있었던 일은 마치 한 편의 백일몽과 같은. {w}한 번 깨어버리면 두 번 다시 되돌아갈 수 없는 환상과도 같은 것이었다."
    "간부가 아닌 병사로 징집된 이의 군생활에서 1년이라는 시간이 가지는 무게는 결코 가볍지 않다. {w}아무리 하루하루를 보내도 끝나지 않을 것만 같은 까마득히 멀기만 한 전역이라는 이름의 결말까지 2/3에 해당하는 시간이기에."
    "찾아왔던 꿈이 마음 속에 자그마한 파문 하나만을 남기고 흩어지듯이. {w}12개월 어치의 과거는 어렴풋한 감정 덩어리와. {w}아스라한 추억과. {w}결코 지워지지 않을 상흔만을 남겼다."
    "고등학교에 입학하기도 전. {w}지금과는 비교도 못할 정도로 미숙하던 시절에 이별으로. {w}헤어짐으로 끝맺음 지어지지 않는 만남은 없음을. {w}그렇기에 관계가 끊어지기 전에. {w}그 사람이 내 눈 앞에 있을 때 보일 수 있는 최선의 모습을 보여한다는 것을 배웠었다."
    "직접 두 눈으로 목도했던 이별 덕분에. {w}나는 깨달았다. {w}...고 생각했었다."
    main "(멍청한 자식...)"
    "안개는 걷혔고, 부옇게 흐려져있던 시야는 또렷한 상을 되찾았다. {w}지금껏 느낄 수 없어썬 진실이 내게 휘몰아쳤고. {w}애써 세워두었던 보루는 폭풍에 휘말려 무너졌다."
    main "(아아... {w}날씨 한 번 좋네...)"
    $SoundPlayer("telering.wav", 1.5)
    $SoundPlayer("teleclick.ogg", 1.0) 
    main "\[통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다.\]"
    "목소리" "\[통신보안. {w}무전실 근무자 상병 ㅁㅁㅁ입니다. {w}전문 준비 완료되서 연락드렸습니다.\]"
    $FaceChange("main_hand", 2.0, 1.0, "main_unhat")
    main "\[예. {w}무전 넣어주십시오.\]"
    $SoundPlayer("teleclick.ogg", 1.0)
    play looping noise
    "목소리" "\[단륜간, 단륜간. {w}새부엌 송신.\]"
    main "\[단륜간 등장.\]"
    "목소리" "\[새부엌 측에 17어수, 17어수 전문 있음.\]"
    main "\[수신 양호. {w}송신 바람.\]"
    "목소리" "\[다음은 첫 번째 줄 전문 구분. {w}"
    play looping2 pen
    extend "둘, 칠, 아홉, 삼 하나. {w} 삼, 오, 둘, 공. {w}넷, 오, 둘, 삼, 하나...\]"
    window hide
    $renpy.pause(1.0) 
    "목소리" "\[... 오, 넷, 팔, 삼. {w}이상 {nw}"
    stop looping2
    extend "17어수 전문 송신 끝.\]"
    main "\[수신 양호.\]"
    stop looping
    $FaceChange("main_unhat", 2.0, 1.0, "main_hand")
    main "어디 보자..."
    show code1 at center_true with dissolve
    "음어자재를 꺼내 전문을 받아 적은 종이 옆에 나란히 놓았다."
    $SoundPlayer("pen.ogg", 2.0)
    show code2 at center_true with dissolve
    hide code1
    $renpy.pause(1.0)
    $SoundPlayer("pen.ogg", 2.0)
    show code3 at center_true with dissolve
    hide code2
    $renpy.pause(1.0)
    $SoundPlayer("pen.ogg", 2.0)
    show code4 at center_true with dissolve
    hide code3
    $renpy.pause(1.0)
    $SoundPlayer("pen.ogg", 2.0)
    show code5 at center_true with dissolve
    hide code4
    $FaceChange("main_hand", 2.0, 1.0, "main_unhat")
    $SoundPlayer("dial.ogg", 1.0)
    $SoundPlayer("phone.wav", 1.0)
    "목소리" "\[통신보안. {w}군단 무전실 근무자 상병 ㅁㅁㅁ입니다.\]"
    main "\[통신보안. {w}ㅇㅇ대대 상황근무자 상병 ㅇㅇㅇ입니다. {w}방금 주셨던 전문에 대한 답이 준비되서 연락드렸습니다.\]"
    "목소리" "예. {w}바로 불러 주십시오."
    play looping noise
    main "\[새부엌, 새부엌. {w}단륜간 송신.\]"
    "목소리" "\[새부엌 등장.\]"
    main "\[단륜간 측에 13어수 전문 있음.\]"
    "목소리" "\[송신 바람.\]"
    main "\[다음은 첫 번째 줄 전문 구분. {w}칠, 둘, 아홉, 삼. {w}여섯, 오, 칠, 삼....\]"
    window hide
    $renpy.pause(1.0)
    main "\[여섯, 넷, 삼, 하나. {w}이상 13어수 전문 송신 완료.\]"
    "목소리" "\[수신 양호. {w}이상 교신 끝.\]"
    stop looping
    $FaceChange("main_unhat", 2.0, 1.0, "main_hand")
    "목소리" "\[관등성명 한 번 다시 여쭤봐도 되겠습니까?\]"
    main "ㅇㅇ대대 상병 ㅇㅇㅇ입니다."
    "목소리" "군단 무전실 근무자 상병 ㅁㅁㅁ이었습니다. {w}고생하십시오."
    main "고생하십시오."
    $SoundPlayer("teleclick.ogg", 1.0)
    hide code5
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("enter.wav", 1.0)
    tie "ㅇㅇ아."
    main "상병 ㅇㅇㅇ."
    tie "CEOI 어떻게 됐어?"
    main "아까 전에 일일상황평가회의 끝나자 마자 제영이랑 통신소대장이 와서 프린트 해 줬습니다. {w}중대 배부는 오전 중에 끝낸다고 했습니다."
    tie "그럼 넌 가지고 있지 지금?"
    main "예."
    tie "화이트보드는?"
    main "최신화 했습니다."
    tie "진짜?"
    main "예.{w} 아까 받자마자 최신화 했습니다." 
    tie "아니기만 해 봐."
    $SoundPlayer("walk_slow.ogg", 2.0)
    tie "진짜네?"
    main "지난 번에 통신소대장이 근무자 전체 대상으로 교육했었습니다. {w}있다가 점심시간 때 제원값만 싸악 바꾸면 됩니다."
    tie "그렇구만."
    "음어자재 교신을 마지막으로 오전 중에 끝내 놓아야 할 일을 전부 마쳤다."
    main "흐아... {w}그래도 오늘은 본청에서 전화를 제때제때 받아 줘서 다행입니다."
    tie "저쪽도 오늘은 한가한가보지."
    main "매일 한가했으면 좋겠습니다."
    tie "그러게... {w}하루면 될 일이 2~3일씩 질질 끌리는 것도 대부분 본청이 바빠서니까..."
    $now_h = 10
    $now_m = 0
    show screen time with dissolve
    tie "아... 오늘 시간 진짜 안 가네."
    main "(몇 시 길래 그러시지? {w}10시? {w}진짜 얼마 안 됐네.)"
    main "그러게 말입니다. {w}아직 점심 때도 안 됐습니다."
    tie "한 건 많은데 시간은 더럽게 안 가고... {w}날씨는 맑고..."
    "보통 후번초가 점심 교대 하러 와 주는 시간이 11시 50분 쯤임을 고려했을 때 짧게 잡아도 1시간 30분이 넘는 시간이 남았다."
    tie "ㅇㅇ아."
    main "상병 ㅇㅇㅇ."
    tie "관등성명 그렇게 계속 안 대도 돼. {w}계속 대화하고 있었잖아. {w}그냥 \'네\'라고 대답만 하면 돼."
    main "알겠습니다."
    tie "전역 전 휴가 얼마나 남았니?"
    main "저 11주 정도 남았습니다."
    tie "11주... {w}77일... {w}하... {w}내가 왜 장교를 해서..."
    main "얼마나 남으셨습니까?"
    tie "글쎄다..."
    main "◇◇대대 작전장교랑 동기시지 않습니까?"
    tie "조원우 중위님? {w}아니야. {w}조원우 중위님이 나보다 1년 먼저 임관하셨어."
    main "아... {w}20군번이십니까?"
    tie "응."
    main "저랑 비슷한 때 입대하셨습니다."
    tie "왜? {w}맞먹게?"
    main "아닙니다."
    tie "에효... {w}부럽다 부러워. {w}나가면 뭐하게?"
    main "아직 좀 남아서 구체적으로 생각하진 않았습니다. {w}아마 글 쓰거나 공부 좀 더 해서 프로그래머 하지 않겠습니까."
    tie "대학 가게?"
    main "한 학기만 하고 휴학했지만 가긴 했습니다."
    tie "어디?"
    main "실업계 출신이라 수능을 안 본 바람에 방통대 들어갔습니다."
    tie "거기 졸업하기 힘들다던데."
    main "열심히 해야하지 않겠습니까."
    tie "그래, 힘 내라."
    $timeCheck(0, 5)
    main "(이제... {w}밥 먹을 때까지 뭐 하지?)"
    $where = ""
    $evented = False
    menu:
        "독서(+20m)":
            $what = "독서"
        "주특기 공부(+20m)":
            $what = "주특기 공부"
        "전공 공부(+20m)":
            $what = "전공 공부"
    call day2_checker
    $SoundPlayer("broadcast.wav", 2.0)\
    "녹음된 목소리" "\[문자형 전파체계 신규 문자 수신 알림입니다.\]"
    main "확인하겠습니다!"
    $SoundPlayer("running.wav", 2.0)
    $SoundPlayer("click.ogg", 2.0)
    tie "뭐야?"
    main "군용 민간통신장비 점검 응신 요청입니다! {w}대상에 ㅇㅇ대대도 포함입니다! {w}제가 무전 넣겠습니다."
    tie "부탁해~"
    $SoundPlayer("running.wav", 2.0)
    $FaceChange("main_hand", 2.0, 1.0, "main_unhat")
    play looping noise
    main "\[장검집, 장검집. {w}단륜간 송신\]"
    $renpy.pause(1.0)
    main "\[장검집, 장검집. {w}단륜간 송신\]"
    "목소리" "\[장검집 등장.\]"
    main "\[장검집 측. {w}사제망 전송 바람.\]"
    "목소리" "\[수신 양호. {w}바로 전송하겠음.\]"
    main "\[양호. {w}이상 교신 끝.\]"
    $FaceChange("main_unhat", 2.0, 1.0, "main_hand")
    stop looping
    $SoundPlayer("alarm.ogg", 3.0)
    play sound rolling
    main "확인해보겠습니다!"
    $SoundPlayer("click.ogg", 2.0)
    main "정훈장교님?"
    tie "왜?"
    main "c4i 체계 점검 응신해달라고 합니다."
    $SoundPlayer("walk_slow.ogg", 2.0)
    show tie_nom at center with dissolve
    main "제목에 c4i 체계 점검 응신이라고 적고 내용은 쓰지 않은 채로 보내라고 하는데 어떻게 합니까?"
    tie "내가 할게. {w}잠깐만."
    $SoundPlayer("typing.ogg", 2.0)
    $SoundPlayer("enter.wav", 1.0)
    main "갑자기 몰아칩니다."
    tie "그러{w=.3}{nw}"
    $SoundPlayer("telering.wav", 1.5)
    $SoundPlayer("teleclick.ogg", 1.0)
    main "\[통신보안. {w}ㅇㅇ대대 상황근무-{w=.3}{nw}"
    "목소리" "\[아, 네... {w}군단 대침투 장교인데요. {w}정작과장님 안 계시나요?\]"
    main "\[잠시만 기다려 주십시오.\] {w}정작과장님!"
    "정작과장" "왜?"
    main "군단 대침투 장교한테 전화왔는데 넘겨드리면 되겠습니까?"
    "정작과장" "어, 넘겨줘."
    main "\[지금 전환해 드리곘습니다.\]"
    $SoundPlayer("dial.ogg", .4)
    $SoundPlayer("teleclick.ogg", 1.0)
    hide screen time
    scene bg_black with blinds
    centered "군대에서의 시간은 다른 어느 곳에서보다 더디게 흐른다고들 한다."
    extend "\n틀린 말은 아니었다. {w}1년 반이라는 시간이. {w}한 달이. {w}일주일이."
    extend "\n이토록이나 긴 시간이란 것을 처음으로 느끼게 되었으니까."
    extend "\n거꾸로 매달아도 국방부 시계는 돌아간다는 말이 시사하듯."
    extend "\n매 순간순간에 흘러가는 모래알 같은 시간들이 모여 끝나지 않을 것만 같은 하루를 채워 나간다."
    extend "\n창문 밖으로 해가 뉘엿이는 것을 보고서도 1시간여. {w}12시간 동안의 상황병 근무가 끝났다."
    $now_h = 19
    $now_m = 50
    scene bg_zitong
    show jeong_atten at center
    show main_atten at right
    with blinds
    main "어우 씨, 죽는 줄 알았네."
    jeong "괜찮아?"
    main "아니... {w}안 괜찮은 것 같아... {w}속 쓰려..."
    jeong "휴게실에서 뭐라도 좀 먹어."
    main "라면 하나 끓이려고."
    jeong "특이사항은?"
    main "탄약고 근무자들 CEOI 배부했고, 화이트보드도 최신화 했고 제원도 다 바꿨어."
    jeong "오키. {w}사령님은?"
    main "5대기 강평 가셨어. {w}점검일지는 올렸고."
    jeong "사령님 누구시지?"
    main "전투지원중대장님."
    jeong "고생했어. {w}쉬어."
    main "욕 봐."
    $FaceChange("main_salute", 2.0, .5, "main_atten")
    main "북진! {w}상병 이지민 근무 마치고 복귀하겠습니다!"
    show sergeant_working at left with dissolve
    adjutant "그래~ {w}푹 쉬고 내일 보자."
    $FaceChange("main_atten", 2.0, .5, "main_salute")
    main "고생하십시오."
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show main_atten at right 
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_bath
    show main_atten
    with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_taba_night
    show main_tabahand
    with dissolve
    $Smoking(img="main", loc=1.0, rep=2 )
    main "(별이 하나도 없네...)"
    $Smoking(img="main", loc=1.0, rep=4)
    "목소리" "ㅇ~ㅇ~아~"
    main "...?"
    zoo "왁! {w=.3}{nw}" 
    hide main_tabahand
    show zoo_smi at Position(xalign=.4, yalign=1.0)
    show main_tabahand_sup at center
    with vpunch
    $FaceChange("main_tabahand", 1.0, .5, "main_tabahand_sup")    
    $FaceChange("main_tabahand_sal", 1.0, .5, "main_tabahand")    
    main "북진."
    zoo "그래."
    show zoo_smi at left with moveinright
    $FaceChange("main_tabahand", 1.0, .5, "main_tabahand_sal")
    $FaceChange("zoo_taba_nof", 0.0, 1.0, "zoo_smi")
    $Smoking(img="zoo", loc=0, rep = 2, first=True)
    if what == "전문하사":
        zoo "근무 끝났어?"
        main "예. {w}막 퇴근했습니다."
        zoo "고생했다."
        $stress_val -= 3
    main "[zoo] 하사님, 퇴근 안하셨습니까?"
    zoo "이제 해야지."
    main "지금까지 일 하신 겁니까?"
    zoo "응. {w}예비조 갔다 와서 하려고 했었는데 오늘 작업 때문에 못했거든."
    main "작업 있었습니까?"
    zoo "응. {w}치장창고 정리하라고 해서. {w}이제 퇴근해야지."
    main "고생하셨습니다."
    $Smoking(img="main", loc=1, rep = 1)
    main "백신 호송도 빨리 끝났으면 좋겠습니다."
    zoo "그러게..."
    $Smoking(img="zoo", loc=0, rep = 1)
    if what == "전문하사":
        zoo "넌 근무 언제까지야?"
        main "금요일까지 쭉입니다."
        zoo "백신호송에 요원화 훈련에... {w}간부도 병사도 죽어 나가는구나."
        main "그러게 말입니다... {w}육지검도 받아야 하고... {w}호국도 해야합니다..."
        zoo "하아... {w}그래도 그것만 끝나면 혹한기까지 큰 건 없다."
        main "그럼 저도 집에 갈 수 있습니다..."
        zoo "언제 가는데?"
        main "11월 초에 나갑니다."
        zoo "이야, 다 했네."
        main "감사합니다."
        $stress_val -= 3
    zoo "오늘은 좀 흐리네."
    main "구름도 많습니다..."
    zoo "비 오는 거 아니겠지... {w}비 오면 일 나는데..."
    main "어우, 끔찍할 거 같습니다... {w}그럼 훈련 연장될 수도 있지 않겠습니까/"
    zoo "에이, 설마... {w}그렇게까지 되겠어?"
    $Smoking(img="main", loc=1, rep = 1)
    $SoundPlayer("putoff.wav", 2.0)
    $FaceChange("main_atten", 1.0, .5, "main_tabahand")
    $renpy.pause(1.0)
    $FaceChange("main_salute", 1.0, .5, "main_atten")
    main "북진! {w}먼저 가 보아도 되겠습니까?"
    zoo "응, 그래. {w}고생했어. {w}내일 보자."
    $FaceChange("main_atten", 1.0, .5, "main_salute")
    $renpy.pause(.5)
    hide main_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_black with Fade(4.0, 1.0, 1.0, color="#000000")
    centered "군대에서의 하루하루는 똑같은 것의 반복이라고들 한다."
    extend "\n오늘은 어제 한 것. {w}내일은 오늘 한 것."
    extend "\n훈련 주간에도 이 사실은 변하지 않는다. {w}소위 말하는 \'짬을 먹었다\'라는 표현이 생겨난 이유이다."
    extend "\n아무리 덜떨어진 사람이라고 해도. {w}머리가 따르지 않는 사람이라 해도."
    extend "\n한정된 상황을 십 수 개월 동안 반복하니 능숙해지지 않을 수 없었다."
    scene bg_zitong 
    show main_nem2 at right
    with Fade(1.0, 1.0, 1.0, color="#000000")
    $now_h = 19
    $now_m = 52
    $renpy.transition(dissolve)
    show screen time 
    $SoundPlayer("sigh.wav", 2.0)
    main "(아무리 그래도 이건 진짜 못 해먹겠다...)"
    $SoundPlayer("knock.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    show go_sal2 at center
    go "북진. {w}상병 [go] 지휘통제실에 용무 있어 왔습니다."
    show tie_working at left with dissolve
    tie "야간이야?"
    $FaceChange("go_atten", 1.0, .5, "go_sal2")
    go "예, 그렇습니다."
    tie "ㅇㅇ아. {w}후번초 왔다."
    main "잘... 못... 들엇...습니다...?"
    tie "아이고... {w}완전 정신줄을 놓아 버렸네."
    go "괜찮으십니까?"
    main "어? {w}균영...이니...?"
    $FaceChange("go_smi", 1.0, .5, "go_atten")
    go "교대하십니까? {w}들어가서 좀 쉬십시오."
    main "뭐야, 지금 몇 시야?"
    go "19시 52분입니다."
    main "그래... {w}특이사항은 딱히 없고... {w}5대기 점검도 실시사항 올렸고, 레이더 점검도 방금 했고... {w}그리고... {w}그리고... {w}없다."
    go "오늘로 며칠 째십니까?"
    main "5일 째지..."
    go "어우, 고생하셨습니다."
    main "너만 하겠니..."
    go "CEOI낭 주십니까?"
    main "여기."
    $SoundPlayer("blanket.wav", 4.0)
    $FaceChange("main_nem2_atten", 2.0, 1.0, "main_nem2")
    $renpy.pause(.5)
    $FaceChange("main_nem2_sal", 2.0, 1.0, "main_nem2_atten")
    main "북진... {w}상병 이지민 근무 마치고 복귀해도 되겠습니까?"
    tie "그래, 고생했다. {w}오늘이 마지막이지?"
    $FaceChange("main_nem2_atten", 2.0, 1.0, "main_nem2_sal")
    main "예, 그렇습니다."
    tie "내일 또 주말이니까 잘 쉬고, 월요일날 웃는 낯으로 다시 만나자."
    main "옙. {w}정훈장교님도 근무 고생하십시오."
    hide main_nem2_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway
    show main_nem2_atten at center
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    "피곤했다. {w}서 있는 것조차 버거울 정도로 머리가 울린다. {w}목구멍이 불타는 듯 쓰려왔다."
    "근무 내내 담배 한 대 입에 대지 않았음에도 흡연욕은 전혀 생기지 않았다. "
    "샤워하고 한시라도 빨리 내 자리에 눕는 것. {w}그것 이외에는 아무런 생각도 들지 않았다."
    main "(으... {w}토할 것 같아...)"
    hide main_nem2_atten
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_room
    show main_nem2_atten at right
    with dissolve
    $SoundPlayer("blanket.wav", 5.0)
    $FaceChange("main_cloth_bath", 2.0, 1.0, "main_nem2_atten")
    $renpy.pause(.5)
    hide main_cloth_bath
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_locker with dissolve
    $SoundPlayer("door.ogg", 2.0)
    show main_cloth_bath with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("blanket.wav", 5.0)
    $FaceChange("main_ord", 1.0, 1.0, "main_cloth_bath")
    scene bg_locker at blur2 
    show main_ord_ita at blur3
    with Dissolve(2.0)
    main "윽...!"
    $SoundPlayer("heartbeat.ogg", 1.0)
    $SoundPlayer("heartbeat.ogg", 1.0)
    "현기증이 몰려왔다."
    main "(진짜 사람 할 짓이 못 되네... {w}탄약고 근무랑은 비교도 안 돼...)"
    "갑작스레 순찰자가 들이닥치지 않는 이상 추위와 더위에 시달리며 서 있기만 하면 되는 탄약고와 달리 언제, 어떻게 시작될 지 모르는 훈련상황과 소홀히 할 수 없는 무전대기."
    "어느 정도의 정형화 된 틀이 있고, 그 안에 맞춰가면 되는 일을 1년 가까이 해 왔던 입장에서 몸은 편할지 몰라도 억지로라도 신경을 곤두세울 필요가 있는 근무를 연속으로 들어가자 몸은 격한 거부반응을 내뱉았다."
    "충분한 수면시간을 보장 받는다 하여도, 그 여파를 완전히 지워내진 못한 것 같았다."
    $now_h = 20
    $now_m = 0
    scene bg_locker at blur2 
    show main_ord_ita at blur3
    with Dissolve(2.0)
    "한 손으로 의자를 짚어 간신히 섰다."
    scene bg_locker at blur2 
    show main_ord_ita at blur3
    with Dissolve(2.0)
    main "(젠장... {w}다리에 힘이...)"
    "의자에 앉았다. {w}잠깐 앉아 쉰다면 금방 회복될 것이다."
    $SoundPlayer("door.ogg", 2.0)
    show prf_cloth_nom at right with dissolve
    prf "혼자 앉아서 뭐하십니까?"
    main "저혈압 때문에..."
    prf "괜찮으십니까?"
    main "어, 괜찮아. {w}잠깐 앉아서 쉬면 금방 나아."
    $FaceChange("main_ord", 1.0, 2.0, "main_ord_ita")
    prf "그건 안 낫는답니까?"
    main "뭐... 몸이 건강해지면 자동적으로 낫는다곤 하는데 난 아직 부족한가 보지."
    prf "저랑 운동하십니까?"
    main "아니오아니오아니오아니오아니오. {w}누구 죽일 일 있냐."
    prf "그렇게 질색하시지 않으셔도 됩니다. {w}저야 군대 오기 전에도 운동을 했었으니 체단실에서 그런 식으로 운동하는 거지 ㅇㅇㅇ 상병님 도와드릴 땐 그렇게 안 합니다. {w}한 번 믿어 보십시오. {w}체력단련병 한 번 믿어주십시오."
    main "에휴..."
    prf "뭐, 그건 그렇고 아직 어지러우십니까?"
    main "이제 괜찮아졌어. {w}씻으러 들어가자."
    hide main_ord
    hide prf_cloth_nom
    scene bg_shower with dissolve
    play looping shower
    scene bg_black with circirisin 
    $renpy.pause(2.0, hard=True)
    stop looping
    $stress_val -= 3
    $timeCheck(0, 20)
    scene bg_locker 
    show main_ord 
    show prf_cloth_nom at right
    with circirisin
    prf "먼저 가보겠습니다."
    main "응."
    hide prf_cloth_nom
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("blanket.wav", 4.0)
    $FaceChange("main_cloth_bath", 1.0, 2.0, "main_ord")
    main "(나도 그만 갈까.)"
    hide main_cloth_bath
    $SoundPlayer("door.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    show main_cloth_bath with dissolve
    $SoundPlayer("door.ogg", 2.0)
    scene bg_room2
    show main_cloth_bath
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    play sound put
    main "(아무도 없나.)"
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_bath")
    $renpy.pause(1.0)
    hide main_cloth
    $SoundPlayer("sheet.ogg", 1.0)
    "개인임무 분담제가 시작될 때까지, 잠깐 눈을 붙이기로 했다."
    hide screen time 
    scene bg_room2:
        linear 2.0 blur 100
        im.Sepia("bg_room.png")
        linear 2.0 blur 0
    show main_ord:
        alpha 0.0
        align(.5, 1.0)
        parallel:
            linear 2.0 blur 100
            im.Sepia("main_ord.png") 
            linear 2.0 blur 0   
        parallel:
            pause 2.0
            linear 2.0 alpha 1.0
    show past1_smi:
        align(.9, 1.0)
        alpha 0.0
        parallel:
            linear 2.0 blur 100
            im.Sepia("past1_smi.png")
            linear 2.0 blur 0
        parallel:
            pause 2.0
            linear 2.0 alpha 1.0
    $renpy.pause(4.0)
    show explain_scene with dissolve
    centered "꿈을, 꾸고 있다."
    extend "\n비록 그것은 내가 확인하지 못한 것을 비춘 환상."
    extend "\n그러나, 동시에. {w}틀림없는 현실."
    extend "\n지금에 이르러서는, 알 수 있었다. {w}잘못된 방향으로 나아가기를 수 차례. {w}그럼에도 나는 정교하게 짜여진 무수한 거짓으로 보호받고 있던 진실을 엿보는데 성공했다."
    extend "\n벗어날 수 없는 족쇄에서 도피하기 위해 내달리던 내가 최소한의 상처만 입은 채 그 굴레를 끊어내지 못함을 깨닫도록 만들기 위해 진의를 숨긴채 행동했음을."
    $blur_val = True
    centered "{size=60}{color=#FF0000}나는 인정받지 못함이니.{/size}"
    centered "{size=60}{color=#FF0000}나는 받아들여지지 못함이니."
    centered "{size=60}{color=#FF0000}모든 이들이 설령 나를 질기한다 하여도."
    centered "{size=60}{color=#FF0000}그들이 은혜를 베풀어 주었음은 틀림없는 사실." 
    centered "{size=60}{color=#FF0000}본래라면 아무런 타격도\n주지 못했을 터인데 어찌하여."
    centered "{size=60}{color=#FF0000}나는 그 사실에 이토록이나 번롱하고 있는가." with circirisin
    $blur_val = False
    $SoundPlayer("laugh.ogg", 1.0)
    past1 "너 설마 지금까지 그렇게 믿고 있었던 거냐? {w}이것 참. {w}우스워서 눈물이 나려고 하네."
    main "......."
    past1 "그 사람들이 네가 없을 때... {w}흡연장에서... {w}나한테 무슨 소리를 했는 지 알게되면 네가 어떤 반응일지 궁금한데?"
    main "......."
    "입에 담을 수 있는 말은 없었다. {w}그저 묵묵히 듣는 것 외에... {w}내가 할 수 있는 것은 없었다."
    $SoundPlayer("slap.ogg", .6)
    past1 "정신 차려 개새X야. {w}넌 존x 이기적인 거라고... {w}이해해?"
    extend "\n네가 그딴 연기에 속아버리는 바람에!" with vpunch
    extend "\n우리가 지금까지 얼마나 힘들었는지 알기나 해?" with vpunch
    $SoundPlayer("slap.ogg", .6)
    $SoundPlayer("slap.ogg", .6)
    past1 "왜, 맞으니까 기분 더러워? {w}더렵냐고? {w}응? {w}대답해."
    $SoundPlayer("slap.ogg", .6)
    extend " 대답해!" with vpunch
    $SoundPlayer("slap.ogg", .6)
    extend " 대답하라고!" with vpunch
    $SoundPlayer("slap.ogg", .6)
    "뺨이 얼얼했다. {w}틀림없는 꿈임에도 생생한 통각이 전해져 온다."
    "[jeong]의 목소리" "ㅇㅇ." with testd
    main "......."
    "[jeong]의 목소리" "괜찮아?" with testd
    main "괜찮아... {w}별 거 아냐..."
    play sound blanket
    scene bg_room3
    show jeong_cloth at center
    with circirisin
    stop sound
    show screen time
    show main_cloth at right 
    with wipeup
    jeong "왜 이렇게 떨어? {w}악몽이라도 꿨어?"
    main "어... {w}좀..."
    jeong "다시 잘 거야? {w}아님 같이 볼래?"
    main "뭐 보고 있었는데?"
    jeong "영화. {w}중간부터 봐야 하는데 상관 없어?"
    main "응."
    hide jeong_cloth
    "침대에 앉아 TV를 바라봤다. {w}골아떨어진 두 명과 근무 중인 한 명을 뺀 세 사람이 이름 모를 영화를 바라봤다."
    $renpy.pause(4.0)
    scene bg_room2
    show main_cloth at right
    $SoundPlayer("tv-off.ogg", 1.0)
    show jeong_cloth with dissolve
    jeong "더럽게 재미없네."
    main "그러게..."
    jeong "이거 봐. {w}지훈이도 골아떨어졌잖아."
    "시간을 죽이는 용도로도 쓰지 못할 수면제 같은 영화. {w}하지만 적어도 그 덕분에 머리 속에 파종된 기억의 씨앗은 성장하지 못한 채 고사했다."
    "다시 잠든다면 쓸데없는 과거에 취하는 일 없이 숙면할 수 있을 듯 했다."
    main "담배 한 대 피고 올게."
    jeong "들어올 때 조용히 들어와."
    main "응."
    $SoundPlayer("door.ogg", 2.0)
    scene bg_hallway2
    show young_cloth at right
    with dissolve
    show main_cloth at center with dissolve
    $SoundPlayer("door.ogg", 2.0)
    wol "어, ㅇㅇ씨. {w}담배 피러 가시나요?"
    main "예."
    wol "같이 가주실 수 있나요? {w}같은 생활관 애가 절 두고 먼저 가 버리는 바람에 전우조가 없거든요."
    main "마침 저도 혼자였는데 그러면 좋죠."
    wol "그럴 줄 알고 미리 보고도 해놨어요. {w}내려 가시죠."
    hide main_cloth
    hide young_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_bath2 with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_black with dissolve
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_taba_night
    show main_cloth_taba_nof
    show young_cloth_taba at right
    with dissolve
    $Smoking(img="main_cloth", loc=1, rep = 1, first=True)
    main "꽤나 쌀쌀해졌네요."
    $Smoking(img="young_cloth", loc=2, rep = 1)
    wol "그러게요."
    main "아, 이번 일주일 너무 길었어요. {w}진짜 죽을 뻔 했네."
    wol "그러고보니 통 안 보이시던데 뭐하고 계셨어요?"
    main "근무가 계속 잡혀서 죽어라 주간 상황만 섰죠."
    wol "아아. {w}요원화요? {w}이번에 본부중대원 거의 대부분이 훈련 참여했다 하던데 그것 때문이가 보네요."
    main "예... {w}오늘도 요원화 훈련 참석자는 전투휴무니까요. {w}오늘까지 근무 섰고 이번 달에는 더 이상 근무 없을 것 같네요."
    wol "와... {w}이번 훈련 꽤 빡세서 훈련 참가 안한 사람들 부럽다고 속으로 궁시렁거리고 있었는데 고생하셨네요..."
    $Smoking(img="main_cloth", loc=1, rep = 1)
    $Smoking(img="young_cloth", loc=2, rep = 1)
    main "몸은 괜찮아요?"
    wol "예... 뭐. {w}이번 훈련 받을 동안에는 말썽 안 부리더라고요."
    main "다행이네요."
    wol "그러는 ㅇㅇ씨야 말로 무릎 괜찮아요? {w}연골이라고 그랬던 것 같은데..."
    main "쭉 근무 섰잖아요. {w}무릎 쓸 일이 없어서 괜찮아요."
    wol "내일 비온다던데 안 시려요?"
    main "아, 망할. {w}왤케 시리나 했더니 그것 때문인 것 같네요."
    $Smoking(img="main_cloth", loc=1, rep = 1)
    "다른 이가 듣는다면 비웃을 대화. {w}아무런 영양가도 없는 여담."
    main "훈련은 어땠어요?"
    wol "힘들었죠..."
    main "이번에도 독도법 했나요?"
    wol "하긴 했는데 시간이 부족해서 실기동은 안하고 시험쳤어요."
    main "잘 보셨나요?"
    wol "예. {w}실제로 찾는 게 어려워서 그렇지 지도 상에 특정하는 건 쉬우니까요."
    main "제가 요원화 훈련 받을 때는 실기동도 했었는데 제가 찾아야 할 차례 때 길 잃어버리는 바람에 암구호도 안 외운 채로 방공진지에 들어가버렸었죠."
    wol "어떻게 됐나요?"
    main "초병들 뛰어와서 수하하는데도 대답 못해서 포박당할 뻔 했는데 뒤쫒아 온 교관님이 해결해 주셨죠, 뭐. {w}그것 때문에 한동안 놀림 받았었는데... {w}그것도 반 년이나 됐네요."
    wol "저도 입대한지 벌써 1년 가까이 됐네요. {w}...이렇게 보면 시간 참 빨라요."
    main "그러니까요. {w}돌이켜보면 막상 군생활도 훅훅 지나가는 거 같은데... {w}하루하루는 무슨 굼뱅이 마냥 밍기적거리고... {w}참 신기해요."
    $Smoking(img="young_cloth", loc=2, rep = 1)
    wol "진짜 지금까지 살면서 군대만큼 신기한 곳은 처음 와 본 거 같아요. {w}비단 시간 뿐 아니라 모든 게 바깥이랑은 다르니까요."
    main "듣고 보니 그렇네요."
    $Smoking(img="main_cloth", loc=1, rep = 1)
    "검푸른 바다에, 바알간.{w} 깜부기풀이 피었다."
    $Smoking(img="main_cloth", loc=1, rep = 1)
    $Smoking(img="young_cloth", loc=2, rep = 1)
    main "내일 주말인데 뭐하실 건가요?"
    wol "글쎄요... {w}어차피 내일 브런치 데이인데 늦게까지 자 버릴까 생각하고 있어요."
    main "저도 그래버릴까요... {w}연속 근무 떄문에 피곤한데..."
    wol "평소엔 항상 일찍 일어났죠?"
    main "예."
    wol "그럼 한 번 속는 셈 치고 깨우러 올 때까지 주무셔 보세요. {w}고작 두 시간 더 잔다고 뭐가 바뀌겠냐 하는데 깼을 때 개운함의 수준이 다르다니까요."
    main "그럴까요..."
    $renpy.pause(.5)
    $Smoking(img="main_cloth", loc=1, rep = 1)
    $Smoking(img="young_cloth", loc=2, rep = 1)
    wol "다 피셨어요?"
    main "예."
    $SoundPlayer("putoff.wav", 2.0)
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_tabahand")
    $SoundPlayer("putoff.wav", 2.0)
    $FaceChange("young_cloth", 2.0, .5, "young_cloth_tabahand")
    main "올라갑시다."
    hide main_cloth
    hide young_cloth
    $SoundPlayer("walk_slow.ogg")
    scene bg_bath2 with dissolve
    $SoundPlayer("walk_slow.ogg")
    scene bg_hallway2
    show main_cloth 
    show young_cloth at right
    with dissolve
    wol "보고는 제가 드릴게요. {w}가서 주무세요."
    main "아, 고마워요. {w}잘 자요, 영월 씨."
    wol "ㅇㅇ 씨도요."
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("door.ogg", 2.0)
    scene bg_room2
    show main_cloth at right 
    with dissolve
    $SoundPlayer("door.ogg", 2.0)
    $renpy.pause(.3)
    hide main_cloth
    $SoundPlayer("sheet.ogg", 1.0)
    "모포를 뒤집어 쓰고 잠을 청했다."
    scene bg_black with testd
    window show
    "금세 머리가 멍해지며 주변의 소리와 감각이 차단되며 졸음이 쏟아졌다."
    "내일 나는... {w}뭘 하면 좋을까?"
    window hide
    call screen schedule with testd
    "내일은 토요일. {w}모처럼 온전히 맞는 브런치 데이이다."
    if morn_do == "잠자기":
        extend " 푹 자고 일어난 다음 아침 겸 점심으로 베이컨과 크림치즈를 바른 빵. {w}상상만으로도 입에 침이 고였다."
        $stress_val -= 2
        $sat_val += 2
    else:
        extend " 간만에 시간에 쫒기지 않고 빵과 베이컨을 먹을 수 있을 것이다."
    "그러한 잡생각들과 함께 마지막으로 남아있던 의식의 마지막 꺼풀마저 벗겨지며 나는 빠르게 잠에 빠져들었다."    
    call saturday1
    $now_h = 10
    $now_m = 10
    show screen time with dissolve
    $SoundPlayer("broadcast.wav", 2.0)
    scene bg_room2 with dissolve
    "당직부사관" "\[통합중대 인원들. {w}식사 출발해주시길 바랍니다.\]"
    $SoundPlayer("blanket.wav", 4.0)
    show main_cloth at right with wipeup
    main "밥 먹으러 가자."
    $SoundPlayer("blanket.wav", 4.0)
    show jeong_cloth at center
    with wipeup
    zeen "으음..."
    main "진욱아. {w}어떻게 할래. {w}일단 깨워달래서 꺠우긴 했는데 더 자고 싶으면 내가 말판 옮겨주고."
    zeen "아닙니다. {w}먹으러 가겠습니다."
    $SoundPlayer("blanket.wav", 4.0)
    show zeen_cloth at left with wipeup
    $renpy.pause(.5)
    scene bg_room2
    $SoundPlayer("walk_slow.ogg")
    #"[morn_do] [af_do] [night_do]"
    play looping walk_slow
    scene bg_resta_front
    show jun_working_sang at right
    with Fade(1.0, 2.0, 1.0, color="#000000")
    stop looping
    show main_cloth at center
    show jeong_cloth at Position(xalign=.3, yalign=1.0)
    show zeen_cloth at left
    with dissolve
    $renpy.pause(.3)
    $timeCheck(0, 5)
    $FaceChange("main_cloth_sal", 1.0, .5, "main_cloth")
    main "북진. {w}고생하십니다. {w}[jun] 하사님."
    jun "밥 맛있게 먹어라."
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_sal")
    $renpy.pause(.3)
    scene bg_resta_front
    show jun_working_sang at right
    $SoundPlayer("walk_slow.ogg", 2.0)
    play looping dish_wash
    scene bg_resta_in 
    show main_cloth at center 
    with dissolve
    "브런치 메뉴는 베이글과 크림치즈, 베이컨 세 조각. 음료로는 탄산과 이온음료가 준비되어 있었다."
    show jeong_cloth at left with wipeup
    jeong "넌 또 탄산이야?"
    main "운동한 것도 아닌데 이온음료는 좀 그렇잖아?"
    jeong "그거 순 설탕덩어리인데..."
    $SoundPlayer("coke.wav", 1.0) 
    $SoundPlayer("drink.wav", 1.0)
    "식도를 강렬히 자극하는 탄산. {w}옅은 기억이 뇌리를 스쳐지나가고."
    "결락된 환부로부터 잊고있었던 통증. {w}존재할 수 없는 환상통이 밀물처럼 몰려들었다."
    main "(.......)"
    "과거는 과거일 뿐이라 말하며 가슴에 묻은 채 나아갈 수 있을 만큼의 굳건한 의지가 나에게도 있었더라면 이 또한 언젠가를 위한 반석으로 삼는 것이 가능했겠지만 꺾여버린 깃대는 두 번 다시 누각에 설 수 없을 듯 보였다."
    "목에 잔류한 통증을 베이컨 기름과 함께 삼켜냈다."
    "쓴웃음이 번져나오는 것을 간신히 막아내고 묵묵히 식사에 집중했다."
    show zeen_cloth at right with dissolve
    jeong "진욱아, 괜찮아?"
    zeen "예. {w}좀 피곤하긴 한데 괜찮습니다."
    main "야간 근무는 처음이었지?"
    zeen "예..."
    main "어떄?"
    zeen "어우... {w}쉽지 않습니다. {w}속도 메슥거리고 어지럽습니다."
    jeong "원래 그래. {w}밥 먹고 올라가서 마저 자."
    zeen "그래야 할 것 같습니다..."
    main "별 일 없었어?"
    zeen "예. {w}고균영 상병이 잘 알려줘서 잘 못한 건 없었습니다."
    main "다행이네."
    "구워진 베이글에 발려진 크림치즈는 하얀색이 거의 보이지 않을 정도로 녹아내려 있었다."
    jeong "브런치가 다 좋긴 한데 양이 좀 적은 것 같단 말이지."
    main "그러게... {w}칼로리로만 보면 평소 먹는 밥이랑 별로 차이 없을 텐데..."
    zeen "아침을 굶고 먹어서 더 그렇지 않겠습니까?"
    jeong "그것도 영향을 주긴 하겠지. {w}안되겠다, PX 가서 냉동 하나 까야겠다."
    main "냉동이라..."
    jeong "왜, 너도 먹게?"
    main "아니. {w}난 감자칩이면 충분해."
    jeong "몸에 냐쁜 것만 먹네."
    main "냉동도 만만치 않게 나빠."
    jeong "뭐 그렇게 나오면 할 말이 없긴 하지만."
    scene bg_resta_front with Fade(1.0, 2.0, 1.0, color="#000000")
    $SoundPlayer("walk_slow.ogg", 2.0)
    stop looping
    show zeen_cloth at left
    show jeong_cloth at Position(xalign=.3, yalign=1.0)
    show main_cloth at center
    with dissolve
    $timeCheck(0, 20)
    zeen "저... {w}[jeong] 병장님?"
    jeong "왜?"
    zeen "제가 너무 피곤해서 그런데 혹시 먼저 올라가도 되겠습니까?"
    jeong "그래, 빨리 가서 자."
    zeen "고생하십시오."
    hide zeen_cloth 
    $SoundPlayer("walk_slow.ogg", 2.0)
    main "먼저 올라가. {w}난 바로 흡연장으로 갈 거니까."
    jeong "알았어. {w}있다 보자."
    hide jeong_cloth
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    scene bg_taba
    show main_cloth_lighter 
    with dissolve
    $Smoking("main_cloth", 1.0, 2, True)
    "할 일을 정리했다."
    if saturday1_list[0] == 4 or saturday1_list[0] == 5:        
        if af_do == "사이버지식정보방":
            "원래대로라면 브런치를 먹은 후 다시 사이버지식정보방에 가려 했지만... {p}[jun] 하사님께서는 내가 저지른 잘못에 대한 일차적인 벌로 사이버지식정보방 이용을 금지하였다."
            "괜히 또 갔다가 일을 키우는 것보다는... {w}다른 일을 하는 게 좋을 듯 싶지만..."
            menu:
                "잠자기":
                    main "(돌아가서 잠이나 자야겠다.)"
                    $af_do = "잠자기"
                "공부":
                    main "(오히려 잘 됐어. {w}훈련도 곧이니까 공부를 좀 더 해 두자.)"
                    $af_do = "공부"
                "휴대폰":
                    main "(대충 폰 만지면서 시간이나 때워야지...)"
                    $af_do = "휴대폰"
                "!!사이버지식정보방!!":
                    "사이버지식 정보방 내부에는 CCTV가 없다. {w}복도를 비추는 CCTV는 외부계단으로 올라간다면 시야에 들지 않을 수 있다."
                    "순찰만 조심한다면 컴퓨터를 사용하는데 문제가 없을 것이다."
    $Smoking("main_cloth", 1.0, 1, False)
    main "(px... 가야하나?)"
    "곰곰히 생각해보았다."
    "과자는 아직 넉넉했다. {w}음료수도 1.5L짜리 페트병으로 한 개 반이 남아있다."
    main "(굳이 살 게 있다면 담배이긴 한데...)"
    menu:
        "PX에 간다":
            $go_px = True
        "PX에 가지 않는다.":
            $go_px = False
    $Smoking("main_cloth", 1.0, 1, False)
    "날씨가 쌀쌀해지고 있다."
    "다시금 가을이 오고 있다. {w}바스락거리는 낙엽과, 터진 은행열매에서 나는 냄새의 계절이."
    "평일 오후, 뜀걸음을 뛰게 된다면 샛노랗게 물든 부대. {w}콧구멍을 찌르는 것은 여린 차가움을 품은 공기."
    "겨우내, 체력 단련 시 엄습하곤 하는 비강을, 기도를, 폐를 에는 듯한 날카로운 냉기가 아닌.{p}흘러 내리는 땀을. {w}불구덩이 속에 뛰어든 것 마냥 달구어지는 피부를 식혀주는 기분 좋은 차가움."    
    "이맘때의 바람은 등 뒤에서 밀어주는 바람. {w}한 없이 높은 고지에 닿을 시간."
    "한 삶이 저무는 겨울이 와, 살아있는 것이 모두 잠에 빠져들기 전. {w}일년에서 가장 아름다운 때."
    main "(작년에는... 이 때 뭘 했었더라.)"
    "처음으로 군대에서 명절을 보냈다. {w}소대 사람들과 함께 맛있는 요리를 해 먹었다. {w}육군지휘검열을 대비해 1달 내내 전투준비태세 훈련만 했다. {w}처음으로 5대기 임무를 수행했다. {w}육군지휘검열 당일날 제때 볼일을 보지 못해 바지에 지릴 뻔 했다."    
    "다른 사람들이 군장을 매고 꽈리고개를 넘을 때 5대기인 덕분에 닷지를 타고 편하게 넘어갔다.{w} 처음으로 나안 야간사격을 했다." 
    "그 때는. {w}파스텔로 덧칠된 나날이었다. {w}내 주변에 있는 모든 것을 한 없이 밝았고. {w}노력이라는 벽돌로 쌓아올려진 거성은 결코 무너지지 않을 듯 보였다."
    "느리게나마 나아가고 있었고. {w}여러 시간이 지난 후에 뒤를 돌아본다면 원근법에 따라 착실히 작아져 가는 풍경이 보였다.{p}이제 와 돌이켜본다면 나는 이미 알고 있었다. {w}모든 것은 만들어진 허상. {w}잘 짜여진 한 편의 연극이라는 것을." 
    "그러나, 나는. {w}한 목적을 위해 창조된 환상임에도 그 정취에 취하여 문득 떠오른 의문을 애써 눌러 죽이고. {w}곳곳에 산재해 있던 진실에 이르는 실마리들을 무시하고 말았다."
    main "(취하지 않았다고 해도... {w}바뀔 건 없었겠지만.)"
    $Smoking("main_cloth", 1.0, 2, False)
    "지금에 이르러서까지 바뀌지 않는 것 하나. {w}나는 은혜를 입었다. {w}그렇기에 이곳에 서 있을 수 있다."
    if saturday1_list[0] == 4 or saturday1_list[0] == 5:        
        "옳다, 와 그르다. {w}이분법으로 생각한다면 틀림없이 내가 한 행동은 그름. {w}분명한 사실이었다."
        "허나, 지금에 이르러서는 남들이 뭐라고 하던.{w} 이런 짓이라도 하지 않으면... {w}제자리에 서 있는 것조차 버거운 몸이 되어버렸다."
        $Smoking("main_cloth", 1.0, 1)
        main "(어떻게 해야 할까... {w}뭘 해야...{w} 다시 기회를 얻을 수 있지?)"
    else:
        $Smoking("main_cloth", 1.0, 1)
    $Smoking("main_cloth", 1.0, 1)
    call taba_event_incounter
    $Smoking("main_cloth", 1.0, 1)
    "강 물살에 되치인 바윗돌이 깎여나가 언젠가 흔적만을 남긴 채 바스러지듯.{p}어떤 일이 벌어지더라도, 시간은 멈추지도, 멈춰 세우지도 못한 채 제각각에게 부여된 절대량을 파먹으며 흘러간다.{p}한 없이 멀게만 느껴졌던 어느 삶의 끝무리가 손에 잡힐 듯 보이기 시작했다."
    "지난 1년 3개월. {w}수 차례 그래왔듯, 눈을 감고, 호흡을 정돈하며. {w}코 앞에 들이닥친 것부터 차례대로 하나씩 처리해 나간다면.{p}이 고난 역시 돌파할 수 있을 것이다. {w}헤쳐 나갈 수 있을 것이다. {w}적어도 내 한 사람에게서는 경험으로서 증명되는 진실이었다."
    $Smoking("main_cloth", 1.0, 1)
    "그 일련의 공식을 마음 속으로부터 부정하게 된 건, 언제부터인가 자리잡은 내면의 언짢음.{p}출처도, 이유도, 그 의의도 모른 채 그저 끌어안고 있었던 어느 한 감정이 그림자의 형상으로 변하였을 때."
    "섞여들어 온 부산물은 \'걱정을 끼치지 않기 위해\'라는 제멋대로인 딱지가 붙은 채 함구 되어 비밀이 되었고.{p}이내 실금투성이 유리 위로 내쳐진 망치가 되었다."
    $Smoking("main_cloth", 1.0, 1)
    "어쩌면 그때, 홀로 온전히 품는 것을 포기한 채. {w}이미 끼쳤던 부담에, 폐에 편승하여. {w}한 번 더 내밀어진 손을 붙잡고서 내게 드리운 그늘의 일부를 넘겼더라면."
    $Smoking("main_cloth", 1.0, 1)
    $SoundPlayer("sigh.wav", 2.0)
    main "(다 무슨 소용이야... {w}이미 다 끝나버렸는데.)"
    $SoundPlayer("walk_slow.ogg", 2.0)
    $SoundPlayer("putoff.wav", 2.0)
    $FaceChange("main_cloth", 1.0, .5, "main_cloth_tabahand")
    $renpy.pause(.5)
    hide main_cloth
    $SoundPlayer("walk_slow.ogg", 2.0)
    $now_day = 5
    call px_incounter
    "." 
    return



###########Card?####
#call events_run_period
#call set_allcard
#call game_reset
#call screen cardgame
#(85, 35, 238, 216)
#$message_list.append(Message())
#call screen test_screen
#$message_list.append(Message())
#call screen test_screen
