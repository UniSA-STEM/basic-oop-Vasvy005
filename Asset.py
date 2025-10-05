"""
File: asset.py
Description: Defines the Asset class. Assets represent digital items like 
CryptoTokens, Data Spikes, and Security Chips. Assets can also be encrypted 
to protect them from being transferred or stolen.
Author: Vedant Vashist
ID: 110315681
Username: VASVY005
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from dataclasses import dataclass

@dataclass
class Asset:
    name: str
    description: str
    encrypted: bool = False

    def __str__(self):
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        return f"{self.name}: {self.description}"
