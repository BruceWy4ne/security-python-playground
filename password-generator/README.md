# 🔐 Secure Password Generator v1.0

A command-line password generator built in Python that creates randomized passwords based on user-selected character types. This project was developed to practice Python fundamentals, function design, input validation, and basic security-oriented programming.

## Features

- Generate passwords of a custom length
- Choose whether to include:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Validates user input for character type selection
- Prevents password generation if no character type is selected
- Randomizes the final password to improve character distribution
- Simple command-line interface

## Technologies Used

- Python 3
- `random` module
- `string` module

## Project Structure

```
password-generator/
│
├── README.md
├── requirements.txt
└── src/
    └── password_generator.py
```

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd password-generator/src
```

3. Run the program.

```bash
python password_generator.py
```

## Example

```
========================================
     Secure Password Generator v1.0
========================================

Enter length of password: 12

Include Uppercase Letter (Y/N): y
Include Lowercase Letter (Y/N): y
Include Numbers (Y/N): y
Include Special Character (Y/N): n

Generated Password:
L9aTp7eQm2Xs
```

## What I Learned

While building this project, I practiced:

- Breaking a problem into multiple functions
- Reusing code to reduce repetition
- Validating user input
- Working with Python's `random` and `string` modules
- Implementing basic exception handling
- Improving code through multiple iterations and debugging

## Future Improvements

Some ideas for future versions include:

- Stronger password strength validation
- Ability to generate multiple passwords at once
- Copy generated password to the clipboard
- Export generated passwords to a file
- Improved error handling and input validation

## License

This project is licensed under the MIT License.