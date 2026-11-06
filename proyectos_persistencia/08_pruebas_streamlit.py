import streamlit as st
import time

st.success("Todo correcto")
msj_error = st.error("No ha ido bien")

time.sleep(3)
msj_error.empty()

st.toast("Mensaje flotante", duration = "long")