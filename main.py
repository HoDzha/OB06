# Игра бива героев

class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, other):
        other.health -= self.attack_power
    def in_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.in_alive() and self.computer.in_alive():
            self.player.attack(self.computer)
            print (f"{self.player.name} атакует {self.computer.name}!")
            print (f"У {self.computer.name} осталось {self.computer.health} жизни.")
            if not self.computer.in_alive():
                print(f"{self.player.name} победил!")
                break
            self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name}!")
            print(f"У {self.player.name} осталось {self.player.health} жизнй.")
            if not self.player.in_alive():
                print(f"{self.computer.name} победил!")
                break

player1 = Hero("Зомби", 100, 20)
player2 = Hero("Компьютер", 100, 20)
game = Game(player1, player2)
game.start()



