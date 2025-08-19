import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------
# Sidebar UI
# -------------------
st.sidebar.title("User Input Panel")

# Sidebar widgets
option = st.sidebar.radio("Choose an option:", ["Option A", "Option B", "Option C"])
checkbox = st.sidebar.checkbox("Enable Feature")
slider_value = st.sidebar.slider("Select a number:", 0, 100, 50)
button_clicked = st.sidebar.button("Submit")

# -------------------
# Create dataframe from user inputs
# -------------------
data = {
    "Option": [option],
    "Checkbox": [checkbox],
    "Slider Value": [slider_value],
    "Button Clicked": [button_clicked]
}
df = pd.DataFrame(data)

st.subheader("User Input DataFrame")
st.write(df)

# -------------------
# Sample dataset for visualization
# -------------------
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
categories = np.random.choice(["A", "B", "C"], size=50)
sample_df = pd.DataFrame({"x": x, "y": y, "category": categories})

# -------------------
# Scatter Plot
# -------------------
st.subheader("Scatter Plot")
fig, ax = plt.subplots()
ax.scatter(sample_df["x"], sample_df["y"], c='blue', alpha=0.6)
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
st.pyplot(fig)

# -------------------
# Histogram
# -------------------
st.subheader("Histogram")
fig, ax = plt.subplots()
ax.hist(sample_df["x"], bins=10, alpha=0.7, color="orange")
ax.set_xlabel("X values")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# -------------------
# Bar Chart
# -------------------
st.subheader("Bar Chart")
bar_data = sample_df["category"].value_counts()
fig, ax = plt.subplots()
bar_data.plot(kind="bar", ax=ax, color=["red", "green", "blue"])
ax.set_ylabel("Count")
st.pyplot(fig)

# -------------------
# Radar Chart
# -------------------
st.subheader("Radar Chart Example")

# Example: using 5 categories with random values
labels = ["Metric 1", "Metric 2", "Metric 3", "Metric 4", "Metric 5"]
values = np.random.randint(1, 10, size=len(labels))
values = np.append(values, values[0])  # close the radar loop
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(subplot_kw={'polar': True})
ax.plot(angles, values, "o-", linewidth=2, label="User Metrics")
ax.fill(angles, values, alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
st.pyplot(fig)
