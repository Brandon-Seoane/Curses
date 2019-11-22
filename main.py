import argparse
import sys
import time
import os
import random

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from progressbar import ProgressBar

import curses


TITTLE = """
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

def do(num:int) -> int:
    time.sleep(random.randint(1,5))
    return num


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(0, 0, TITTLE)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()

    with ProgressBar(10) as pbar:
        with ThreadPoolExecutor() as executor:
            threads = [executor.submit(do,i) for i in range(10)]
            for thread in concurrent.futures.as_completed(threads):
                stdscr.addstr(15, 0, pbar.update(1))
                stdscr.refresh()
    
    key = stdscr.getch()
    while key not in [curses.KEY_ENTER,10,13,101]:
        key = stdscr.getch()
        stdscr.addstr(16, 0, str(key))


if __name__ == "__main__":
    curses.wrapper(main)

   