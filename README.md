# customer-churn-predictor
# Customer Churn Predictor

A Streamlit app that predicts whether a customer is likely to churn based on their usage and account details. The app provides both single‑point and batch predictions by loading a trained model and preprocessing pipeline.

## Features

- Single‑point prediction: Enter customer details via sliders and inputs to get an instant churn prediction.
- Batch prediction: Upload a `.csv` file to predict churn for multiple customers at once.
- Simple UI: Built with Streamlit for easy interaction and deployment.
- Ready to deploy on Streamlit Community Cloud.

## Repository Structure
customer-churn-predictor/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── model/ # Trained model files
├── data/ # Dataset and processed files
└── README.md


## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/Chaitra804/customer-churn-predictor.git
   cd customer-churn-predictor
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open `http://localhost:8501` in your browser.

## Deployment on Streamlit Community Cloud

1. Make sure your files are pushed to GitHub:
   ```bash
   git add .
   git commit -m "Add app and requirements"
   git push origin main
   ```

2. Go to [Streamlit Community Cloud](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app** → **From GitHub repo** and select:
   - Repository: `Chaitra804/customer-churn-predictor`
   - Branch: `main`
   - Main file path: `app.py`
4. Click **Deploy**. Your app will be live at a URL like:
https://customer-churn-predictor-qzaqpwr4verq2lc4a3rypj.streamlit.app/

text

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.