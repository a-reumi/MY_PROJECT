def fruit_quiz():
    while True:
        print("영어-스페인어 과일 단어 맞추기 퀴즈에 오신 것을 환영합니다!")
        print("힌트를 보고 영어 과일 이름을 맞춰보세요!") 
        
        print('-' * 100)    
        print(f"힌트: 이 과일은 아침에 먹으면 좋아요") 
        right_anwser=input("정답은 무엇인가요? ").strip()
        if right_anwser == "apple": 
            print(f"정답입니다! 'apple'은 'manzana'입니다!")
        else:
            print(f"틀렸습니다. 정답은 'apple' 입니다. 스페인어로는 'manzana' 라고 해요.")
            print(f"다음 문제를 도전하시겠어요?")
            answer=input("yes/no => ").strip()
            if answer == "no":
                print("안녕히 가십시오.") 
                break
            else:
                print("아주 좋습니다!") 
                
        print('-' * 100)     
        print(f"힌트: 이 과일은 노란색이고 원숭이가 좋아해요 ") 
        right_anwser = input("정답은 무엇인가요? ").strip()
        if right_anwser == "banana": 
            print(f"정답입니다! 'banana'는 'plátano'입니다!")
        else:
            print(f"틀렸습니다. 정답은 'banana'입니다. 스페인어로는 'plátano' 라고 해요.")
            print(f"다음 문제를 도전하시겠어요?")
            answer=input("yes/no => ").strip()
            if answer == "no":
                print("안녕히 가십시오.") 
                break
            else:
                print("아주 좋습니다!") 
                
        print('-' * 100) 
        print("힌트: 이 과일은 주황색이고 주스로도 많이 마시며 상큼해요")
        right_anwser = input("정답은 무엇인가요? ").strip()
        if right_anwser == "orange":
            print("정답입니다! 'orange'는 'naranja'입니다!")
        else:
            print("틀렸습니다. 정답은 'orange'입니다. 스페인어로는 'naranja' 라고 해요.")
            print(f"다음 문제를 도전하시겠어요?")
            answer=input("yes/no => ").strip()
            if answer == "no":
                print("안녕히 가십시오.") 
                break
            else:
                print("아주 좋습니다!") 
                
        print('-' * 100) 
        print(f"힌트: 이 과일은 껍질이 두껍고 피자 토핑으로 쓰여요 ") 
        right_anwser = input("정답은 무엇인가요? ").strip()
        if right_anwser == "pineapple":
            print(f"정답입니다! 'pineapple'은 'piña' 입니다!")
        else:
            print(f"틀렸습니다. 정답은 ''pineapple'입니다. 스페인어로는 'piña' 라고 해요.")
            print(f"다음 문제를 도전하시겠어요?")
            answer=input("yes/no => ").strip()
            if answer == "no":
                print("안녕히 가십시오.") 
                break
            else:
                print("아주 좋습니다!") 
                
        print('-' * 100)     
        print(f"힌트: 이 과일은 겨울에 나오고 빨갛고 씨가 많아요")     
        right_anwser = input("정답은 무엇인가요? ").strip()
        if right_anwser == "strawberry":
            print(f"정답입니다! 'strawberry'는 'fresa'입니다!")
        else:
            print(f"틀렸습니다. 정답은 'strawberry'입니다. 스페인어로는 'fresa' 라고 해요.")
            print(f"다음 문제를 도전하시겠어요?")
            answer=input("yes/no => ").strip()
            if answer == "no":
                print("안녕히 가십시오.") 
                break
            else:
                print("아주 좋습니다!") 
                
        print('-' * 100)     
        print(f"힌트: 이 과일은 여름에 나오며 화채로도 먹어요")     
        right_anwser = input("정답은 무엇인가요? ").strip()
        if right_anwser == "watermelon":
            print(f"정답입니다! 'watermelon'은 'sandía'입니다!")
        else:
            print(f"틀렸습니다. 정답은 'watermelon'입니다. 스페인어로는 'sandía' 라고 해요.")   

            # 퀴즈 계속 여부 묻기
        print('-' * 100) 
        play_again = input("다시 하시겠습니까? (yes/no): ").strip()
        if play_again == "yes": 
            fruit_quiz() 
        else:
            print("퀴즈를 종료합니다. 즐거운 하루 되세요!")
            break
fruit_quiz() 