char_point = None

    new2or4()
    new2or4()

    while True:
        score_record(score, best_score)
        print_table()

        if game_over() == 1:
            char_point = input()

            if char_point == 'w':
                w_move()
            elif char_point == 'd':
                d_move()
            elif char_point == 's':
                s_move()
            elif char_point == 'a':
                a_move()
            elif char_point == 'e':
                print("【已離開遊戲】")
                return
            elif char_point == 'r':
                restart()
            else:
                print("\n【輸入錯誤】\n\n請重新輸入:")
                continue

            if score > best_score:
                best_score = score
        else:
            print("【Game Over】\n\n")
            break

    print("請選擇:\n【離開】請輸入'e'\n【重玩】請輸入'r'\n")

    while True:
        char_point = input()

        if char_point == 'e':
            print("【已離開遊戲】")
            return
        elif char_point == 'r':
            restart()
        else:
            print("\n【輸入錯誤】\n\n請重新輸入:")