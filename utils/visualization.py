import matplotlib.pyplot as plt

def plot_cases(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Cases'])
    plt.title("Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.show()
