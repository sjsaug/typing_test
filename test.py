import curses

def term_screen(stdscr):
    curses.echo()
    stdscr.refresh()
    key = stdscr.getch()
    if key == curses.KEY_BACKSPACE:
        print("backspace")

def main():
    curses.wrapper(term_screen)


if __name__ == "__main__":
    # Calls the main function for program to proceed
    main()
