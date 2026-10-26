from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('burglary','Alarm'),('earthquake','Alarm')
    ])
cpd_burglary = TabularCPD(
    variable = 'burglary',
    variable_card = 2,
    values = [[0.999],[0.001]]
    )
cpd_earthquake = TabularCPD(
    variable = 'earthquake',
    variable_card = 2,
    values = [[0.998],[0.002]]
    )
cpd_alarm = TabularCPD(
    variable = 'Alarm',
    variable_card = 2,
    values = [[0.999,0.71,0.08,0.05],[0.001,0.29,0.94,0.95]],
    evidence = ['burglary','earthquake'],
    evidence_card = [2,2]
    )
