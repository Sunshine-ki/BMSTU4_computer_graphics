def SignVectorProduct(line1, line2):
    V1 = [line1[2] - line1[0], line1[3] - line1[1]]
    V2 = [line2[2] - line2[0], line2[3] - line2[1]]
    return 1 if (V1[0] * V2[1] - V2[0] * V1[1]) > 0 else -1


def IsConvex(polygon):
    for temp in polygon:
        if len(temp):
            sign = SignVectorProduct(temp[-1], temp[0])
        for i in range(len(temp) - 1):
            if sign != SignVectorProduct(temp[i], temp[i + 1]):
                return False

    return sign

# def Length(vector1):
#     length = float()
#     for i in range(len(vector1)):
#         length += vector1[i] * vector1[i]
#     return sqrt(length)


# def DotProduct(vector1, vector2):
#     result = float()
#     for i in range(len(vector1)):
#         result += vector1[i] * vector2[i]
#     return result


# def Angle(line1, line2):
#     vector1 = [line1[2] - line1[0], line1[3] - line1[1]]
#     vector2 = [line2[2] - line2[0], line2[3] - line2[1]]
#     return acos(DotProduct(vector1, vector2) / Length(vector1) / Length(vector2)) * 180 / pi
