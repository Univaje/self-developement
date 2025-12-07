# 🤖 Robot Framework -- Learning & Practice

This is a work in progress.

Welcome to my **Robot Framework learning repository**!\
This folder contains exercises, test scripts, demos, and experiments
created while I'm learning how to automate testing using **Robot
Framework**.

The goal of this project is to improve my skills in:

-   Writing Robot Framework test suites\
-   Using keywords (built-in + custom)\
-   Working with locators\
-   Handling browser automation\
-   Structuring test files\
-   Integrating external libraries\
-   Debugging and experimenting with different test scenarios

------------------------------------------------------------------------

## 📂 Repository Structure

    RobotFramework/
    │
    ├── Tests/               # Practice test cases  
    ├── Resources/           # Shared keywords and variable files  
    ├── Libraries/           # Custom Python libraries (if any)  
    ├── Results/             # Output and log files  
    └── README.md

> Folder names may vary depending on the lesson or experiment.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Robot Framework**\
-   **Python**
-   **SeleniumLibrary**
-   **pipenv / venv** (optional for environment control)
-   **VS Code** with Robot Framework extensions

------------------------------------------------------------------------

## ▶️ How to Run the Tests

### 1. Install Robot Framework

``` bash
pip install robotframework
```

### 2. Install SeleniumLibrary (if used)

``` bash
pip install robotframework-seleniumlibrary
```

### 3. Install browser driver (example: Chrome)

``` bash
rfbrowser init
```

Or install manually with WebDriver Manager:

``` bash
pip install webdriver-manager
```

### 4. Run a test file

``` bash
robot Tests/
```

Run a specific test:

``` bash
robot Tests/example.robot
```

------------------------------------------------------------------------

## 🎯 Learning Goals

This repository is for personal learning, focusing on:

-   Creating reusable test keywords\
-   Exploring Robot Framework syntax\
-   Practicing automation logic\
-   Understanding real automation project structure\
-   Writing clean, readable test cases\
-   Experimenting with failures, logs, and debugging

------------------------------------------------------------------------

## 📄 Notes

This repository is primarily a **self-development playground**.\
Not all tests here represent production-level structure, but they
document my progress and experiments.

------------------------------------------------------------------------

## ⭐ Future Plans

-   Add more advanced test suites\
-   Integrate CI (GitHub Actions)\
-   Create custom libraries\
-   Learn Browser library (Playwright for Robot)\
-   Add API testing examples\
-   Add data-driven tests
