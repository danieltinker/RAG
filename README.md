# RAG X Python 3.11 Project
This project implements a Retrieval Augmented Generation (RAG) system using Python 3.11 currently supporting splitting of cpp, c files only. It integrates retrieval-based methods with generative models to enhance tasks such as question answering, summarization, and more.

# Prerequisites
- **Python:** Version 3.11 is required.
- **pip:** Ensure you have the latest version of pip installed.
- **Virtual Environment (Optional but Recommended):** To keep dependencies isolated.

# Setup And Execution
1. Create a Virtual Environment:
    [Linux]
        -   python3 -m venv env
        -   source env/bin/activate
    [Windows]
        -   python -m venv env
        -   env\Scripts\activate  

2. Install Dependencies:
        -   pip install -r requirements.txt

3. Run the Project: you can run the project in two interfaces:
    **GUI:**        run: python3 streamlit_main.py
    **Terminal:**   run: python3 main.py

# Disclaimers
there is NO caching layer, if you stop the program your embbedings will be recalculated from scratch.
