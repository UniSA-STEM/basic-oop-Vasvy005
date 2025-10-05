"""
File: hacker.py
Description: Defines the Hacker class. A hacker has a name, an inventory, a trace 
level, and may acquire a rig. Hackers can attack other rigs with data spikes, 
extract assets, encrypt/decrypt items, and upgrade their rigs.
Author: Vedant Vashist
ID: 110315681
Username: VASVY005
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name: str):
        self.name = name
        self.inventory = [Asset("CryptoToken", "Used to buy/repair rigs")]
        self.rig = None
        self.trace = 0

    def __str__(self):
        inv = ", ".join([f"{a.name}{'(E)' if a.encrypted else ''}" for a in self.inventory]) or "Empty"
        rig_name = self.rig.name if self.rig else "No Rig"
        return f"Hacker {self.name} | Rig: {rig_name} | Trace: {self.trace} | Inventory: [{inv}]"

    def _consume_from_inventory(self, name):
        for i, a in enumerate(self.inventory):
            if a.name == name:
                return self.inventory.pop(i)
        return None

    def acquire_rig(self, rig: Rig = None):
        token = self._consume_from_inventory("CryptoToken")
        if not token:
            print("No CryptoToken to acquire a rig. (Need 1)")
            return False
        if rig is None:
            rig = Rig(f"{self.name}'s Rig")
        self.rig = rig
        print(f"{self.name} acquired rig '{rig.name}' and activated it.")
        return True

    def launch_data_spike(self, target_rig: Rig):
        if self.trace > 5:
            print("Trace too high — action blocked.")
            return False
        if not self.rig:
            print("No rig to launch from.")
            return False
        for i, a in enumerate(self.rig.storage):
            if a.name == "Data Spike":
                self.rig.storage.pop(i)
                target_broken = target_rig.take_hit()
                self.trace += 1
                print(f"{self.name} launched Data Spike at {target_rig.name}. Broken: {target_broken}")
                return True
        print("No Data Spike available in rig.")
        return False

    def extract_from(self, target_rig: Rig):
        has_drive = any(a.name == "Removable Drive" for a in (self.rig.storage if self.rig else []))
        if not has_drive:
            drive = self._consume_from_inventory("Removable Drive")
            if not drive:
                print("No Removable Drive available to extract.")
                return False
        else:
            for i, a in enumerate(self.rig.storage):
                if a.name == "Removable Drive":
                    self.rig.storage.pop(i)
                    break
        if not target_rig.broken:
            print("Target rig is not broken; extraction not allowed.")
            return False
        moved = []
        remaining = []
        for a in target_rig.storage:
            if not a.encrypted:
                self.inventory.append(a)
                moved.append(a.name)
            else:
                remaining.append(a)
        target_rig.storage = remaining
        print(f"Extracted assets: {moved}")
        self.trace += 2
        return True

    def encrypt_asset(self, asset_name):
        chip = self._consume_from_inventory("Security Chip")
        if not chip:
            print("Encryption requires a Security Chip.")
            return False
        for a in self.inventory:
            if a.name == asset_name and not a.encrypted:
                a.encrypted = True
                print(f"{asset_name} encrypted in inventory.")
                return True
        if self.rig:
            for a in self.rig.storage:
                if a.name == asset_name and not a.encrypted:
                    a.encrypted = True
                    print(f"{asset_name} encrypted in rig storage.")
                    return True
        print(f"No unencrypted asset named {asset_name} found.")
        return False

    def decrypt_asset(self, asset_name):
        chip = self._consume_from_inventory("Security Chip")
        if not chip:
            print("Decryption requires a Security Chip.")
            return False
        for a in self.inventory:
            if a.name == asset_name and a.encrypted:
                a.encrypted = False
                print(f"{asset_name} decrypted in inventory.")
                return True
        if self.rig:
            for a in self.rig.storage:
                if a.name == asset_name and a.encrypted:
                    a.encrypted = False
                    print(f"{asset_name} decrypted in rig storage.")
                    return True
        print(f"No encrypted asset named {asset_name} found.")
        return False

    def upgrade_rig(self):
        if not self.rig:
            print("No rig to upgrade.")
            return False
        patch = self._consume_from_inventory("Hardware Patch")
        if not patch:
            print("Hardware Patch required to upgrade.")
            return False
        self.rig.upgrade()
        self.trace += 1
        return True

    def store_to_rig(self, asset_name):
        if not self.rig:
            print("No rig to store assets to.")
            return False
        for i, a in enumerate(self.inventory):
            if a.name == asset_name:
                if a.encrypted:
                    print("Encrypted assets cannot be transferred until decrypted.")
                    return False
                self.rig.storage.append(self.inventory.pop(i))
                print(f"{asset_name} moved to rig storage.")
                return True
        print(f"No asset named {asset_name} in inventory.")
        return False

    def retrieve_from_rig(self, asset_name):
        if not self.rig:
            print("No rig to retrieve from.")
            return False
        for i, a in enumerate(self.rig.storage):
            if a.name == asset_name:
                if a.encrypted:
                    print("Cannot retrieve encrypted asset until decrypted.")
                    return False
                self.inventory.append(self.rig.storage.pop(i))
                print(f"{asset_name} retrieved from rig.")
                return True
        print(f"No asset named {asset_name} in rig storage.")
        return False

    def find_in_inventory(self, name):
        for i, a in enumerate(self.inventory):
            if a.name == name:
                return self.inventory.pop(i)
        return None
