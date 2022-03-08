#!/bin/sh

# Скрипт первым аргументом принимает путь, по которому нужно запустить тесты и линтеры.

PROJECT_DIR=$1 ;
if [ -z $PROJECT_DIR ]; then
    PROJECT_DIR=$(pwd)
fi

RESULT_CODE=0 ;

ALL_PACKAGES_DIRS=$(find $PROJECT_DIR -maxdepth 2 -mindepth 1 -type f -name "__init__.py" -print0 | xargs -0 -n1 dirname)

echo "RUN pytest" ;
pytest tests -o cache_dir=/dev/null --cov || RESULT_CODE=1 ;

echo "RUN black" ;
black --check $ALL_PACKAGES_DIRS || RESULT_CODE=1 ;

echo "RUN pylint" ;
pylint --rcfile=$PROJECT_DIR/.pylintrc $ALL_PACKAGES_DIRS || RESULT_CODE=1 ;

echo "RUN pycodestyle" ;
pycodestyle || RESULT_CODE=1 ;

echo "RUN pydocstyle" ;
pydocstyle --source --count $PROJECT_DIR || RESULT_CODE=1 ;

echo "RUN mypy" ;
mypy --cache-dir=/dev/null --config-file=$PROJECT_DIR/mypy.ini $PROJECT_DIR || RESULT_CODE=1 ;

echo "RESULT_CODE=${RESULT_CODE}" ;
exit $RESULT_CODE
