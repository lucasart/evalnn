#include "nn.h"

static void train(FILE *in)
{
    (void)in;
}

int main(int argc, char **argv)
{
    if (argc == 2 && argv[1][0] != '-') {
        FILE *in = fopen(argv[1], "rb");
        if (in) {
            train(in);
            fclose(in);
        } else
            printf("cannot read from '%s'\n", argv[1]);
    } else {
        printf("Syntax: %s samples.bin\n", argv[0]);
        puts("samples.bin: sample file in binary format, as produced by c-chess-cli");
    }

    return 0;
}
