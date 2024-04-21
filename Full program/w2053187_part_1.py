# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2053187
# Date: 14.12.2023

# Part 01

from graphics import *

# Define progression outcomes based on credit values

count = 0

students = []
progress = []
Progress_module_trailer = []
module_retriever = []
exclude = []

#Function for get credits and check the range
def get_credits(prompt):
    while True:
        try:
            credits = int(input(prompt))
            if credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue
            return credits
        except ValueError:
            print("Integer required.")

#Function for predict the progression of the student
def predict_progression(pass_credits, defer_credits, fail_credits):
    if pass_credits + defer_credits + fail_credits != 120:
        return "Total incorrect."
    else:
        if pass_credits == 120:
            outcome = "progress"
        elif pass_credits == 100:
            outcome = "progress (module trailer)"
        elif fail_credits >= 80:
            outcome = "Exclude"
        else:
            return "Do not progress - module retriever"
        return outcome

#Main programme
def main():
    global progress
    global Progress_module_trailer
    global module_retriever
    global exclude
    global students
    
    while True:
        pass_credits = get_credits("Enter your total PASS credits: ")
        defer_credits = get_credits("Enter your total DEFER credits: ")
        fail_credits = get_credits("Enter your total FAIL credits: ")
        
        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        print(outcome)
        
        # store the data to list 
        if outcome == "progress":
            progress.append(outcome)
        if outcome == "progress (module trailer)":
            Progress_module_trailer.append(outcome)
        if outcome == "Do not progress - module retriever":
            module_retriever.append(outcome)
        if outcome == "Exclude":
            exclude.append(outcome)
        if outcome == "progress" or outcome == "progress (module trailer)" or outcome == "Do not progress - module retriever" or outcome == "Exclude":
            students.append(outcome)

        
        
        choice = check_choice("Would you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ")
        if choice == 'q':
            print(f" progress :{len(progress)} \n module trailer :{len(Progress_module_trailer)} \n module retriever :{len(module_retriever)} \n exclude :{len(exclude)}")
            break
    
    # Create a histogram

    # Variables
    WIN_WIDTH, WIN_HEIGHT = 1200, 700
    LINES = WIN_WIDTH/4
    MARGIN = LINES/2
    RECT_WIDTH = 70
    RECT_HEIGHT = 20
    RECT_HEIGHT_POINT = WIN_HEIGHT - WIN_HEIGHT/4

    win = GraphWin("Progression Histogram", WIN_WIDTH, WIN_HEIGHT)
    win.setBackground("#ECECEC")

    # Lines
    line5 = Line(Point(LINES - MARGIN - 100, WIN_HEIGHT - WIN_HEIGHT / 4), Point(LINES*3 + MARGIN + 100 ,WIN_HEIGHT - WIN_HEIGHT / 4))

    for ln in [line5]:
        ln.setOutline(color_rgb(0, 0, 0))
        ln.draw(win)

    # Function for draw Rectangles
    def draw_rectangle(line_position, rect_height, data_list, color):
        rect = Rectangle(Point(line_position - RECT_WIDTH, RECT_HEIGHT_POINT),
                         Point(line_position + RECT_WIDTH, RECT_HEIGHT_POINT - RECT_HEIGHT * len(data_list)))
        rect.setOutline(color_rgb(0, 0, 0))
        rect.setFill(color)
        rect.draw(win)
    
    # Function for display count above the bars
    def display_count(line_position, data_list):
        label = Text(Point(line_position - 70 + RECT_WIDTH, RECT_HEIGHT_POINT - RECT_HEIGHT * len(data_list) - 50), f"{len(data_list)}")
        label.setTextColor("#797B89")
        label.draw(win)
    
    #Function for display titles below the baseline
    def display_titles(line_position, data_list):
        label = Text(Point(line_position - 70 + RECT_WIDTH, RECT_HEIGHT_POINT + 40), f"{data_list}")
        label.setTextColor("#797B89")
        label.setFace("arial")
        label.setStyle("bold")
        label.draw(win)

    draw_rectangle(MARGIN, RECT_HEIGHT, progress, "#95FFA6")
    draw_rectangle(LINES + MARGIN, RECT_HEIGHT, Progress_module_trailer, "#91AD74")
    draw_rectangle(LINES * 2 + MARGIN, RECT_HEIGHT, module_retriever, "#B8BD69")
    draw_rectangle(LINES * 3 + MARGIN, RECT_HEIGHT, exclude, "#E1A5A5")
    
    display_count(MARGIN , progress)
    display_count(LINES + MARGIN, Progress_module_trailer)
    display_count(LINES * 2 + MARGIN, module_retriever)
    display_count(LINES * 3 + MARGIN, exclude)

    display_titles(MARGIN , "Progress")
    display_titles(LINES + MARGIN, "Trailer")
    display_titles(LINES * 2 + MARGIN, "Retriever")
    display_titles(LINES * 3 + MARGIN, "Exclude")

    #Total outcomes label
    total_label = Text(Point(MARGIN + RECT_WIDTH - 11, RECT_HEIGHT_POINT + 70), f"{len(students)} outcomes in total.")
    total_label.setTextColor("#797B89")
    total_label.setSize(15)
    total_label.setStyle("bold")
    total_label.setFace("arial")
    total_label.draw(win)

    #Main title
    title_label = Text(Point(150, 100), "Histogram Results")
    title_label.setTextColor("#4F4F4F")
    title_label.setSize(17)
    title_label.setStyle("bold")
    title_label.draw(win)

    win.getMouse()
    win.close()

#Function for check user's choice to cotinue or quit the programme
def check_choice(prompt):
    while True:
        try:
            choice = input(prompt).lower()
            if choice not in ['y', 'q']:
                print("invaild option")
                continue
            if choice in ['y', 'q']:
                return choice
        except: ValueError


if __name__ == "__main__":
    main()
