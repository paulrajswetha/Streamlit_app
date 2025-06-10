import streamlit as st
from streamlit_option_menu import option_menu

st.title("📝Vinsup Infotech")

# with st.sidebar:
#     st.header("Vinsup")

# st.write("haii hello") 
# st.write("# haii hello") #bold
# st.write("## haii hello") #normal 
# st.write("_haii hello_")  #Italic
# st.write("- haii hello")  #bulletin
# st.text_input("Enter your name:")
# st.button("submit")
with st.sidebar:
    data=option_menu(
        menu_title="Vinsup",
        options=["Home","About","Contact"],
        icons=["house","people","phone"],
    )

if data=="Home":
    st.header("Registration Form")
    col1,col2=st.columns(2)
    with col1:
        Name=st.text_input("Enter Your Name:")
        Email=st.text_input("Enter Your Email:")
    with col2:
        Phone= st.text_input("Enter Your Phone Number:")
        Password=st.text_input("Enter Your Password:",type="password")
    if  st.button("Submit"):
        st.write(Name,Email,Phone,Password)
        st.success("Data Inserted Successfully")
        st.balloons()
        #st.snow()
    st.metric(label="python",value=20,delta="20%")
    #st.metric(label="python",value=20,delta="-20%")
    st.number_input("Integer",min_value=0)
    st.radio(label=":rainbow[Select ur option]",options=["male","female"],index=None)
    st.selectbox(label="City",options=["Madurai","America","Chennai"])
    st.multiselect(label="City",options=["Madurai","America","Chennai"])
    st.slider("Numbers",0,100)
    st.file_uploader("Upload")
    

elif data=="About":
    st.header("About Page")
elif data=="Contact":
    st.header("Contact Page")