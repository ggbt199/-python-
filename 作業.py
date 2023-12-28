def not_game(table):
    for x in table:
        if x[0] !=0 and x[1 ]!=0 and x[2] !=0 and x[3 ]!=0:
             print("gameover")
        for s in x:
            if s  ==32:
                print("win")
 not_game(table)