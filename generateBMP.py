def readbyte(file):
    result = file.read(1)
    result = round((int(result)) * 25.5)
    return result


with open("result.bmp", "wb") as img:
    with open("pi-billion.txt") as f:
        f.read(2)
        i = 0
        while True:
            if i == 750000:
                break
            r = readbyte(f)
            img.write(r.to_bytes(1, 'big'))
            g = readbyte(f)
            img.write(g.to_bytes(1, 'big'))
            b = readbyte(f)
            img.write(b.to_bytes(1, 'big'))

            i += 1
