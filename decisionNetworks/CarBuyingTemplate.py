def normalize(v):
    s = sum(v)
    for i in range(len(v)):
        v[i] /= s
    return v

def decision_network(purchase_cost, good_value, repair_cost,
                     p_good,
                     p_pass_given_good, p_pass_given_bad,
                     test_cost=0):

    # 1. Expected utility of buying the car without a test
    utility_no_test = 0
    " *** YOUR CODE HERE ***"

    print()
    print(f"Expected utility of purchase w/o test: {utility_no_test:.2f}")

    # 3. P(Quality | Test)
    # Initializing with placeholder values that allow template to run.
    # First value in a list is for good quality, second for bad.
    quality_given_pass = [0.0, 0.0] 
    quality_given_fail = [0.0, 0.0]
    " *** YOUR CODE HERE ***"

    print()
    print( "              | P(Quality | Test)")
    print( "  Test Result |  Good  |  Bad")
    print(f"     Pass     | {quality_given_pass[0]:6.4} | {quality_given_pass[1]:5.4}")
    print(f"     Fail     | {quality_given_fail[0]:6.4} | {quality_given_fail[1]:5.4}")

    # 4. Expected utility of buying car with test passing or test failing.
    #    Utilities are decreased by cost of test.
    utility_pass_test = 0
    utility_fail_test = 0
    " *** YOUR CODE HERE ***"

    print()
    print(f"Expected utility of purchase w/ passing test: {utility_pass_test:.2f}")
    print(f"Expected utility of purchase w/ failing test: {utility_fail_test:.2f}")

    # 5. Probability that the test passes
    p_pass = 0
    " *** YOUR CODE HERE ***"

    print()
    print(f"Probability of passing test: {p_pass:.4f}")

    # 6. VPI for the test
    VPI = 0
    " *** YOUR CODE HERE ***"

    print()
    print(f"VPI for the test: {VPI:.4f}")
    
if __name__ == "__main__":
    # Textbook version of problem that can be used for testing.
    '''
    decision_network(purchase_cost=1500, good_value=2000, repair_cost=700,
                     p_good=0.7,
                     p_pass_given_good=0.8, p_pass_given_bad=0.35)
    '''

    # Problem data for three test costs
    decision_network(purchase_cost=5500, good_value=6000, repair_cost=1000,
                     p_good=0.6,
                     p_pass_given_good=0.85, p_pass_given_bad=0.2)
    decision_network(purchase_cost=5500, good_value=6000, repair_cost=1000,
                     p_good=0.6,
                     p_pass_given_good=0.85, p_pass_given_bad=0.2,
                     test_cost=100)
    decision_network(purchase_cost=5500, good_value=6000, repair_cost=1000,
                     p_good=0.6,
                     p_pass_given_good=0.85, p_pass_given_bad=0.2,
                     test_cost=200)
