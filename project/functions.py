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


def array2(paso, MC, CL1, CL2, CL3, CL4, n, ES, maqServer, maqCola):
    paso = paso
    maqCola = maqCola
    maqServer = maqServer
    n = 0
    ES = 0
    MC = 0

    collection = [
        paso, MC, CL1, CL2, CL3, CL4, n, ES, maqServer, maqCola]
    return collection


def returnData(collection):
    for i in range(len(collection)):
        aux = collection[i]
        return aux


# def ValidationOfData(dataCollection, DataMinimun):
#     Out1 = 1001
#     Out2 = 1002
#     Out3 = 1003
#     Out4 = 1004
#     AuxSever = 1
#     for i in range(0, 4):
#         if DataMinimun == dataCollection[2]:
#             dataCollection[1] = DataMinimun
#             dataCollection[2] = Out1
#             dataCollection[5] = dataCollection[1] + 5
#             dataCollection[6] = 1
#             dataCollection[7] = 1
#             dataCollection[8] = AuxSever
#             return dataCollection
