# 1. Example
CFLAGS ?= -g

all: helloworld

helloworld: helloworld.o
  $(CC) $(LDFLAGS) -o $@ $^

helloworld.o: helloworld.c
  $(CC) $(CFLAGS) -c -o $@ $<

clean: FRC
  rm -f helloworld helloworld.o