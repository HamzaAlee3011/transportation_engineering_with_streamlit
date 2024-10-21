import streamlit as st

col0a, col0b, col0c = st.columns([0.6, 1, 0.6])
with col0b:
    st.title("About Application")
    st.write('\n')

st.write("### :blue-background[**:material/code_blocks: Developer**]")
st.write("""

***Ameer Hamza Ali***  
***Batch 2022***  
***Department of Civil Engineering***  
***NED University of Engineering & Technology, Karachi, Pakistan***  

Check out my profile:  
https://about-hamza-ali.streamlit.app/  
  
Let's connect!:  
https://www.linkedin.com/in/hamza-ali-35449a2aa/
""")

# st.write('\n')
# st.write("### :blue-background[**:material/update: Version**]")
# st.write(":grey-background[**Version 1.0**] - Initial Release (01/09/2024)")


st.write('\n')
st.write("### :blue-background[**Purpose**]")
st.write("""
This application is designed to assist engineers in the field of transportation engineering by providing a reliable tool for solving design equations and designing rigid & flexible pavements. The app utilizes the AASHTO pavement design equations to calculate the required pavement thickness (D) or Structural Number (SN) based on various input parameters related to equations. By offering a user-friendly interface and accurate computational methods, the app helps streamline the pavement design process.
""")


st.write('\n')
st.write("### :blue-background[**:material/view_module: Modules Used**]")
st.write("""
- **:grey-background[Streamlit]:** For creating the interactive web application interface. [Streamlit Documentation](https://docs.streamlit.io/)
- **:grey-background[SymPy]:** For symbolic mathematics, solving equations, and implementing numerical methods. [SymPy Documentation](https://docs.sympy.org/)
""")

st.write('\n')
st.write("###  :blue-background[**:material/call: Contact**]")
st.write("""
For further assistance, feedback, or to report any bugs, please contact me at ameer.hamza.alee3011@gmail.com.
""")

