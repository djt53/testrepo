import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('/source.csv')

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

            # Company Name centered and bold
            st.markdown(f"<h2 style='text-align: center;'><b>{company_data['company_name']}</b></h2>", unsafe_allow_html=True)

            # Display additional information with non-clickable thumbs up and thumbs down buttons
            info_fields = ["location", "industry", "last_raise"]
            for field in info_fields:
                st.write(f"{field.capitalize()}: {company_data[field]}")
                col1, col2 = st.columns(2)
                with col1:
                    st.button("👍", key=f"thumbs_up_{field}", disabled=True)
                with col2:
                    st.button("👎", key=f"thumbs_down_{field}", disabled=True)

            # Save and Pass buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save", key="save_button"):
                    st.session_state.page += 1

            with col2:
                if st.button("Pass", key="pass_button"):
                    st.session_state.page += 1
        else:
            st.write("Nice. That's it for today. Check back tomorrow for some fresh deals.")

if __name__ == "__main__":
    main()
