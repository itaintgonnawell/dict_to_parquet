# a streamlit application to covert a dictionary string dump (print(dict_data)) to a parquet file and download it
import streamlit as st
import pandas as pd
from decimal import Decimal
import datetime

def dict_str_to_parquet(dict_str):
    try:
        # Convert the string representation of the dictionary to an actual dictionary
        dict_data = eval(dict_str)
        # Convert the dictionary to a pandas DataFrame
        df = pd.DataFrame([dict_data])
        # Save the DataFrame to a parquet file
        parquet_file = "output.parquet"
        df.to_parquet(parquet_file, index=False)
        return parquet_file
    except Exception as e:
        st.error(f"Error converting dictionary string to parquet: {e}")
        return None
def main():
    st.title("Dictionary String to Parquet Converter")
    st.write("Paste your dictionary string below and convert it to a Parquet file.")

    dict_str = st.text_area("Dictionary String", height=200)

    if st.button("Convert to Parquet"):
        if dict_str:
            parquet_file = dict_str_to_parquet(dict_str)
            if parquet_file:
                with open(parquet_file, "rb") as f:
                    st.download_button(
                        label="Download Parquet File",
                        data=f,
                        file_name="output.parquet",
                        mime="application/octet-stream"
                    )
        else:
            st.warning("Please enter a valid dictionary string.")
if __name__ == "__main__":
    main()
