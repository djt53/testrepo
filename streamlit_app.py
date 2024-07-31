import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('source.csv')

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
        .stButton.green-button>button {
            background-color: #28a745;
        }
        .stButton.red-button>button {
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
                col1, col2, col3 = st.columns([3, 1, 1])
                col1.write(f"{field.capitalize()}: {company_data[field]}")
                col2.button("👍", key=f"thumbs_up_{field}", disabled=True)
                col3.button("👎", key=f"thumbs_down_{field}", disabled=True)

            # Save and Pass buttons with customized colors
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save", key="save_button", args=(st.session_state.page + 1,)):
                    st.session_state.page += 1

            with col2:
                if st.button("Pass", key="pass_button", args=(st.session_state.page + 1,)):
                    st.session_state.page += 1

            # Custom styling for buttons
            col1.markdown(
                """
                <style>
                div.stButton > button:first-child {
                    background-color: #28a745;
                    color: white;
                }
                </style>
                """, 
                unsafe_allow_html=True
            )

            col2.markdown(
                """
                <style>
                div.stButton > button:first-child {
                    background-color: #dc3545;
                    color: white;
                }
                </style>
                """, 
                unsafe_allow_html=True
            )

        else:
            st.write("Nice. That's it for today.")

if __name__ == "__main__":
    main()
