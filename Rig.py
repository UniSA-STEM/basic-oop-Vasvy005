"""
File: rig.py
Description: Defines the Rig class. A rig is the hacker’s computer system that 
can take damage, be repaired, upgraded, and store assets. It starts with 
basic assets and can generate new ones during the simulation.
Author: Vedant Vashist
ID: 110315681
Username: VASVY005
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from Asset import Asset

class Rig:
    def __init__(self, name: str):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        self.storage = [
            Asset("Data Spike", "Used to attack other rigs"),
            Asset("Data Spike", "Used to attack other rigs"),
            Asset("Removable Drive", "Used to extract assets")
        ]

    def condition(self):
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        if self.damage == 0:
            return f"Pristine (Level {self.upgrade_level})"
        return f"Damaged({self.damage}) (Level {self.upgrade_level})"

    def __str__(self):
        stored = ", ".join([a.name + ("(E)" if a.encrypted else "") for a in self.storage]) or "No assets"
        return f"{self.name} - {self.condition()} - Storage: [{stored}]"

    def take_hit(self):
        threshold = max(2 + self.upgrade_level, 1)
        self.damage += 1
        if self.damage >= threshold:
            self.broken = True
        print(f"[DEBUG] {self.name} took a hit; damage={self.damage}, broken={self.broken}")
        return self.broken

    def repair(self, crypto_token: Asset = None):
        if self.damage == 0 and not self.broken:
            print("No repair needed — rig is fine.")
            return False
        self.damage = 0
        self.broken = False
        print(f"{self.name} repaired.")
        return True

    def upgrade(self, hardware_patch: Asset = None):
        self.upgrade_level += 1
        self.storage.append(Asset("Data Spike", "Used to attack other rigs"))
        print(f"{self.name} upgraded to level {self.upgrade_level}.")

    def generate_asset(self):
        choice = random.choice(["CryptoToken", "Data Spike", "Security Chip"])
        if choice == "CryptoToken":
            a = Asset("CryptoToken", "Used to buy/repair rigs")
        elif choice == "Security Chip":
            a = Asset("Security Chip", "Used to encrypt/decrypt assets")
        else:
            a = Asset("Data Spike", "Used to attack other rigs")
        self.storage.append(a)
        return a

    def store_asset(self, asset: Asset):
        self.storage.append(asset)

    def remove_asset(self, name: str):
        for i, a in enumerate(self.storage):
            if a.name == name and not a.encrypted:
                return self.storage.pop(i)
        return None
