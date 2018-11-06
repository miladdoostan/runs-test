def runs_test(data):
### The function for conducting the runs test on a data in a numpy array or pandas series ###
    seq = (data > np.median(data))*1
    n1 = sum(seq==1)
    n2 = sum(seq==0)
    r_hat = ((2*n1*n2)/(n1+n2)) + 1
    var_r = (2*n1*n2*(2*n1*n2-n1-n2))/((n1+n2)**2*(n1+n2-1))
    
    run=1
    v_prev = 0
    for v in seq:
        if v!=v_prev:
            run+=1
            v_prev=v
            
    z = (run - r_hat)/(var_r**0.5)
    print('The z statistics is: {}'.format(z))
    if abs(z) < 1.96:

        print('The data is produced in a random manner.')
    else:
        print('The data is not produced in a random manner.')
