# RealEstate-App
# Machine Learning Project 

This project is a Streamlit application for real estate price prediction, analysis, and features an interactive AI property assistant chatbot.

## Prerequisites

- Python 3.8+
- pip

## Installation

1.  **Dependencies**:
    ```bash
    pip install streamlit pandas numpy scikit-learn
    ```

## Running the Application

To start the application, run the following command in your terminal from the project directory:

```bash
streamlit run main.py
```

If the `streamlit` command is not found, use:

```bash
python -m streamlit run main.py
```

This will launch the application in your default web browser at `http://localhost:8501`.

## Application Structure

- `main.py`: The main entry point.
- `Pages/`: Contains the application pages.
- `chatbot.py`: Interactive AI property assistant.
- `df.pkl`, `pipeline.pkl`: Serialized data and model files.
