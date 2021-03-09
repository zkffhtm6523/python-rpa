# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 땐 + 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0: >10}".format(500))
print("{0: >10}".format(500))
print("{0:>10}".format(500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0: <+10}".format(500))

# 3자리 마다 .찍어주기
print("{0:,}".format(1000000000))
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

# 3자리 마다 .찍기 + 부호 + 자릿수 확보
print("{:^<+30,}".format(10000000000000))

# 소수점 출력
print("{:f}".format(5/3))
# 소수점 특정 자리수까지 표시(소수점 3째 자리에서 반올림)
print("{:.2f}".format(5/3))