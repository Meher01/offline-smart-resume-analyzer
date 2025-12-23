
<strong> <h1> SMART RESUME ANALYZER </h1> </strong>
<h2> Project Documentation </h2>

<strong> 1. Project Overview </strong>
Smart Resume Analyzer is an offline, AI-inspired resume analysis web application built using Streamlit. The system analyzes resumes (PDF/TXT), extracts key information, evaluates skill relevance, and generates an estimated fit score along with actionable suggestions for improvement. It is designed to help job seekers optimize resumes for specific job roles.
________________________________________
<strong> 2. Objectives </strong><br>
•	Analyze resumes automatically without internet dependency<br>
•	Extract technical, non-technical, and extra qualifications<br>
•	Provide a quantified resume fit score (out of 100)<br>
•	Suggest improvements to increase job relevance<br>
•	Support PDF and TXT resume formats<br>
________________________________________
<strong> 3. Key Features </strong><br>
•	📄 Upload Resume (PDF/TXT)<br>
•	📌 Target Job Role Matching<br>
•	🧠 Skill Extraction (Technical & Soft Skills)<br>
•	💯 Resume Fit Scoring System<br>
•	📊 Score Breakdown with Progress Bars<br>
•	🛠 Personalized Improvement Suggestions<br>
•	📖 Resume Text Excerpt Preview<br>
•	🎨 Modern UI with CSS Animations<br>
________________________________________
<strong> 4. Technology Stack </strong><br>
•	Frontend/UI: Streamlit, Custom CSS<br>
•	Backend Logic: Python<br>
•	PDF Processing: PyPDF2<br>
•	Text Processing: Regex, String Matching<br>
•	Environment: Offline / Localhost<br>
________________________________________
<strong> 5. System Architecture </strong><br>
User → Streamlit UI → Resume Parser → Analyzer Engine → Score & Suggestions → UI Output
________________________________________
<strong> 6. Functional Modules </strong><br>
<strong> 6.1 Resume Upload Module </strong><br>
•	Accepts .pdf and .txt files<br>
•	Uses PyPDF2 for PDF text extraction<br>
•	Supports demo resume for testing<br>

<strong> 6.2 Text Extraction & Cleaning </strong><br>
•	Extracts raw text from resumes<br>
•	Cleans whitespace and formats content<br>
•	Generates a readable excerpt (700 characters)<br>

<strong> 6.3 Skill Detection Engine </strong><br>
<strong> Skill Categories: </strong><br>
•	Technical Skills (Python, Java, SQL, Docker, AWS, etc.)<br>
•	Non-Technical Skills (Communication, Leadership, Teamwork)<br>
•	Extra Signals (Certifications, Degree, Internship)<br>
Skills are detected using keyword matching on lowercased resume text.<br>

<strong> 6.4 Suggestion Generator </strong><br>
Based on missing or weak sections, the system suggests:<br>
•	Adding job role keywords<br>
•	Improving technical coverage<br>
•	Highlighting soft skills<br>
•	Including projects with impact<br>
•	Adding certifications or education<br>
________________________________________
<strong> 7. Installation & Setup </strong><br>
Prerequisites<br>
•	Python 3.9+<br>
•	pip<br>
<strong>Required Libraries</strong><br>
<code> pip install streamlit PyPDF2 </code><br>
<strong>Run Application</strong><br>
<code> streamlit run analyzer.py </code><br>
________________________________________
<strong> 9. Input & Output </strong><br>
Input<br>
•	Resume file (PDF or TXT)<br>
•	Optional target job role<br>
Output<br>
•	Extracted skills<br>
•	Resume fit score (/100)<br>
•	Category-wise score breakdown<br>
•	Improvement suggestions<br>
________________________________________
<strong> 10. Limitations </strong><br>
•	Keyword-based analysis (not true NLP/ML)<br>
•	No semantic understanding of experience depth<br>
•	Limited predefined skill list<br>
•	English language resumes only<br>
________________________________________
<strong> 11. Future Enhancements </strong><br>
•	NLP-based skill extraction<br>
•	Machine Learning resume ranking<br>
•	Job description comparison<br>
•	ATS compatibility scoring<br>
•	Multi-language support<br>
•	Resume export with suggestions applied<br>
________________________________________
<strong> 12. Conclusion </strong><br>
The Smart Resume Analyzer is an effective offline tool for resume evaluation and optimization. It provides instant insights, scoring, and suggestions, making it ideal for students, job seekers, and early professionals preparing resumes for technical roles.
________________________________________
Project Type: Resume Analysis System<br>
Platform: Offline Web App<br>
Language: Python<br>
Framework: Streamlit<br>
________________________________________
<strong> Team Members </strong><br>
A. Vaishnavi<br>
L. P. M. Lasya<br>

