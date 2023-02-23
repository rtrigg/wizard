from wizard import Wizard, Shop


def test_eat():
    wizard = Wizard()
    initial_food = wizard.food
    wizard.eat()
    assert (
        wizard.food > initial_food
    ), f"Hunger meter not filled after eating. Expected > {initial_food}, but got {wizard.food}."


def test_buy_item():
    wizard = Wizard()
    shop = Shop()
    initial_inventory = wizard.inventory.copy()
    item_to_buy = shop.items[0]
    wizard.buy_item(shop, item_to_buy)
    assert (
        item_to_buy not in initial_inventory
    ), f"{item_to_buy} not added to inventory after buying"
    assert (
        item_to_buy in wizard.inventory
    ), f"{item_to_buy} not found in the wizard's inventory after buying"
    assert (
        item_to_buy not in shop.items
    ), f"{item_to_buy} not removed from the shops's inventory after buying"


def test_wizard_starve():
    wizard = Wizard()
    wizard.food = -1
    wizard.update()
    assert not wizard.alive, "Wizard did not die when food fell below 0."


def test_wizard_death_mana():
    wizard = Wizard()
    wizard.mana = -1
    wizard.update()
    assert not wizard.alive, "Wizard did not die when mana below 0."


def test_wizard_power():
    wizard = Wizard()
    power = wizard.power
    spell_power = 3
    wizard.cast_spell(spell_power)
    assert (
        wizard.power == power + spell_power
    ), f"Wizard's power did not increase by {spell_power} after casting a spell."


def test_wizard_mana():
    wizard = Wizard()
    mana = wizard.mana
    spell_power = 3
    wizard.cast_spell(spell_power)
    assert (
        wizard.mana == mana - spell_power
    ), f"Wizard's mana did not decrease by {spell_mana} after casting a spell."
