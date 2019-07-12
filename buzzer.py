01 import pygame
02 import curses
03 import RPi.GPIO as GPIO
04
05 GPIO.setmode ( GPIO.BCM )
06 GPIO.setup ( 4 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
07 GPIO.setup ( 18 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
08 GPIO.setup ( 22 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
09 GPIO.setup ( 23 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
10 GPIO.setup ( 25 , GPIO.IN , pull_up_down=GPIO.PUD_UP )
11
12 def showWinner ( winner ):
13    global screen
14    global numbers
15
16    winner -= 1
17    screen.blit ( numbers [ winner ] [ 0 ] , ( numbers [ winner ] [ 1 ] , 0 ) )
18    pygame.display.flip()
19
20 def reset():
21    global screen
22
23    screen.fill ( ( 0 , 0 , 0 ) )
24    pygame.display.flip()
25
26 def getBuzzers():
27    while 1:
28       if GPIO.input ( 4 ) == GPIO.LOW:
29          return 1
30          break
31       if GPIO.input ( 18 ) == GPIO.LOW:
32          return 2
33          break
34       if GPIO.input ( 22 ) == GPIO.LOW:
35          return 3
36          break
37       if GPIO.input ( 23 ) == GPIO.LOW:
38          return 4
39          break
40       if GPIO.input ( 25 ) == GPIO.LOW:
41          return 5
42          break
43
44
45 pygame.display.init()
46 screen = pygame.display.set_mode ( ( 1680 , 1050 ) )
47
48 terminal = curses.initscr()
49 curses.cbreak()
50 terminal.nodelay ( 1 )
51
52 terminal.addstr ( 5 , 5 , "Trivia Buzzers and Scoring" )
53 terminal.addstr ( 7 , 5 , "          1 - 5 -- Show team as buzzed in" )
54 terminal.addstr ( 8 , 5 , "              r -- Reset buzzers" )
55 terminal.addstr ( 10 , 5 , "             b -- enable buzzers" )
56 terminal.addstr ( 11 , 5 , "             x -- Exit (Careful, no confirmation)" )
57
58 numbers = list()
59 left = 0
60 numbers.append ( ( pygame.image.load ( "numbers_01.jpg" ) , left ) )
61 left += numbers [ 0 ] [ 0 ].get_width()
62 numbers.append ( ( pygame.image.load ( "numbers_02.jpg" ) , left ) )
63 left += numbers [ 1 ] [ 0 ].get_width()
64 numbers.append ( ( pygame.image.load ( "numbers_03.jpg" ) , left ) )
65 left += numbers [ 2 ] [ 0 ].get_width()
66 numbers.append ( ( pygame.image.load ( "numbers_04.jpg" ) , left ) )
67 left += numbers [ 3 ] [ 0 ].get_width()
68 numbers.append ( ( pygame.image.load ( "numbers_05.jpg" ) , left ) )
69
70 running = True
71 while running == True:
72    choice = terminal.getch ( 12 , 5 )
73    if choice == -1: continue
74    if choice == ord ( "1" ):
75       showWinner ( 1 )
76    elif choice == ord ( "2" ):
77       showWinner ( 2 )
78    elif choice == ord ( "3" ):
79       showWinner ( 3 )
80    elif choice == ord ( "4" ):
81       showWinner ( 4 )
82    elif choice == ord ( "5" ):
83       showWinner ( 5 )
84
85    elif choice == ord ( "b" ):
86       showWinner ( getBuzzers() )
87
88    elif choice == ord ( "r" ):
89       reset()
90    elif choice == ord ( "x" ):
91       running = False
92
93 curses.endwin()