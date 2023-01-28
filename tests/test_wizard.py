from wizard import Wizard

def test_eat():
    wizard = Wizard("Bob", 0)
    initial_satiety = wizard.satiety
    wizard.eat()
    assert wizard.satiety > initial_satiety, f"Hunger meter not filled after eating. Expected > {initial_satiety}, but got {wizard.satiety}."

