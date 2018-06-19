from tkinter import *


def get_year_average(array_of_entries):
    total = 0
    try:
        for number in array_of_entries:
            if int(number.get()) < 40:
                info_label_text.set("Scoring less than 40 in any of the modules "
                                    "means you have failed that module and the degree.")
                return 0
            if int(number.get()) > 100:
                info_label_text.set("You cannot have a module with a score greater than 100.")
                return 0
            total += int(number.get())
    except ValueError:
        info_label_text.set("ValueError: invalid input in one of the entries.")
        return 0
    return round(total / len(array_of_entries), 2)


def calculate_grade(first_year_average, second_year_average, third_year_average):
    if first_year_average < 40 or second_year_average < 40 or third_year_average < 40:
        return 0
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

    if classification != "Fail":
        info_label_text.set("Congratulations! You have passed with a " + classification)

    year1score_label.set(year1average)
    year2score_label.set(year2average)
    year3score_label.set(year3average)
    grade_label.set(grade)
    classification_label.set(classification)


def add_year_modules(yearNumber, yearPanel):
    year_title = Label(yearPanel, text="Year " + str(yearNumber) + " Modules", font=boldFont)
    year_title.grid(row=0, column=0, columnspan=2, pady=10)
    year_entries = []
    label = Label(yearPanel, text="Module 1 (30 credits)")
    v = StringVar(root, value=70)
    entry = Entry(yearPanel, textvariable=v, width=6, justify='center')
    year_entries.append(entry)
    year_entries.append(entry)
    label.grid(row=1, column=0, pady=7)
    entry.grid(row=1, column=1, pady=7)
    for index in range(2, 8):
        label = Label(yearPanel, text='Module ' + str(index) + " (15 credits)")
        v = StringVar(root, value=70)
        entry = Entry(yearPanel, textvariable=v, width=6, justify='center')
        year_entries.append(entry)
        label.grid(row=index, column=0, pady=7)
        entry.grid(row=index, column=1, pady=7)
    return year_entries


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

# adding all 7 modules to the year panels
year1Entries = add_year_modules(1, firstYearPanel)
year2Entries = add_year_modules(2, secondYearPanel)
year3Entries = add_year_modules(3, thirdYearPanel)

year1score_label = StringVar()
Label(firstYearPanel, text="Year 1 Average:", font=boldFont).grid(row=8, column=0, pady=7, padx=7)
Label(firstYearPanel, textvariable=year1score_label, font=boldFont).grid(row=8, column=1, pady=7, padx=7)
year2score_label = StringVar()
Label(secondYearPanel, text="Year 2 Average:", font=boldFont).grid(row=8, column=0, pady=7, padx=7)
Label(secondYearPanel, textvariable=year2score_label, font=boldFont).grid(row=8, column=1, pady=7, padx=7)
year3score_label = StringVar()
Label(thirdYearPanel, text="Year 3 Average:", font=boldFont).grid(row=8, column=0, pady=7, padx=7)
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
