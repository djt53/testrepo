import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('/mnt/data/source.csv')

# Define main function
def main():
    st.set_page_config(page_title="VC Tinder", layout="centered")
    st.markdown(
        """
        <style>
        .main {
            background-color: black;
            color: white;
        }
        .stButton>button {
            color: white;
            border-radius: 5px;
            padding: 10px;
            margin: 5px;
        }
        .green-button .stButton>button {
            background-color: #28a745;
        }
        .red-button .stButton>button {
            background-color: #dc3545;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )
    
    if "page" not in st.session_state:
        st.session_state.page = 0

    # Landing page
    if st.session_state.page == 0:
        st.title("VC Tinder")
        if st.button("Start", key="start_button"):
            st.session_state.page += 1

    # Display cards with company info
    else:
        if st.session_state.page <= len(df):
            company_data = df.iloc[st.session_state.page - 1]

            st.header(company_data['company_name'])
            st.write(f"Location: {company_data['location']}")
            st.write(f"Industry: {company_data['industry']}")
            st.write(f"Funding: {company_data['funding']}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Save", key="save_button", help="Save this option"):
                    st.session_state.page += 1

            with col2:
                if st.button("Pass", key="pass_button", help="Pass this option"):
                    st.session_state.page += 1
        else:
            st.write("You've reached the end of the list.")

if __name__ == "__main__":
    main()
