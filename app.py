import pytz
import streamlit as st
from zoneinfo import ZoneInfo
import datetime

# Select four time zones
time_zones = st.multiselect('Select Time Zones', pytz.all_timezones, default=['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney'])

# Display clocks in four columns
col1, col2, col3, col4 = st.columns(4)

for tz in time_zones:
    current_time = datetime.datetime.now(ZoneInfo(tz))
    col1.write(tz)
    col2.write(current_time.strftime('%H:%M:%S'))
    col3.write(current_time.strftime('%Y-%m-%d'))
    col4.write(current_time.strftime('%Z'))
