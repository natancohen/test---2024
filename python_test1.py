# Total_numbers_taken = 0
# positive_numbers = 0
# Same_numbers = 0
# a = int(input("Enter 2 whole numbers:"))
# b = int(input("Enter 2 whole numbers:"))
# while not a + b == 0:
#     Total_numbers_taken += 2
#     positive_numbers += a if a > 0 else 0
#     positive_numbers += b if b > 0 else 0
#     Same_numbers += 1 if a == b else 0
#     a = int(input("Enter 2 whole numbers:"))
#     b = int(input("Enter 2 whole numbers:"))
# print(Total_numbers_taken)
# print(positive_numbers)
# print(Same_numbers)


# def Is_array_triangular(a):
#     if not len(a) % 3 == 0:
#         return False
#     n = len(a) // 3
#     first_slice = a[:n]  # [1,2]
#     mid_slice = a[n: n * 2]
#     last_slice = a[n * 2:]
#     if first_slice == mid_slice == last_slice:
#         for index in a:
#             if isinstance(index, int):
#                 return True
#             else:
#                 return False
#     else:
#         return False
# print(Is_array_triangular([1, 2, 3, 1, 2, 3, 1, 2, 3]))
# print(Is_array_triangular([1, 2, 1, 2, 1, 2]))


# def is_array_triangular(a):
#     if len(a) % 3 != 0:
#         return False
#     n = len(a) // 3
#     for i in range(n):
#         if a[i] != a[i + n] or a[i] != a[i + 2 * n]:
#             return False
#     return True
#
#
# print(is_array_triangular([1, 2, 3, 1, 2, 3, 1, 2, 3]))
# print(is_array_triangular([1, 2, 1, 2, 1, 2]))


# class Song:
#     def __init__(self, name, performer, length):
#         self.name = name
#         self.performer = performer
#         self.length = length
#
#     def __str__(self):
#         return f"name = {self.name}, performer = {self.performer}, length = {self.length}"
#
#     def status(self):
#         return (f"{self.name}/{self.performer}:{self.length}")
#
#
# song1 = Song("Ququ", "Buko", 120)
# song2 = Song("yama", "beny", 20)
# song3 = Song("nekuda", "shily", 6)
# print(song1.status())
# print(song2.status())


# class Disk:
#     def __init__(self, disk_name, songs):
#         self.disk_name = disk_name
#         self.songs = songs
#
#     def __str__(self):
#         return f"disk_name = {self.disk_name}, songs = {self.songs}"
#
#     def exist(self, n_song, p_song):
#         for song in self.songs:
#             if n_song == song.name and p_song == song.performer:
#                 return True
#         return False


# def large_disk_name(d1, d2):
#     if len(disk1.songs) > len(disk2.songs):
#         return disk1.disk_name
#     else:
#         return disk2.disk_name
#
#
# disk1 = Disk("disk1", [song1, song2])
# disk2 = Disk("disk2", [song1, song2, song3])
# print(disk1.exist("yama", "beny"))
# print(large_disk_name("disk1", "disk2"))


class Student:
    def __init__(self, id, arr_grades_a, arr_grades_b):
        self.id = id
        self.arr_grades_a = arr_grades_a
        self.arr_grades_b = arr_grades_b

    def __str__(self):
        return f"id = {self.id}, arr_grades_a = {self.arr_grades_a}, arr_grades_b = {self.arr_grades_b}"

    def is_improved(self):
        counter = 0
        for index in range(len(self.arr_grades_a)):

            if not self.arr_grades_b[index] >= self.arr_grades_a[index]:
                if self.arr_grades_a[index] == -1 or self.arr_grades_b[index] == -1:
                    continue
                counter += 1
                return False

            if counter >= 5:
                return False
        return True


# student1 = Student(1234, [-1, 60, -1, 60, 90], [50, -1, 60, -1, 95])
# student2 = Student(5678, [20, 50, 70, 80, 90], [40, 50, 70, 74, 90])
# student3 = Student(9101, [45, 55, 60, 65, 70], [50, 55, 65, 70, 90])
# students = [student1, student2, student3]
# print(student1.is_improved())
# print(student2.is_improved())
# print(student3.is_improved())


# def is_student_improved(a):
#     students_improve = []
#     for student in students:
#         if Student.is_improved():
#             students_improve.append(student.id)
#         else:
#             return "None"
#     return students_improve
#
#
# print(is_student_improved(students))


# class Student:
#     def __init__(self, id, arr_grades_a, arr_grades_b):
#         self.id = id
#         self.arr_grades_a = arr_grades_a
#         self.arr_grades_b = arr_grades_b
#
#     def __str__(self):
#         return f"id = {self.id}, arr_grades_a = {self.arr_grades_a}, arr_grades_b = {self.arr_grades_b}"
#
#     def is_improved(self):
#         counter = 0
#         for index in range(len(self.arr_grades_a)):
#             if self.arr_grades_a[index] == -1 or self.arr_grades_b[index] == -1:
#                 continue
#             if not self.arr_grades_b[index] >= self.arr_grades_a[index]:
#                 counter += 1
#                 if counter >= 5:
#                     return False
#         return True
#
# student1 = Student(1234, [-1, 60, -1, 60, 90], [50, -1, 60, -1, 95])
# student2 = Student(5678, [20, 50, 70, 80, 90], [40, 50, 70, 74, 90])
# student3 = Student(9101, [45, 55, 60, 65, 70], [50, 55, 65, 70, 90])
# students = [student1, student2, student3]
#
# print(student1.is_improved())  # אמור להחזיר True
# print(student2.is_improved())  # אמור להחזיר True
# print(student3.is_improved())  # אמור להחזיר True
#
#
# def is_student_improved(students):
#     students_improve = []
#     for student in students:
#         if not student.is_improved():
#             return None
#         else:
#             students_improve.append(student.id)
#     return students_improve
#
#
# print(is_student_improved(students))  # אמור להחזיר רשימה של מזהי הסטודנטים שהשתפרו


def what(s1, s2):
    if len(s1) != len(s2):
        print(s1, s2)
        return False

    if len(s1) == 0:
        return True

    place = s2.find(s1[0])
    if place < 0:
        print(s1, s2)
        print(len(s1))
        print(len(s2))
        return False

    else:
        a = s2[:place]
        b = s2[place + 1:]
        c = a + b
        return what(s1[1:], c)


print(what("hello", "oeloh"))

