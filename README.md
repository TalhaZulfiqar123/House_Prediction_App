<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 40px;">

  <h1>🏠 House Price Prediction App</h1>

  <p>
    <strong>Description:</strong> A machine learning-powered web application built with Streamlit to predict house prices based on user inputs such as number of bedrooms, bathrooms, living area size, condition, and number of nearby schools.
  </p>

  <hr>

  <h2>🚀 Features</h2>
  <ul>
    <li>🎯 Accurate price prediction based on key house features</li>
    <li>🖥️ User-friendly UI with real-time predictions</li>
    <li>💾 Loads a trained model using <code>joblib</code></li>
    <li>📊 Displays prediction results dynamically</li>
  </ul>

  <hr>

  <h2>🧠 Model Info</h2>
  <p>The machine learning model is saved as <code>model.pkl</code> and expects the following inputs:</p>
  <ul>
    <li>Number of Bedrooms</li>
    <li>Number of Bathrooms</li>
    <li>Living Area (sqft)</li>
    <li>House Condition</li>
    <li>Number of Schools Nearby</li>
  </ul>

  <hr>

  <h2>🛠️ How to Run</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor</code></pre>
    </li>
    <li>Install the required libraries:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the Streamlit app:
      <pre><code>streamlit run app.py</code></pre>
    </li>
  </ol>
  <p><strong>Note:</strong> Make sure <code>model.pkl</code> is present in the root directory.</p>

  <hr>

  <h2>📁 File Structure</h2>
  <pre>
house-price-predictor/
│
├── app.py              # Main Streamlit application
├── model.pkl           # Trained ML model
├── requirements.txt    # Required libraries
└── README.html         # Project documentation (this file)
  </pre>

  <hr>

  <h2>📈 Example Prediction</h2>
  <ul>
    <li><strong>Input:</strong>
      <ul>
        <li>Bedrooms: 3</li>
        <li>Bathrooms: 2</li>
        <li>Living Area: 1800 sqft</li>
        <li>Condition: 4</li>
        <li>Nearby Schools: 2</li>
      </ul>
    </li>
    <li><strong>Output:</strong> Price prediction is <strong>$450,000.00</strong></li>
  </ul>

  <hr>

  <h2>📋 Requirements</h2>
  <ul>
    <li>streamlit</li>
    <li>joblib</li>
    <li>numpy</li>
  </ul>
  <p>Add these to <code>requirements.txt</code>:</p>
  <pre><code>streamlit
joblib
numpy</code></pre>

  <hr>

  <h2>🤝 Contributing</h2>
  <p>Feel free to fork this repo, suggest improvements, or add new features via pull requests.</p>

  <hr>

  <h2>👨‍💻 Author</h2>
  <p><strong>Your Name</strong><br>
    <a href="https://github.com/TalhaZulfiqar123" target="_blank">GitHub Profile</a>
  </p>

</body>
</html>
