import streamlit as st
import pandas as pd

def main():
    # Title of the app
    st.title("Excel File Analyzer")

    # File uploader
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Load the uploaded Excel file
        xls = pd.ExcelFile(uploaded_file)
        df = pd.read_excel(xls)

        # Display the original dataframe
        st.subheader("Original DataFrame")
        st.write(df)

        # Transpose the dataframe
        df_transposed = df.T
        st.subheader("Transposed DataFrame")
        st.write(df_transposed)

        # Remove empty columns
        def remove_empty_columns(df):
            """
            Removes all columns that contain NaN in all their rows.
            """
            return df.dropna(axis=1, how="all")

        df_noNaN = remove_empty_columns(df_transposed)
        st.subheader("Cleaned DataFrame (Empty Columns Removed)")
        st.write(df_noNaN)

        # Add download button for the cleaned data
        st.download_button(
            label="Download cleaned data as CSV",
            data=df_noNaN.to_csv().encode("utf-8"),
            file_name="cleaned_data.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()
