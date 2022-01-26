# 10.01.22 14:50-15:25
def r(path='BIO/rosalind/algorithmic_heights/test.txt'):
    file = open(path, 'r')
    F = []
    for line in file.readlines():
        try:
            F.append(int(line.strip()))
        except:
            line = line.strip().split()
            try:
                line = [int(item) for item in line]
            except:
                pass
            F.append(line)
    file.close
    return F

def w(Arr, path = 'BIO/rosalind/algorithmic_heights/output.txt'):
    file = open(path, 'w')
    file.write(' '.join(str(a) for a in Arr))
    file.close

# 10.01.22 15:25-16:00, 16:30-16:56 +
def bins(F = r('BIO/rosalind/algorithmic_heights/rosalind_bins.txt')):
    A = F[2]
    Ans = []
    for x in F[3]:
        l = 0
        r = F[0]
        while r-l>0:
            m=int((l+r)/2)
            if A[m]>x:
                r = m
            elif A[m]<x:
                l=m+1
            else:
                Ans.append(m+1)
                break
        else:
            Ans.append(-1)
    print( ' '.join(str(a) for a in Ans) )
    w(Ans)
    return Ans
# bins()

# 10.01.22 16:57-17:14 -+
def deg(F = r('BIO/rosalind/algorithmic_heights/rosalind_deg — копия.txt')):
    M = []
    Ans = []
    for i in range(1, len(F)):
        M = M + F[i]
    for j in range(1, F[0][0]+1):
        Ans.append(M.count(j))
    print(' '.join(str(x) for x in Ans))
    w(Ans)
# deg()

# 10.01.22 17:24-17:35 +
def ins(F=r('BIO/rosalind/algorithmic_heights/rosalind_ins.txt')):
    swapcounter = 0
    for i in range(1, F[0]):
        j = i
        while j > 0 and F[1][j] < F[1][j-1]:
            F[1][j], F[1][j-1] = F[1][j-1],  F[1][j]
            swapcounter +=1
            j -= 1
    print (swapcounter)
# ins()

# 10.01.22 18:00-18:12 +
def ddeg(F=r('BIO/rosalind/algorithmic_heights/rosalind_ddeg.txt')):
    Ans = []
    D = {}
    for i in range (1, F[0][0]+1):
        D[i] = []
    for x in F[1:]:
        D[x[0]].append(x[1])
        D[x[1]].append(x[0])
    for i in range (1, F[0][0]+1):
        ans = 0
        for j in D[i]:
            ans+=len(D[j])
        Ans.append(ans)
    print(' '.join(str(x) for x in Ans))
# ddeg()

# 10.01.22 18:20-18:33 +
def mer(F=r('BIO/rosalind/algorithmic_heights/rosalind_mer.txt')):
    C = []
    while len(F[1])>0 and len(F[3])>0:
        if F[1][0] <= F[3][0]:
            C.append(F[1].pop(0))
        else:
            C.append(F[3].pop(0))
    C = C + F[1] + F[3]
    w(C)
# mer()

# 10.01.22 17:50-18:00 ~
# 11.01.22 4:57-5:38 +
def maj(F = r('BIO/rosalind/algorithmic_heights/rosalind_maj.txt')):
    Ans = []
    for arr in F[1:]:
        counter = 0
        zerocounter = 0
        candidate = None
        for num in arr:
            if counter == 0:
                candidate = num
                zerocounter+=1
            counter += (1 if candidate == num else -1)
        Ans.append(candidate if counter - zerocounter >= 0 else -1)
    print(' '.join(str(x) for x in Ans))
# maj()

# 11.01.22 5:38-6:41 -+
def _2sum(F=r('BIO/rosalind/algorithmic_heights/rosalind_2sum — копия.txt')):
    for arr in F[1:]:
        ans = False
        D = {}
        for i in range(len(arr)):
            D[arr[i]] = i
        for i in range(len(arr)):
            if -(arr[i]) in D and D[-(arr[i])] != i:
                print(i+1, D[-(arr[i])]+1)
                ans = True
                break
        if ans == False:
            print(-1)
