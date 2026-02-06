📘 Project Documentation
University FAQ Assistant

1. Project Title
University FAQ Assistant using Streamlit and Dataset-based AI

2. Introduction
With the rapid growth of educational institutions, students and parents often face difficulty in finding accurate and quick information about universities. Common queries related to admissions, fees, courses, hostels, placements, and campus facilities are usually scattered across websites or require manual support.
The University FAQ Assistant is a simple and interactive application designed to solve this problem by providing instant answers to frequently asked university-related questions using a structured dataset. The project focuses on simplicity, usability, and real-world relevance rather than complex AI APIs.
This project was developed as part of the Gen AI for Gen Z course by Scaledown in association with Intel.

3. Objectives
The main objectives of this project are:
To create an easy-to-use FAQ assistant for university-related queries
To demonstrate practical application of GenAI concepts using datasets
To avoid dependency on external APIs and work fully offline
To build a clean and interactive web interface using Streamlit
To help users quickly search and retrieve accurate information

4. Scope of the Project
The scope of this project includes answering commonly asked questions related to:
Admissions process
Courses and programs offered
Fee structure and scholarships
Hostel and campus facilities
Placements and salary packages
Rankings and accreditations
Student life, clubs, and events
Exams, results, and academic policies
The project is suitable for students, parents, and academic staff.

5. Technology Stack Used
Technology
Purpose
Python
Core programming language
Streamlit
Web application framework
Pandas
Data handling and processing
CSV Dataset
Knowledge base for FAQs
GitHub
Code hosting and version control

6. Dataset Description
The project uses a CSV-based dataset containing over 400 frequently asked university questions along with their respective answers.
Dataset Features:
Simple question-answer format
Covers all major university-related topics
Easy to extend and update
Lightweight and fast to load

Sample Dataset Format:
Question
Answer
What courses are offered?
The university offers undergraduate and postgraduate programs.
What is the admission process?
Admissions are based on merit and entrance exams.

7. System Architecture
User enters a question in the Streamlit interface
The application reads the dataset using Pandas
The system searches for the most relevant question
The corresponding answer is displayed instantly
This approach ensures fast response and offline functionality.

8. Features of the System
User-friendly and interactive UI
Dataset-driven responses (no API usage)
Quick and accurate answers
Scalable dataset (more FAQs can be added easily)
Fully offline and reliable
Lightweight and easy to deploy

9. Implementation Details
The application is built using Streamlit for frontend interaction
Pandas is used to load and search the CSV dataset
The logic matches user queries with stored FAQs
Results are displayed dynamically on the web interface
The code is structured in a clean and readable manner to ensure easy understanding and maintenance.

10. Advantages
No internet dependency for AI APIs
Low cost and simple architecture
Easy to modify and expand
Suitable for academic projects and demos
Beginner-friendly implementation

11. Limitations
Answers are limited to the dataset
Does not generate new responses beyond stored FAQs
Exact or close keyword matching is required

12. Future Enhancements
Adding semantic search using embeddings
Voice-based question input
Admin panel for managing FAQs
Support for multiple universities
Analytics for frequently asked questions

13. Conclusion
The University FAQ Assistant successfully demonstrates how GenAI concepts can be applied in a practical and meaningful way using structured datasets. The project emphasizes simplicity, usability, and real-world application, making it ideal for academic evaluation and learning purposes.
This project enhanced understanding of data-driven AI systems, user interface design, and deployment workflows.

14. References
Streamlit Documentation
Python Official Documentation
Pandas Documentation
GitHub
