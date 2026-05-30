import streamlit as st
st.write("Hello, Streamlit!")

st.title("My First Streamlit App")
st.header("Welcome to Streamlit")
st.subheader("This is a subheader")
st.text("This is some sample text to demonstrate Streamlit's text display capabilities.")
st.markdown("**This is bold text using Markdown.**")
st.markdown("*This is italic text using Markdown.*")
st.markdown("Here is a list of features:\n- Easy to use\n- Fast development\n- Interactive apps")
st.markdown("[Click here to visit Streamlit's website](https://streamlit.io)")

## Buttons, Checkboxes, and Radio Buttons
if st.button("Click Me"):
    st.write("Button clicked!")
if st.checkbox("Check me out"):
    st.write("Checkbox is checked!")
options = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {options}")    
st.slider("Select a value", 0, 100, 50)
st.selectbox("Choose a number", [1, 2, 3, 4, 5]) 
st.multiselect("Select multiple options", ["Option A", "Option B", "Option C"])
st.date_input("Select a date")  

uploaded_file=st.file_uploader("Upload a file", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File type: {uploaded_file.type}")
    st.write(f"File size: {uploaded_file.size} bytes")
    # You can also read the file content if needed
    # For example, if it's a CSV file, you can use pandas to read it

    if uploaded_file.type == "text/csv":
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)

