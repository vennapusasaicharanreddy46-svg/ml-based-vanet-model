# 🚗 ML-Based VANET Model Using SUMO

## 📌 Project Overview

This project implements a Machine Learning-based Vehicular Ad-Hoc Network (VANET) model using SUMO (Simulation of Urban Mobility) and Python.

The objective is to simulate vehicle communication scenarios and apply machine learning techniques to analyze and improve important network performance metrics such as delay, packet loss, throughput, and congestion levels.

This project was developed as part of a Data Communication and Networks (DCN) academic project.

---

## 🎯 Objectives

- Simulate a VANET environment using SUMO
- Collect and analyze network performance metrics
- Implement a baseline routing approach
- Apply Machine Learning for optimization
- Compare baseline vs ML-based performance
- Visualize results using graphs

---

## 🛠️ Technologies Used

- Python 3
- SUMO (Simulation of Urban Mobility)
- TraCI Interface
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Git & GitHub
- Linux (Ubuntu)

---

## 📂 Project Structure

```
ml-based-vanet-model/
│
├── config/                # SUMO configuration files
├── net/                   # Network topology files (.net.xml)
├── routes/                # Route definition files (.rou.xml)
├── data/                  # Dataset files generated from simulation
├── ml/                    # Machine learning models & scripts
├── results/               # Output results and graphs
│
├── main.py                # Main simulation controller
├── main_baseline.py       # Baseline routing implementation
├── main_ml.py             # ML-based routing implementation
├── generate_graphs.py     # Script to generate performance graphs
├── dataset.csv            # Processed dataset
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Install SUMO

Download and install SUMO from:

https://www.eclipse.org/sumo/

Verify installation:

```bash
sumo --version
```

---

### 2️⃣ Clone the Repository

```bash
git clone git@github.com:vennapusasaicharanreddy46-svg/ml-based-vanet-model.git
cd ml-based-vanet-model
```

---

### 3️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## ▶️ How to Run the Project

### 🔹 Run Baseline Model

```bash
python main_baseline.py
```

---

### 🔹 Run ML-Based Model

```bash
python main_ml.py
```

---

### 🔹 Generate Performance Graphs

```bash
python generate_graphs.py
```

Graphs will be saved inside the `results/` folder.

---

## 📊 Performance Metrics Evaluated

- End-to-End Delay
- Packet Delivery Ratio (PDR)
- Packet Loss Rate
- Throughput
- Network Congestion Level

---

## 🧠 Machine Learning Approach

The ML pipeline includes:

1. Data collection from SUMO simulation
2. Data preprocessing
   - Removing duplicates
   - Feature selection
   - Cleaning and formatting
3. Feature engineering
4. Model training
5. Performance comparison

Possible models used:
- Linear Regression
- Random Forest
- Supervised Learning techniques

The ML-based routing is compared against baseline routing to measure performance improvements.

---

## 📈 Results

The ML-based approach shows improvements in:

- Reduced average delay
- Improved packet delivery ratio
- Better congestion management
- Higher overall network efficiency

All results and comparisons are stored in:

```
results/
```

---

## 🔬 Dataset Information

The dataset is generated from simulated VANET scenarios and includes:

- Vehicle ID
- Speed
- Delay
- Packet Loss
- Throughput
- Timestamp

Data preprocessing steps:

- Duplicate removal
- Column filtering
- Sampling (if applied)
- Normalization
- Rounding for clean formatting

---

## 🎓 Academic Context

This project demonstrates the practical application of:

- Vehicular Ad-Hoc Networks (VANET)
- Network simulation using SUMO
- Machine Learning-based performance optimization
- Data analysis and visualization

It is designed for academic submission under Data Communication and Networks (DCN).

---

## 🔮 Future Enhancements

- Deep Learning-based routing
- Reinforcement Learning integration
- Real-time traffic API integration
- Larger scale network simulations
- Cloud-based deployment
- Live dashboard visualization

---

## 👨‍💻 Author

Venna Pusa Sai Charan Reddy

GitHub:
https://github.com/vennapusasaicharanreddy46-svg

---

## 📜 License

This project is developed for academic and research purposes.

