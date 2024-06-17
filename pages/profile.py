import streamlit as st
import streamlit.components.v1 as components

st.header("Your Profile", divider="grey")
col1, col2 = st.columns([1 ,1])


with col1:
    st.image("https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=1780&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=330)
with col2:
    st.subheader("Jackson Scott")
    st.markdown(f"###### 📍 New York, New York")
    st.markdown(f"###### ⭐ 47 rewards unlocked")
    st.markdown(f"###### Bio: I'm a 26 year old learning how to vote! I'm excited to meet new friends, use the app, and get involved in the civics process!")    
    st.markdown(f"###### Badges:")
    
    with st.container(height=None, border = None):
        c1, c2, c3 = st.columns(3)
        c4, c5, c6 = st.columns(3)
        with c1:
            st.button("🦅")
        with c2:
            c2 =st.button("👗")
        with c3:
            c3 =st.button("🌮")
        with c4:
            c4= st.button("🐟")
        with c5:
            c5 = st.button("🐧")
        with c6:
            c6 = st.button("⭐")
        



