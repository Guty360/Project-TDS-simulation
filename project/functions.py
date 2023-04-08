from constants import constantes


def MinimumData(CL1, CL2, CL3, CL4):
    MC = 0
    CL1 = CL1
    CL2 = CL2
    CL3 = CL3
    CL4 = CL4
    if (CL1 < CL2):
        if (CL1 < CL3):
            if (CL1 < CL4):
                return CL1
    if (CL2 < CL1):
        if (CL2 < CL3):
            if (CL2 < CL4):
                return CL2
    if (CL3 < CL1):
        if (CL3 < CL2):
            if (CL3 < CL4):
                return CL3
    if (CL4 < CL1):
        if (CL4 < CL2):
            if (CL4 < CL3):
                return CL4


def array2(data, CL1, CL2, CL3, CL4):
    asignacion = 1000
    paso = 0
    n = 0
    ES = 0
    MC = 0
    MinimumData = data

    collection = [
        paso, MC, CL1, CL2, CL3, CL4, n, n, n, n]
    returnData(collection)
    return collection


def returnData(collection):
    print()
