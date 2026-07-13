def welcome():
    print("היי, מה נשמע? 😊")
    print("ראיתי שהתעניינת בקעקוע ורציתי להבין קצת יותר מה הכיוון שלך.")
    print("יש לך כבר רעיון, סגנון או אזור בגוף שחשבת עליו?")
    print("אפשר לשלוח לי גם תמונות השראה, ומשם אכוון אותך בצורה הכי מדויקת.")

welcome()
def collect_customer_info ():
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
        collect_customer_info
        
        print(f"\nנעים מאוד {customer_name}! 😊")
print("תודה שענית על כל השאלות.")
print("אני אעבור על כל הפרטים ואחזור אליך עם הכיוון הכי מדויק.")


reference_images = input("יש לך תמונות השראה? (כן/לא) ")

print(f"\nנעים מאוד {customer_name}! 😊")
print("תודה שענית על כל השאלות.")
print("אני אעבור על כל הפרטים ואחזור אליך עם הכיוון הכי מדויק.")

if reference_images == "כן":
    print("מעולה! אפשר לשלוח לי את תמונות ההשראה כאן ואעבור עליהן.")
else:
    print("אין בעיה, נמצא יחד את הכיוון המושלם לקעקוע שלך.")