MENU={
    "actions": {
        "desc": "Displays actions available in the Net Virtual Interface ",
        "help": "Executing `actions` does not understand arguments.",
        "usage": {}
    },
    "deck": {
        "desc": "Displays available interface modifications.",
        "help": "Executing `deck` does not understand arguments.",
        "usage": {
        }
    },
    "chip": {
        "desc": "Displays equipped chip interface modifications.",
        "help": "Executing `chip` does not understand arguments.",
        "usage": {
        }
    },
    "contacts": {
        "desc": "Display contacts stored in  Net Virtual Interface ",
        "help": "Executing `contacts` does not understand arguments",
        "usage": {
        }
    },
    "gear": {
        "desc": "Modify the current cyberdeck interface.",
        "help": "Execute `gear` with the type and the id.\n\tExample: `gear -d 1` sets the daemon to Berserk (ID: 1).",
        "usage": {
            "-d": "Equips daemon. Provide the Daemon ID.",
            "-o": "Equips operating system. Provide the Operating System ID.",
            "-i": "Equips ice. Provide the ice ID."
        }
    },
    "net_debug": {
        "desc": "Debug the internal system of the Net Virtual Interface subnet.",
        "help": "Execute `net_debug` to test and validate correct functionality.",
        "usage": {
            "-c [[command]]": "Executes a debugging internal command.",
        },
    },
    "disconnect": {
        "desc": "Disconnects from Net Virtual Interface.",
        "help": "Executing `disconnect` does understand arguments",
        "usage": {}
    }
}

CONTACTS = {
        "Maine" : "We'll meet tomorrow at 31:20, where we always meet.\n\tDon't be late, something big is coming.",
        "Rebecca" : "Small details matter.",
        "Faraday" : "[[ No messages ]]",
        "David" : "I have left something for Lucy where I usually leave it.\n\tPlease make sure she gets it.",
        "Lucy" : "I have left a back door in the Faraday device.\n\tTo get into it you just have to equip yourself with the right things."
}

DECK_ART= """\n
    +--[PWR]--------------| USB |--+
    |                     +-----+  |
    |       GND/RST2   [ ][ ]      |
    |       MOSI2/SCK2 [ ][ ]      |
    |                           +------+
    | [ ] N/C                   | ICE  | <-- {} (equipped)
    | [ ] v.ref                 +------+
    |            +---+             |
    | [ ] A0    -| N |-         +------+
    | [ ] A1    -| V |-         |DAEMON| <-- {} (equipped)
    | [ ] A2    -| I |-         +------+
    | [ ] A3     +---+             |
    |                           +-----+
    |                           | O S |  <-- {} (equipped)
    |         GENBUOPS          +-----+
    |                              |
    |       RST SCK MISO           |
    |       [ ] [ ] [ ]            |
    |       [ ] [ ] [ ]      ______/
     \______________________/
\n     
"""

# Status Code 
STATUS_ERROR = 1
STATUS_ALIVE = 2
STATUS_EXIT  = 3
