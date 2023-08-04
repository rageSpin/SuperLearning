import streamlit as st 

st.header("Monte Carlo modeling of carrier transport in crystalline materials")

questions = [
    'Discuss the main approximations that we have to make to reach the BTE (classical particles, Newton’s laws, local band structure approximation, Stosszahlansatz and other assumptions concerning the scattering processes)',
    'Why is the Monte Carlo approach named “semi-classical”? Discuss the classical and the quantum ingredients in the Monte Carlo method',

]


options = st.selectbox("Select the question or topic", questions)

st.write('\n')
st.divider()

st.subheader(options)
with st.expander('See Answer'):
    st.write("BULA BULA")
    cols = st.columns(3)
    cols[0].button(":green[Correct]", key='correct', use_container_width=True , on_click=st.balloons)
    cols[1].button("To review", key='torev')
    cols[2].button(":red[Wrong]", key='wrong')

# only for multiselect
# for i, q in enumerate(options):
#     st.subheader(str(i)+'. '+q)