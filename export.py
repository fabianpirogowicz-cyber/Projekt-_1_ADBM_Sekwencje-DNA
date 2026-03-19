import pandas as pd


def export_to_csv(data, filename="results.csv"):

    df = pd.DataFrame({
        "motif": [data["motif"]],
        "count": [data["count"]],
        "positions": [",".join(map(str, data["positions"]))]
    })

    df.to_csv(filename, index=False)