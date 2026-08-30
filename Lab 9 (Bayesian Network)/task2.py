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