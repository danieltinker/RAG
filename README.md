# RAG X Python 3.11 Project
This project implements a Retrieval Augmented Generation (RAG) system using Python 3.11 currently supporting splitting of cpp, c files only. It integrates retrieval-based methods with generative models to enhance tasks such as question answering, summarization, and more.

# Goal
Retrieval-Augmented Generation (RAG) is designed to enhance the quality and factual accuracy of generated content by combining a language generation model with a retrieval mechanism.

# Prerequisites
- **Python:** Version 3.11 is required.
- **pip:** Ensure you have the latest version of pip installed.
- **LLVM with LIBCLANG:** If you haven’t already, download and install LLVM from the LLVM website.

- **OPENAI API KEY:** The program is operating via the authenticated OpenAI API.
- **C\C++ CODEBASE:** The program is proccessing only c\c++ files.

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

3. set up a .env file with the openAI API Key

4. Run the Project: you can run the project in two interfaces:
    **GUI:**        run: python3 streamlit_main.py
    **Terminal:**   run: python3 main.py

# Disclaimers
1. There is NO caching layer, if you stop the program your embbedings will be recalculated from scratch.
2. Cpp Methods are not supported.
