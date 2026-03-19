import matplotlib.pyplot as plt


def plot_motif_positions(sequence_length, positions):

    plt.figure(figsize=(10,3))

    y = [1]*len(positions)

    plt.scatter(positions, y)

    plt.title("Rozmieszczenie motywów w sekwencji DNA")
    plt.xlabel("Pozycja w sekwencji")
    plt.yticks([])

    plt.show()


def bar_plot(count):

    plt.bar(["Motif"], [count])
    plt.title("Liczba wystąpień motywu")

    plt.show()