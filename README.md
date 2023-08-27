# Site of GameCenter
Site for event GameCenter

[![Django CI](https://github.com/kill-your-soul/gamecenter/actions/workflows/django.yml/badge.svg)](https://github.com/kill-your-soul/gamecenter/actions/workflows/django.yml)

## Prerequisites
1. [Git](https://git-scm.com/)
2. [Python 3.8+](https://www.python.org/downloads/)

## Installation

1. Clone the repository

    ```shell
    git clone https://github.com/kill-your-soul/gamecenter.git
    ```
   
2. Create virtual environment 
    
    - For Windows:

        ```Powershell
        python -m venv .venv
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 -m venv .venv
        ```

3. Activate virtual environment

    - For Windows:
    
        ```Powershell
        .\.venv\Scripts\activate
        ```

    - For Linux, MacOS:

        ```shell
        source ./.venv/bin/activate
        ```

4. Install requirements

    - For Windows:

        ```shell
        pip install -r requirements.txt
        ```

    - For Linux, MacOS:
    
        ```shell
        pip3 install -r requirements.txt
        ```

5. Setting environment variables

    - For Windows:

        + Powershell:

            ```Powershell
            $env:SECRET_KEY="TOKEN_TO_YOUR_BOT";
            ```

        + cmd:

            ```cmd
            set SEKRET_KEY=TOKEN_TO_YOUR_BOT
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export SECRET_KEY="TOKEN_TO_YOUR_BOT"
            ```

6. Run site

    - For Windows:

        ```shell
        python manage.py runserver
        ```

    - For Linux, MacOS:
     
        ```shell
        python3 manage.py runserver
        ```