# Task#3:
# Bayesian Network for Online Shopping Behavior:
# You are modeling whether a user makes a purchase.
# Nodes:
# • AdExposure (A) — {Yes, No}
# • WebsiteExperience (W) — {Good, Poor}
# • ProductPrice (P) — {High, Low}
# • Purchase (C) — {Yes, No}
# Dependencies:
# • AdExposure influences WebsiteExperience
# • WebsiteExperience and ProductPrice influence Purchase
# Prior Probabilities:
# • P(AdExposure = Yes) = 0.6
# • P(WebsiteExperience = Good | AdExposure = Yes) = 0.8
# • P(WebsiteExperience = Good | AdExposure = No) = 0.4
# • P(ProductPrice = Low) = 0.55
# • P(ProductPrice = High) = 0.45
# Tasks to do:
# • Draw the Bayesian Network structure
# • Define full CPTs for Purchase
# • Implement using Python (pgmpy or similar)


from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('AdExposure', 'WebsiteExperience'),
    ('WebsiteExperience', 'Purchase'),
    ('ProductPrice', 'Purchase')
])

cpd_ad = TabularCPD(
    variable='AdExposure',
    variable_card=2,
    values=[[0.6], [0.4]]
)

cpd_price = TabularCPD(
    variable='ProductPrice',
    variable_card=2,
    values=[[0.55], [0.45]]
)

cpd_web = TabularCPD(
    variable='WebsiteExperience',
    variable_card=2,
    values=[
        [0.8, 0.4],
        [0.2, 0.6]
    ],
    evidence=['AdExposure'],
    evidence_card=[2]
)

cpd_purchase = TabularCPD(
    variable='Purchase',
    variable_card=2,
    values=[
        [0.9, 0.6, 0.7, 0.2],
        [0.1, 0.4, 0.3, 0.8]
    ],
    evidence=['WebsiteExperience', 'ProductPrice'],
    evidence_card=[2, 2]
)

model.add_cpds(cpd_ad, cpd_price, cpd_web, cpd_purchase)

assert model.check_model()

inference = VariableElimination(model)

result = inference.query(
    variables=['Purchase'],
    evidence={'WebsiteExperience': 0, 'ProductPrice': 1}
)

print(result)
