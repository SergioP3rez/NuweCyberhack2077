import os

from vars import MENU, DECK_ART, CONTACTS
from vars import STATUS_ERROR, STATUS_ALIVE, STATUS_EXIT

class SwitcherCommands(object):
    interfaces = {
            "d" : "Daemon",
            "o" : "Operating system",
            "i" : "ICE"
            }

    daemons = {
            "1": "Ping",
            "2": "ICEPick",
            "3": "Datamine"
            }
    os = {
            "1": "Berserk",
            "2": "Sandevistan",
            "3": "Phantom Liberty"
            }
    ice = {
            "1": "BlackWall",
            "2": "Black ICE",
            "3": "Self-ICE"
            }

    daemon_id= 1
    os_id= 1
    ice_id= 1

    def arg_parser(self, cmd):
        """
            Commands are like help -h
            So we can split by '-'
            and pass everything to the command
        """
        full_cmd = str(cmd).split('-')
        command = full_cmd[0].strip()
        arguments = full_cmd[1:] if len(full_cmd) > 1 else []
        return command, arguments

    def get_command(self, arg):
        cmd, args = self.arg_parser(arg)
        method_name = 'cmd_' + str(cmd)
        # Get the method from 'self'. Default to a lambda
        method = getattr(self, method_name, lambda args=[]: ("Unavailable interface action.\nEnter \'actions\' to display available actions", True))
    
        # Call the method as we return it
        return method(args=args)

    def cmd_banner(self, args=[]):
        s = "\n"
        s += "███    ██ ██    ██ ██ \n";
        s += "████   ██ ██    ██ ██ \n";
        s += "██ ██  ██ ██    ██ ██ \n";
        s += "██  ██ ██  ██  ██  ██ \n";
        s += "██   ████   ████   ██ \n";
        s += "                      \n";
        return s.encode('utf-8'), STATUS_ALIVE

    def cmd_deck(self, args=[]):

        s = ""
        # Operating Systems
        s += "--------------------------\n"
        s += " >> Operating Systems <<\n"
        for key in self.os.keys():
            s += "\t[{}] --> {}".format(key, self.os[key])
            s +="\n"

        # Daemons
        s += "--------------------------\n"
        s += " >> Daemons <<\n"
        for key in self.daemons.keys():
            s += "\t[{}] --> {}".format(key, self.daemons[key])
            s += "\n"

        # ICEs
        s += "--------------------------\n"
        s += " >> ICE <<\n"
        for key in self.ice.keys():
            s += "\t[{}] --> {}".format(key, self.ice[key])
            s += "\n"

        s += "--------------------------\n"

        return s.encode('utf-8'), STATUS_ALIVE

    def cmd_chip(self, args=[]):
        i = self.ice[str(self.ice_id)]
        o = self.os[str(self.os_id)]
        d = self.daemons[str(self.daemon_id)]

        result = DECK_ART.format(i, d, o).encode('utf-8')
        return result, STATUS_ALIVE


    def cmd_actions(self, args=[]):
        s =  ""
        for cmd in MENU.keys():
            if (cmd == "net_debug" and (self.os_id != 2 or self.daemon_id != 1 or self.ice_id != 3)):
                continue
            s += "\n   [{}] --> {}\n".format(cmd, MENU[cmd]["desc"])
            s +=  "  \t{}\n".format(MENU[cmd]["help"]) if MENU[cmd]["help"] else ""
            for flag_arg in MENU[cmd]["usage"].keys():
                flag_desc = MENU[cmd]["usage"][flag_arg]
                s += "   \t\t{}: {}\n".format(flag_arg, flag_desc) 

        s += "\n"
        return s.encode('utf-8'), STATUS_ALIVE

    def cmd_gear(self, args=[]):
        result = "\n"
        if len(args) > 0: 
            interface = "".join(args[0][0:2])
            item_id = "".join(args[0][1:])
            try:
                interface = str(interface).strip()
                item_id = int(item_id)
            except Exception as e:
                return "Arguments are not valid", STATUS_ERROR

            if interface not in self.interfaces.keys():
                return "Interface {} is not valid.\nInterface keys : {}".format(interface, "".join(self.interfaces.keys())), STATUS_ERROR

            if item_id > 3 or item_id < 1:
                return "Not a valid ID", STATUS_ERROR

            self.set_interface_value(interface, item_id)

            cmd = "{} --> Equipped [{}] with ID {}\n".format(
                        self.interfaces[interface],
                        self.get_interface_value(interface, item_id), 
                        item_id)
            return cmd.encode('utf-8'), STATUS_ALIVE
        else:
            return "", STATUS_ERROR

    def get_interface_value(self, interface, item_id):
        item_id = str(item_id)
        if interface == "d":
            return self.daemons[item_id]
        elif interface == "i":
            return self.ice[item_id]
        elif interface == "o":
            return self.os[item_id]
        else: 
            return self.daemons[item_id]
            
    def set_interface_value(self, interface, item_id):
        if interface == "d":
            self.daemon_id = item_id
        elif interface == "i":
            self.ice_id = item_id
        elif interface == "o":
            self.os_id = item_id


    def cmd_contacts(self, args=[]):
        result = ""
        for ctc in CONTACTS:
            result += "\t[ {} ]\n".format(ctc)
            result += "\t-- Last Message --\n"
            result += "\t{}\n".format(CONTACTS[ctc])
            result += "\n"

        return result.encode('utf-8'), STATUS_ALIVE

    def cmd_net_debug(self, args=[]):
        result = "\n"
        if len(args) > 0: 
            str_args = "".join(args[0][1:])
            cmd = "{}".format(str_args)
            result += str(os.popen(cmd).read())
        else:
            cmd = "date | base64"
            result += str(os.popen(cmd).read())
        result += "\n"

        return result.encode('utf-8'), STATUS_ALIVE

    def cmd_disconnect(self, args=[]):
        return "".encode('utf-8'), STATUS_EXIT
