# cs699-project-audience-poll
# Audience Poll - Empowering Informed Decisions Through Collective Knowledge

Audience Poll is a web-based platform that allows users to create polls on conflicting topics and receive votes from other users based on their knowledge or experience. The system aggregates the results in real-time to help users make better, more informed decisions.

## Why Polling App:
<ul>
    <li>Lack of user-friendly platforms for creating and managing polls.</li>
    <li>Difficulty in analyzing voting patterns and user preferences.</li>
    <li>Lack of personalized poll recommendations in existing systems.</li>
</ul>


## Objectives:
<ul>
    <li>Simplify poll creation and voting.</li>
    <li>Provide insights through voting results.</li>
    <li>Recommend polls to users based on their voting history.</li>
</ul>

## Technologies Used:
<ul>
        <li>Frameworks and Libraries:</li>
        <ul>
            <li>Backend: Flask (Python), SQLAlchemy</li>
            <li>Frontend: HTML, CSS, Jinja2</li>
            <li>Analysis: Matplotlib, Pandas</li>
            <li>Authentication: Flask-Login</li>
            <li>Recommendation: Scikit-Learn</li>
        </ul>
        <li>Database: SQLite</li>
        <li>Version Control: Git/GitHub</li>
</ul>


## Key Features of Project:
<ol>
    <li>Secure login and registration.</li>
    <li>Role-based access control: granting superuser privileges to select users.</li>
    <li>Poll Creation and Voting:</li>
    <ol>
        <li>Voting is restricted to logged-in users.</li>
        <li>Vote Results Visualization: Poll results are displayed in an easy-to-understand format.</li>
        <li>Poll Sharing using Link and QR code.</li>
        <li>Reporting on inappropriate polls by users.</li>
    </ol>
    <li>Beautiful Minimal UI.</li>
    <li>Data Analytics:</li>
    <ol>
        <li>Analysis of poll results in the form of various graphs based on user demographics (anonymous data).</li>
    </ol>
    <li>Personalized Recommendations: Suggest polls based on a user's voting history using Machine Learning.</li>
</ol>

## Class Diagram:


## UI Screenshots:

## Running the web-app:
1) Clone this repository / Or download zip and unzip the repository
2) Navigate to poll_app folder
3) Run command: <b>flask --app run.py run --debug</b>
4) Open Browser and Navigate to: <a href="http://localhost:5000/">http://localhost:5000/</a>

