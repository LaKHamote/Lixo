from math import sqrt

def div(A, a, B, b):
    '''https://edisciplinas.usp.br/pluginfile.php/1375560/mod_resource/content/1/Apos_erros.pdf'''
    print (f'{A/B:.5f}  { ((A/B)*(a/A + b/B)):.5f}')


def div_sqrt(A, a, B, b):
    '''http://www.fis.uc.pt/data/20102011/apontamentos/apnt_5_10.pdf  --> pg 5'''

    print(f'{A/B:.5f}  { A/B * sqrt((a/A)**2 + (b/B)**2):.5f}')



def div_derivada(A,a,B,b):
    '''http://www.fis.uc.pt/data/20102011/apontamentos/apnt_5_10.pdf  --> pg 7
        tbm tem no arquivo do Enzo'''
    print(f'{A/B:.5f}  { (a/B + (A*b)/(B**2)):.5f}')




x = [   (9.90,	0.20),
        (14.0	,0.20),
        (17.4	,0.40),
        (20.1	,0.40),
        (22.4	,0.40),
        (24.7	,0.50),
        (26.4	,0.60)
    ]

# for i in x:
#     div(i[0], i[1],10, 0)
#     div_sqrt(i[0], i[1], 10, 0)
#     div_derivada(i[0], i[1], 10, 0)

div(6.284, 0.001, 2.001, 0.005)
div_sqrt(6.284, 0.001, 2.001, 0.005)
div_derivada(6.284, 0.001, 2.001, 0.005)




