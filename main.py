import re


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, birth_day: tuple):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._birth_day = birth_day

    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value: tuple):
        if len(value) == 3 and all(isinstance(i, int) for i in value):
            self._birth_day = value
        else:
            raise ValueError("birth_day uchta butun sondan iborat bo'lishi kerak (day, month, year)")

    def get_info(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nBirth Day: {self.birth_day}"

    def get_life_path_number(self):
        day, month, year = self.birth_day
        day_sum = sum(int(digit) for digit in str(day))
        month_sum = sum(int(digit) for digit in str(month))
        year_sum = sum(int(digit) for digit in str(year))

        total_sum = day_sum + month_sum + year_sum

        while total_sum >= 10:
            total_sum = sum(int(digit) for digit in str(total_sum))

        return total_sum

    def get_info_by_number(self, number):
        with open('numerology_advice.txt', 'r') as file:
            content = file.read()
            pattern = re.compile(r'#' + str(number) + r'\s*(.*?)(?=\n#|$)', re.DOTALL)
            match = pattern.search(content)
            if match:
                return match.group(1).strip()
            else:
                return "Bu raqam uchun hech qanday maslahat topilmadi."


# Function to interact with the user and create a Person object
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    birth_day = tuple(map(int, input(" Tug'ilgan kuningizni (day, month, year) vergul bilan ajrating: ").split(',')))

    person = Person(first_name, last_name, age, email, birth_day)

    print("\nPerson Information:")
    print(person.get_info())

    life_path_number = person.get_life_path_number()
    print(f"\nSizning hayot yo'lingiz raqamingiz: {life_path_number}")

    advice = person.get_info_by_number(life_path_number)
    print(f"\nSizning hayot yo'lingiz soniga asoslangan psixologik maslahat: {advice}")


if __name__ == "__main__":
    main()
