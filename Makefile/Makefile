#https://opensource.com/article/18/8/what-how-makefile
#Most open source projects use make to compile a final executable binary, which can then be installed using make install.

.PHONY: all hello compile clean
FILE = hello.py
OUTPUT_FILE = python.txt

all: hello compile
	@echo ${FILE}

#phony target
hello:
	@echo "Hello World"

run: ${FILE}
	@echo "Running ${FILE}"
	@python hello.py

compile:
	@echo "Compiling python file ${FILE} unnecessary. Python files are interpreted."

#clean should always be called manually
clean: ${OUTPUT_FILE}
	@echo "Cleaning up..."
	rm ${OUTPUT_FILE}