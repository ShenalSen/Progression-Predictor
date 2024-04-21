'''
from graphics import *
import sys

# Define progression outcomes based on credit values
progression_table = {
    (120, 0, 0): "Progress",
    (100, 20, 0): "Progress (module trailer)",
    (100, 0, 20): "Progress (module trailer)",
    (80, 40, 0): "Do not Progress - module retriever",
    (80, 20, 20): "Do not Progress - module retriever",
    (80, 0, 40): "Do not Progress - module retriever",
    (60, 60, 0): "Do not progress - module retriever",
    (60, 40, 20): "Do not progress - module retriever",
    (60, 20, 40): "Do not progress - module retriever",
    (60, 0, 60): "Do not progress - module retriever",
    (40, 80, 0): "Do not progress - module retriever",
    (40, 60, 20): "Do not progress - module retriever",
    (40, 40, 40): "Do not progress - module retriever",
    (40, 20, 60): "Do not progress - module retriever",
    (20, 100, 0): "Do not progress - module retriever",
    (20, 80, 20): "Do not progress - module retriever",
    (20, 60, 40): "Do not progress - module retriever",
    (20, 40, 60): "Do not progress - module retriever",
    (0, 120, 0): "Do not progress - module retriever",
    (0, 100, 20): "Do not progress - module retriever",
    (0, 80, 40): "Do not progress - module retriever",
    (0, 60, 60): "Do not progress - module retriever"
}

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

def predict_progression(pass_credits, defer_credits, fail_credits):
    if pass_credits + defer_credits + fail_credits != 120:
        return "Total incorrect."
    
    return progression_table.get((pass_credits, defer_credits, fail_credits), "Exclude")

def main():
    students = []
    
    while True:
        pass_credits = get_credits("Enter your total PASS credits: ")
        defer_credits = get_credits("Enter your total DEFER credits: ")
        fail_credits = get_credits("Enter your total FAIL credits: ")
        
        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        print(outcome)
        
        students.append(outcome)
        
        choice = input("Would you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ").lower()
        if choice == 'q':
            break
    
    # Create a histogram
    win = GraphWin("Progression Histogram", 1200, 700)
    win.setBackground("White")
    
    categories = ["Progress", "Progress (module trailer)", "Module retriever", "Exclude"]
    counts = [students.count(cat) for cat in categories]
    
    x = 50
    width = 75
    total_students = len(students)
    
    for cat, count in zip(categories, counts):
        bar = Rectangle(Point(x, 350 - 300 * count / total_students), Point(x + width, 350))
        bar.setFill("blue")
        bar.draw(win)
        
        label = Text(Point(x + width / 2, 380), cat)
        label.draw(win)
        
        x += 2 * width
    
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
'''





'''
from graphics import *

# Define progression outcomes based on credit values
progression_table = {
    (120, 0, 0): "Progress",
    (100, 20, 0): "Progress (module trailer)",
    (100, 0, 20): "Progress (module trailer)",
    (80, 40, 0): "Do not Progress - module retriever",
    (80, 20, 20): "Do not Progress - module retriever",
    (80, 0, 40): "Do not Progress - module retriever",
    (60, 60, 0): "Do not progress - module retriever",
    (60, 40, 20): "Do not progress - module retriever",
    (60, 20, 40): "Do not progress - module retriever",
    (60, 0, 60): "Do not progress - module retriever",
    (40, 80, 0): "Do not progress - module retriever",
    (40, 60, 20): "Do not progress - module retriever",
    (40, 40, 40): "Do not progress - module retriever",
    (40, 20, 60): "Do not progress - module retriever",
    (20, 100, 0): "Do not progress - module retriever",
    (20, 80, 20): "Do not progress - module retriever",
    (20, 60, 40): "Do not progress - module retriever",
    (20, 40, 60): "Do not progress - module retriever",
    (0, 120, 0): "Do not progress - module retriever",
    (0, 100, 20): "Do not progress - module retriever",
    (0, 80, 40): "Do not progress - module retriever",
    (0, 60, 60): "Do not progress - module retriever"
}

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

def predict_progression(pass_credits, defer_credits, fail_credits):
    if pass_credits + defer_credits + fail_credits != 120:
        return "Total incorrect."
    
    return progression_table.get((pass_credits, defer_credits, fail_credits), "Exclude")

def main():
    students = []
    
    win = GraphWin("Progression Histogram", 1200, 700)
    win.setBackground("white")
    
    categories = ["Progress", "Progress (module trailer)", "Module retriever", "Exclude"]
    counts = [0, 0, 0, 0]  # Initialize counts for each category
    
    while True:
        pass_credits = get_credits("Enter your total PASS credits: ")
        defer_credits = get_credits("Enter your total DEFER credits: ")
        fail_credits = get_credits("Enter your total FAIL credits: ")
        
        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        print(outcome)
        
        students.append(outcome)
        
        # Update counts based on the outcome
        if outcome == "Progress":
            counts[0] += 1
        elif outcome == "Progress (module trailer)":
            counts[1] += 1
        elif outcome == "Module retriever":
            counts[2] += 1
        elif outcome == "Exclude":
            counts[3] += 1
        
        choice = input("Would you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ").lower()
        if choice == 'q':
            break
    
    # Generate the histogram
    x = 50
    width = 75
    total_students = len(students)
    
    for cat, count in zip(categories, counts):
        bar = Rectangle(Point(x, 350 - 300 * count / total_students), Point(x + width, 350))
        bar.setFill("blue")
        bar.draw(win)
        
        label = Text(Point(x + width / 2, 380), cat)
        label.setSize(16)
        label.setTextColor("white")
        label.draw(win)
        
        x += 2 * width
    
    win.getMouse()  # Wait for user interaction
    win.close()  # Close the window when done

if __name__ == "__main__":
    main()
'''

