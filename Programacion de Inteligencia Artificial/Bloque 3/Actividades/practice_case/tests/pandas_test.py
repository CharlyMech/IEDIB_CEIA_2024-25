import pandas as pd

dades = {
    "illa": ["Mallorca", "Menorca", "Eivissa", "Formentera"],
    "superficie": [3620, 692, 577, 83],
    "poblacio": [923608, 94885, 147914, 11708],
}
df = pd.DataFrame(dades)
print("Superfície total:", df["superficie"].sum(), "km2")
