    # Import libraries
    import pgmpy.models
    import pgmpy.inference
    import networkx as nx
    import pylab as plt
    # Create a bayesian network
    model = pgmpy.models.BayesianModel([('Guest', 'Monty'), 
                                        ('Price', 'Monty')])
    # Define conditional probability distributions (CPD)
    # Probability of guest selecting door 0, 1 and 2
    cpd_guest = pgmpy.factors.discrete.TabularCPD('Guest', 3, [[0.33, 0.33, 0.33]])
    # Probability that the price is behind door 0, 1 and 2
    cpd_price = pgmpy.factors.discrete.TabularCPD('Price', 3, [[0.33, 0.33, 0.33]])
    # Probability that Monty selects a door (0, 1, 2), when we know which door the guest has selected and we know were the price is
    cpd_monty = pgmpy.factors.discrete.TabularCPD('Monty', 3, [[0, 0, 0, 0, 0.5, 1, 0, 1, 0.5], 
                                                               [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5], 
                                                               [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]], 
                                                  evidence=['Guest', 'Price'], 
                                                  evidence_card=[3, 3])
    # Add CPDs to the network structure
    model.add_cpds(cpd_guest, cpd_price, cpd_monty)
    # Check if the model is valid, throw an exception otherwise
    model.check_model()
    # Print probability distributions
    print('Probability distribution, P(Guest)')
    print(cpd_guest)
    print()
    print('Probability distribution, P(Price)')
    print(cpd_price)
    print()
    print('Joint probability distribution, P(Monty | Guest, Price)')
    print(cpd_monty)
    print()
    # Plot the model
    nx.draw(model, with_labels=True)
    plt.savefig('C:\\DATA\\Python-data\\bayesian-networks\\monty-hall.png')
    plt.close()
    # Perform variable elimination for inference
    # Variable elimination (VE) is a an exact inference algorithm in bayesian networks
    infer = pgmpy.inference.VariableElimination(model)
    # Calculate probabilites for doors including price, the guest has selected door 0 and Monty has selected door 2
    posterior_probability = infer.query(['Price'], evidence={'Guest': 0, 'Monty': 2})
    # Print posterior probability
    print('Posterior probability, Guest(0) and Monty(2)')
    print(posterior_probability)
    print()
