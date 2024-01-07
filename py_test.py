#!/usr/bin/env python3


class network_device:
    nos_1 = "ios"
    nos_2 = "junos"
    nos_3 = "eos"

    def nos_types(self):
        print(f"{self.nos_2} is the best CLI Structure")
        print(f"{self.nos_1} is a classic")
        print(f"{self.nos_3} is a good up-and-comer")

    def router_command(self, nos):
        if nos == "ios":
            print("show ip interface brief")
        elif nos == "junos":
            print("show interface description")
        elif nos == "eos":
            print("show interface status")
        else:
            print(f"{nos} is an unsupported platform")


rtr_type = input(f"select platform:\n")
router = network_device()
print(router.router_command(rtr_type))
