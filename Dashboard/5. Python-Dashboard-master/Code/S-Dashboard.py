import plotly
import numpy
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Set up the Streamlit page configuration
st.set_page_config(page_title="DataXplore", page_icon="	:mag:", layout="wide")

# Title of the application
st.title(" :bar_chart: Sample SuperStore EDA")
st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

try:
    # File uploader for users to upload their data files
    fl = st.file_uploader(":file_folder: Upload a Superstore file", type=["csv", "txt", "xlsx", "xls"])
    
    # Load data based on file upload
    if fl is not None:
        df = pd.read_csv(fl, encoding="ISO-8859-1")
    else:
        # If no file is uploaded, set the working directory and load a default CSV
        os.chdir(r"C:\Users\Vishal.Dubey\Downloads\Dashboard Folder")
        df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")
    
    # Create two columns for layout
    col1, col2 = st.columns((2))
    
    # Convert 'Order Date' to datetime format with error handling
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')
    
    # Get the minimum and maximum dates from the dataset
    startDate = df["Order Date"].min()
    endDate = df["Order Date"].max()
    
    # Date input widgets for user to select a date range
    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))
    
    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))
    
    # Filter the DataFrame based on the selected date range
    df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()
    
    # Sidebar for filtering options
    st.sidebar.header("Choose your filter: ")
    
    # Multiselect for Region filtering
    region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
    df2 = df.copy() if not region else df[df["Region"].isin(region)]
    
    # Multiselect for State filtering
    state = st.sidebar.multiselect("Pick the State", df2["State"].unique())
    df3 = df2.copy() if not state else df2[df2["State"].isin(state)]
    
    # Multiselect for City filtering
    city = st.sidebar.multiselect("Pick the City", df3["City"].unique())
    
    # Filter the data based on selected Region, State, and City
    if not region and not state and not city:
        filtered_df = df
    elif not state and not city:
        filtered_df = df[df["Region"].isin(region)]
    elif not region and not city:
        filtered_df = df[df["State"].isin(state)]
    elif state and city:
        filtered_df = df3[df3["State"].isin(state) & df3["City"].isin(city)]
    elif region and city:
        filtered_df = df3[df3["Region"].isin(region) & df3["City"].isin(city)]
    elif region and state:
        filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state)]
    elif city:
        filtered_df = df3[df3["City"].isin(city)]
    else:
        filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]
    
    # Group the filtered data by Category and sum Sales
    category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()
    
    # Bar chart for Category-wise Sales
    with col1:
        st.subheader("Category wise Sales")
        fig = px.bar(category_df, x="Category", y="Sales", 
                      text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
                      template="seaborn")
        st.plotly_chart(fig, use_container_width=True, height=200)
    
    # Pie chart for Region-wise Sales
    with col2:
        st.subheader("Region wise Sales")
        fig = px.pie(filtered_df, values="Sales", names="Region", hole=0.5)
        fig.update_traces(text=filtered_df["Region"], textposition="outside")
        st.plotly_chart(fig, use_container_width=True)
    
    # Create two columns for additional data views
    cl1, cl2 = st.columns((2))
    
    # Expandable section for Category View Data
    with cl1:
        with st.expander("Category_ViewData"):
            st.write(category_df.style.background_gradient(cmap="Blues"))
            csv = category_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="Category.csv", mime="text/csv",
                               help='Click here to download the data as a CSV file')
    
    # Expandable section for Region View Data
    with cl2:
        with st.expander("Region_ViewData"):
            region = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
            st.write(region.style.background_gradient(cmap="Oranges"))
            csv = region.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name="Region.csv", mime="text/csv",
                               help='Click here to download the data as a CSV file')
    
    # Create a 'month_year' column for time series analysis
    filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
    st.subheader('Time Series Analysis')
    
    # Create a DataFrame for monthly sales
    linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
    # Line chart for monthly sales
    fig2 = px.line(linechart, x="month_year", y="Sales", labels={"Sales": "Amount"}, height=500, width=1000, template="gridon")
    st.plotly_chart(fig2, use_container_width=True)
    
    # Expandable section to view time series data
    with st.expander("View Data of TimeSeries:"):
        st.write(linechart.T.style.background_gradient(cmap="Blues"))
        csv = linechart.to_csv(index=False).encode("utf-8")
        st.download_button('Download Data', data=csv, file_name="TimeSeries.csv", mime='text/csv')
    
    # Treemap for hierarchical sales view
    st.subheader("Hierarchical view of Sales using TreeMap")
    fig3 = px.treemap(filtered_df, path=["Region", "Category", "Sub-Category"], values="Sales", hover_data=["Sales"],
                      color="Sub-Category")
    fig3.update_layout(width=800, height=650)
    st.plotly_chart(fig3, use_container_width=True)
    
    # Create two columns for segment and category pie charts
    chart1, chart2 = st.columns((2))
    
    # Pie chart for Segment-wise Sales
    with chart1:
        st.subheader('Segment wise Sales')
        fig = px.pie(filtered_df, values="Sales", names="Segment", template="plotly_dark")
        fig.update_traces(text=filtered_df["Segment"], textposition="inside")
        st.plotly_chart(fig, use_container_width=True)
    
    # Pie chart for Category-wise Sales
    with chart2:
        st.subheader('Category wise Sales')
        fig = px.pie(filtered_df, values="Sales", names="Category", template="gridon")
        fig.update_traces(text=filtered_df["Category"], textposition="inside")
        st.plotly_chart(fig, use_container_width=True)
    
    import plotly.figure_factory as ff
    
    # Display a sample summary table for sub-category sales
    st.subheader(":point_right: Month wise Sub-Category Sales Summary")
    with st.expander("Summary_Table"):
        df_sample = df[0:5][["Region", "State", "City", "Category", "Sales", "Profit", "Quantity"]]
        fig = ff.create_table(df_sample, colorscale="Cividis")
        st.plotly_chart(fig, use_container_width=True)
    
        st.markdown("Month wise sub-Category Table")
        filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
        sub_category_Year = pd.pivot_table(data=filtered_df, values="Sales", index=["Sub-Category"], columns="month")
        st.write(sub_category_Year.style.background_gradient(cmap="Blues"))
    
    # Create a scatter plot for Sales vs. Profit
    data1 = px.scatter(filtered_df, x="Sales", y="Profit", size="Quantity")
    data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
                           titlefont=dict(size=20), xaxis=dict(title="Sales", titlefont=dict(size=19)),
                           yaxis=dict(title="Profit", titlefont=dict(size=19)))
    st.plotly_chart(data1, use_container_width=True)
    
    # Expandable section to view detailed filtered data
    with st.expander("View Data"):
        st.write(filtered_df.iloc[:500, 1:20:2].style.background_gradient(cmap="Oranges"))
    
    # Download the original dataset
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name="Data.csv", mime="text/csv")
    
except Exception:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center;">
            <h3 style="color: grey;">Welcome in DataXplore :)</h3>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.stop()