# _2sum()

# 11.01.22 6:42-7:05 +
def bfs(F=r('BIO/rosalind/algorithmic_heights/rosalind_bfs.txt')):
    Ans=[]
    D = {}
    for i in range(F[0][0]):
        Ans.append(-1)
        D[i+1] = []
    Ans[0] = 0
    for edges in F[1:]:
        D[edges[0]].append(edges[1])
    que = [1]
    while len(que) > 0:
        v = que.pop(0)
        for u in D[v]:
            if Ans[u-1] == -1:
                Ans[u-1] = Ans[v-1] + 1
                que.append(u) 
    print(' '.join(str(x) for x in Ans))
# bfs()

# 11.01.22 7:17-7:35 +
def dfs(v, mark, D):
    mark[v-1] = 1
    for u in D[v]:
        if mark[u-1] == 0:
            dfs(u, mark, D)
def cc(F=r('BIO/rosalind/algorithmic_heights/rosalind_cc.txt')):
    D = {}
    mark = []
    for i in range(1, F[0][0]+1):
        D[i] = []
        mark.append(0)
    for e in F[1:]:
        D[e[0]].append(e[1])
        D[e[1]].append(e[0])
    cccounter = 0
    for j in range(F[0][0]):
        if mark[j] == 0:
            cccounter +=1
            dfs(j+1, mark, D)
    print(cccounter)      
# cc()

# 11.01.22 7:38-7:48 +
def hea(F=r('BIO/rosalind/algorithmic_heights/rosalind_hea.txt')):
    A = []
    for num in F[1]:
        A.append(num)
        i = len(A) - 1
        while i > 0 and A[i] > A[int((i-1)/2)]:
            A[i], A[int((i-1)/2)] = A[int((i-1)/2)], A[i]
            i = int((i-1)/2)
    # print(' '.join(str(x) for x in A))
    w(A)
# hea()

# 11.01.22 7:50-8:20 +
def merge(A, B):
    C = []
    while len(A)>0 and len(B)>0:
        if A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    C = C + A + B
    return C
def mergesort(A):
    if len(A) <= 1:
        return A
    Aleft = A[:int(len(A)/2)]
    Aright = A[int(len(A)/2):]
    Aleft = mergesort(Aleft)
    Aright = mergesort(Aright)
    return merge(Aleft, Aright)
# w(mergesort(r('BIO/rosalind/algorithmic_heights/rosalind_ms.txt')[1]))


# 11.01.22 8:36-9:28, 9:40-10:34 -
# 12.01.22 6:20-7:40 +

# for potom(with oshibka)
# from random import randint
# def part(A, l, r, y): 
#     # if r-l==1:
#     x = A[randint(l, r-1)]
#     m=l
#     x = A[randint(l, r-1)]
#     if A[x] == y:
#         print (m)
#         return 
#     for i in range(l, r):
#         if A[i] < x:
#             A[i], A[m] = A[m], A[i]
#             m+=1
#     if y < A[x]:
#         part(A, l, m, y)
#     else:
#         part(A, m, r, y)

def par(F=r('BIO/rosalind/algorithmic_heights/rosalind_par — копия.txt')):
    A = F[1]
    l = 0
    r = len(A)
    x = A[0]
    for i in range(l, r):
        if A[i] < x:
            A[i], A[l] = A[l], A[i]
            l+=1
    for j in range(l, r):
        if A[j] == x:
            A[j], A[l] = A[l], A[j]
            break
    w(A)
    return A
# par()


