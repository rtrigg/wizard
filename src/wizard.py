from dataclasses import dataclass, field

@dataclass
class Wizard:
    """Class for keeping track of Wizard."""
    name: str
    inventory: list = field(default_factory=lambda: [])
    food: int = 25
    gold: int = 25
    alive: bool = True

    def update(self):
        if self.food < 0:
            self.alive = False

    def eat(self) -> None:
        self.food += 10

    def buy_item(self, shop, item) -> None:
        self.gold -= shop.sell(item)
        self.inventory.append(item)


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


