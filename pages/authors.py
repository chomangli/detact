
import streamlit as st
import os

AUTHORS_DIR = "authors"

st.title("Authors")

a1,a2,a3 = st.columns(3)

with a1:
    st.image(os.path.join(AUTHORS_DIR,"Chomangli1.jpg"),width=300)
    st.markdown("**Chomangli T Sangtam**")
    st.write("B.Tech Student")
    st.write("National Institute of Technology Nagaland")

with a2:
    st.image(os.path.join(AUTHORS_DIR,"maloy1.jpg"),width=300)
    st.markdown("**Mr. Maloy Kumar Dey**")
    st.write("PhD Scholar")
    st.write("Department of Computer Science and Engineering")
    st.write("National Institute of Technology Nagaland")

with a3:
    st.image(os.path.join(AUTHORS_DIR,"dushman1.jpg"),width=300)
    st.markdown("**Dr. Dushmanta Kumar Das**")
    st.write("Associate Professor")
    st.write("Department of Electrical and Electronics Engineering")
    st.write("National Institute of Technology Nagaland")