# 12.01.22 7:55-8:43 +
def _3sum(F=r('BIO/rosalind/algorithmic_heights/rosalind_3sum.txt')):
    lenarr = F[0][1]
    for arr in F[1:]:
        ans = False
        for i in range(lenarr):
            D = {}
            for j in range(i+1, lenarr):
                D[arr[j]] = j
            for j in range(i+1, lenarr):
                if -(arr[i]+arr[j]) in D and D[-(arr[i]+arr[j])] != j:
                    print(i+1, j+1, D[-(arr[i]+arr[j])]+1)
                    ans = True
                    break
            if ans == True:
                break
        if ans == False:
            print(-1)
# _3sum()

# 12.01.22 8:49-9:34, 9:45-10:18 -+
def bip(F=r('BIO/rosalind/algorithmic_heights/rosalind_bip — копия.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    ans = []
    for G in Gs[1:]:
        ansis = True
        D = {}
        mark = []
        for v in range(1, G[0][0]+1):
            D[v] = []
            mark.append(-1)
        for e in G[1:]:
            D[e[0]].append(e[1])
            D[e[1]].append(e[0])
        mark[0] = 0 
        q = [1]
        while len(q)>0:
            v = q.pop(0)
            for u in D[v]:
                if mark[u-1] == -1:
                    q.append(u)
                    mark[u-1] = 1 if mark[v-1] == 0 else 0
                elif mark[u-1] == mark[v-1]:
                    ansis = False
        ans.append(1 if ansis == True else -1)
    print(' '.join(str(x) for x in ans))
# bip()

# 12.01.22 10:21-11:13, 11:38-12:38, 14:20-14:55 --+
def dfs_c(v, D, mark, cycles):
    mark[v-1] = 1
    for u in D[v]:
        if mark[u-1] == 1:
            cycles.append(u)
        if mark[u-1] == -1:
            dfs_c(u, D, mark, cycles)
    mark[v-1] = 2

def dag(F=r('BIO/rosalind/algorithmic_heights/rosalind_dag — копия 2.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    ans = []
    for G in Gs[1:]:
        D = {}
        mark = []
        for v in range(1, G[0][0]+1):
            D[v] = []
            mark.append(-1)
        for e in G[1:]:
            D[e[0]].append(e[1])
        cycles = []
        for v in range(1, G[0][0]+1):
            # mark2=mark[:]
            if mark[v-1] == -1:
                dfs_c(v, D, mark, cycles)
        ans.append(-1 if len(cycles)>0 else 1)
    print(' '.join(str(x) for x in ans))
# dag()

# 12.01.22 17:40-19:10 ~
# 13.01.22 7:45-9:00 ±±+

def dij(F=r('BIO/rosalind/algorithmic_heights/rosalind_dij — копия 2.txt')):
    E = {}
    D = []
    Q = {}
    for v in range(1, F[0][0]+1):
        E[v] = {}
        Q[v] = float('inf')
        D.append(float('inf'))
    for e in F[1:]:
        E[e[0]][e[1]] = float('inf')
    for e in F[1:]:
        if e[2] < E[e[0]][e[1]]:
            E[e[0]][e[1]] = e[2]
    D[0] = 0
    Q[1] = 0
    Processed = []
    while len(Q)>0:
        minvalue = float('inf')
        v = None
        for key, val in Q.items():
            if val <= minvalue:
                minvalue = val
                v = key
        del Q[v]
        # A.append(v)
        for u in E[v].keys():
            if u in Q:
                D[u-1] = min(D[u-1], D[v-1]+E[v][u])
                Q[u] = D[u-1]
    for i in range(len(D)):
        D[i] = -1 if D[i] == float('inf') else D[i]
    print(' '.join(str(x) for x in D))
    w(D)
# dij()

# 13.01.22 9:10-9:33 +
def hs(F=r('BIO/rosalind/algorithmic_heights/rosalind_hs.txt')):
    A = []
    for k in range(F[0]):
        A.append(F[1][k])
        i = len(A) - 1
        while i > 0 and A[i] < A[int((i-1)/2)]:
            A[i], A[int((i-1)/2)] = A[int((i-1)/2)], A[i]
            i = int((i-1)/2)
    B = []
    for i in range(len(A)):
        B.append(A[0])
        A[0] = A[len(A)-1]
        A.pop()
        i = 0
        while 1:
            j = i
            if 2*i+1<len(A) and A[2*i+1] < A[j]:
                j = 2*i + 1
            if 2*i+2<len(A) and A[2*i+2] < A[j]:
                j = 2*i + 2
            if i == j:
                break
            A[i], A[j] = A[j], A[i]
            i = j
    w(B)
# hs()


# 13.01.22 18:10:18:55
# quicksort for potom (ne rabotaet)
# from random import randint
# def qs(arr, l, r): 
#     if r-l <= 1:
#         return
#     x = arr[randint(l, r-1)]
#     m = l
#     k = 0
#     for i in range(l, r):
#         if arr[i] <= x:
#             if arr[i] == x:
#                 k+=1
#             arr[i], arr[m] = arr[m], arr[i]
#             m+=1
#     qs(arr, l, m+1-k)
#     qs(arr, m, r)

# 13.01.22 16:53-18:01, 19:00-19:34 -+
def merge2(A, B, sw):
    C = []
    while len(A)>0 and len(B)>0:
        if A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
            sw.append(len(A))
    C = C + A + B
    return C
def mergesort2(A, sw):
    if len(A) <= 1:
        return A
    Aleft = A[:int(len(A)/2)]
    Aright = A[int(len(A)/2):]
    Aleft = mergesort2(Aleft,sw)
    Aright = mergesort2(Aright,sw)
    return merge2(Aleft, Aright,sw)
def inv(F=r('BIO/rosalind/algorithmic_heights/rosalind_inv — копия.txt')):
    arr = F[1]
    sw = []
    mergesort2(arr, sw)
    print(sum(sw))
# inv()


# 13.01.22 19:39-19:54, 20:20-20:31 +
def par3(F=r('BIO/rosalind/algorithmic_heights/rosalind_par3.txt')):
    arr = F[1]
    n = F[0]
    x = arr[0]
    j = 0
    for i in range(n):
        if arr[j] > x:
            arr.append(arr.pop(j))
            j-=1
        j+=1
    j = n-1
    for i in range(n-1, -1, -1):
        if arr[j] < x:
            arr.insert(0, arr.pop(j))
            j+=1
        j-=1
    w(arr)
# par3()


# 13.01.22 20:50-21:36 +
def sq(F=r('BIO/rosalind/algorithmic_heights/rosalind_sq.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    for G in Gs[1:]:
        M = []
        for i in range(G[0][0]):
            M.append([])
            for j in range(G[0][0]):
                M[-1].append(0)
        for e in G[1:]:
            M[e[0]-1][e[1]-1] = 1
            M[e[1]-1][e[0]-1] = 1
        sqc = -1
        for i in range(G[0][0]-1):
            for j in range (i+1, G[0][0]-1):
                c = 0
                for k in range(G[0][0]):
                    if (M[i][k] + M[j][k]) == 2:
                        c+=1
                    if c == 2:
                        sqc = 1
                        break
        print(sqc, end = ' ')
    print()
# sq()

# 14.01.22 7:41-8:44 +
def bd(F=r('BIO/rosalind/algorithmic_heights/rosalind_bf.txt')):
    E = {}
    D = []
    ans = []
    for v in range(1, F[0][0]+1):
        E[v] = {}
        ans.append(float('inf'))
        D.append([])
        for i in range(F[0][0]):
            D[-1].append(float('inf'))
    for e in F[1:]:
        E[e[1]][e[0]] = float('inf')
    for e in F[1:]:
        if e[2] < E[e[1]][e[0]]:
            E[e[1]][e[0]] = e[2]
    D[0][0] = 0
    for k in range(F[0][0]):
        print(k, F[0][0])
        for v in range(1, F[0][0]+1):
            min_d = float('inf')
            for u, val in E[v].items():
                if val + D[k-1][u-1] < min_d:
                    D[k][v-1] = val + D[k-1][u-1]
            if D[k][v-1] < ans[v-1]:
                ans[v-1] = D[k][v-1]
    for i in range(len(ans)):
        if ans[i] == float('inf'):
            ans[i] = 'x'
    print(' '.join(str(x) for x in ans))
    w(E)
# bd()


# 14.01.22 8:55-9:33 ±+
def cte(F=r('BIO/rosalind/algorithmic_heights/rosalind_cte — копия.txt')):
    ans = []
    Gs = [[F[0]]]
    for i in range(F[0]):
        Gs.append([])
        for j in range (F[1][1]+1):
            Gs[-1].append(F.pop(1))
    for G in Gs[1:]:
        E = {}
        D = []
        Q = {}
        for v in range(1, G[0][0]+1):
            E[v] = {}
            Q[v] = float('inf')
            D.append(float('inf'))
        for e in G[1:]:
            E[e[0]][e[1]] = float('inf')
        for e in G[1:]:
            if e[2] < E[e[0]][e[1]]:
                E[e[0]][e[1]] = e[2]
        D[G[1][1]-1] = 0
        Q[G[1][1]] = 0
        # Processed = []
        while len(Q)>0:
            minvalue = float('inf')
            v = None
            for key, val in Q.items():
                if val <= minvalue:
                    minvalue = val
                    v = key
            del Q[v]
            # A.append(v)
            for u in E[v].keys():
                if u in Q:
                    D[u-1] = min(D[u-1], D[v-1]+E[v][u])
                    Q[u] = D[u-1]
        if D[G[1][0]-1]+E[G[1][0]][G[1][1]] != float('inf'):
            ans.append(D[G[1][0]-1]+E[G[1][0]][G[1][1]])
        else:
            ans.append(-1)
        print('graph processed')
    print(' '.join (str(x) for x in ans))
# cte()

# 14.01.22 9:50-10:34 
def partition(arr, l, r):
    if r-l<=1:
        return l
    pivot = arr[r-1]
    i = l
    j = r-2
    while i <= j:
        while arr[i] < pivot:
            i+=1
        while arr[j] >= pivot and j>=0:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    arr[r-1], arr[i] = arr[i], arr[r-1]
    return i

# 14.01.22 10:50-11:35 +
def kth(arr, l, r, k):
    part = partition(arr, l, r)
    if k-1 == part:
        print(arr[k-1])
    if k-1 < part:
        kth(arr, l, part, k)
    if k-1 > part:
        kth(arr, part, r, k)  
def med(F=r('BIO/rosalind/algorithmic_heights/rosalind_med.txt')):
    arr = F[1]
    n = F[0]
    k = F[2]
    res = []
    kth(arr, 0, n, k)
# med()


# 14.01.22 11:37-12:02, 12:12-13:01, 14:40-14:58 +
def partsort(arr, l, r, k):
    # print(l, r, r-l)
    part = partition(arr, l, r)
    if part > l:
        partsort(arr, l, part, k)
    if part+1 < r and k-1 > part:
        partsort(arr, part+1, r, k)
def ps(F=r('BIO/rosalind/algorithmic_heights/rosalind_ps — копия.txt')):
    arr = F[1]
    k = F[2]
    partsort(arr, 0, len(arr), k)
    print(' '.join(str(x) for x in arr[:k]))
# ps()

# 14.01.22 13:03-13:16 +
def dfs_t(v, mark, D, topsort):
    if mark[v-1] == 1:
        return
    mark[v-1] = 1
    for u in D[v]:
        if mark[u-1] == 0:
            dfs_t(u, mark, D, topsort)
    topsort.append(v)
def ts(F=r('BIO/rosalind/algorithmic_heights/rosalind_ts.txt')):
    topsort = []
    Adj = {}
    mark=[]
    for i in range(1, F[0][0]+1):
        Adj[i] = []
        mark.append(0)
    for e in F[1:]:
        Adj[e[0]].append(e[1])
    for i in range(1, F[0][0]+1):
        dfs_t(i, mark, Adj, topsort)
    print(' '.join(str(x) for x in topsort[::-1]))
# ts()


# 14.01.22 14:59-15:02 +
def quicksort(arr, l, r):
    part = partition(arr, l, r)
    if part > l:
        quicksort(arr, l, part)
    if part+1 < r:
        quicksort(arr, part+1, r)
def qs(F=r('BIO/rosalind/algorithmic_heights/rosalind_qs.txt')):
    n = F[0]
    arr = F[1]
    quicksort(arr, 0, n)
    w(arr)
# qs()


# 14.01.22 15:03-15:25 +
def hdag(F=r('BIO/rosalind/algorithmic_heights/rosalind_hdag.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    for G in Gs[1:]:
        topsort = []
        Adj = {}
        mark=[]
        for i in range(1, G[0][0]+1):
            Adj[i] = []
            mark.append(0)
        for e in G[1:]:
            Adj[e[0]].append(e[1])
        for i in range(1, G[0][0]+1):
            dfs_t(i, mark, Adj, topsort)
        topsort.reverse()
        hamilton = True
        for i in range(len(topsort)-1):
            if topsort[i+1] not in Adj[topsort[i]]:
                hamilton = False
        if hamilton == True:
            print(1, end=' ')
            print(' '.join(str(x) for x in topsort))
        else:
            print(-1)
# hdag()

# 14.01.22 15:33-16:35, 16:57-17:21
# 16.01.22 13:50-15:16 +
def dfs_ts(v, mark, Adj, topsort):
    if mark[v-1] == 1:
        return
    mark[v-1] = 1
    for u in Adj[v].keys():
        if mark[u-1] == 0:
            dfs_ts(u, mark, Adj, topsort)
    topsort.append(v)
def nwc(F=r('BIO/rosalind/algorithmic_heights/rosalind_nwc — копия.txt')):
    ans = []
    # Gs = [[]]
    # for f in F:
    #     if f == []:
    #         Gs.append([])
    #     else:
    #         Gs[-1].append(f)
    Gs = [[F[0]]]
    for i in range(F[0]):
        Gs.append([])
        for j in range (F[1][1]+1):
            Gs[-1].append(F.pop(1))
    Gcounter = 0
    for G in Gs[1:]:
        Gcounter+=1
        Adj = {}
        Ddefault = []
        mark = []
        topsort = []
        for v in range(1, G[0][0]+1):
            Adj[v] = {}
            Ddefault.append(float('inf'))
            mark.append(0)
        for e in G[1:]:
            Adj[e[1]][e[0]] = float('inf')
        for e in G[1:]:
            if e[2] < Adj[e[1]][e[0]]:
                Adj[e[1]][e[0]] = e[2]
        for v in Adj.keys():
            dfs_ts(v, mark,  Adj, topsort)
        topsort.reverse()
        Candidate = []
        for v in topsort:
            minvalue = float('inf')
            for key, value in Adj[v].items():
                if value < minvalue:
                    minvalue = value
            if minvalue < 0:
                Candidate.append(v)
        withcycle=False
        while len(Candidate) > 0 and withcycle == False:
            v = Candidate.pop(0)
            D = Ddefault[:]
            D[v-1] = 0
            ok = False
            counter = 0
            while not ok and counter <= G[0][0]:
                ok = True
                for v in Adj.keys():
                    for u in Adj[v].keys():
                        if D[v-1] > D[u-1] + Adj[v][u]:
                            D[v-1] = D[u-1] + Adj[v][u]
                            ok = False
                counter+=1
            if counter > G[0][0]:
                withcycle = True
            print('Graph#', Gcounter, 'Candidates left', len(Candidate), ' Counter/vertices =', counter,'/', G[0][0], withcycle)
        if withcycle == True:
            ans.append(1)
            print('With cycle')
        else:
            ans.append(-1)
            print('No cycle')
    print(' '.join(str(x) for x in ans))
# nwc()


# 14.01.22 17:22-17:51 +
def scc(F=r('BIO/rosalind/algorithmic_heights/rosalind_scc.txt')):
    topsort = []
    Adj_out = {}
    Adj_in = {}
    mark_clear=[]
    for i in range(1, F[0][0]+1):
        Adj_out[i] = []
        Adj_in[i] = []
        mark_clear.append(0)
    for e in F[1:]:
        Adj_out[e[0]].append(e[1])
        Adj_in[e[1]].append(e[0])
    mark = mark_clear[:]
    for i in range(1, F[0][0]+1):
        dfs_t(i, mark, Adj_out, topsort)
    topsort.reverse()
    mark = mark_clear[:]
    cc = 0
    for i in range(len(topsort)):
        if mark[topsort[i]-1] == 0:
            cc +=1
            dfs_t(topsort[i], mark, Adj_in, topsort)
    print(cc)
# scc()


# 16.01.22 15:30-16:08 ±+
def sdag(F=r('BIO/rosalind/algorithmic_heights/rosalind_sdag — копия 4.txt')):
    Adj = {}
    Ddefault = []
    mark = []
    topsort = []
    for v in range(1, F[0][0]+1):
        Adj[v] = {}
        Ddefault.append(float('inf'))
        mark.append(0)
    for e in F[1:]:
        # Вес ребра = последний назначенный, а не наименьший
        # Adj[e[1]][e[0]] = float('inf')
        Adj[e[1]][e[0]] = e[2]
    # for e in F[1:]:
    #     if e[2] < Adj[e[1]][e[0]]:
    #         Adj[e[1]][e[0]] = e[2]
    for v in Adj.keys():
        dfs_ts(v, mark,  Adj, topsort)
    print(len(topsort))
    v = 1
    D = Ddefault[:]
    D[v-1] = 0
    ok = False
    counter = 0
    while not ok:
        counter +=1
        print(counter)
        ok = True
        for v in topsort:
            for u in Adj[v].keys():
                if D[v-1] > D[u-1] + Adj[v][u]:
                    D[v-1] = D[u-1] + Adj[v][u]
                    ok = False
    for i in range(len(D)):
        if D[i] == float('inf'):
            D[i] = 'x'
    w(D)
    # print(' '.join(str(x) for x in D))
# sdag()


# 16.01.22 17:40-19:08, 19:28-20:28 ----
# 17.01.22 16:14-17:56 -+
import sys, copy
sys.setrecursionlimit(2000)
def dfs2(v, mark, Adj, topsort):
    if mark[v] == 1:
        return
    mark[v] = 1
    for u in Adj[v]:
        if mark[u] == 0:
            dfs2(u, mark, Adj, topsort)
    topsort.append(v)
def _2sat(F=r('BIO/rosalind/algorithmic_heights/rosalind_2sat — копия 6.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    for G in Gs[1:]:
        # print('>>> graph with', G[0][0], 'vertices and', G[0][1], 'edges')
        Adjout = {}
        topsort = []
        mark_clear = {}
        sign = {}
        for v in range(1, G[0][0]+1):
            Adjout[-v] = []
            Adjout[v] = []
            mark_clear[-v] = 0
            mark_clear[v] = 0
            sign[-v] = 0
            sign[v] = 0
        Adjin = copy.deepcopy(Adjout)
        for e in G[1:]:
            Adjout[-e[0]].append(e[1])
            Adjout[-e[1]].append(e[0])
            Adjin[e[0]].append(-e[1])
            Adjin[e[1]].append(-e[0])
        mark = mark_clear.copy()
        for v in Adjout.keys():
            dfs2(v, mark, Adjout, topsort)
        topsort.reverse()
        mark = mark_clear.copy()
        CC = []
        ans = True
        # print(topsort)
        for v in topsort:
            if mark[v] == 0:
                topsort2 = []
                dfs2(v, mark, Adjin, topsort2)
                for v in topsort2:
                    if -v in topsort2:
                        ans = False
                        break
                if ans == False:
                    break
                CC.append(topsort2)
        # print(CC)
        Ans = []
        if ans == True:
            for i in range(len(CC)-1, -1, -1):
                for v in CC[i]:
                    if v not in Ans and -v not in Ans:
                        Ans.append(v)
            Ans = sorted(Ans, key = abs)
            Ans.insert(0, 1)
        else:
            Ans.append(0)
        print(' '.join(str(x) for x in Ans))
_2sat()


# 17.01.22 15:25-16:02 +
def dfs3(v, mark, Adj, topsort):
    if mark[v] == 1:
        return
    mark[v] = 1
    for u in Adj[v]:
        if mark[u] == 0:
            dfs3(u, mark, Adj, topsort)
    topsort.append(v)
def gs(F=r('BIO/rosalind/algorithmic_heights/rosalind_gs.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    ans = []
    for G in Gs[1:]:
        Adjout = {}
        Adjin = {}
        mark_clear = {}
        topsort = []
        for v in range(1, G[0][0]+1):
            mark_clear[v] = 0
            Adjin[v] = []
            Adjout[v] = []
        for e in G[1:]:
            Adjout[e[0]].append(e[1])
            Adjin[e[1]].append(e[0])
        mark = mark_clear.copy()
        for v in range(1, G[0][0]+1):
            dfs3(v, mark, Adjout, topsort)
        topsort.reverse()
        mark = mark_clear.copy()
        CC = []
        for v in topsort:
            if mark[v] == 0:
                topsort2 = []
                dfs3(v, mark, Adjin, topsort2)
                CC.append(topsort2)
        source_list = []
        for cc in CC:
            source = 1
            for v in cc:
                for u in Adjin[v]:
                    if u not in cc:
                        source = 0
                        break
                if source == 0:
                    break
            source_list.append(source)
        if sum(source_list) == 1:
            for i in range(len(source_list)):
                if source_list[i] == 1:
                    ans.append(CC[i][0])
                    break
        else:
            ans.append(-1)
    print(' '.join(str(x) for x in ans))               
# gs()

# 17.01.22 16:04-16:12 +
def sc(F=r('BIO/rosalind/algorithmic_heights/rosalind_sc.txt')):
    Gs = [[]]
    for f in F:
        if f == []:
            Gs.append([])
        else:
            Gs[-1].append(f)
    ans = []
    for G in Gs[1:]:
        Adjout = {}
        Adjin = {}
        mark_clear = {}
        topsort = []
        for v in range(1, G[0][0]+1):
            mark_clear[v] = 0
            Adjin[v] = []
            Adjout[v] = []
        for e in G[1:]:
            Adjout[e[0]].append(e[1])
            Adjin[e[1]].append(e[0])
        mark = mark_clear.copy()
        for v in range(1, G[0][0]+1):
            dfs3(v, mark, Adjout, topsort)
        topsort.reverse()
        mark = mark_clear.copy()
        CC = []
        for v in topsort:
            if mark[v] == 0:
                topsort2 = []
                dfs3(v, mark, Adjin, topsort2)
                CC.append(topsort2)
        source_list = []
        sink_list = []
        for cc in CC:
            source = 1
            sink = 1
            for v in cc:
                for u in Adjin[v]:
                    if u not in cc:
                        source = 0
                        break
                for u in Adjout[v]:
                    if u not in cc:
                        sink = 0
                        break               
            source_list.append(source)
            sink_list.append(sink)
        if sum(source_list) == 1 and sum(sink_list) == 1:
            ans.append(1)
        else:
            ans.append(-1)
    print(' '.join(str(x) for x in ans))               
# sc()
