'''
coin flipping problem - utilising bayesian techniques (PyMC3)
utilising gpu C++ and returns TensorVariable
'''

import numpy as np
import scipy.stats as stats
import pymc3 as pm
import arviz as az

az.style.use('arviz-white')

np.random.seed(123)
trials = 4
theta_real = 0.35 # unknown value in a real experiment
data = stats.bernoulli.rvs(p=theta_real, size=trials)
print(data)

'''
with pm.Model() as our_first_model:

    θ = pm.Beta('θ', alpha=1., beta=1.)
    y = pm.Bernoulli('y', p=θ, observed=data)   
    trace = pm.sample(1000, random_seed=123)
az.plot_trace(trace)
'''