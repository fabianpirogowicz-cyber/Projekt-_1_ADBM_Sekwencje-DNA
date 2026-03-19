import numpy as np
import pandas as pd
from Bio import SeqIO


def load_sequence(file_path):
    """Wczytanie sekwencji z FASTA lub TXT"""

    if file_path.endswith(".fasta") or file_path.endswith(".fa"):
        for record in SeqIO.parse(file_path, "fasta"):
            return str(record.seq)
    else:
        with open(file_path, "r") as f:
            return f.read().strip()


def find_motif(sequence, motif):
    """Znajduje wszystkie pozycje motywu w sekwencji"""

    positions = []

    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            positions.append(i)

    return positions


def motif_statistics(sequence, motif):

    positions = find_motif(sequence, motif)

    data = {
        "motif": motif,
        "count": len(positions),
        "positions": positions
    }

    return data


def segment_sequence(sequence, segment_size=100):

    segments = []

    for i in range(0, len(sequence), segment_size):
        segment = sequence[i:i+segment_size]
        segments.append(segment)

    df = pd.DataFrame({
        "segment_start": np.arange(0, len(sequence), segment_size),
        "segment": segments
    })

    return df