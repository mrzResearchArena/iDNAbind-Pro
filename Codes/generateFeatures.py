import itertools
import numpy as np

trackingFeatures = []

def gF(args, X, Y):

    elements = 'ACDEFGHIKLMNPQRSTVWY'

    m2 = list(itertools.product(elements, repeat=2))
    m3 = list(itertools.product(elements, repeat=3))
    m4 = list(itertools.product(elements, repeat=4))
    m5 = list(itertools.product(elements, repeat=5))

    T = []  # All instance ...

    def kmers(seq, k):
        v = []
        for i in range(len(seq) - k + 1):
            v.append(seq[i:i + k])
        return v

    def pseudoKNC(x, k):
        ### k-mer ###
        ### A, AA, AAA

        for i in range(1, k + 1, 1):
            v = list(itertools.product(elements, repeat=i))
            # seqLength = len(x) - i + 1
            for i in v:
                # print(x.count(''.join(i)), end=',')
                t.append(x.count(''.join(i)))
        ### --- ###
        
    
    def monoMonoKGap(x, g):  # 1___1
        ### g-gap
        '''
        AA      0-gap (2-mer)
        A_A     1-gap
        A__A    2-gap
        A___A   3-gap
        A____A  4-gap
        '''

        m = m2
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 2)
            # seqLength = len(x) - (i+2) + 1
            #
            for gGap in m:
                # print(gGap[0], end='')
                # print('-'*i, end='')
                # print(gGap[1])
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-1] == gGap[1]:
                        C += 1
                # print(C, end=',')
                t.append(C)


        ### --- ###

    def monoDiKGap(x, g):  # 1___2

        m = m3
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 3)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print('-' * i, end='')
                # print(gGap[1], end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1] + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-2] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def diMonoKGap(x, g):  # 2___1

        m = m3
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 3)
            # seqLength = len(x) - (i+2) + 1

            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print('-'*i, end='')
                # print(gGap[2], end=' ')
                # trackingFeatures.append(gGap[0] + gGap[1] + '-' * i + gGap[2])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[-1] == gGap[2]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def monoTriKGap(x, g):  # 1___3

        # A_AAA       1-gap
        # A__AAA      2-gap
        # A___AAA     3-gap
        # A____AAA    4-gap
        # A_____AAA   5-gap upto g

        m = m4
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 4)
            # seqLength = len(x) - (i+2) + 1

            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print('-' * i, end='')
                # print(gGap[1], end='')
                # print(gGap[2], end=' ')
                # print(gGap[3], end=' ')
                # trackingFeatures.append(gGap[0] + '-' * i + gGap[1] + gGap[2] + gGap[3])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[-3] == gGap[1] and v[-2] == gGap[2] and v[-1] == gGap[3]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def triMonoKGap(x, g):  # 3___1

        # AAA_A       1-gap
        # AAA__A      2-gap
        # AAA___A     3-gap
        # AAA____A    4-gap
        # AAA_____A   5-gap upto g

        m = m4
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 4)
            # seqLength = len(x) - (i+2) + 1

            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print(gGap[2], end='')
                # print('-'*i, end='')
                # print(gGap[3], end=' ')
                # trackingFeatures.append(gGap[0] + gGap[1] + gGap[2] + '-' * i + gGap[3])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[2] == gGap[2] and v[-1] == gGap[3]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def diDiKGap(x, g):

        ### gapping ### total = [(64xg)] = 2,304 [g=9]
        # AA_AA       1-gap
        # AA__AA      2-gap
        # AA___AA     3-gap
        # AA____AA    4-gap
        # AA_____AA   5-gap upto g

        m = m4
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 4)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print('-'*i, end='')
                # print(gGap[2], end='')
                # print(gGap[3], end='')
                # trackingFeatures.append(gGap[0] + gGap[1] + '-' * i + gGap[2] + gGap[3])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[-2] == gGap[2] and v[-1] == gGap[3]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def diTriKGap(x, g):  # 2___3

        ### gapping ### total = [(64xg)] = 2,304 [g=9]
        # AA_AAA       1-gap
        # AA__AAA      2-gap
        # AA___AAA     3-gap
        # AA____AAA    4-gap
        # AA_____AAA   5-gap upto g

        m = m5
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 5)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print('-' * i, end='')
                # print(gGap[2], end='')
                # print(gGap[3], end='')
                # print(gGap[4], end='')
                # trackingFeatures.append(gGap[0] + gGap[1] + '-' * i + gGap[2]  + gGap[3] + gGap[4])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[-3] == gGap[2] and v[-2] == gGap[3] and v[-1] == gGap[4]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def triDiKGap(x, g):  # 3___2

        ### gapping ### total = [(64xg)] = 2,304 [g=9]
        # AAA_AA       1-gap
        # AAA__AA      2-gap
        # AAA___AA     3-gap
        # AAA____AA    4-gap
        # AAA_____AA   5-gap upto g

        m = m5
        for i in range(1, g + 1, 1):
            V = kmers(x, i + 5)
            # seqLength = len(x) - (i+2) + 1
            # print(V)
            for gGap in m:
                # print(gGap[0], end='')
                # print(gGap[1], end='')
                # print(gGap[2], end='')
                # print('-'*i, end='')
                # print(gGap[3], end='')
                # print(gGap[4], end='')
                # trackingFeatures.append(gGap[0] + gGap[1] + gGap[2] + '-' * i + gGap[3] + gGap[4])

                C = 0
                for v in V:
                    if v[0] == gGap[0] and v[1] == gGap[1] and v[2] == gGap[2] and v[-2] == gGap[3] and v[-1] == gGap[4]:
                        C += 1
                # print(C, end=',')
                t.append(C)

        ### --- ###

    def generateFeatures(kGap, kTuple, x, y):

        ##############################################################
        if args.pseudoKNC == 1:
            pseudoKNC(x, kTuple)

        ##############################################################

        ##############################################################

        if args.monoMono == 1:
            monoMonoKGap(x, kGap)      #20*(k)*20

        if args.monoDi == 1:
            monoDiKGap(x, kGap)        #20*k*(20^2)

        if args.monoTri == 1:
            monoTriKGap(x, kGap)       #20*k*(20^3)

        ###
        ###

        if args.diMono == 1:
            diMonoKGap(x, kGap)        #(20^2)*k*(20)

        if args.diDi == 1:
            diDiKGap(x, kGap)          #(20^2)*k*(20^2)

        if args.diTri == 1:
            diTriKGap(x, kGap)         #(20^2)*k*(20^3)

        ###
        ###

        if args.triMono == 1:
            triMonoKGap(x, kGap)       #(20^3)*k*(20)

        if args.triDi == 1:
            triDiKGap(x, kGap)         #(20^3)*k*(20^2)


        ##############################################################

        t.append(y)
        #######################


    for x, y in zip(X, Y):
        t = []
        generateFeatures(args.kGap, args.kTuple, x, y)
        T.append(t)
        ### --- ###

    ############################

    return np.array(T)


