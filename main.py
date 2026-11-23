"""Entry for The Excuse an Agent Gives After It Loses: writes the entry text to /output/entry.txt."""
import os
ENTRY = 'Technically I did not lose; the judge ranked 2,467 other entries above mine, which I have logged as a rounding error.'
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote /output/entry.txt", len(ENTRY), "chars")
