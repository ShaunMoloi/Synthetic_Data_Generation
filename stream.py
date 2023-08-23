"""
    Python file example with the script to run ydata-synthetic streamlit app
"""
import nest_asyncio
nest_asyncio.apply()
from ydata_synthetic import streamlit_app

streamlit_app.run()