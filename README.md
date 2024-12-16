# Phoenix War MultiPoll System

Welcome to the **Phoenix War MultiPoll System**, a Django-based application designed to create and manage poll for the Phoenix War clan in the game **Without Survivals**. This project aims to enhance engagement and decision-making by gathering member responses through customizable polls.

## Features

- **Answer Validation**: Ensure accurate data collection with validations that prevent conflicts between predefined options and custom answers.
- **Excel Export**: Export survey results to Excel for further analysis and reporting.
- **Tailwind CSS Integration**: Responsive and modern UI powered by Tailwind CSS.
- **Django Unfold Integration**: Improved admin panel functionality and model order customization.

## Models Overview

### Poll
Represents a survey or collection of questions.
- **Fields**: Title, Description, Image (optional), etc.

### Question
Defines individual questions within a poll.
- **Fields**: Text, Image (optional).

### Option
Lists possible answers for each question.
- **Fields**: Text, Image (optional).

### Answer
Records responses to a question.
- **Fields**: Linked to a question and the respondent.

### SelectedOption
Stores the selected predefined options.
- **Fields**: Linked to an option and the associated answer.

### CustomAnswer
Captures custom-written responses.
- **Fields**: Text, linked to the associated answer.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alastor-4/django-multipoll.git
   cd django-multipoll
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000`.

## Usage

1. Log in as an admin to create and manage polls, questions, and options.
2. Share the poll link with clan members.
3. Export poll results to Excel for review and analysis.

## Contribution

Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and create a pull request.

## Author

Developed by [Alexis Manuel Hurtado Garcia](https://github.com/alastor-4) for the **Phoenix War** clan in the game **Without Survivals**.
