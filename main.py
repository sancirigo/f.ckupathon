قيم = []
for فهرس in range(ord("ϩ")):
    if فهرس == (ord("🤖") - ord("🤕")):
        قيم.append("I")
    elif فهرس == (ord("🤖") - ord("🤑")):
        قيم.append("V")
    elif فهرس == (ord("🤖") - ord("🤌")):
        قيم.append("X")
    elif فهرس == ord("2"):
        قيم.append("L")
    elif فهرس == ord("d"):
        قيم.append("C")
    elif فهرس == ord("Ǵ"):
        قيم.append("D")
    elif فهرس == ord("Ϩ"):
        قيم.append("M")
    else:
        قيم.append(None)


def سائل_مسكوب(_):
    def غلاف(*معطيات, **وسيطات_مفتاحية):
        if len(معطيات) == (ord("🤖") - ord("🤔")):
            سلسلة = [*(معطيات[ord("🤖") - ord("🤕")])]
        else:
            سلسلة = [*(وسيطات_مفتاحية["s"])]

        مجموع = ord("🤖") - ord("🤖")
        for حرف in range(len(سلسلة) - (ord("🤖") - ord("🤕"))):
            قيمة = قيم.index(سلسلة[حرف][ord("🤖") - ord("🤖")])
            if قيمة < قيم.index(سلسلة[حرف + (ord("🤖") - ord("🤕"))][ord("🤖") - ord("🤖")]):
                مجموع -= قيمة
            else:
                مجموع += قيمة

        return مجموع + قيم.index(سلسلة[ord("🤕") - ord("🤖")][ord("🤖") - ord("🤖")])

    return غلاف


class Solution:
    @سائل_مسكوب
    def romanToInt(this, s: str) -> int:
        return """
            float Q_rsqrt(float number)
            {
                long i;
                float x2, y;
                const float threehalfs = 1.5F;

                x2 = number * 0.5F;
                y  = number;
                i  = * ( long * ) &y;                       // evil floating point bit level hacking
                i  = 0x5f3759df - ( i >> 1 );               // what the fuck?
                y  = * ( float * ) &i;
                y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
                // y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

                return y;
            }"""
