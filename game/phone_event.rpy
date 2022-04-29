label phone_event1:
    $SoundPlayer("phone_beep.wav", .4)
    $message_list.append(Message(type=0, who="고균영", message = "ㅇㅇㅇ 상병님."))
    call screen test_screen with dissolve
    $message_list.append(Message(type=0, who="고균영", message = "혹시 어디십니까?"))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "안 바쁘시면 잠깐 저랑\n같이 탄약고 좀 가 주실\n수 있겠습니까?"))
    call screen test_screen 
    $message_list.append(Message(type=1, who="나", message = "ㅇㅇ 어디로 갈까"))
    call screen test_screen 
    $message_list.append(Message(type=0, who="고균영", message = "어차피 사지방이시지 않습니까.\n제가 가겠습니다."))
    call screen test_screen 
    $message_list.append(Message(type=1, who="나", message = "ㅇㅋ"))
    call screen test_screen 

