import curses

tittle = """
 _______                                                                
/       \                                                               
$$$$$$$  | ______    ______    ______    ______   ______   _____  ____  
$$ |__$$ |/      \  /      \  /      \  /      \ /      \ /     \/    \ 
$$    $$//$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$ $$$$  |
$$$$$$$/ $$ |  $$/ $$ |  $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ | $$ | $$ |
$$ |     $$ |      $$ \__$$ |$$ \__$$ |$$ |     /$$$$$$$ |$$ | $$ | $$ |
$$ |     $$ |      $$    $$/ $$    $$ |$$ |     $$    $$ |$$ | $$ | $$ |
$$/      $$/        $$$$$$/   $$$$$$$ |$$/       $$$$$$$/ $$/  $$/  $$/ 
                             /  \__$$ |                                 
                             $$    $$/                                  
                              $$$$$$/                                   
"""



def main(stdscr):
	curses.curs_set(0)
	curses.mousemask(1)
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

	stdscr.addstr(0, 0, tittle)
	stdscr.addstr(15, 0, "Red")
	stdscr.addstr(16, 0, "Green")

	while 1:
		stdscr.refresh()
		key = stdscr.getch()

		if key == curses.KEY_MOUSE:
			_, x, y, _, _ = curses.getmouse()
			if y == 15 and x in range(3):
				stdscr.attron(curses.color_pair(1))
				stdscr.addstr(0, 0, tittle)
				stdscr.attroff(curses.color_pair(1))
			elif y == 16 and x in range(5):
				stdscr.attron(curses.color_pair(2))
				stdscr.addstr(0, 0, tittle)
				stdscr.attroff(curses.color_pair(2))
		elif key == 27:
			break



curses.wrapper(main)