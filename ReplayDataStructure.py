from dataclasses import dataclass


@dataclass
class GameMetadata:
    """Data structure to store metadata of a replay file"""
    id: str
    time_stamp: str  # debateable if this should be a datetime object