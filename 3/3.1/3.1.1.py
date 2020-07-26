def gsd(_list):
    if len(_list) >= 2:
        first = _list.pop()
        second = _list.pop()
        while first and second:
            if first > second:
                first %= second
            else:
                second %= first
        st = set(_list)
        st.add(first + second)
        return gsd(sorted(st))
    else:
        return _list[0]


st = set()

while True:
    n = int(input())
    if n == 0:
        break
    st.add(n)

print(gsd(sorted(st)))