"""
from graphics import *

# Define progression outcomes based on credit values
progression_table = {
    (120, 0, 0): "Progress",
    (100, 20, 0): "Progress (module trailer)",
    (100, 0, 20): "Progress (module trailer)",
    (80, 40, 0): "Do not Progress - module retriever",
    (80, 20, 20): "Do not Progress - module retriever",
    (80, 0, 40): "Do not Progress - module retriever",
    (60, 60, 0): "Do not progress - module retriever",
    (60, 40, 20): "Do not progress - module retriever",
    (60, 20, 40): "Do not progress - module retriever",
    (60, 0, 60): "Do not progress - module retriever",
    (40, 80, 0): "Do not progress - module retriever",
    (40, 60, 20): "Do not progress - module retriever",
    (40, 40, 40): "Do not progress - module retriever",
    (40, 20, 60): "Do not progress - module retriever",
    (20, 100, 0): "Do not progress - module retriever",
    (20, 80, 20): "Do not progress - module retriever",
    (20, 60, 40): "Do not progress - module retriever",
    (20, 40, 60): "Do not progress - module retriever",
    (0, 120, 0): "Do not progress - module retriever",
    (0, 100, 20): "Do not progress - module retriever",
    (0, 80, 40): "Do not progress - module retriever",
    (0, 60, 60): "Do not progress - module retriever"
}

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

def predict_progression(pass_credits, defer_credits, fail_credits):
    if pass_credits + defer_credits + fail_credits != 120:
        return "Total incorrect."
    
    return progression_table.get((pass_credits, defer_credits, fail_credits), "Exclude")

def main():
    students = []
    
    win = GraphWin("Progression Histogram", 1200, 700)
    win.setBackground("white")
    
    categories = ["Progress", "Progress (module trailer)", "Module retriever", "Exclude"]
    counts = [0, 0, 0, 0]  # Initialize counts for each category
    
    while True:
        pass_credits = get_credits("Enter your total PASS credits: ")
        defer_credits = get_credits("Enter your total DEFER credits: ")
        fail_credits = get_credits("Enter your total FAIL credits: ")
        
        outcome = predict_progression(pass_credits, defer_credits, fail_credits)
        print(outcome)
        
        students.append(outcome)
        
        # Update counts based on the outcome
        if outcome == "Progress":
            counts[0] += 1
        elif outcome == "Progress (module trailer)":
            counts[1] += 1
        elif outcome == "Module retriever":
            counts[2] += 1
        elif outcome == "Exclude":
            counts[3] += 1
        
        choice = input("Would you like to enter another set of data? (Enter 'y' for yes or 'q' to quit): ").lower()
        if choice == 'q':
            break
    
    # Generate the histogram
    x = 50
    width = 75
    total_students = len(students)
    
    for cat, count in zip(categories, counts):
        bar = Rectangle(Point(x, 350 - 300 * count / total_students), Point(x + width, 350))
        bar.setFill("blue")
        bar.draw(win)
        
        label = Text(Point(x + width / 2, 380), cat)
        label.setSize(16)
        label.setTextColor("white")
        label.draw(win)
        
        x += 2 * width
    
    win.getMouse()  # Wait for user interaction
    
    # Close the window after user interaction
    win.close()

if __name__ == "__main__":
    main()
"""
