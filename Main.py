"""
File: main.py
Description: Main test program for the "Into the Grid" assignment. This script 
creates hackers and rigs, simulates battles, upgrades, encryption/decryption, 
trace management, and edge cases for testing purposes.
Author: Vedant Vashist
ID: 110315681
Username: VASVY005
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from hacker import Hacker
from rig import Rig
from asset import Asset

def demo():
    alice = Hacker("Alice")
    bob = Hacker("Bob")
    bob.acquire_rig(Rig("Bob-Rig"))

    print("=== START STATES ===")
    print(alice)
    print(bob.rig)

    alice.acquire_rig()
    alice.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs"))
    alice.inventory.append(Asset("Security Chip", "Used to encrypt/decrypt"))
    alice.rig.generate_asset()
    print(alice.rig)

    print("\n=== ATTACK SEQUENCE (Alice -> Bob) ===")
    alice.launch_data_spike(bob.rig)
    alice.launch_data_spike(bob.rig)
    print(bob.rig)

    print("\n=== EXTRACTION (if broken) ===")
    alice.inventory.append(Asset("Removable Drive", "Used to extract assets"))
    alice.extract_from(bob.rig)
    print(alice)

    print("\n=== ENCRYPTION DEMO ===")
    alice.encrypt_asset("CryptoToken")
    print(alice)

    print("\n=== EDGE CASE: upgrade without rig ===")
    other = Hacker("NoRigGuy")
    other.upgrade_rig()

if __name__ == "__main__":
    demo()
