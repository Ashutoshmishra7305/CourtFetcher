import streamlit as st
import sqlite3
import os

st.title("Court Data Fetcher")

# --- Step 1: User Inputs ---
case_type = st.text_input("Case Type")
case_number = st.text_input("Case Number")
year = st.text_input("Year")

# --- Step 2: Connect / Create Database ---
conn = sqlite3.connect('court_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS cases
             (case_type TEXT, case_number TEXT, year TEXT, parties TEXT, status TEXT, filing_date TEXT, next_hearing TEXT, pdf_link TEXT)''')

# --- Step 3: Fetch Button ---
if st.button("Fetch Case Details"):
    if case_type and case_number and year:
        # --- Dummy scraper data ---
        parties = "Party A vs Party B"
        status = "Pending"
        filing_date = "2025-01-01"
        next_hearing = "2025-02-01"
        pdf_link = "sample.pdf"

        # --- Save to Database ---
        c.execute("INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (case_type, case_number, year, parties, status, filing_date, next_hearing, pdf_link))
        conn.commit()

        # --- Display Data ---
        st.write("**Case Details:**")
        st.write(f"Parties: {parties}")
        st.write(f"Status: {status}")
        st.write(f"Filing Date: {filing_date}")
        st.write(f"Next Hearing: {next_hearing}")

        # --- PDF Download ---
        if not os.path.exists(pdf_link):
            with open(pdf_link, "w") as f:
                f.write("This is a dummy judgment PDF.")
        st.download_button("Download Judgment", data=open(pdf_link, "rb"), file_name="judgment.pdf")
    else:
        st.warning("Please fill all fields!")

conn.close()
