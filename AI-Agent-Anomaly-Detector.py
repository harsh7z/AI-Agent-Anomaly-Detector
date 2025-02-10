# File: groq_agent_anomaly_detector.py
import os
import random
import json
from datetime import datetime
from sklearn.ensemble import IsolationForest
import numpy as np


# Simulate agent actions
ACTIONS = [
    {"type": "web_search", "query": "weather", "timestamp": None},
    {"type": "api_call", "endpoint": "/public", "timestamp": None},
    {"type": "web_search", "query": "weather", "timestamp": None},
    {"type": "file_write", "filename": "log.txt", "timestamp": None},
    {"type": "api_call", "endpoint": "/admin", "timestamp": None},  # Anomaly
    {"type": "file_write", "filename": "log.txt", "timestamp": None},
    {"type": "api_call", "endpoint": "/admin", "timestamp": None},  
    {"type": "web_search", "query": "weather", "timestamp": None},
    {"type": "api_call", "endpoint": "/admin", "timestamp": None},  # Anomaly
    {"type": "api_call", "endpoint": "/admin", "timestamp": None},  # Anomaly
]

# Generate mock activity log
def simulate_agent_actions(num_actions=20):
    log = []
    for _ in range(num_actions):
        action = random.choice(ACTIONS).copy()
        action["timestamp"] = datetime.now().isoformat()
        log.append(action)
    return log

# Feature engineering for ML model
def prepare_features(log):
    # Convert action types to numerical values
    type_map = {"web_search": 0, "api_call": 1, "file_write": 2}
    features = []
    for entry in log:
        features.append([
            type_map[entry["type"]],
            1 if "/admin" in entry.get("endpoint", "") else 0  # Suspicious endpoint
        ])
    return np.array(features)

# Detect anomalies with Isolation Forest
def detect_anomalies(log):
    model = IsolationForest(contamination=0.1)
    features = prepare_features(log)
    model.fit(features)
    preds = model.predict(features)
    return [log[i] for i in range(len(log)) if preds[i] == -1]

# Main workflow
def main():
    activity_log = simulate_agent_actions()
    anomalies = detect_anomalies(activity_log)
    
    print("Detected Anomalous Actions:")
    for action in anomalies:
        print(f"- {action['type'].upper()}: {action.get('endpoint', action.get('filename', ''))}")

if __name__ == "__main__":
    main()
