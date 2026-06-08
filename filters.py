import pandas as pd
def load_data():
    
    df = pd.read_csv("data/forestfires.csv")

    return df
df = load_data()
def apply_filters(
        df,
        selected_months,
        temp_range,
        selected_days,
        search_text
):
    
    if selected_months:
        df = df[df["month"].isin(selected_months)]

    if selected_days:
        df = df[df["day"].isin(selected_days)]

    df = df[
        (df["temp"] >= temp_range[0])
        &
        (df["temp"] <= temp_range[1])
    ]

    if search_text:
        df = df[
            df["month"]
            .str.contains(
                search_text,
                case=False,
                na=False
            )
        ]

    return df
