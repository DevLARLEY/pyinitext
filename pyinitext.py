import base64
import binascii
import re
from itertools import zip_longest


# Extract pssh/key ids from init.mp4

def swap_endian(x):
    return ''.join(str(x) for x in list(reversed([b + j for b, j in zip_longest(x[::2], x[1::2], fillvalue='0')])))


def hex_to_ascii(x):
    return bytes.fromhex(x.replace("00", "")).decode("utf-8")


def ext(file) -> list:
    rt = []
    with open(file, "rb") as f:
        c = f.read()
    heX = binascii.hexlify(c).decode("utf-8")
    pssh = [m.start() for m in re.finditer("70737368", heX)]
    res = []
    for r in pssh:
        sysid = heX[r + 16:r + 48]
        if sysid == "edef8ba979d64acea3c827dcd51d21ed":
            s = int(heX[r - 8:r], 16) * 2
            if s < 100:
                continue
            f = heX[r + 56:r + 56 + s - 64]
            t = [heX[r - 8:r - 8 + s]]
            p = 0
            while p < len(f):
                h = f[p:p + 2]
                if h == "08":
                    p += 4
                elif h == "48":
                    p += 12
                else:
                    s2 = int(f[p + 2:p + 4], 16) * 2
                    if h == "12":
                        t.append(f[p + 4:p + 4 + s2])
                    p += s2 + 4
            res.append(t)
        elif sysid == "9a04f07998404286ab92e65be0885f95":
            s = int(heX[r - 8:r], 16) * 2
            if s < 90:
                continue
            os = int(swap_endian(heX[r + 56:r + 56 + 8]), 16) * 2
            obj = heX[r + 64:r + 64 + os - 8]
            t = [heX[r - 8:r - 8 + s]]
            p = 4
            for i in range(int(swap_endian(obj[:4]), 16)):
                s2 = int(swap_endian(obj[p + 4:p + 8]), 16) * 2
                typ = int(swap_endian(obj[p:p + 4]), 16)
                if typ == 1:
                    ms = re.findall('<KID ALGID=".{6}" VALUE=".{24}">', hex_to_ascii(obj[p + 12:p + 8 + s2]))
                    for m in ms:
                        t.append(base64.b64decode(m[27:51]).hex())
                p += s2 + 8
            res.append(t)
    for r in res:
        if len(r) >= 2:
            r[0] = base64.b64encode(bytes.fromhex(r[0])).decode()
            rt.append(r)
    return rt


if __name__ == '__main__':
    file = input("init.mp4 file ~: ")
    rs = ext(file.replace('"', ''))
    if len(rs) > 0:
        for r in rs:
            print(f"PSSH (Base64): {r[0]}")
            for i in range(1, len(r)):
                print(f"   |=> Key ID: {r[i]}")
    else:
        print("No pssh found that contains a key id.")
