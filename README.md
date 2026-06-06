import streamlit as st

from filters import *
from charts import *
st.set_page_config(

    page_title="Forest Fire Dashboard",

    layout="wide"

)
st.title(

    "🔥 Forest Fire Dashboard"

)
df = load_data() 
st.sidebar.header(

    "Dashboard Filters"

)
selected_months = (

    st.sidebar.multiselect(

        "Select Month",

        df["month"].unique()

    )

)
selected_days = (

    st.sidebar.multiselect(

        "Select Day",

        df["day"].unique()

    )

)
temp_range = (

    st.sidebar.slider(

        "Temperature Range",

        float(df["temp"].min()),

        float(df["temp"].max()),

        (

            float(df["temp"].min()),

            float(df["temp"].max())

        )

    )

) 
search_text = (

    st.sidebar.text_input(

        "Search Month"

    )

)

filtered_df = apply_filters(

    df,

    selected_months,

    temp_range,

    selected_days,

    search_text

)
if st.sidebar.button(

    "Reset Filters"

):

    st.rerun() 
    c1, c2, c3 = st.columns(3) 
    c1.metric(

    "Average Temp",

    round(

        filtered_df["temp"].mean(),

        2

    )

)
     
    c2.metric(

    "Average Humidity",

    round(

        filtered_df["RH"].mean(),

        2

    )

)
    c3.metric(

    "Maximum Area",

    round(

        filtered_df["area"].max(),

        2

    )

)
    st.header("Pie Chart")

st.pyplot(

    pie_chart(filtered_df)

)
st.header("Histogram")

st.pyplot(

    histogram(filtered_df)

) 
st.header("Line Chart")

st.pyplot(

    line_chart(filtered_df)

)
st.header("Bar Chart")

st.pyplot(

    bar_chart(filtered_df)

)
st.header("Scatter Plot")

st.pyplot(

    scatter_plot(filtered_df)

)
st.header("Box Plot")

st.pyplot(

    box_plot(filtered_df)

)
st.header("Heatmap")

st.pyplot(

    heatmap(filtered_df)

)
st.header("Area Chart")

st.pyplot(

    area_chart(filtered_df)

)
st.header("Count Plot")

st.pyplot(

    count_plot(filtered_df)

)
st.header("Violin Plot")

st.pyplot(

    violin_plot(filtered_df)

)
st.download_button(

    "Download Filtered Data",

    filtered_df.to_csv(

        index=False

    ),

    "filtered_data.csv"

)
st.header(

    "Key Insights"

)
st.write("""



1. August and September have

the highest number of fires.



2. Temperature has positive

impact on burned area.



3. Rain is very low in most

fire events.



4. Humidity influences fire

spread.



5. Some extreme outliers

exist in burned area.



""")

