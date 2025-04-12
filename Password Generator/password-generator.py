import streamlit as st
import re

st.set_page_config(page_title="Password Generator", page_icon="🔒")

st.title("🔒 Password Generator")
st.markdown("""
### welcome to the password generator app 👋
this app is designed to generate strong passwords for your accounts.
            we will give you suggestions to generate a **strong password** 🚀 """)

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long")

    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Password must contain lowercase and uppercase letters")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password must contain numbers")
        
    if re.search(r'[!@#$%^]', password):
        score += 1
    else:
        feedback.append("❌ Password must contain special characters (!@#$%^)")

    if score == 4:
        feedback.append("✅ Your password is strong")
    elif score == 3:
        feedback.append("🔒 Your password is medium. try to make it stronger")
    else:
        feedback.append("❌ Your password is weak. try to make it stronger 🎉")

    if feedback:
        st.markdown("## Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter a password")


        
        
        
        
        



