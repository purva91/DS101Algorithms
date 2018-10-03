def calc_ode(name):
    '''
    Function to calculate the ODE of a name
    :param name: Name of the person in form a list
    :returns: ODE of the name
    '''
    letters_sum = 0
    for n in name:
        letters_sum = letters_sum + len(n)
    sum_list = [int(i) for i in str(letters_sum)]
    ode = sum(sum_list)
    return ode

name = input("Enter your name").split()
m_name = input("Enter your mother's name").split()
f_name = input("Enter your father's name").split()

if (calc_ode(name) % 2) == 0:
    if (calc_ode(m_name) % 2) == 0:
        print("Scratch")
    elif (calc_ode(m_name) % 2) != 0:
        print("Python")
    if (calc_ode(f_name) % 2) == 0:
        print("Python")
    elif (calc_ode(f_name) % 2) != 0:
        print("Scratch")

else:
    if (calc_ode(m_name) % 2) == 0:
        print("Python")
    elif (calc_ode(m_name) % 2) != 0:
        print("Scratch")
    if (calc_ode(f_name) % 2) == 0:
        print("Scratch")
    elif (calc_ode(f_name) % 2) != 0:
        print("Python")
