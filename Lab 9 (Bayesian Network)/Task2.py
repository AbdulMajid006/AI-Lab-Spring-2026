Task#2:
Bayesian Network for Car Fault Diagnosis:
You are diagnosing whether a car has an issue based on symptoms.
Nodes:
• Fault (F) — {EngineIssue, BatteryIssue}
• Symptoms:
    o CarWon’tStart (S) — {Yes, No}
    o DimLights (D) — {Yes, No}
    o StrangeNoise (N) — {Yes, No}

Network Structure:
• Fault → CarWon’tStart
• Fault → DimLights
• Fault → StrangeNoise
Prior Probabilities:
• P(EngineIssue) = 0.4
• P(BatteryIssue) = 0.6
Conditional Probabilities (example assumptions):
• P(CarWon’tStart = Yes | EngineIssue) = 0.85
• P(CarWon’tStart = Yes | BatteryIssue) = 0.7
• P(DimLights = Yes | EngineIssue) = 0.3
• P(DimLights = Yes | BatteryIssue) = 0.8
• P(StrangeNoise = Yes | EngineIssue) = 0.75
• P(StrangeNoise = Yes | BatteryIssue) = 0.2
Tasks to do:
1. Construct the Bayesian Network diagram
2. Define full CPTs for all nodes
3. Perform inference:


from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Fault', 'CarWontStart'),
    ('Fault', 'DimLights'),
    ('Fault', 'StrangeNoise')
])

cpd_fault = TabularCPD(
    variable='Fault',
    variable_card=2,
    values=[[0.4], [0.6]]
)

cpd_start = TabularCPD(
    variable='CarWontStart',
    variable_card=2,
    values=[
        [0.85, 0.7],
        [0.15, 0.3]
    ],
    evidence=['Fault'],
    evidence_card=[2]
)

cpd_dim = TabularCPD(
    variable='DimLights',
    variable_card=2,
    values=[
        [0.3, 0.8],
        [0.7, 0.2]
    ],
    evidence=['Fault'],
    evidence_card=[2]
)

cpd_noise = TabularCPD(
    variable='StrangeNoise',
    variable_card=2,
    values=[
        [0.75, 0.2],
        [0.25, 0.8]
    ],
    evidence=['Fault'],
    evidence_card=[2]
)

model.add_cpds(cpd_fault, cpd_start, cpd_dim, cpd_noise)

assert model.check_model()

inference = VariableElimination(model)

result = inference.query(
    variables=['Fault'],
    evidence={'CarWontStart': 0, 'DimLights': 0, 'StrangeNoise': 0}
)

print(result)
