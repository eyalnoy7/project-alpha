print("היי מה שלומך? אשמח לקעקע אותך מה חשבת לקעקע?")

customer_name = input("איך קוראים לך? ")
customer_phone = input("מה מספר הטלפון שלך? ")
tattoo_idea = input("איזה קעקוע תרצה לעשות? ")
body_location = input("באיזה אזור בגוף? ")
first_tattoo = input("האם זה הקעקוע הראשון שלך? (כן/לא) ")

print("===================================")
print("סיכום פרטי הלקוח")
print("===================================")
print("שם:", customer_name)
print("טלפון:", customer_phone)
print("רעיון לקעקוע:", tattoo_idea)
print("אזור בגוף:", body_location)
print("קעקוע ראשון:", first_tattoo)
print("===================================")

if first_tattoo == "כן":
    print("מדהים! נסביר לך את כל התהליך.")
else:
    print("כיף שחזרת להתקעקע אצלי!")
