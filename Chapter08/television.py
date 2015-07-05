class Television(object):
    def __init__(self):
        self.channel = 1
        self.volume = 10
    
    def __str__(self):
        rep = "Televison object"
        return rep
        
    def turn_volume_up(self):
        self.volume += 1
        if self.volume > 30:
            print("Volume: MAX")
            self.volume = 30
        else:
            print("Volume: {}".format(self.volume))
        
    def turn_volume_down(self):
        self.volume -= 1
        if self.volume < 0:
            print("Volume: MUTE")
            self.volume = 0
        else:
            print("Volume: {}".format(self.volume))
        
    def change_channel(self):
        while True:
            try:
                channel = int(input("Channel number: "))
                break
            except ValueError:
                print("Please enter a number (1-4)")
        if channel == 1:
            print("BBC One.")
        elif channel == 2:
            print("BBC Two.")
        elif channel == 3:
            print("ITV.")
        elif channel == 4:
            print("Channel 4.")
        else:
            print("Out of Range.")
        

def main():
    
    tv = Television()
    while True:
        print("""
            1 - Change Channel
            2 - Turn up Volume
            3 - Turn down Volume
            """)
        user_choice = input("> ")
        
        if user_choice == "1":
            tv.change_channel()
        elif user_choice == "2":
            tv.turn_volume_up()
        elif user_choice == "3":
            tv.turn_volume_down()
        else:
            print("{} isn't a valid choice".format(user_choice))
            
main()
                
            