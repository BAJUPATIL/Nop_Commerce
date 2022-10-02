pytest -rA -m "sanity" --html=./Reports/reportssanity.html testCases/ --browser chrome

REM pytest -rA -m "sanity or regression" --html=./Reports/reportssanity.html testCases/ --browser chrome
REM pytest -rA -m "regression" --html=./Reports/reportssanity.html testCases/ --browser chrome
REM pytest -rA -m "regrission" --html=./Reports/reportssanity.html testCases/ --browser chrome