<a name="readme-top"></a>

<h1 align="center">Projeto Job Insights 📊</h1>

<details>
  <summary>Sumário</summary><br />
  <ol>
    <li><a href="#sobre-o-projeto">Sobre o Projeto</a></li>
    <li><a href="#tecnologias">Tecnologias</a></li>
    <li><a href="#funcionalidades">Funcionalidades</a></li>
    <li><a href="#como-executar-o-projeto">Como Executar o Projeto</a></li>
    <li><a href="#habilidades">Habilidades</a></li>
    <li><a href="#sobre-a-trybe">Sobre a Trybe</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

## Sobre o Projeto

Projeto **29** do curso de Desenvolvimento Web da [Trybe][trybe-site-url].

O Job Insights é uma aplicação desenvolvida em [Python][python-url] direcionada a análises de dados reais de empregos. Sua implementação foi incorporada a um aplicativo web desenvolvido com [Flask][flask-url], permitindo que a pessoa usuária possa realizar consultas e utilizar diferentes filtros para resultados mais acurados.

Os dados foram extraídos do site [Glassdoor][glassdor-site-url] e obtidos através do [Kaggle][kaggle-site-url].

> ℹ️ Todo aplicativo web em Flask foi desenvolvido e disponibilizado pela Trybe. Fui responsável somente pela implementação da rota `/job/<index>`.

> ℹ️ As funções implementadas por mim estão em `src/insights`.

> ℹ️ Escrevi testes para funções implementadas pela Trybe. Tais testes podem ser encontrados nos diretórios `brazilian`, `counter` e `sorting` de `tests`.

<br/>

## Tecnologias

O projeto foi desenvolvido em [Python][python-url]. As implementações foram incorporadas a um aplicativo web desenvolvido com o framework [Flask][flask-url]. Os testes foram escritos com [Pytest][pytest-url] e a qualidade de código foi garantida com o linter [Flake8][flake8-url].

[![Python][python-badge]][python-url] [![Flask][flask-badge]][flask-url] [![Pytest][pytest-badge]][pytest-url] [![Flake8][flake8-badge]][flake8-url]

<br/>

## Funcionalidades

<ul>
  <li>Acessar um conjunto de dados sobre empregos.</li>
  <li>Filtrar os dados de acordo com o tipo de trabalho (Ex.: temporário, estágio...).</li>
  <li>Filtrar os dados de acordo com o setor das empresas.</li>
  <li>Filtrar os dados de acordo com o salário anual.</li>
  <li>Controlar a quantidade de linhas que aparecem a cada consulta.</li>
  <li>Acessar páginas específicas de cada trabalho, as quais exibem todas as informações relacionadas a cada trabalho.</li>
</ul>

<br/>

## Como Executar o Projeto

Para rodar o projeto localmente, siga os passos abaixo.

1. Clone o repositório.

```
git clone git@github.com:garciaagui/trybe-project-29_jobs-insights.git
```

2. Navegue até a raiz do projeto.

```
cd trybe-project-29_jobs-insights/
```

3. Crie o ambiente virtual.

```
python3 -m venv .venv
```

4. Ative o ambiente virtual.

```
source .venv/bin/activate
```

- Note que no começo da linha do terminal haverá `(.venv)`, como no exemplo abaixo.

```
(.venv) gui@gui-desktop:~/Trybe/projetos-trybe-personal/trybe-project-29_jobs-insights$
```

- Para desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativá-lo novamente quando retornar ao projeto.

5. Instale as dependências no ambiente virtual.

```
python3 -m pip install -r dev-requirements.txt
```

6. Inicialize a aplicação flask com o comando abaixo e acesse `http://localhost:5000` em seu navegador.

```
flask run
```

<details>
  <summary><strong> ℹ️ Para instruções adicionais, clique aqui.</strong></summary><br />

- 🧪 Para rodar **todos** os testes, execute o comando abaixo.

```
python3 -m pytest
```

- 🧪 Para rodar apenas um arquivo de teste, siga o exemplo abaixo.

```
python3 -m pytest tests/nomedoarquivo.py
```

- 🧪 Para rodar apenas um teste específico, siga o exemplo abaixo.

```
python3 -m pytest -k nome_da_func_de_tests
```

- Caso deseje fazer testes manuais diretamente nos módulos onde as funções foram implementadas, siga o exemplo abaixo.

```
python3 -m src.insights.jobs
```

</details>

<br/>

## Habilidades

<ul>
  <li>Utilizar o terminal interativo do Python.</li>
  <li>Utilizar estruturas condicionais e de repetição.</li>
  <li>Utilizar funções built-in do Python.</li>
  <li>Utilizar tratamento de exceções.</li>
  <li>Realizar a manipulação de arquivos.</li>
  <li>Escrever funções.</li>
  <li>Escrever testes com Pytest.</li>
  <li>Escrever módulos e importá-los em outros códigos.</li>
  <li>Implementação de páginas em Flask.</li>
</ul>

<br/>

## Sobre a Trybe

_"A [Trybe][trybe-site-url] é uma escola do futuro para qualquer pessoa que queira melhorar de vida e construir uma carreira de sucesso em tecnologia, onde a pessoa só paga quando conseguir um bom trabalho."_

_"O programa conta com mais de 1.500 horas de aulas presenciais e online, aborda introdução ao desenvolvimento de software, front-end, back-end, ciência da computação, engenharia de software, metodologias ágeis e habilidades comportamentais._"

<br/>

## Contato

Projeto desenvolvido por Guilherme Garcia. Seguem abaixo minhas redes sociais e meios de contato. 🤘

[![Gmail][gmail-badge]][gmail-url]
[![Linkedin][linkedin-badge]][linkedin-url]
[![GitHub][github-badge]][github-url]
[![Instagram][instagram-badge]][instagram-url]

<p align="right"><a href="#readme-top">Voltar ao topo</a></p>

<!-- MARKDOWN LINKS & IMAGES -->

[trybe-site-url]: https://www.betrybe.com/
[glassdor-site-url]: https://www.glassdoor.com.br/index.htm
[kaggle-site-url]: https://www.kaggle.com/datasets/atharvap329/glassdoor-data-science-job-data
[flake8-url]: https://flake8.pycqa.org/en/latest/
[flake8-badge]: https://img.shields.io/badge/Flake8-000000?style=for-the-badge&logo=flake8&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[flask-badge]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[pytest-url]: https://docs.pytest.org/en/7.2.x/
[pytest-badge]: https://img.shields.io/badge/-Pytest-0A9EDC?logo=pytest&logoColor=white&style=for-the-badge
[python-url]: https://www.python.org/
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:garciaguig@gmail.com
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/garciaagui/
[github-badge]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/garciaagui
[instagram-badge]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://www.instagram.com/garciaagui/
