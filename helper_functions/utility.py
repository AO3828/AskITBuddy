# filename: utility.py
import streamlit as st  

  
# """  
# This file contains the common components used in the Streamlit App.  
# This includes the sidebar, the title, the footer, and the password check.  
# """

# File deletion function
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        st.success(f"File '{file_path}' has been deleted.")
    else:
        st.error(f"File '{file_path}' does not exist.")
