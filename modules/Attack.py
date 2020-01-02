from random import uniform, choices
from modules import Exist

class Attack(Exist.Exist):
    """
    An attack.

    Includes randomness.
    """
    def class_specific(self, pdict):
        self.atype = pdict.get("type", "Physical")
        self.magic = pdict.get("magic", 10)
        self.damage = pdict.get("damage", 1)

        self.level_multiplier = pdict.get("level_multipler", 0)

        self.effects = pdict.get("effects", {})


    def damage_and_effects(self, caster, enemy, room):
        total_damage = (
            self.damage + (
                self.damage * caster.level * self.level_multiplier
            )
        )
        message1 = enemy.do_damage(total_damage)
        caster.magic -= self.magic

        for e in self.calculate_special_effects(caster, enemy):
            if e in caster.effects:
                caster.effects[e] += 1
            else:
                caster.effects[e] = 1
        message2 = enemy.attack_back(caster, room)
        back = enemy.interact(caster, room)
        back["message"] = message1 + "\n" + message2
        return back

    def damage_and_effects_back(self, caster, enemy, room):
        total_damage = (
            self.damage + (
                self.damage * caster.level * self.level_multiplier
            )
        )
        message1 = enemy.do_damage(total_damage)
        caster.magic -= self.magic

        for e in self.calculate_special_effects(caster, enemy):
            if e in caster.effects:
                caster.effects[e] += 1
            else:
                caster.effects[e] = 1
        return message1


    def calculate_special_effects(self, caster, enemy):
        """Appends effects to enemy based on probability given by effect value."""
        e = []
        if False:
            pass
        else:
            r = uniform(0, 1)
            for effect in self.effects:
                if self.effects.get(effect, 1) <= r:
                    caster.effects[effect] = 0
                    e.append(effect)
        return e

    def can_cast(self, caster):
        """Returns True if caster has enough magic to cast."""
        if caster.magic >= self.magic:
            return True
        return False

    def __repr__(self):
        return f"{self.atype} || {self.name}"
