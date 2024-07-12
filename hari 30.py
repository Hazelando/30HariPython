def tentukan_zodiak(hari, bulan):
    zodiak = [
        (20, 'Capricorn'), (19, 'Aquarius'), (20, 'Pisces'), (20, 'Aries'),
        (21, 'Taurus'), (21, 'Gemini'), (22, 'Cancer'), (22, 'Leo'),
        (22, 'Virgo'), (23, 'Libra'), (22, 'Scorpio'), (21, 'Sagittarius'),
        (31, 'Capricorn')
    ]
    if (hari > zodiak[bulan-1][0]):
        return zodiak[bulan][1]
    else:
        return zodiak[bulan-1][1]

print(tentukan_zodiak(15, 1))
print(tentukan_zodiak(25, 6))