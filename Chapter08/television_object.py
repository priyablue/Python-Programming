# Create a television object which the user can use to turn
# the volume up or down, or enter a channel number

# define class
class Television(object):
    """A television with volume and channel controls"""
    
    # constructor method which sets attributes
    def __init__(self, volume = 15, channel = 1):
        self.volume = volume
        self.channel = channel
        print('The television has been switched on')
        
    
    def volume_up(self):
        self.volume += 1
        if self.volume > 30:
            self.volume = 30
            print ('Volume: 30 MAXIMUM')
        else:
            print('Volume:', self.volume)
            
    def volume_down(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
            print ('Volume: MUTE')
        else:
            print('Volume:', self.volume)
            
    def change_channel(self, channel):
        if channel > 4:
            print('That channel doesn\'t exist')
        elif channel == 4:
            print('Channel 4')
        elif channel == 3:
            print('BBC 3')
        elif channel == 2:
            print('Comedy Central')
        elif channel == 1:
            print('Sky 1')
        else:
            print('That channel is out of range')
            
def main():
    choice = None
    tv = Television()
    
    # set up loop so user can pick choices and exit
    while choice != "0":
        print\
        ("""
        0 - Turn off television
        1 - Volume up
        2 - Volume down
        3 - Change channel
        """)
        
        choice = input("Choice: ")
        
        # turn off tv and break loop
        if choice == "0":
            print('Switching off...')
            
        # turn volume up by one
        elif choice == "1":
            tv.volume_up()
            
        # turn volume down by one
        elif choice == "2":
            tv.volume_down()
            
        # change channel via user input
        elif choice == "3":
            channel = input('Which channel: ')
            tv.change_channel(int(channel))
        
        # else will catch any invalid options
        else:
            print('That was an invalid choice.')
            
main()

print('\nGoodbye.')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
            
