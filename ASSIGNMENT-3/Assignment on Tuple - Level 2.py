# #lex_auth_01269442027919769669
#
# #Global variables
#
# child_id=(10,20,30,40,50)
# chocolates_received=[12,5,3,4,6]
#
# def reward_child(child_id_rewarded,extra_chocolates):
#     if (extra_chocolates<1):
#         print("Extra chocolates is less than 1")
#     elif (child_id_rewarded not in child_id):
#         print("Child id is invalid")
#     else:
#         s=0
#         s=extra_chocolates+calculate_total_chocolates()
#         print(s)
#         print(chocolates_received)
#
#
# def calculate_total_chocolates():
#     return sum(chocolates_received)
#
#         # Use the below given print statements to display the output
#     # Also, do not modify them for verification to work
#
#     #print("Extra chocolates is less than 1")
#     #print("Child id is invalid")
#     #print(chocolates_received)
#
# reward_child(20,2)
# #Test your code by passing different values for child_id_rewarded,extra_chocolates

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
def calculate_total_chocolates():
    return sum(chocolates_received)
def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates>0:
        if child_id_rewarded in child_id:
            child_id_index=child_id.index(child_id_rewarded)
            chocolates_received[child_id_index]+=extra_chocolates
            print(chocolates_received)
        else:
            print('Child id is invalid')
    else:
        print('Extra chocolates is less than 1')
print(calculate_total_chocolates())
reward_child(20,2)