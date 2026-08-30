# Task#1:
# Bayesian Network for Job Hiring:
# You are modeling whether a candidate gets hired.
# Nodes:
# • Education (E) — {High, Low}
# • Experience (X) — {Experienced, Inexperienced}
# • Interview (I) — {Good, Bad}
# • HiringDecision (H) — {Hired, NotHired}
# Dependencies:
# • Education and Experience influence Interview performance
# • Interview influences HiringDecision
# Prior Probabilities:
# • P(Education = High) = 0.65, Low = 0.35
# • P(Experience = Experienced) = 0.5, Inexperienced = 0.5
# Tasks to do:
# • Draw the Bayesian Network structure
# • Define CPTs for:
#     o Interview | Education, Experience
#     o HiringDecision | Interview
# • Implement the network using Python (pgmpy or similar)


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
