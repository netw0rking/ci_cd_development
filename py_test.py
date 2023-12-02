#!/usr/bin/env python3

class network_device():
    nos_1 = 'ios'
    nos_2 = 'junos'
    nos_3 = 'eos'

    def nos_types(self):
        print(f'{self.nos_2} is the best CLI Structure')
        print(f'{self.nos_1} is a classic')
        print(f'{self.nos_3} is a good up-and-comer')

r1 = network_device()
print(r1.nos_3)
r1.nos_types()
