class DigitRetrieve:

    def __call__(self, string):
        try:
            return int(string)
        except:
            return None


dg = DigitRetrieve()

d1 = dg("123")  # 123 (целое число)
d2 = dg("45.54")  # None (не целое число)
d3 = dg("-56")  # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")  # None (не целое число)


print(d1, d2, d3, d4, d5)

st = ["123", "abc", "-56.4", "0", "-5"]
digits = filter(dg, st) # [123, None, None, 0, -5]

print(*digits)