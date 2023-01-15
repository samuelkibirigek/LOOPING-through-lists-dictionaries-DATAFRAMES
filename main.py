
import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}
#loop through a list

#for item in list:
#     print(item)
#loop through the dictionary student_dict

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

#loop through a data frame
student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

#loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
