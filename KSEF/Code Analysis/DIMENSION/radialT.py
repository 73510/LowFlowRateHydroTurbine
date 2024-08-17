#radial documentation and calculation

CRAtoFRA = 60
FRAtoFPS = 25
thickness = 3

lagwidth_center = 26.5

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