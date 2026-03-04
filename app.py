import streamlit as st
import pandas as pd

# Pagina instellingen
st.set_page_config(page_title="Uren Teller", page_icon="⏱️")

# Data initialiseren in de 'sessie' (zodat het niet verdwijnt bij verversen)
if 'totaal' not in st.session_state:
    st.session_state.totaal = 0.0
if 'geschiedenis' not in st.session_state:
    st.session_state.geschiedenis = []

st.title("⏱️ Mijn Uren Teller")

# --- INPUT SECTIE ---
st.subheader("Uren toevoegen")
nieuwe_uren = st.number_input("Hoeveel uur gewerkt?", min_value=0.0, step=0.25, format="%.2f")

if st.button("➕ Voeg uren toe", use_container_width=True):
    if nieuwe_uren > 0:
        st.session_state.totaal += nieuwe_uren
        st.success(f"{nieuwe_uren} uur toegevoegd!")

# --- DISPLAY SECTIE ---
st.divider()
st.metric(label="Huidige Sessie Totaal", value=f"{st.session_state.totaal:.2f} uur")

col1, col2 = st.columns(2)

with col1:
    if st.button("💾 Reset naar Lijst", type="primary", use_container_width=True):
        if st.session_state.totaal > 0:
            st.session_state.geschiedenis.insert(0, st.session_state.totaal)
            st.session_state.totaal = 0.0
            st.rerun()

with col2:
    if st.button("🗑️ Alles Wissen", use_container_width=True):
        st.session_state.totaal = 0.0
        st.session_state.geschiedenis = []
        st.rerun()

# --- GESCHIEDENIS ---
st.subheader("Vorige Sessies")
if st.session_state.geschiedenis:
    for i, uren in enumerate(st.session_state.geschiedenis):
        cols = st.columns([3, 1])
        cols[0].write(f"Sessie {len(st.session_state.geschiedenis)-i}: **{uren:.2f} uur**")
        if cols[1].button("❌", key=f"del_{i}"):
            st.session_state.geschiedenis.pop(i)
            st.rerun()
else:
    st.info("Nog geen opgeslagen sessies.")