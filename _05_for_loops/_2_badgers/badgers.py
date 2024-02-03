bad = "Badger"
mush = "Mushroom"
verse_1 = ""
verse_2 = ""
end = "A Snake!!!"
for i in range(29):
    if i <= 11:
        verse_1 = verse_1 + bad + ", "
    elif i<=13:
        if i == 13:
            verse_1 = verse_1 + mush
        else:
            verse_1 = verse_1 + mush + ", "
    elif i<=25:
        verse_2 = verse_2 + bad + ", "
    elif i <= 27:
        if i == 27:
            verse_2 = verse_2 + mush
        else:
            verse_2 = verse_2 + mush + ", "
print(verse_1)
print()
print(verse_2)
print()
print(end)

