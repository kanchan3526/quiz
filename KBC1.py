print("****Welcome To kon banega Karodpati in python😁****")
print("1)start\n2)End")
n = int(input("Enter 1 or 2:"))
match n:
    case 1:
        print("Start Game🤩\n")
        print("Aur ye pahla sawal apki  screen par...⛳")
        questions = [
            {
                "question": "1)python is... languge",
                "option": [
                    "A.binary ",
                    "B.high level",
                    "C.medium level",
                    "D.low level",
                ],
                "answer": "B",
            },
            {
                "question": "2)Who Developed Python Language?",
                "option": [
                    "A.Bajarne Strostroup",
                    "B.james gosling",
                    "C.Guido  van Rossum",
                    "D.Travis Oliphant",
                ],
                "answer": "C",
            },
            {
                "question": "3)Which is not part of oop's concept?",
                "option": [
                    "A.Inheritance",
                    "B.polymorphism",
                    "C.method overloading",
                    "D.pointer",
                ],
                "answer": "D",
            },
            {
                "question": "4)which language does not support multiple inheritance with class?",
                "option": ["A.python", "B.java", "C.C++", "D.C"],
                "answer": "B",
            },
            {
                "question": "5)Basic Syntax of Docstring?",
                "option": ["A).__doc__", "B)__doc__", "C).--doc--", "D)._doc_"],
                "answer": "A",
            },
            {
                "question": "6)what is PEP8?",
                "option": [
                    "A.python library",
                    "B.python function",
                    "C.zen of python",
                    "D.python module",
                ],
                "answer": "C",
            },
            {
                "question": "7)Which module is used  to perform methematical and statistical operation in python?",
                "option": ["A.random", "B.statistics", "C.numpy", "D.pandas"],
                "answer": "C",
            },
            {
                "question": "8)which keyword is used to declare function in python?",
                "option": ["A.def", "B.Def", "C.function", "D.def()"],
                "answer": "A",
            },
            {
                "question": "9)which language store diffrent type of data in list?",
                "option": ["A.python", "B.C#", "C.Cpp", "D.All of the above"],
                "answer": "A",
            },
            {
                "question": "10)To find the length which function is used?",
                "option": ["A.Len()", "B.lenght()", "C.Lenght()", "D.len()"],
                "answer": "D",
            },
        ]
        score = 0
        for q in questions:
            print("\n" + q["question"])
            for option in q["option"]:
                print(option)
            ans = input("Answer(A/B/C/D):").upper()
            if ans == q["answer"]:
                print("\nsahi jawab❤️!")
                score += 1000
            else:
                print("\nGalat jawab😔!")
        print("\nApp jit gaye ho pure", score, "rupey😀")
        print("Congratulations dear🥳🏆")
    case 2:
        print("\nGame End...🙂")
    case _:
        print("\nPlease Enter 1 or 2.🤨")
