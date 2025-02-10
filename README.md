# AI-Agent-Anomaly-Detector
This script simulates and detects anomalous actions performed by a system agent. It utilizes machine learning with the Isolation Forest algorithm to identify actions that deviate from normal behavior, such as suspicious API calls or unusual file writes. The script is primarily focused on helping security and monitoring teams identify potentially malicious behavior by an agent based on logged actions.

## Features

- Simulates agent actions (e.g., web searches, API calls, file writes).
- Detects anomalies based on the action log using the Isolation Forest algorithm.
- Flags suspicious actions such as repeated API calls to "/admin" endpoints.
- Provides an easy-to-understand output of the detected anomalies.

## Requirements

The following libraries are required to run the script:

- `numpy`
- `scikit-learn`

You can install the necessary libraries using pip:
pip install numpy scikit-learn

## How It Works
Simulated Agent Actions: The script generates a series of agent actions such as web searches, API calls, and file writes.
Feature Engineering: It converts these actions into numerical features, such as the type of action and whether an endpoint is suspicious (e.g., "/admin").
Anomaly Detection: It uses the Isolation Forest machine learning model to detect anomalies in the generated action log.
Output: Anomalies (suspicious actions) are printed out for review.

## Functions
simulate_agent_actions(num_actions=20): Simulates a list of agent actions with a timestamp. The number of actions is customizable.
prepare_features(log): Prepares a numerical feature set from the simulated agent actions, converting action types and checking for suspicious endpoints.
detect_anomalies(log): Applies the Isolation Forest algorithm to the prepared feature set to detect anomalous actions.
main(): Runs the full workflow—simulates agent actions, detects anomalies, and outputs the results.

## Customization
Simulated Actions: You can modify the ACTIONS list to include different types of actions and endpoints.
Anomaly Detection: You can adjust the contamination parameter of the Isolation Forest model to change the sensitivity of anomaly detection.
Number of Actions: You can change the number of simulated actions by passing a value to the simulate_agent_actions() function when calling it.
