from tkinter import *


def get_year_average(array_of_entries):
    total = 0
    try:
        for number in array_of_entries:
            total += int(number.get())
    except ValueError:
        print('ValueError')
        return 0
    return round(total / len(array_of_entries), 2)


def calculate_grade(first_year_average, second_year_average, third_year_average):
    total = first_year_average + (second_year_average * 3) + (third_year_average * 5)
    return round(total / 9, 2)


def degree_classification(final_grade):
    if final_grade >= 70:
        return "1st"
    elif final_grade >= 60:
        return "2.1"
    elif final_grade >= 50:
        return "2.2"
    elif final_grade >= 40:
        return "3rd"
    else:
        return "Fail"


def calculate_grade_and_classification(event):
    year1average = get_year_average(year1Entries)
    year2average = get_year_average(year2Entries)
    year3average = get_year_average(year3Entries)

    grade = calculate_grade(year1average, year2average, year3average)
    classification = degree_classification(grade)

    year1score_label.set(year1average)
    year2score_label.set(year2average)
    year3score_label.set(year3average)
    grade_label.set(grade)
    classification_label.set(classification)


root = Tk()
root.title("My Uni Grades Calculator")

boldFont = ("Helvetica", 16, "bold")

# creating the 4 main containers
top_frame = Frame(root, bg='#E67E22', width=200, pady=5, padx=5)
center_frame = Frame(root, bg='#E67E22', width=200)
info_frame = Frame(root, bg='gray', width=200, height=100, pady=20, padx=10)
btm_frame = Frame(root, bg='#E67E22', width=200, pady=5)

# adding the 4 main containers to the root
top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="nsew")
info_frame.grid(row=2, sticky="ew")
btm_frame.grid(row=3, sticky="ew")

# adding the main title to the top frame
mainTitle = Label(top_frame, text="Welcome to My Uni Grades Calculator", fg="red", font=("Helvetica", 20, "bold"))
message = Label(top_frame, text="Enter your marks in each of the following modules then " +
                                "click submit to find out your final grade and degree classification")
mainTitle.pack(expand=YES, fill=X)
message.pack(expand=YES, fill=X)

# creating the 3 middle vertical containers
firstYearPanel = Frame(center_frame, bg='#5499C7', padx=30, pady=10)
secondYearPanel = Frame(center_frame, bg='#F4D03F', padx=30, pady=10)
thirdYearPanel = Frame(center_frame, bg='#2ECC71', padx=30, pady=10)

# adding the 3 middle containers to the centre frame
firstYearPanel.grid(row=0, column=0, sticky="ns")
secondYearPanel.grid(row=0, column=1, sticky="nsew")
thirdYearPanel.grid(row=0, column=2, sticky="ns")

# adding the title, labels and entries in the year 1 container
year1Title = Label(firstYearPanel, text="Year 1 Modules", font=boldFont)
year1Title.grid(row=0, column=0, columnspan=2, pady=10)
year1Entries = []
for index in range(1, 8):
    label = Label(firstYearPanel, text='Module ' + str(index) + " (15 credits)")
    entry = Entry(firstYearPanel, width=6, justify='center')
    year1Entries.append(entry)
    label.grid(row=index, column=0, pady=7)
    entry.grid(row=index, column=1, pady=7)
year1score_label = StringVar()
Label(firstYearPanel, text="Year Average:", font=boldFont).grid(row=8, column=0, pady=7, padx=7)
Label(firstYearPanel, textvariable=year1score_label, font=boldFont).grid(row=8, column=1, pady=7, padx=7)

# adding the title, labels and entries in the year 2 container
year2Title = Label(secondYearPanel, text="Year 2 Modules", font=boldFont)
year2Title.grid(row=0, column=0, columnspan=2, pady=10)
year2Entries = []
for index in range(1, 8):
    label = Label(secondYearPanel, text='Module ' + str(index) + " (15 credits)")
    entry = Entry(secondYearPanel, width=6, justify='center')
    year2Entries.append(entry)
    label.grid(row=index, column=0, pady=7)
    entry.grid(row=index, column=1, pady=7)
year2score_label = StringVar()
Label(secondYearPanel, text="Year Average:", font=boldFont).grid(row=8, column=0, pady=7, padx=7)
Label(secondYearPanel, textvariable=year2score_label, font=boldFont).grid(row=8, column=1, pady=7, padx=7)

# adding the title, labels and entries in the year 3 container
year3Title = Label(thirdYearPanel, text="Year 3 Modules", font=boldFont)
year3Title.grid(row=0, column=0, columnspan=2, pady=10)
year3Entries = []
for index in range(1, 8):
    label = Label(thirdYearPanel, text='Module ' + str(index) + " (15 credits)")
    entry = Entry(thirdYearPanel, width=6, justify='center')
    year3Entries.append(entry)
    label.grid(row=index, column=0, pady=7)
    entry.grid(row=index, column=1, pady=7)
year3score_label = StringVar()
Label(thirdYearPanel, text="Year Average:", font=boldFont).grid(row=8, column=0, pady=7, padx=7)
Label(thirdYearPanel, textvariable=year3score_label, font=boldFont).grid(row=8, column=1, pady=7, padx=7)


# add information label to the info container
info_label_text = StringVar()
info_label_text.set('No information available.')
information = Label(info_frame, text="INFO:", font=boldFont, anchor="w")
info_label = Label(info_frame, textvariable=info_label_text, wraplength=800, anchor="w")
information.pack(expand=YES, fill=X)
info_label.pack(expand=YES, fill=X)


# creating 2 containers for the result labels and submit button
resultsPanel = Frame(btm_frame, bg='#E74C3C', height=250, padx=20, pady=10)
buttonPanel = Frame(btm_frame, bg='#E74C3C', height=250, padx=30, pady=10)

# adding the 2 containers to the bottom frame
buttonPanel.pack(side=RIGHT)
resultsPanel.pack(side=RIGHT, fill=BOTH, expand=YES)

# mock data
grade_label = StringVar()
classification_label = StringVar()

# adding labels and submit button to their containers
Label(resultsPanel, text='Final Grade', font=boldFont).grid(row=0, column=0, pady=5, padx=5, sticky="E")
Label(resultsPanel, text='Degree Classification', font=boldFont).grid(row=1, column=0, pady=5, padx=5, sticky="E")
Label(resultsPanel, textvariable=grade_label, font=boldFont).grid(row=0, column=1, pady=5, padx=5, sticky="W")
Label(resultsPanel, textvariable=classification_label, font=boldFont).grid(row=1, column=1, pady=5, padx=5, sticky="W")
Label(resultsPanel, text="Note the weight of the modules of each year is higher than\n" +
                         "the weight of previous years' modules and that the ratio is \n" +
                         "1st-year : 2nd-year : 3rd-year \n1 : 3 : 5") \
    .grid(row=0, column=2, columnspan=2, rowspan=2, pady=5, padx=5, sticky="W")

submitButton = Button(buttonPanel, text='Submit')
submitButton.grid(row=0, column=0)
submitButton.bind("<Button-1>", calculate_grade_and_classification)

root.mainloop()
