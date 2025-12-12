Steps to execute tests


1. After copying the repository, create a virtual environment(venv) in your system
2. Install dependencies using 'pip install -r requirements.txt' command
3. Download a chromedriver(version 143) and add chromedriver.exe it to your system path
   - For mac/linux -> /usr/local/bin
   - For windows -> add the path of the folder where you downloaded chromedriver.exe to your system path
4. Depending on your system, execute run_tests.sh(for Mac/Linux) or run_tests.bat(for Windows)
5. The tests will generate a test reports in reports/ folder and a csv file containing product data
