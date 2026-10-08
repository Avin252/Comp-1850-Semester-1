import os
import random
import sys
from typing import Dict, List, Optional, Tuple


DIRECTIONS = {
    "n": (0, -1),
    "s": (0, 1),
    "e": (1, 0),
    "w": (-1, 0),
    "north": (0, -1),
    "south": (0, 1),
    "east": (1, 0),
    "west": (-1, 0),
}


def clear_screen():
    if os.environ.get("TERM"):
        os.system("cls" if os.name == "nt" else "clear")


class Game:
    def __init__(self):
        self.player_pos = (0, 0)
        self.player_hp = 12
        self.max_hp = 12
        self.gold = 0
        self.inventory = ["potion", "potion"]
        self.relics = []
        self.turn = 0
        self.map = self._build_map()
        self.exit_room = (2, 2)
        self.game_over = False
        self.victory = False

    def _build_map(self) -> Dict[Tuple[int, int], Dict[str, object]]:
        rooms = {
            (0, 0): {
                "name": "Sunlit Clearing",
                "description": "A bright clearing where the forest opens up to a warm breeze.",
                "items": ["potion"],
                "enemy": None,
            },
            (1, 0): {
                "name": "Old Bridge",
                "description": "Wooden planks creak over a dark ravine. A thin fog drifts below.",
                "items": [],
                "enemy": "goblin",
            },
            (2, 0): {
                "name": "Ancient Gate",
                "description": "A broken stone arch hums with old magic. The air smells of rain.",
                "items": ["emerald relic"],
                "enemy": None,
            },
            (0, 1): {
                "name": "Mossy Path",
                "description": "This trail is covered in moss and tiny glowing mushrooms.",
                "items": [],
                "enemy": "slime",
            },
            (1, 1): {
                "name": "Moonwell",
                "description": "A still pool reflects the moon, and a soft blue glow ripples across it.",
                "items": ["potion"],
                "enemy": None,
            },
            (2, 1): {
                "name": "Ruined Hut",
                "description": "A collapsed hut sits under a twisted tree. Scraps of leather lie around.",
                "items": ["ruby relic"],
                "enemy": "bat",
            },
            (0, 2): {
                "name": "Whispering Woods",
                "description": "The trees lean close and whisper in a language you almost understand.",
                "items": [],
                "enemy": "skeleton",
            },
            (1, 2): {
                "name": "Hidden Cave",
                "description": "A cave mouth opens into darkness, and a faint chime echoes ahead.",
                "items": ["sapphire relic"],
                "enemy": "goblin",
            },
            (2, 2): {
                "name": "Sky Portal",
                "description": "A shimmering portal waits at the edge of the world. You need 3 relics to leave.",
                "items": [],
                "enemy": None,
            },
        }
        return rooms

    def room(self):
        return self.map[self.player_pos]

    def look(self):
        room = self.room()
        print(f"\nYou are in the {room['name']}.")
        print(room["description"])
        if room["items"]:
            print("Here: " + ", ".join(room["items"]))
        else:
            print("There is nothing obvious here.")
        if room["enemy"]:
            enemy_name = room["enemy"].title()
            print(f"You see a {enemy_name} blocking the path!")
        else:
            print("The room feels safe for now.")
        self._show_exits()

    def _show_exits(self):
        directions = []
        x, y = self.player_pos
        for name, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy
            if (nx, ny) in self.map:
                directions.append(name.capitalize())
        print("Exits: " + ", ".join(directions) if directions else "Exits: none")

    def show_status(self):
        room = self.room()
        print(f"\nHP: {self.player_hp}/{self.max_hp} | Gold: {self.gold} | Relics: {len(self.relics)}/3")
        print(f"Location: {room['name']} | Inventory: {', '.join(self.inventory) if self.inventory else 'empty'}")

    def move(self, direction: str):
        dx, dy = DIRECTIONS.get(direction.lower(), (0, 0))
        if (dx, dy) == (0, 0):
            print("You can't move that way.")
            return

        x, y = self.player_pos
        nx, ny = x + dx, y + dy
        target = (nx, ny)
        if target not in self.map:
            print("A wall blocks your path.")
            return

        self.player_pos = target
        self.turn += 1
        room = self.room()
        print(f"You move to the {room['name']}.")

        if room["enemy"]:
            self._encounter_enemy(room["enemy"])
        else:
            self._check_room_loot()

    def _check_room_loot(self):
        room = self.room()
        if room["items"]:
            print("You scan the room and find: " + ", ".join(room["items"]))

    def _encounter_enemy(self, enemy_name: str):
        enemy_hp = 6
        print(f"A wild {enemy_name.title()} attacks!")

        while enemy_hp > 0 and self.player_hp > 0:
            action = input("Do you attack, use potion, or flee? ").strip().lower()
            if action in {"attack", "hit", "fight"}:
                damage = random.randint(2, 5)
                enemy_hp -= damage
                print(f"You hit for {damage} damage. Enemy HP: {enemy_hp}")
                if enemy_hp <= 0:
                    print(f"You defeated the {enemy_name.title()}!")
                    self.gold += random.randint(3, 8)
                    self.room()["enemy"] = None
                    self._check_room_loot()
                    return
                enemy_damage = random.randint(1, 4)
                self.player_hp = max(0, self.player_hp - enemy_damage)
                print(f"The {enemy_name.title()} hits you for {enemy_damage}.")
                if self.player_hp == 0:
                    print("You collapse in battle. Game over.")
                    self.game_over = True
                    return
            elif action in {"potion", "use potion"}:
                self.use_potion()
                if self.player_hp <= 0:
                    print("You collapse in battle. Game over.")
                    self.game_over = True
                    return
                enemy_damage = random.randint(1, 4)
                self.player_hp = max(0, self.player_hp - enemy_damage)
                print(f"The {enemy_name.title()} hits you for {enemy_damage}.")
                if self.player_hp == 0:
                    print("You collapse in battle. Game over.")
                    self.game_over = True
                    return
            elif action in {"flee", "run", "escape"}:
                if random.randint(1, 2) == 1:
                    print("You escape safely.")
                    return
                enemy_damage = random.randint(1, 3)
                self.player_hp = max(0, self.player_hp - enemy_damage)
                print(f"The {enemy_name.title()} blocks your escape and hits you for {enemy_damage}.")
                if self.player_hp == 0:
                    print("You collapse in battle. Game over.")
                    self.game_over = True
                    return
            else:
                print("Please choose: attack, use potion, or flee.")

    def take(self, item_name: str):
        room = self.room()
        item = item_name.lower().strip()
        if item in room["items"]:
            room["items"].remove(item)
            self.inventory.append(item)
            print(f"You picked up the {item}.")

            if item.endswith("relic"):
                self.relics.append(item)
                print(f"A relic hums in your hands. You now have {len(self.relics)}/3 relics.")
                if len(self.relics) >= 3:
                    print("The air crackles with power. The portal will accept you now!")
        else:
            print(f"You can't take '{item}' here.")

    def use_potion(self):
        if "potion" not in self.inventory:
            print("You have no potion to use.")
            return
        self.inventory.remove("potion")
        self.player_hp = min(self.max_hp, self.player_hp + 5)
        print(f"You drink a potion and restore 5 HP. HP is now {self.player_hp}/{self.max_hp}.")

    def check_exit(self):
        if self.player_pos == self.exit_room and len(self.relics) >= 3:
            print("\nThe gateway opens and the sky lights up in gold. You win!")
            self.victory = True
            self.game_over = True
        elif self.player_pos == self.exit_room:
            print("\nThe portal is sealed. It needs 3 relics to awaken.")

    def help_text(self):
        print("\nCommands:")
        print("  move north / n | south / s | east / e | west / w")
        print("  look")
        print("  inventory")
        print("  stats")
        print("  take <item>")
        print("  use potion")
        print("  attack")
        print("  help")
        print("  quit")

    def process_command(self, raw_command: str):
        command = raw_command.strip()
        if not command:
            return

        if command.lower() in {"quit", "exit"}:
            print("You leave the adventure unfinished.")
            self.game_over = True
            return

        if command.lower() in {"help", "?"}:
            self.help_text()
            return

        if command.lower() in {"look", "l"}:
            self.look()
            return

        if command.lower() in {"stats", "status"}:
            self.show_status()
            return

        if command.lower() in {"inventory", "inv"}:
            print("Inventory: " + (", ".join(self.inventory) if self.inventory else "empty"))
            return

        words = command.split()
        first = words[0].lower()

        if first in {"move", "go"} and len(words) > 1:
            direction = words[1].lower()
            if direction in DIRECTIONS:
                self.move(direction)
            else:
                print("Choose a valid direction: north, south, east, west.")
            return

        if first in {"north", "south", "east", "west", "n", "s", "e", "w"}:
            self.move(first.lower())
            return

        if first == "take":
            if len(words) < 2:
                print("Use: take <item>")
            else:
                self.take(" ".join(words[1:]))
            return

        if first == "use":
            if len(words) > 1 and words[1].lower() == "potion":
                self.use_potion()
            else:
                print("Use a potion from your inventory.")
            return

        if first == "attack":
            if self.room()["enemy"]:
                self._encounter_enemy(self.room()["enemy"])
            else:
                print("There is no enemy here.")
            return

        print("Unknown command. Type 'help' for a list of commands.")

    def run(self):
        clear_screen()
        print("=== Lost in the Moonlit Woods ===")
        print("Collect 3 relics and escape through the sky portal.")
        print("Type 'help' at any time.\n")
        self.look()

        while not self.game_over:
            if self.player_pos == self.exit_room:
                self.check_exit()
                if self.game_over:
                    break
            try:
                raw = input("\nWhat do you do? ")
            except EOFError:
                print("\nGoodbye.")
                break
            self.process_command(raw)
            if self.player_hp <= 0:
                self.game_over = True
                break
            self.show_status()

        if self.victory:
            print("\nYou win! The portal carries you home beneath the stars.")
        elif not self.game_over:
            print("\nThe adventure ends.")
        else:
            print("\nThanks for playing!")


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
        sys.exit(0)
