# Student Progression Prediction Program

This Python program predicts progression outcomes for students at the end of each academic year based on provided credit data.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Outcomes](#outcomes)
- [Validation](#validation)
- [Multiple Outcomes](#multiple-outcomes)
- [Histogram](#histogram)
- [Part 2 - List Extension](#part-2---list-extension)
- [Part 3 - Text File Extension](#part-3---text-file-extension)
- [Contribution](#contribution)
- [License](#license)

## Introduction

This program is designed to assist university staff in predicting the progression outcomes of students based on the credits they have earned. It utilizes user input to gather credits at pass, defer, and fail levels and then determines the appropriate progression outcome for each student.

## Usage

To use the program, simply run the Python script and follow the prompts to input credits at each level for individual students. Follow the instructions provided for the correct input format and options to continue or quit.

## Outcomes

The program allows users to predict progression outcomes for individual students by prompting for the number of credits at each level (pass, defer, fail) and displaying the appropriate outcome.

## Validation

- Displays 'Integer required' if a credit input is not of integer type.
- Displays 'Out of range' if credits entered are not within the range 0, 20, 40, 60, 80, 100, or 120.
- Displays 'Total incorrect' if the total of pass, defer, and fail credits is not 120.
- Utilizes efficient conditional statements to handle multiple outcomes.

## Multiple Outcomes

The program loops to allow staff members to predict progression outcomes for multiple students. It prompts for credits at each level and displays the appropriate progression for each student until the staff member chooses to quit by entering 'q'.

## Histogram

Upon entering 'q' to quit, the program generates a histogram representing the number of students who achieved progress, trailing, module retriever, and exclude outcomes. It displays the number of students for each progression category and the total number of students.

| Outcome Category   | Number of Students |
|--------------------|--------------------|
| Progress           | X                  |
| Trailer            | X                  |
| Module Retriever   | X                  |
| Exclude            | X                  |
| **Total Students** | **X**              |

## Part 2 - List Extension

In this extension, the program stores input progression data in a list and prints the data in a specified format.

## Part 3 - Text File Extension

An additional program or extension of the original version saves inputted progression data to a text file. Later, it accesses the stored data and prints it out in the specified format.

## Contribution

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate test coverage.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This program was developed as part of a university coursework assignment. The specifications and requirements were provided by the university.
