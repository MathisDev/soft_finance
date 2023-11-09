# compile tools
CC =	gcc
FL =	-Wall -Werror -Wextra
COMP =	$(CC) $(FL)
EX =	prog
# SRC
SRC = run.c

train:
	$(COMP) $(SRC) -o $(EX)
	./$(EX)
clean:
	rm $(EX)
re:	clean run
