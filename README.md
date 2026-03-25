<!-- Animated Header --><p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00F7FF&center=true&vCenter=true&lines=EpiGuard+-+Agentic+AI+Epidemic+Prediction;CodeCure+AI+Hackathon+Prototype;Hotspot+Detection+%7C+Risk+Analysis+%7C+Forecasting;Built+for+SPIRIT'26+IIT+BHU" />
</p>---

🤖 EpiGuard: Agentic AI Epidemic Spread Prediction System

🧪 CodeCure – AI Hackathon Prototype | IIT (BHU) SPIRIT'26

EpiGuard is a multi-agent AI-powered epidemic forecasting system designed to predict outbreak trends, detect high-risk regions, and generate preventive policy suggestions using real-world epidemiological datasets.

This prototype demonstrates how Agentic AI + Machine Learning + Public Health Data can assist early outbreak monitoring and decision support systems.

---

🚀 Key Features

🧠 Multi-Agent AI Pipeline
📊 Epidemic Growth Trend Detection
📉 Future Case Prediction using ML
🔥 Hotspot Risk Identification
📍 Country-wise Risk Analysis
📑 AI-Based Risk Explanation
🏥 Policy Recommendation Engine
🌐 Interactive Streamlit Dashboard

---

🧩 Agentic AI Architecture

The system is built using multiple intelligent agents working together:

User Input
   ↓
Data Agent
   ↓
Trend Analysis Agent
   ↓
Prediction Agent
   ↓
Hotspot Detection Agent
   ↓
Explanation Agent
   ↓
Policy Recommendation Agent
   ↓
Interactive Dashboard Output

Each agent performs a specialized epidemiological reasoning task.

---

📂 Project Structure

epiguard-agentic-ai/
│
├── agents/
│   ├── data_agent.py
│   ├── trend_agent.py
│   ├── prediction_agent.py
│   ├── hotspot_agent.py
│   ├── explanation_agent.py
│   └── policy_agent.py
│
├── models/
│   ├── train_model.py
│   └── saved_models/
│
├── workflows/
│   └── agent_pipeline.py
│
├── utils/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── visualization.py
│
├── dashboard/
│   └── streamlit_ui.py
│
├── data/
├── outputs/
│
├── config.py
├── app.py
├── requirements.txt
└── README.md

---

📊 Dataset Used

Primary Dataset:

Johns Hopkins COVID-19 Global Time Series Dataset

Includes:

- Daily confirmed cases
- Death statistics
- Regional outbreak patterns
- Historical epidemic spread timeline

Used for forecasting outbreak growth trends.

---

⚙️ Tech Stack

Python
Pandas
Scikit-learn
Streamlit
Matplotlib
Joblib

Agentic AI Pipeline (Custom Multi-Agent Workflow)

---

🧠 Agents in the System

1️⃣ Data Agent

Loads epidemiological dataset
Handles missing values
Filters country-specific outbreak records

---

2️⃣ Trend Analysis Agent

Detects infection growth trends:

Example output:

Trend: Increasing

---

3️⃣ Prediction Agent

Forecasts upcoming case counts using trained ML model.

Example:

Next-day predicted cases generated successfully

---

4️⃣ Hotspot Detection Agent

Classifies outbreak risk levels:

Low Risk
Medium Risk
High Risk

---

5️⃣ Explanation Agent

Explains outbreak behavior in natural language:

Example:

Cases increasing due to rising infection growth rate in recent days.

---

6️⃣ Policy Recommendation Agent

Suggests preventive public-health actions:

Example:

Increase testing
Limit public mobility
Accelerate vaccination coverage

---

📈 Example Output

Input:

Country: India

Output:

Trend: Increasing
Risk Level: High
Forecast: Next-day outbreak prediction generated
Policy Suggestions:
- Increase testing
- Restrict mobility
- Improve vaccination coverage

---

🧪 How to Run the Project

Step 1: Install Dependencies

pip install -r requirements.txt

---

Step 2: Train Prediction Model

python models/train_model.py

---

Step 3: Launch Dashboard

streamlit run app.py

---

🖥️ Dashboard Preview

(Add screenshots here before submission)

Example:

/screenshots/dashboard.png

---

🏆 Hackathon Objective Alignment

This prototype satisfies CodeCure AI Hackathon Track-C requirements:

✔ Epidemic spread prediction
✔ Growth trend detection
✔ Risk hotspot identification
✔ AI-based explanation system
✔ Preventive policy suggestions
✔ Interactive dashboard interface
✔ Agentic AI workflow implementation

---

🌍 Real-World Applications

Public health monitoring systems
Government outbreak dashboards
Hospital preparedness planning
Early epidemic warning systems
Smart healthcare analytics platforms

---

🔮 Future Improvements

Add LSTM time-series forecasting
Integrate vaccination datasets
Include mobility trend analysis
Deploy LangGraph agent orchestration
Generate automated PDF outbreak reports
Create geo-spatial hotspot heatmaps

---

👨‍💻 Built For

CodeCure – AI Hackathon
SPIRIT'26 | IIT (BHU) Varanasi

This prototype demonstrates how Agentic AI can transform epidemic forecasting into an intelligent decision-support healthcare system.

---

<p align="center">
⭐ If you like this project, consider starring the repository ⭐
</p>
