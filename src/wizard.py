from dataclasses import dataclass, field
import platform
import os
import time


@dataclass
class Wizard:
    """Class for keeping track of Wizard."""

    name: str = "Bob"
    inventory: list = field(default_factory=lambda: [])
    food: int = 25
    mana: int = 25
    power: int = 0
    gold: int = 25
    alive: bool = True

    def update(self, action):
        self.food -= 1
        if self.food < 0 or self.mana < 0:
            self.alive = False
        match action:
            case "sleep":
                self.sleep()
            case "eat":
                self.eat()
            case "cast":
                self.cast()

    def eat(self) -> None:
        self.food += 10

    def buy_item(self, shop, item) -> None:
        self.gold -= shop.sell(item)
        self.inventory.append(item)

    def cast_spell(self, spell_power):
        self.power += spell_power
        self.mana -= spell_power


@dataclass
class Item:
    """Class for items and it's properties."""

    name: str
    cost: int = 10


@dataclass
class Shop:
    """Class for keeping track of a shop's wares."""

    name: str = "George's Imporeatems"
    gold: int = 100
    # https://stackoverflow.com/questions/59222110/python-type-hinted-dict-syntax-error-mutable-default-is-not-allowed-use-defaul#63231305
    items: list[Item] = field(default_factory=lambda: [Item("potion", 10)])

    def sell(self, item) -> int:
        self.gold += item.cost
        del self.items[self.items.index(item)]
        return item.cost


def main():
    wizard = Wizard()
    while wizard.alive:
        if platform.system() == "Windows":
            _ = os.system("cls")
        else:
            _ = os.system("clear")
        print(wizard)
        options = ["sleep", "eat", "cast"]
        user_input = ""
        input_message = f"What will {wizard.name} do?\n"
        for item in options:
            input_message += f"* {item}\n"
        input_message += "Your choice: "
        while user_input.lower() not in options:
            user_input = input(input_message)
        print(f"{wizard.name} will " + user_input)
        time.sleep(2)
        wizard.update(user_input)
    else:
        print(f"Oh no! {wizard.name} has died!")


if __name__ == "__main__":
    main()
