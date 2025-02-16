Ru: # GitHub Repository Parser

Этот проект представляет собой парсер для поиска лучших репозиториев на GitHub по различным темам. Он использует GitHub API для получения данных о репозиториях, отсортированных по количеству звезд, и выводит информацию о наиболее популярных репозиториях по указанной теме.

## Описание

Парсер позволяет искать репозитории по ключевым словам, например, "Python", "Machine Learning", "Web Development" и другим. Для каждой темы выводится информация о топ-3 репозиториях, включая:

- Имя репозитория
- Владелец репозитория
- Количество звезд
- Описание репозитория
- Ссылка на репозиторий

## Как использовать

1. Клонируй репозиторий на свой локальный компьютер:

    
    git clone https://github.com/твое_имя/название_репозитория.git
   

3. Установи необходимые библиотеки (если еще не установлены):

    
    pip install requests
  

4. Запусти скрипт, указав тему поиска:

    
    get_github_repos("Python")  # Для поиска репозиториев по Python
    get_github_repos("Machine Learning")  # Для поиска репозиториев по Machine Learning
    

    Ты можешь изменить тему поиска, просто заменив строку в функции `get_github_repos()` на любой другой запрос, который тебя интересует (например, "JavaScript", "Data Science", "AI").

## Как изменить темы

Чтобы изменить тему для поиска, нужно просто передать новый запрос в функцию `get_github_repos`. Например:


get_github_repos("Web Development")  # Для поиска репозиториев по Web Development
get_github_repos("Data Science")  # Для поиска репозиториев по Data Science

Eng: # Github Repository Parser

This project is a parser for finding the best repositories on GitHub on various topics. He uses the GitHub API to obtain data on repositories sorted by the number of stars, and displays information about the most popular repositories on the specified topic.

## Description
Parser allows you to look for repositories by keywords, for example, Python, Machine Learning, Web Development and others. For each topic, information about the top 3 repositories is displayed, including:

- The name of the repository
- The owner of the repository
- The number of stars
- Description of the repository
- Link to the repository

## How to use

1.
Clon the repository on your local computer:

    
    GIT CLONE https://github.com/ Imoy_im/Roadsaurium.git
   

3. Install the necessary libraries (if not yet installed):

    
    Pip Install Reques
  

4. Launch the script, indicating the topic of the search:

    
    Get_GITHUB_REPOS ("Python") # to search for repositories by Python
Get_github_repos ("Machine Learning") # to search for repositories by Machine Learning
    

    You can change the search topic by simply replacing the line in the function `get_github_repos ()` on any other request that interests you (for example, "JavaScript", "Data Science", "Ai").

## how to change topics

To change the topic for the search,
You just need to transfer a new request to the `get_github_repos` function. For example:


Get_GITHUB_REPOS ("Web Development") # to search for repositories by Web Development
Get_GITHUB_REPOS ("Data Science") # to search for repositories by Data Science
