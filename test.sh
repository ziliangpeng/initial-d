#!/usr/bin/env bash


curl -X POST -d $'x=5\nb=x\nreturn b\n' -H "Content-Type: text/plain" localhost:922/run; echo ""
# EXPECT: 5


curl -X POST -d $'x=6\ny=9\nz=x*y\nreturn z\n' -H "Content-Type: text/plain" localhost:922/run; echo ""
# EXPECT: 54


curl -X POST -d $'x= 6\ny =9\nz=x *y\n a= z\nz=a+x \nreturn z\n' -H "Content-Type: text/plain" localhost:922/run; echo ""
# x = 6
# y = 9
# z = x * y = 54
# a = z = 54
# z = a + x = 54 + 6 = 60
# EXPECT: 60


curl -X POST -d $'x= 6\ny =9\nz=x *y\n a= z\nz=a+b \nreturn z\n' -H "Content-Type: text/plain" localhost:922/run; echo ""
# b undefined
# EXPECT: error


curl -X POST -d $'x= 6\ny=7\nreturn x\n return y' -H "Content-Type: text/plain" localhost:922/run; echo ""
# return x first
# EXPECT: 6


curl -X POST -d $'x= 6\ny=7+4\nreturn x\n return y' -H "Content-Type: text/plain" localhost:922/run; echo ""
# cannot do 7+4
# EXPECT: error

curl -X POST -d $'x = 5\ny = 6\nz = 7\na = x + y\nb = a * z\nreturn b' -H "Content-Type: text/plain" localhost:922/run; echo ""
# official example
# EXPECT: 77
