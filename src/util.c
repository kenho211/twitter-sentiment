/*
 * File       : util.c
 * Author     : Douglas Anderson
 * Description: This file contains various miscellaneous functions
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globals.h"
#include "util.h"
#include "scan.h"

void printToken(token_t token_type, char* token_str){
    switch(token_type){
        case WORD:
            fprintf(output_file, "word\t%s\n", token_str);
            break;
        case NUMBER:
            fprintf(output_file, "num \t%s\n", token_str);
            break;
        case USER:
            fprintf(output_file, "user\t%s\n", token_str);
            break;
        case HASHTAG:
            fprintf(output_file, "hash\t%s\n", token_str);
            break;
        case URL:
            fprintf(output_file, "url \t%s\n", token_str);
            break;
        case EMOTICON:
            fprintf(output_file, "emot\t%s\n", token_str);
            break;
        case PUNCT:
            fprintf(output_file, "punc\t%s\n", token_str);
            break;
        case ERROR:
            /*fprintf(output_file, "ERROR\t%s  \n", token_str); // Hiding the error*/
            break;
        default: fprintf(output_file, "Unknown Token\t%s\n", token_str);
    }
}

