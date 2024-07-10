def konversi_waktu_12_ke_24(waktu_12):
    periode = waktu_12[-2:]
    waktu = waktu_12[:-2]
    jam, menit = map(int, waktu.split(':'))

    if periode == 'AM' and jam == 12:
        jam = 0
    elif periode == 'PM' and jam != 12:
        jam += 12

    return f"{jam:02}:{menit:02}"

def konversi_waktu_24_ke_12(waktu_24):
    jam, menit = map(int, waktu_24.split(':'))
    periode = 'AM'
    if jam >= 12:
        periode = 'PM'
        if jam > 12:
            jam -= 12
    elif jam == 0:
        jam = 12

    return f"{jam:02}:{menit:02} {periode}"

print(konversi_waktu_12_ke_24('07:45 PM'))
print(konversi_waktu_24_ke_12('19:45'))
