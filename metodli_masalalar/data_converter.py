class DateConverter:
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k

    def convert_number_to_word(self):
        switcher = {
            0: "nol",
            1: "bir",
            2: "ikki",
            3: "uch",
            4: "to'rt",
            5: "besh",
            6: "olti",
            7: "yetti",
            8: "sakkiz",
            9: "to'qqiz",
        }
        return switcher.get(self.n, "Noto'g'ri raqam")

    def convert_day_to_weekday(self):
        weekdays = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba"]
        return weekdays[self.m - 1] if 1 <= self.m <= 7 else "Noto'g'ri hafta kun"

    def convert_month_to_name(self):
        months = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"]
        return months[self.k - 1] if 1 <= self.k <= 12 else "Noto'g'ri oy nomeri"


if __name__ == "__main__":
    n_value = 4
    m_value = 3
    k_value = 12
    date_obj = DateConverter(n_value, m_value, k_value)
    print(f"Raqam {n_value} so'zi bilan: {date_obj.convert_number_to_word()}")
    print(f"Haftaning {m_value} kuni: {date_obj.convert_day_to_weekday()}")
    print(f"Oy nomeri {k_value} oy nomi: {date_obj.convert_month_to_name()}")

# count_number = print(len(set(input("Son kiriting vergul bilan: ").split(","))))
