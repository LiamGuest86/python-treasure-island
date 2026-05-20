print(r'''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input("\n"
                 "You find yourself on the beach of the mysterious Treasure Island,\n"
                 "You see trees up ahead with two routes,\n"
                 "Which Direction would you like to go? type LEFT or RIGHT: ").upper()

if choice_1 == "LEFT":
    print("\n"
          "You manage to find a clear path and proceed with caution.")
    choice_2 = input("You make your way through the trees and stumble across a river,\n"
                     "do you want to wait here, or swim across?\n"
                     "Type SWIM or WAIT: ").upper()
    if choice_2 == "WAIT":
        print("\n"
              "You wait for some time, and a man on a boat turns up, he offers you a lift across the river. How convenient!")
        choice_3 = input("\n"
                         "You cross the river, and find yourself in front of a building with three doors.\n"
                         "A Blue door, a Yellow door, and a Red door.\n"
                         "Which door would you like to try? Type BLUE, YELLOW, or RED: ").upper()
        if choice_3 == "BLUE":
            print("\n"
                  "You open the Blue door, wait, what was an octopus doing in here!?\n"
                  "It pulls you in with it's tentacles and squishes you to death.\n"
                  "GAME OVER!!")
        elif choice_3 == "YELLOW":
            print("\n"
                  "You open the Yellow door, and inside find a chest brimming with gold.\n"
                  "Congratulations, you've found the treasure!!")
            print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
            ''')
        elif choice_3 == "RED":
            print("\n"
                  "You open the Red door and enter the room. It's a bit warm in here.\n"
                  "Wait a minute, this is a room of fire, you burn to death!\n"
                  "GAME OVER!!!!")
        else:
            print("\n"
                  "Due to your indecision, you have entered an incorrect input.\n"
                  "Because of this, The Angry Text Adventure Monkey eats your face.\n"
                  "Game Over!!!")
    else:
        print("\n"
              "You decide to swim across. Unfortunately, that log you thought you saw, turned out to be a Crocodile.\n"
              "You have now become his dinner. GAME OVER!")


else:
    print("\n"
          "You were not looking where you were going, and fall into a pit.\n"
          "GAME OVER!")
