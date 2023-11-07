class Game:
    def __init__(self):
        self.player_name = ""
        self.inventory = []
        self.story_progress = 0

    def start(self):
        print("Welcome to 'The Quest for the Golden Bow' - An Epic Text-Based Adventure Game!")
        print("Enter your name, valiant adventurer:")
        self.player_name = input("> ")
        print(f"Welcome, {self.player_name}! Your journey begins now.")
        self.intro()

    def intro(self):
        print("\nYou find yourself in the sacred city of Ayodhya, where a great crisis has struck. The powerful demon king Ravana has stolen the Golden Bow.")
        print("1. Offer to retrieve the Golden Bow.")
        print("2. Seek guidance from the sage Valmiki.")
        choice = input("> ")

        if choice == "1":
            print("\nYou decide to offer your services to Lord Rama and vow to retrieve the Golden Bow from Ravana.")
            self.inventory.append("Loyal Servant of Rama")
            self.story_progress += 1
            self.rama_quest()
        elif choice == "2":
            print("\nYou seek guidance from the wise sage Valmiki, who offers you his blessings and a sacred mantra to aid your quest.")
            self.inventory.append("Valmiki's Blessing")
            self.story_progress += 1
            self.rama_quest()
        else:
            print("Invalid choice. Please try again.")
            self.intro()

    def rama_quest(self):
        print("\nYou set off on your epic journey to rescue the Golden Bow from Ravana's kingdom of Lanka.")
        print("1. Begin your journey to Lanka.")
        print("2. Gather information in Ayodhya before departing.")
        choice = input("> ")

        if choice == "1":
            self.begin_journey_to_lanka()
        elif choice == "2":
            print("\nYou gather information and supplies in Ayodhya, preparing for the long and perilous journey ahead.")
            self.story_progress += 1
            self.rama_quest()
        else:
            print("Invalid choice. Please try again.")
            self.rama_quest()

    def begin_journey_to_lanka(self):
        print("\nYou embark on your quest, facing numerous challenges, allies, and adversaries along the way.")
        print("1. Continue your journey to Lanka.")
        print("2. Rest and regroup in a nearby village.")
        choice = input("> ")

        if choice == "1":
            self.face_perils_on_the_way()
        elif choice == "2":
            print("\nYou decide to rest and regroup, ensuring you're well-prepared for the adventures ahead.")
            self.story_progress += 1
            self.rama_quest()
        else:
            print("Invalid choice. Please try again.")
            self.begin_journey_to_lanka()

    def face_perils_on_the_way(self):
        print("\nAs you journey towards Lanka, you encounter various challenges, including mystical forests, cunning demons, and treacherous waters.")
        print("1. Overcome the challenges and continue your quest.")
        print("2. Seek help from Hanuman, the Monkey God.")
        choice = input("> ")

        if choice == "1":
            print("\nYou face the challenges with determination, making progress towards Lanka.")
            self.story_progress += 1
            self.reach_lanka()
        elif choice == "2":
            print("\nYou call upon Hanuman, the devoted servant of Lord Rama, who aids you in overcoming the perils on your way.")
            self.story_progress += 1
            self.reach_lanka()
        else:
            print("Invalid choice. Please try again.")
            self.face_perils_on_the_way()

    def reach_lanka(self):
        print("\nYou finally arrive in Lanka, where you must devise a plan to retrieve the Golden Bow from Ravana's fortress.")
        print("1. Infiltrate Ravana's fortress.")
        print("2. Seek help from Vibhishana, Ravana's brother and a devotee of Lord Rama.")
        choice = input("> ")

        if choice == "1":
            print("\nYou stealthily infiltrate Ravana's fortress, determined to find and retrieve the Golden Bow.")
            self.inventory.append("Infiltrator")
            self.story_progress += 1
            self.retrieve_golden_bow()
        elif choice == "2":
            print("\nYou seek Vibhishana's help, and he offers his support and guidance in your mission.")
            self.inventory.append("Vibhishana's Support")
            self.story_progress += 1
            self.retrieve_golden_bow()
        else:
            print("Invalid choice. Please try again.")
            self.reach_lanka()

    def retrieve_golden_bow(self):
        print("\nYou locate the Golden Bow within the heart of Ravana's fortress.")
        print("1. Attempt to steal the Golden Bow quietly.")
        print("2. Confront Ravana and challenge him for the bow.")
        choice = input("> ")

        if choice == "1" and "Infiltrator" in self.inventory:
            print("\nYou manage to steal the Golden Bow without alerting Ravana's guards, and you make your escape.")
            self.story_progress += 1
            self.win_game()
        elif choice == "2":
            print("\nYou confront Ravana in a mighty battle, showcasing your valor and determination. Lord Rama's blessings are with you.")
            self.story_progress += 1
            self.win_game()
        else:
            print("Invalid choice. Please try again.")
            self.retrieve_golden_bow()

    def win_game(self):
        print("\nCongratulations, valiant adventurer! You have successfully retrieved the Golden Bow and completed your epic quest.")
        print(f"{self.player_name}, your name will be celebrated for your bravery and devotion to Lord Rama.")
        print("Thank you for playing 'The Quest for the Golden Bow'!")

if __name__ == "__main__":
    game = Game()
    game.start()
