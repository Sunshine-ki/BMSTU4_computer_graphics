from math import fabs


def SignVectorProduct(line1, line2):
    V1 = [line1[2] - line1[0], line1[3] - line1[1]]
    V2 = [line2[2] - line2[0], line2[3] - line2[1]]
    temp = V1[0] * V2[1] - V2[0] * V1[1]
    if fabs(temp) <= 1e-3:
        return
    return 1 if temp > 0 else -1


def IsConvex(polygon):
    for temp in polygon:
        if len(temp):
            sign = SignVectorProduct(temp[-1], temp[0])
        for i in range(len(temp) - 1):
            next_sign = SignVectorProduct(temp[i], temp[i + 1])
            if not next_sign:
                continue
            if sign != next_sign:
                return False

    return sign


# def Dot(line1, line2):
#     vector1 = GetVector(line1)
#     vector2 = GetVector(line2)

#     result = float()
#     for i in range(len(vector1)):
#         result += vector1[i] * vector2[i]
#     return result

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
