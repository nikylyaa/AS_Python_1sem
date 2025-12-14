def Simm(S):
    if len(S) <= 1:
        return True
    if S[0] != S[-1]:
        return False
    return Simm
text = "radar" #ввод любого слова
if Simm(text):
    print("Строка симметрична")
else:
    print("Строка несимметрична")
