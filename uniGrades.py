from tkinter import *

root = Tk()
root.title("My Uni Grades Calculator")

boldFont = ("Helvetica", 16, "bold")

# creating the 3 main containers
top_frame = Frame(root, bg='#E67E22', width=200, height=50, pady=5, padx=5)
center_frame = Frame(root, bg='#E67E22', width=200, height=40)
btm_frame = Frame(root, bg='#E67E22', width=200, height=100, pady=5)

# adding the 3 main containers to the root
top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="nsew")
btm_frame.grid(row=2, sticky="ew")

# adding the main title to the top frame
mainTitle = Label(top_frame, text="Welcome to My Uni Grades Calculator", fg="red", font=("Helvetica", 20, "bold"))
message = Label(top_frame, text="Enter your marks in each of the following modules then " +
                                "click submit to find out your final grade and degree classification")
mainTitle.pack(expand=YES, fill=X)
message.pack(expand=YES, fill=X)

# creating the 3 middle vertical containers
firstYearPanel = Frame(center_frame, bg='#5499C7', height=250, padx=30, pady=10)
secondYearPanel = Frame(center_frame, bg='#F4D03F', height=250, padx=30, pady=10)
thirdYearPanel = Frame(center_frame, bg='#2ECC71', height=250, padx=30, pady=10)

# adding the 3 middle containers to the centre frame
firstYearPanel.grid(row=0, column=0, sticky="ns")
secondYearPanel.grid(row=0, column=1, sticky="nsew")
thirdYearPanel.grid(row=0, column=2, sticky="ns")

# adding the title, labels and entries in the year 1 container
year1Title = Label(firstYearPanel, text="Year 1 Modules", font=boldFont)
year1Title.grid(row=0, column=0, columnspan=2, pady=10)
for index in range(1, 8):
    label = Label(firstYearPanel, text='Module ' + str(index) + " (15 credits)")
    entry = Entry(firstYearPanel, width=6, justify='center')
    label.grid(row=index, column=0, pady=7)
    entry.grid(row=index, column=1, pady=7)

# adding the title, labels and entries in the year 2 container
year2Title = Label(secondYearPanel, text="Year 2 Modules", font=boldFont)
year2Title.grid(row=0, column=0, columnspan=2, pady=10)
for index in range(1, 8):
    label = Label(secondYearPanel, text='Module ' + str(index) + " (15 credits)")
    entry = Entry(secondYearPanel, width=6, justify='center')
    label.grid(row=index, column=0, pady=7)
    entry.grid(row=index, column=1, pady=7)

# adding the title, labels and entries in the year 3 container
year3Title = Label(thirdYearPanel, text="Year 3 Modules", font=boldFont)
year3Title.grid(row=0, column=0, columnspan=2, pady=10)
for index in range(1, 8):
    label = Label(thirdYearPanel, text='Module ' + str(index) + " (15 credits)")
    entry = Entry(thirdYearPanel, width=6, justify='center')
    label.grid(row=index, column=0, pady=7)
    entry.grid(row=index, column=1, pady=7)

# creating 2 containers for the result labels and submit button
resultsPanel = Frame(btm_frame, bg='#E74C3C', height=250, padx=20, pady=10)
buttonPanel = Frame(btm_frame, bg='#E74C3C', height=250, padx=30, pady=10)

# adding the 2 containers to the bottom frame
buttonPanel.pack(side=RIGHT)
resultsPanel.pack(side=RIGHT, fill=BOTH, expand=1)

# mock data
grade = "100.0"
classification = "1st Class"

# adding labels and submit button to their containers
Label(resultsPanel, text='Final Grade', font=boldFont).grid(row=0, column=0, pady=5, padx=5, sticky="E")
Label(resultsPanel, text='Degree Classification', font=boldFont).grid(row=1, column=0, pady=5, padx=5, sticky="E")
Label(resultsPanel, text=grade, font=boldFont).grid(row=0, column=1, pady=5, padx=5, sticky="W")
Label(resultsPanel, text=classification, font=boldFont).grid(row=1, column=1, pady=5, padx=5, sticky="W")
Label(resultsPanel, text="Note the weight of the modules of each year is higher than\n" +
                         "the weight of previous years' modules and that the ratio is \n" +
                         "1st-year : 2nd-year : 3rd-year \n1 : 3 : 5") \
    .grid(row=0, column=2, columnspan=2, rowspan=2, pady=5, padx=5, sticky="W")

Button(buttonPanel, text='Submit').grid(row=0, column=0)

root.mainloop()
