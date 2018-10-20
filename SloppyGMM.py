import math

ma = mean
va = var
        
print(np.shape(ma))
print(np.shape(va))

l = np.shape(ma)[0]

r = [[0 for i in range(k)] for j in range(l)]
wts = [0 for i in range(k)]
cm = [0 for i in range(k)]
cv = [0 for i in range(k)]
vm = [0 for i in range(k)]
vv = [0 for i in range(k)]
ocla = [0 for i in range(l)]

for i in range (l):
    cmean = ma[i]
    cvar = va[i]
    cla = 0
    md = (ans[0][0] - cmean) * (ans[0][0] - cmean) + (ans[0][1] - cvar) * (ans[0][1] - cvar)
    for a in range (1, k):
        td = (ans[a][0] - cmean) * (ans[a][0] - cmean) + (ans[a][1] - cvar) * (ans[a][1] - cvar)
        if(td < md):
            md = td
            cla = a
    wts[cla] += 1
    cm[cla] += cmean
    cv[cla] += cvar
    ocla[i] = cla
    
for i in range(k):
    cm[i] /= wts[i]
    cv[i] /= wts[i]

for i in range(l):
    vm[ocla[i]] += (ma[i] - cm[ocla[i]])**2
    vv[ocla[i]] += (va[i] - vm[ocla[i]])**2
for i in range(k):
    vm[i] /= wts[i]
    vv[i] /= wts[i]
    wts[i] /= l
#     vm[i] = vm[i]**(0.5)
#     vv[i] = vv[i]**(0.5)

cnt = 0

print("hellp")
print(k)

while(cnt < 100):
    print(cnt)
    fff = 0
    print(wts)
    for i in range (k):
        print(str(cm[i]) + " " + str(cv[i]))
#     print(cm)
#     print(cv)
#     print(vm)
#     print(vv)
    cnt += 1
    resp = [0 for i in range(k)]
    total_resp = 0
#     print(l)
#     print(k)
    for i in range (l):
        tp = 0
        for c in range(k):
            r[i][c] = (wts[c] * math.exp(-0.5 * ((ma[i] - cm[c])**2 / vm[c] + (va[i] - cv[c])**2 / vv[c]))) / (vm[c] * vv[c])**(0.5)
            #print(r[i][c])
            tp += r[i][c]
        for c in range(k):
            r[i][c] /= tp
            resp[c] += r[i][c]
            total_resp += r[i][c]
        fff += tp
    
    print(fff)
    #print(resp)

    for c in range(k):
        wts[c] = resp[c] / total_resp
        cm[c] = 0
        cv[c] = 0
        vv[c] = 0
        vm[c] = 0
        for i in range(l):
            cm[c] += r[i][c] * ma[i]
            cv[c] += r[i][c] * va[i]
        cm[c] /= resp[c]
        cv[c] /= resp[c]
        for i in range(l):
            vm[c] += r[i][c] * (cm[c] - ma[i])**2
            vv[c] += r[i][c] * (cv[c] - va[i])**2
        vm[c] /= resp[c]
        vv[c] /= resp[c]
