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