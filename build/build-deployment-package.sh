#!/bin/bash
set -e

# To Do:
# - Set absolute paths as variables
# - Refactor (folder checks can probably move into functions, paths to check can probably be a list & then loop through them all)

not_found () {
  printf "\n\n------------------------------------------------------------"
  printf "\n\nDid you mount the project folder into the docker container?"
  printf "\n\nTry this: \n\ndocker run -v \$\(pwd\):/usr/src/app wlabatey/python-build:latest"
  printf "\n\nOr maybe you didn't run with docker-compose? Is the correct docker-compose.yml file still here?"
  printf "\n\nTry: \n\ndocker-compose up"
  printf "\n\nOr maybe the project folder structure has changed?"
  printf "\n\n------------------------------------------------------------\n\n"
}

printf "\n\n----------------------------------------"
printf "\nChecking project folder structure..."
printf "\n------------------------------------------"

printf "\n\nChecking for scraper folder... "
if [[ -d /usr/src/app/scraper ]]; then
  printf "scraper directory found!"
else
  printf "\n\n| ERROR | scraper folder not found..."
  not_found
  exit 1
fi

printf "\n\nChecking for dist folder... "
if [[ -d /usr/src/app/dist ]]; then
  printf "dist directory found!"
  printf "\n\nChecking for /dist/src... "
  if [[ -d /usr/src/app/dist/src ]]; then
    printf "src directory found!"
    printf "\n\nclearing..."
    rm -rf /usr/src/app/dist/src/ 
    mkdir -p /usr/src/app/dist/src/ 
  else
    printf "\n\n| WARNING | /dist/src folder not found... "
    printf "creating..." 
    mkdir -p /usr/src/app/dist/src
  fi
  printf "\n\nChecking for /dist/bundle... "
  if [[ -d /usr/src/app/dist/bundle ]]; then
    printf "bundle directory found!" 
    printf "\n\nclearing..."
    rm -rf /usr/src/app/dist/src/ 
    mkdir -p /usr/src/app/dist/src/ 
  else
    printf "\n\n| WARNING | /dist/bundle folder not found... "
    printf "creating..."
    mkdir -p /usr/src/app/dist/bundle
  fi
else
  printf "\n\n| WARNING | dist folder not found... "
  printf "creating..." 
  mkdir -p /usr/src/app/dist/src
  mkdir /usr/src/app/dist/bundle
fi

printf "\n\nChecking for virtualenv folder... "
if [[ -d /usr/src/app/virtualenv ]]; then
  printf "virtualenv folder found!"
  printf "\n\nclearing..."
  rm -rf /usr/src/app/virtualenv/
  mkdir -p /usr/src/app/virtualenv/
else
  printf "\n\n| WARNING | virtualenv folder not found... "
  printf "creating..."
  mkdir -p /usr/src/app/virtualenv
fi

printf "\n\n----------------------------------------"
printf "\nChecking python, pip & virtualenv..."
printf "\n------------------------------------------\n\n"

command -v python >/dev/null 2>&1 || { printf "\n\n| ERROR | Python is not installed." ; exit 1; }
python --version && printf "\n"
command -v pip >/dev/null 2>&1 || { printf "\n\n| ERROR | Pip is not installed." ; exit 1; }
pip --version && printf "\n"
command -v virtualenv >/dev/null 2>&1 || { printf "\n\n| ERROR | Virtualenv is not installed." ; exit 1; }
printf "virtualenv $(virtualenv --version)\n"


printf "\n\n--------------------------------------------------------"
printf "\nCreating virtual environment & installing dependencies..."
printf "\n--------------------------------------------------------\n\n"

printf "\n\nCreating virtual environment...\n\n"
virtualenv -p $(which python2) /usr/src/app/virtualenv

printf "\n\nActivating virtual environment...\n\n"
source /usr/src/app/virtualenv/bin/activate

printf "\n\nInstalling dependencies...\n\n"
pip install -r /usr/src/app/scraper/requirements.txt

printf "\n\n----------------------------------------------------"
printf "\nCopying source code & dependencies to dist/src folder"
printf "\n----------------------------------------------------\n\n"

printf "\n\nCopying pip packages...\n\n"
cd /usr/src/app/virtualenv/lib/python2.7/site-packages/ && cp -rf . /usr/src/app/dist/src/

printf "\n\nCopying source code from scraper folder...\n\n"
cd /usr/src/app/scraper/ && cp -rf . /usr/src/app/dist/src/

printf "\n\nCreating zip file...\n\n"
cd /usr/src/app/dist/src/ && zip -r9 /usr/src/app/dist/bundle/lambda-bundle.zip .

printf "\n---------------------------------------------------"
printf "\n  ⚡️ Deployment package created successfully!  ⚡️  "
printf "\n---------------------------------------------------\n\n"
exit 0 

##### CHECK PROJECT FILES / FOLDERS / DEPENDENCIES

# Check for job_scraper folder in current directory (/usr/src/app in container).

# If not found, exit with error. Remind to mount project directory to /usr/src/app in container.
# If found, check for dist folder.
# If dist folder found, echo folder has been found.
# If found & not empty, clear contents.
# If not found, prompt to create dist folder.
# Check for dist/src & dist/bundle, if not found then create
# Check for virtualenv folder.
# If found, echo virtualenv doler has been found.
# If found & not empty, clear contents.

# Check for existence of python2 & virtualenv.
# If python2 exists, Create python2 virtualenv environment inside virtualenv folder

# Check for existence of pip.

# pip install all dependencies from requirements.txt
# Recursively copy all pip packages from virtualenv/lib/python2.7/site-packages* to dist/src* (make sure . files/folders get copied too)
# Recursively copy all files from job_scraper/* to dist/src/
# Check for existence of .zip files in dist/bundle. If found, count number and add total + 1 to name of zip file. 
# Zip all files in dist/src/* to dist/bundle/lambda-bundle{1}.zip
# Exit with status 0
