import streamlit as st
from datetime import datetime
import pytz
import time

def page_config():
    st.set_page_config(
        page_title="World Clock",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def get_time_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    local_time = datetime.now(tz)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

def world_clock():
    st.title("World Clock")
    
    # Add some HTML elements for better visualization
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            text-align: center;
            color: #333333;
            margin-bottom: 30px;
        }
        .timezone-column {
            padding: 20px;
            border: 1px solid #CCCCCC;
            border-radius: 10px;
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write("### Current Time in Selected Timezones:")
    # Create four columns
    col1, col2, col3, col4 = st.columns(4)

    # Allow users to select time zones for each column with unique keys
    selected_timezones_col1 = col1.multiselect("Select Timezones (Col 1):", pytz.all_timezones, key="col1_multiselect")
    selected_timezones_col2 = col2.multiselect("Select Timezones (Col 2):", pytz.all_timezones, key="col2_multiselect")
    selected_timezones_col3 = col3.multiselect("Select Timezones (Col 3):", pytz.all_timezones, key="col3_multiselect")
    selected_timezones_col4 = col4.multiselect("Select Timezones (Col 4):", pytz.all_timezones, key="col4_multiselect")
    


    
    # Combine selected time zones from all columns
    selected_timezones = (
        selected_timezones_col1 + selected_timezones_col2 +
        selected_timezones_col3 + selected_timezones_col4
    )
    
    if not selected_timezones:
        st.warning("Please select at least one timezone.")
        return

    

    # Create placeholders for live time updates for each column
    time_placeholders_col1 = [col1.empty() for _ in selected_timezones_col1]
    time_placeholders_col2 = [col2.empty() for _ in selected_timezones_col2]
    time_placeholders_col3 = [col3.empty() for _ in selected_timezones_col3]
    time_placeholders_col4 = [col4.empty() for _ in selected_timezones_col4]

    while True:
        for idx, timezone in enumerate(selected_timezones):
            current_time = get_time_in_timezone(timezone)
            
            # Update the time placeholder based on the column
            if timezone in selected_timezones_col1:
                time_placeholders_col1[selected_timezones_col1.index(timezone)].write(f"<div class='timezone-column'><strong>{timezone}:</strong> {current_time}</div>", unsafe_allow_html=True)
            elif timezone in selected_timezones_col2:
                time_placeholders_col2[selected_timezones_col2.index(timezone)].write(f"<div class='timezone-column'><strong>{timezone}:</strong> {current_time}</div>", unsafe_allow_html=True)
            elif timezone in selected_timezones_col3:
                time_placeholders_col3[selected_timezones_col3.index(timezone)].write(f"<div class='timezone-column'><strong>{timezone}:</strong> {current_time}</div>", unsafe_allow_html=True)
            elif timezone in selected_timezones_col4:
                time_placeholders_col4[selected_timezones_col4.index(timezone)].write(f"<div class='timezone-column'><strong>{timezone}:</strong> {current_time}</div>", unsafe_allow_html=True)

        # Update every second
        time.sleep(1)

if __name__ == "__main__":
    page_config()
    world_clock()
    
