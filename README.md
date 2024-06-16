# luigi-data-pipelines
Playing with Luigi, Python, SQLite, AWS S3

Environment setup:
- Using WSL2 on Windows
- Ubuntu 22.04.3 LTS

- Python 3
$ sudo apt update  
$ sudo apt install python3  
$ python3 --version  
Python 3.10.12  

- Create virtual environments
$ sudo apt update  
$ sudo apt install python3.10-venv  
$ python3.10 -m venv ~/envs/playing-with-luigi  
$ source ~/envs/playing-with-luigi/bin/activate  

- Install Luigi
$ pip list  
$ pip install luigi  

- Run Linux GUI apps on the Windows Subsystem for Linux
https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps  

- Install PyCharm Community
- Download pycharm-community-2024.1.2.tar.gz
$ tar -xvzf pycharm-community-2024.1.2.tar.gz  
$ mkdir sw  
$ tar -xvzf ~/Download/pycharm-community-2024.1.2.tar.gz -C ~/sw  
$ cd sw/  
$ cd pycharm-community-2024.1.2/  
$ cd bin/  
$ ./pycharm.sh  

- Install SQLite
$ sudo apt update  
$ sudo apt install sqlite3  
$ sqlite3 --version  

- AWS S3
AWS Credentials  
AWS_ACCESS_KEY_ID: XXXXX  
AWS_SECRET_ACCESS_KEY: xxxxx  

Data Pipelines:
- hello-world: simple data pipeline with one task
- two-sequential-tasks: data pipeline with two sequential tasks
- three-sequential-tasks: data pipeline with three sequential tasks
- three-parallel-tasks: data pipeline with three parallel tasks
- parallel-and-sequential-tasks: data pipeline with parallel and sequential tasks
- many-tasks: data pipeline with many tasks
- dynamic-tasks: data pipeline with dynamic tasks
