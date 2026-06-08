import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
def pie_chart(df):

    fig, ax = plt.subplots()

    df["month"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_title("Fire Distribution by Month")

    return fig
def histogram(df):

    fig, ax = plt.subplots()

    sns.histplot(
        df["temp"],
        bins=20,
        kde=True,
        ax=ax
    )

    ax.set_title("Temperature Distribution")

    return fig
def line_chart(df):

    monthly = (
        df.groupby("month")["area"]
        .mean()
    )

    fig, ax = plt.subplots()

    monthly.plot(
        marker="o",
        ax=ax
    )

    ax.set_title(
        "Average Burned Area by Month"
    )

    return fig
def bar_chart(df):

    fig, ax = plt.subplots()

    sns.barplot(
        x="month",
        y="temp",
        data=df,
        ax=ax
    )

    ax.set_title(
        "Average Temperature"
    )

    return fig
def scatter_plot(df):

    fig, ax = plt.subplots()

    sns.scatterplot(
        x="temp",
        y="area",
        data=df,
        ax=ax
    )

    ax.set_title(
        "Temperature vs Area"
    )

    return fig

def box_plot(df):

    fig, ax = plt.subplots()

    sns.boxplot(
        y=df["temp"],
        ax=ax
    )

    ax.set_title(
        "Temperature Spread"
    )

    return fig
def heatmap(df):

    fig, ax = plt.subplots(
        figsize=(10,8)
    )

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    ax.set_title(
        "Correlation Matrix"
    )

    return fig
def area_chart(df):

    monthly = (
        df.groupby("month")["area"]
        .sum()
    )

    fig, ax = plt.subplots()

    monthly.plot(
        kind="area",
        ax=ax
    )

    ax.set_title(
        "Total Burned Area"
    )

    return fig
def count_plot(df):

    fig, ax = plt.subplots()

    sns.countplot(
        x="day",
        data=df,
        ax=ax
    )

    ax.set_title(
        "Fire Count by Day"
    )

    return fig
def violin_plot(df):

    fig, ax = plt.subplots()

    sns.violinplot(
        y="temp",
        data=df,
        ax=ax
    )

    ax.set_title(
        "Temperature Density"
    )

    return fig
