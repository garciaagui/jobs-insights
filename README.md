<a name="readme-top"></a>

<h1 align="center">Job Insights 📊</h1>

> [🇧🇷 Clique aqui para acessar a versão em português.](README_pt-br.md)

## Summary

<ol>
  <li><a href="#description">Description</a></li>
  <li><a href="#technologies">Technologies</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#how-to-run">How to Run</a></li>
  <li><a href="#about-trybe">About Trybe</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

## Description

**29th project** of the [Trybe][trybe-site-url] Web Development course.

Job Insights is an application developed in [Python][python-url] aimed at analyzing real job data. Its implementation was incorporated into a web application developed with [Flask][flask-url], allowing the user to make queries and use different filters for more accurate results.

The data was extracted from the [Glassdoor][glassdor-site-url] website and obtained through [Kaggle][kaggle-site-url].

> ℹ️ The entire Flask web application was developed and provided by Trybe. Of all the routes, I implemented only `/job/<index>`.

> ℹ️ The functions implemented by me are in `src/insights`.

> ℹ️ I wrote tests for the functions implemented by Trybe. These tests can be found in the `brazilian`, `counter`, and `sorting` subdirectories of `tests`.

![Project Jobs Insights][project-demo]

<br/>

## Technologies

The project was developed in [Python][python-url]. The implementations were incorporated into a web application developed using the [Flask][flask-url] framework and [Jinja][jinja-url] templates. The tests were written using [Pytest][pytest-url], and code quality was ensured using the [Flake8][flake8-url] linter.

[![Python][python-badge]][python-url] [![Flask][flask-badge]][flask-url] [![Jinja][jinja-badge]][jinja-url] [![Pytest][pytest-badge]][pytest-url] [![Flake8][flake8-badge]][flake8-url]

<br/>

## Features

<ul>
  <li>Access a set of job-related data.</li>
  <li>Filter the data according to the job type (e.g. temporary, internship...).</li>
  <li>Filter the data according to the industry sector.</li>
  <li>Filter the data according to the annual salary.</li>
  <li>Control the number of rows displayed in each query.</li>
  <li>Access specific pages for each job, which display all the information related to that job.</li>
</ul>

<br/>

## How to Run

To run the project locally, follow the steps below.

1. Clone the repository.

```
git clone git@github.com:garciaagui/jobs-insights.git
```

2. Navigate to the root of the project.

```
cd jobs-insights/
```

3. Create the virtual environment.

```
python3 -m venv .venv
```

4. Activate the virtual environment.

```
source .venv/bin/activate
```

- Note that at the beginning of the terminal line there will be `(.venv)`, as in the example below.

```
(.venv) gui@gui-desktop:~/Trybe/jobs-insights$
```

- To deactivate the virtual environment, run the command `deactivate`. Remember to activate it again when you return to the project.

5. Install dependencies in the virtual environment.

```
python3 -m pip install -r dev-requirements.txt
```

6. Initialize the Flask application with the command below and access `http://localhost:5000` in your browser.

```
flask run
```

<details>
  <summary><strong> ℹ️ For additional instructions, click here.</strong></summary><br />

- 🧪 To run **all** tests, execute the command below.

```
python3 -m pytest
```

- 🧪 To run only one test file, follow the example below.

```
python3 -m pytest tests/sorting/test_sorting.py
```

- 🧪 To run only one specific test, follow the example below.

```
python3 -m pytest -k test_sort_by_max_salary_criteria
```

- If you wish to manually test directly in the modules where the functions were implemented, follow the example below.

```
python3 -m src.insights.jobs
```

</details>

<br/>

## About Trybe

_"[Trybe][trybe-site-url] is a future school for anyone who wants to improve their lives and build a successful career in technology, where the person only pays when they get a good job."_

_"The program features over 1,500 hours of online classes covering introduction to software development, front-end, back-end, computer science, software engineering, agile methodologies, and behavioral skills."_

<br/>

## Contact

Project developed by **Guilherme Garcia**. Below are my social networks and means of contact. 🤘

[![Gmail][gmail-badge]][gmail-url]
[![Linkedin][linkedin-badge]][linkedin-url]
[![GitHub][github-badge]][github-url]
[![Instagram][instagram-badge]][instagram-url]

<p align="right"><a href="#readme-top">Back to top</a></p>

<!-- MARKDOWN LINKS & IMAGES -->

[project-demo]: ./project-demo.gif
[trybe-site-url]: https://www.betrybe.com/
[glassdor-site-url]: https://www.glassdoor.com.br/index.htm
[kaggle-site-url]: https://www.kaggle.com/datasets/atharvap329/glassdoor-data-science-job-data

<!-- STACKS -->

[flake8-url]: https://flake8.pycqa.org/en/latest/
[flake8-badge]: https://img.shields.io/badge/Flake8-000000?style=for-the-badge&logo=flake8&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[flask-badge]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[jinja-url]: https://jinja.palletsprojects.com/en/3.1.x/
[jinja-badge]: https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=jinja&logoColor=white
[pytest-url]: https://docs.pytest.org/en/7.2.x/
[pytest-badge]: https://img.shields.io/badge/-Pytest-0A9EDC?logo=pytest&logoColor=white&style=for-the-badge
[python-url]: https://www.python.org/
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

<!-- CONTACT -->

[gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:garciaguig@gmail.com
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/garciaagui/
[github-badge]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/garciaagui
[instagram-badge]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://www.instagram.com/garciaagui/
