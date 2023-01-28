from wizard import Wizard, Shop

def test_eat():
    wizard = Wizard("Bob", 0)
    initial_satiety = wizard.satiety
    wizard.eat()
    assert wizard.satiety > initial_satiety, f"Hunger meter not filled after eating. Expected > {initial_satiety}, but got {wizard.satiety}."


def test_buy_item():
    wizard = Wizard("Bob")
    shop = Shop()
    initial_inventory = wizard.inventory.copy()
    item_to_buy = shop.items[0]
    wizard.buy_item(shop, item_to_buy)
    assert item_to_buy not in initial_inventory, f"{item_to_buy} not added to inventory after buying"
    assert item_to_buy in wizard.inventory, f"{item_to_buy} not found in the wizard's inventory after buying"
    assert item_to_buy not in shop.items, f"{item_to_buy} not removed from the shops's inventory after buying"

