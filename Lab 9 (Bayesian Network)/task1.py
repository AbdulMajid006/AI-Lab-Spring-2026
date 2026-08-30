from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Education', 'Interview'),
    ('Experience', 'Interview'),
    ('Interview', 'HiringDecision')
])

cpd_education = TabularCPD(
    variable='Education',
    variable_card=2,
    values=[[0.65], [0.35]]
)

cpd_experience = TabularCPD(
    variable='Experience',
    variable_card=2,
    values=[[0.5], [0.5]]
)

cpd_interview = TabularCPD(
    variable='Interview',
    variable_card=2,
    values=[
        [0.9, 0.7, 0.6, 0.3],
        [0.1, 0.3, 0.4, 0.7]
    ],
    evidence=['Education', 'Experience'],
    evidence_card=[2, 2]
)

cpd_hiring = TabularCPD(
    variable='HiringDecision',
    variable_card=2,
    values=[
        [0.85, 0.2],
        [0.15, 0.8]
    ],
    evidence=['Interview'],
    evidence_card=[2]
)

model.add_cpds(cpd_education, cpd_experience, cpd_interview, cpd_hiring)

assert model.check_model()

inference = VariableElimination(model)

result = inference.query(
    variables=['HiringDecision'],
    evidence={'Interview': 0}
)

print(result)