import pandas as pd
import matplotlib.pyplot as plt

# Sample solar data
data = {
    "Day": [1, 2, 3, 4, 5],
    "Energy_Output": [20, 22, 19, 23, 18]
}

df = pd.DataFrame(data)

# Basic analysis
average_output = df["Energy_Output"].mean()
print("Average Energy Output:", average_output)

# Plot graph
plt.plot(df["Day"], df["Energy_Output"])
plt.xlabel("Day")
plt.ylabel("Energy Output")
plt.title("Solar Energy Output Analysis")
plt.show()
