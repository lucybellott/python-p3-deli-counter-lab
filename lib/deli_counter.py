katz_deli = ['lucas','amy','heino']

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:    
        for i in range(len(katz_deli)):
            print(f"the line is currently {i + 1}. {katz_deli[i]}")


def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f'Welcome, {new_customer}. ' +\
        f'You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    print(f"Currently serving{katz_deli[0]}")
    katz_deli.pop(0)




line(katz_deli)
