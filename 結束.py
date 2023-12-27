def not_game(state):
   action = game_field.get_user_action(stdscr)
   if action == 'Restart':
        return 'Init' 
   if action == 'Exit': 
        return 'Exit' 
  if game_field.move(action): # move successful 
       if game_field.is_win():
           return 'Win' 
     if game_field.is_gameover(): 
         return 'Gameover'
        game_field = GameField(win=32) 
     