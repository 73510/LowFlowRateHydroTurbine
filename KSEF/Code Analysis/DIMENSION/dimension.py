gearAT = 10
s = 2
stand1 = 10
stand2 = 10
AB = 22
LAG_2 = 12 + 3*2
FLAP = 150
FC = 5

CRAtoFRA = 60
FRAtoFPS = 25
thickness = 3

lagwidth_center = 26.5

for axialparts in range(1) : 
    

    CRA_L = gearAT + s + stand1 + AB + s + LAG_2 + s + FC + s + FLAP +s + FC + s + LAG_2 + s + AB + stand2

    외곽봉길이 = stand1 + AB + s + LAG_2 + s + FC + s + FLAP +s + FC + s + LAG_2 + s + AB + stand2

    FRA = FC + s + FLAP +s + FC

    FPS = LAG_2 + s + FC + s + FLAP +s + FC + s + LAG_2

    b_ala_s = s + LAG_2/2

    print("CRA_L : ", CRA_L)
    print("외곽봉길이 : ", 외곽봉길이)
    print("FRA : ", FRA )
    print("FPS : ", FPS)

    print("distancing______....")

    print("b_ala_s : ", b_ala_s)

print("\n\n radial\n\n")
for radialparts in range(1) :
    #radial documentation and calculation

    

    자석두께 = 3
    mag_margin = 0.25 #single sided 0.25, total 0.5

    #20 * 10 * 3
    mag_holdermargin  = 1.5#singlesided 1.5

    자석구멍두께 = mag_margin*2 + 자석두께
    LAGradialT = lagwidth_center + 자석구멍두께 + mag_holdermargin*2

    LAG존재범위min = CRAtoFRA - FRAtoFPS- LAGradialT/2
    LAG존재범위max = CRAtoFRA + FRAtoFPS+ LAGradialT/2

    LAGcentermax = CRAtoFRA - FRAtoFPS
    LAGcentermin = CRAtoFRA - FRAtoFPS


    print("LAGradialT : ", LAGradialT)

    print("LAG존재영역 : ", LAG존재범위min, LAG존재범위max)

    print("ABwidthfromoLAG : ", lagwidth_center - 자석구멍두께 - mag_holdermargin*2)