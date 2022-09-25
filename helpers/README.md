# Python env setup
run
``` bash
# python venv and pip install airflow
source ./helpers/python-env-prepare.sh
```

# Init airflow
run
``` bash
#initialize db for airflow
export workdir=workdir
mkdir $workdir
cd $workdir
source ../helpers/init-vars.sh
source ../helpers/fresh-start.sh
#a password prompt will appear to set password
``` 

# Start airflow web
run
``` bash
# assuming workdirectory has changed to $workdir
# environment vairable must be set
source ../helpers/init-vars.sh
source ../helpers/run-web.sh
```

# Start airflow scheduler
run
``` bash
# run this on a separate shell
# assuming workdirectory has changed to $workdir
# environment vairable must be set
source ../helpers/init-vars.sh
source ../helpers/run-scheduler.sh
```
