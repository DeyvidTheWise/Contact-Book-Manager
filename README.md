# Contact Book Manager

## Table of Contents

[Introduction](#introduction)
[Features](#features)
[Contributing](#contributing)
[License](#license)
[BG Documentation](#мениджър-на-контакти)

### Introduction

Contact Book Manager is a Python-based application designed to help users efficiently manage their personal contacts. With an easy-to-use interface, users can import/export contacts, add/delete contacts, search and sort contacts, edit contact information, and receive reminders for birthdays.

### Features

- Add new contacts with detailed information
- Delete and update contact information
- Search for contacts for quick access
- Create contact groups and add/delete contacts to/from groups
- Send birthday reminders for contacts 10 days prior to the scheduled day
- Import/Export contacts to/from other applications via .csv files
- Print contact lists to text files (common details only)
- Print detailed information of a selected contact to a text file

### Contributing

We welcome contributions to the Contact Book Manager project! If you would like to contribute, please follow the steps below:

1. Fork the repository: Go to the [Contact Book Manager repository](https://github.com/DeyvidTheWise/Contact-Book-Manager) and click the "Fork" button in the upper-right corner. This will create a copy of the repository in your own GitHub account.
2. Clone your fork: Use the following command in your local development environment to clone your fork of the repository:

```markdown
git clone https://github.com/YOUR-USERNAME/Contact-Book-Manager.git
```

Replace YOUR-USERNAME with your GitHub username. 3. Create a new branch: To keep your changes organized, create a new branch with a descriptive name for the feature or bugfix you're working on:

```markdown
git checkout -b YOUR-FEATURE-BRANCH-NAME
```

Replace YOUR-FEATURE-BRANCH-NAME with a name that describes the changes you're making. 4. Make your changes: Implement the feature or bugfix in your local development environment. 5. Commit your changes: Once you've made your changes, stage and commit them to your local repository:

```markdown
git add .
git commit -m "YOUR COMMIT MESSAGE DESCRIBING THE CHANGES"
```

Replace YOUR COMMIT MESSAGE DESCRIBING THE CHANGES with a short description of the changes you've made. 6. Push your changes: Push your changes to your fork on GitHub:

```markdown
git push origin YOUR-FEATURE-BRANCH-NAME
```

7. Create a pull request: Go to the original [Contact Book Manager repository](https://github.com/DeyvidTheWise/Contact-Book-Manager) and click on the "Pull Requests" tab. Click the "New pull request" button, then choose your fork and your feature branch. Add a descriptive title and any relevant information in the description, then click "Create pull request."

Please note that all pull requests should follow the project's coding standards and should include appropriate tests, if applicable.

If you have any questions or need assistance, feel free to create an issue in the repository or reach out to the project maintainers.

Thank you for your interest in contributing to the Contact Book Manager project!

### License

Apache License 2.0: A permissive license similar to the MIT License but with additional terms covering patents and a requirement to include a NOTICE file if one exists. It allows for free use, modification, and distribution of your code, while providing some protection against patent litigation.

---

# МЕНИДЖЪР НА КОНТАКТИ

## За проекта

Проектът представлява мениджър на контакти, който предоставя възможност за съхранение, обработка и организация на контакти, групи и мелодии. Основните функционалности са:

1. Добавяне, актулизиране и премахване на контакти - За контактите има създаден шаблон с полета, като основните полета, които трябва да бъдат попълнени са име, номер, група и мелодия. Ако досега не са били въвеждани групи и мелодии от потребителя, то той няма да има възможност да си избере. Всички данни за контактите биват съхранявани в CSV файл, което се намира в директорията на проекта.
2. Добавяне, актулизиране и премахване на групи и мелодии. - Клиентът има възможност да зададе свои собствени мелодии и групи, като тези данни се съхраняват в TXT файлове. За тях се пазят име и брояч. Броячът се използва при изтриването на информацията, като се проверява дали някой от контактите не е в дадената група или не звъни с дадената мелодия.
3. Управление на контакти и групи - Потребителят има възможност да добавя или премахва контакти от различни групи.
4. Известия за предстоящ рожден ден - Тази опция представя списък с всички контакти, които имат рожден ден в следващите 10 дни. Системата работи с дати във формат YYYY-MM-DD.
5. Опция за доклади - Крайният потребител може да изисква обща информация за всички потребители или детайлна за един.
