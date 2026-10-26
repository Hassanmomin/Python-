P_D = 0.01
P_notD = 0.99
P_T_given_D = 0.99
P_T_given_notD = 0.05
P_T = (P_T_given_D*P_D)+(P_T_given_notD*P_notD)
P_D_given_T = (P_T_given_D*P_D) / P_T
print("probability that person actually has disease given positive test:")
print(P_D_given_T)
