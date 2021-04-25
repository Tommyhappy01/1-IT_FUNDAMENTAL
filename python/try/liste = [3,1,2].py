liste = [3,1,2]
n = len(liste)
olasılık = []  # su tutma olasılığı olan blocklar
sol = []
sol_max = []
sağ_max = []
sağ = []
su = 0
block = 0
​for i in range(1,n-1):
    olasılık.append(liste[i])
print(olasılık) 
​
# sol tarafta kalanlar için
for i in range(0,n-1):
    sol.append(liste[i])
print("sol", sol)
​
# sağ kanat için
for i in range(2,n):
    sağ.append(liste[i])
print("sağ",sağ)
​
for i in range(len(olasılık)):
    block = olasılık[i]
    for j in range(i+1):
          sol_max = sol[j]
    for k in range(i+1):
        sağ_max = sağ[k]
    su += min(sol_max , sağ_max)
print(su)