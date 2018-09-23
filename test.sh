#!/usr/bin/env bash


curl -X POST -d $'x=5\nb=x\nreturn b\n' -H "Content-Type: text/plain" localhost:922/run
