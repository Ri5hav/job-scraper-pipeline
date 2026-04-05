import matplotlib.pyplot as plt

def plot_bar(data, title):
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel("")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_pie(data, title):
    data.plot(kind='pie', autopct='%1.1f%%')
    plt.title(title)
    plt.ylabel("")
    plt.tight_layout()
    plt.show()