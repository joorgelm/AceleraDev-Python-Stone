from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    WORKLOAD = 8

    def __init__(self, code, name, salary) -> None:
        self.code = code
        self.name = name
        self.salary = salary
        self.__departament = None

    @abstractmethod
    def set_departament(self, departament: Department) -> None:
        self.__departament = departament

    @abstractmethod
    def get_departament(self) -> Department:
        return self.__departament

    @abstractmethod
    def calc_bonus(self):
        pass

    @staticmethod
    def get_hours():
        return Employee.WORKLOAD


class Manager(Employee):

    def __init__(self, code, name, salary) -> None:
        super().__init__(code, name, salary)
        super().set_departament(Department('managers', 1))

    def set_departament(self, departament: str) -> None:
        super().set_departament(Department(departament, 1))

    def get_departament(self) -> str:
        return super().get_departament().name

    def calc_bonus(self) -> float:
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary) -> None:
        super().__init__(code, name, salary)
        super().set_departament(Department('sellers', 2))
        self.__sales = 0

    def set_departament(self, departament: str) -> None:
        super().set_departament(Department(departament, 2))

    def get_departament(self) -> str:
        return super().get_departament().name

    def get_sales(self) -> float:
        return self.__sales

    def put_sales(self, sale_value: float) -> None:
        self.__sales += sale_value

    def calc_bonus(self) -> float:
        return self.__sales * 0.15
