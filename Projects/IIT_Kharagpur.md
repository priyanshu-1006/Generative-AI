ML Hackathon: The Predictive Modeling
Optimization Challenge
1. Introduction and Background
The modern chemical industry relies heavily on complex computational fluid dynamics and
boundary value problem (BVP) simulations to design and operate chemical reactors.
However, these rigorous physics-based simulations are computationally expensive and too
slow for real-time plant optimization.
At modern continuous flow facilities, process engineers oversee highly sensitive reaction
networks. They constantly face a bottleneck: predicting reactor behavior quickly when
operating setpoints change, without having to wait for heavy differential equations to solve.
Your task is to bridge the gap between chemical engineering and computer science by
building a Predictive Model (a data-driven machine learning surrogate) that can instantly
predict a reactor's performance based on historical plant data.
2. The Chemical Process
The dataset is derived from a non-isothermal, continuous flow reactor operating in a realworld industrial setting. The reactor operates with the following series-parallel reaction
network:
1. 1. Desired Reaction: A ----> B (rate constant: k1)
2. 2. Side Reaction: B ----> C (rate constant: k2)
The Challenge: The reactor involves competing reactions that are highly sensitive to
operating conditions. The kinetic and thermodynamic behaviors of this system create
complex, non-linear trade-offs. Your predictive model must independently learn these
hidden relationships—balancing flow rates, concentrations, and thermal profiles—to
accurately predict the final yield of the desired product (B).
3. The Objective
You are provided with historical data from the plant. Your objective is to train a machine
learning model that can accurately predict the Overall Yield of Product B given a new set of
operating conditions.
• Phase 1 (Model Training): Use the provided train_dataset.csv to build and validate your
model locally.
• Phase 2 (Prediction): Process the unseen operating conditions in test_dataset.csv and
generate your predicted yield for each of the test cases.
4. Dataset Description
You will be provided with two files:
- train_dataset.csv (150 rows): Contains the input features and the target variable.
Link: https://drive.google.com/file/d/15lmh-VS6jx0UgE11Rq_xsoggopuo3RQa/view?usp=sharing
- test_dataset.csv (50 rows): Contains only the input features.
Link: https://drive.google.com/file/d/1J1jFgaMVUT6CWz_FWEMboU9w7R9Hdono/view?usp=sharing
Features (Input Variables)
• flow_rate_L_min: Volumetric flow rate of the reactant mixture (L/min).
• concentration_mol_L: Inlet concentration of Reactant A (CA0 in mol/L).
• inlet_temperature_K: Temperature of the feed entering the reactor (K).
• length_m: The specific length of the reactor (m).
• jacket_temperature_K: The temperature of the external heating jacket (K).
Target (Output Variable)
• overall_yield: The final yield percentage of Product B at the reactor exit.
5. Submission Guidelines
Final submissions must include the predictions in the file format specified below via the
Unstop platform by the end hackathon period.
• The file must be a single .csv named [TeamName].csv containing exactly 50 rows
(matching the order of test_dataset.csv).
• It must contain exactly one column with the header overall_yield.
• Predictions must be continuous numerical values (floats) rounded to at least 3 decimal
places.
• Crucial Rule: Only one final submission is allowed per team. You must thoroughly
evaluate and cross-validate your model locally before making your final upload.
• Finalists Requirement: Shortlisted teams will also be required to submit their fully
documented Jupyter Notebook (.ipynb) files containing their complete workflow prior
to the final presentation.
6. Evaluation Criteria
This competition evaluates both predictive accuracy and engineering intuition. Bruteforcing mathematical algorithms without understanding the underlying chemical system
will not win this hackathon.
Phase 1: Quantitative Shortlisting (RMSE)
All 50 test rows will be evaluated blindly against a hidden master solution containing the
true physics outputs. The primary evaluation metric is Root Mean Squared Error (RMSE).
RMSE = √ [ (1/n) * Σ (yᵢ - ŷᵢ)² ]
Based strictly on this score, the Top 6 teams will be shortlisted for the final phase.
Phase 2: Final Pitch & System Understanding
The Top 5 shortlisted teams will be invited to campus to deliver their final pitch to the
judging panel. You must be prepared to defend your model and demonstrate a deep
understanding of the reactor system, proving your results are grounded in physical reality.
Judges will evaluate the innovation, robustness, and scalability of your model, along with
your overall pitch, based on:
• Process Insight: Your ability to explain the physical and thermodynamic trade-offs
happening inside the reactor.
• Innovation & Feature Engineering: How creatively and accurately you translated
chemical engineering principles into mathematical features for your model.
• Robustness & Scalability: How your model handles the realities of raw industrial data,
your strategies to prevent overfitting on a strictly limited dataset, and how effectively
the model could scale to real-time plant operations.
The final hackathon winners will be decided by the judges based on a holistic combination
of your Phase 1 predictive accuracy and your Phase 2 pitch.