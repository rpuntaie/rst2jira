#!/bin/sh
# Runs rst2jira.py on all .rst files in test/ and compares them
# to the expected output (.exp)
if [ $# -eq 0 ]; then
    files=test/*.rst
else
    files="$*"
fi

for i in $files; do
    echo -n Testing $i
    expFile="$i.exp"
    outFile="$i.out"
    diffFile="$i.diff"

    options=""
    case $i in test/excerpt-enabled*)
        options="--excerpt"
    esac

    ./scripts/rst2jira.py $options "$i" > "$outFile" --traceback
    if [ $? -ne 0 ]; then
        echo -e "\e[00;31merror running scripts/rst2jira.py\e[00m"
        exit 1
    fi

    if [ ! -f "$expFile" ]; then
        expFile=/dev/null
    fi

    diff -u "$expFile" "$outFile" > "$diffFile"
    if [ "$?" -ne "0" ]; then
        echo -e "\e[00;31merror\e[00m"
        cat "$diffFile" | colordiff
        exit 2
    else
        #all fine
        echo -e "\e[00;32mok\e[00m"
        rm "$outFile"
        rm "$diffFile"
    fi
done
