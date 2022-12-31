#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <sys/types.h>
#include <string.h>
#include <regex.h>
#include <errno.h>
#include <ctype.h>

//removes desired characters from a string
void removeSubstr (char *string, char *sub) {
    char *match;
    int len = strlen(sub);
    while ((match = strstr(string, sub))) {
        *match = '\0';
        strcat(string, match+len);
    }
}

//equivalent of strip() function in python
char *strstrip(char *s)
{
        size_t size;
        char *end;

        size = strlen(s);

        if (!size)
                return s;

        end = s + size - 1;
        while (end >= s && isspace(*end))
                end--;
        *(end + 1) = '\0';

        while (*s && isspace(*s))
                s++;

        return s;
}

//fetch the desired line from a file and returns it's pointers
char *fetchline(char* regex, char* fileName, char* match){
    FILE *fp;
    char *line;
    int retval = 0;
    regex_t re;
    regmatch_t rm[2];
  
    if (regcomp(&re, regex, REG_EXTENDED) != 0)
    {
        fprintf(stderr, "Failed to compile regex '%s'\n", regex);
    }

    fp = fopen(fileName, "r");
    if (fp == 0)
    {
        fprintf(stderr, "Failed to open file %s (%d: %s)\n", fileName, errno, strerror(errno));
    }

    bool flag = false; 
    while ((fgets(line, 1024, fp)) != NULL)
    {
        line[strcspn(line, "\n")] = '\0';
        if ((retval = regexec(&re, line, 2, rm, 0)) == 0)
        {
            char arr[8];
            strcpy(arr,line + rm[0].rm_so);
            removeSubstr(arr, " NO");
            arr[8] = '\0';
            
            if(strcmp(match,arr) == 0){
                return line;
            }
            else{
                flag = false;
                continue;
            }
        }
    } 
    if(flag == false){
        return NULL;
    }
}


//use findAndReplace function instead; written below; Ignore this
char* replaceWord(const char* s, const char* oldW, 
                const char* newW) 
{ 
    char* result; 
    int i, cnt = 0; 
    int newWlen = strlen(newW); 
    int oldWlen = strlen(oldW); 
  
    // Counting the number of times old word 
    // occur in the string 
    for (i = 0; s[i] != '\0'; i++) { 
        if (strstr(&s[i], oldW) == &s[i]) { 
            cnt++; 
  
            // Jumping to index after the old word. 
            i += oldWlen - 1; 
        } 
    } 
  
    // Making new string of enough length 
    result = (char*)malloc(i + cnt * (newWlen - oldWlen) + 1); 
  
    i = 0; 
    while (*s) { 
        // compare the substring with the result 
        if (strstr(s, oldW) == s) { 
            strcpy(&result[i], newW); 
            i += newWlen; 
            s += oldWlen; 
        } 
        else
            result[i++] = *s++; 
    } 
  
    result[i] = '\0'; 
    return result; 
} 


//finds a string in a file and replaces it; but the the change is reflected in diff file(for eg, I want to replace RRR with TYU in Walletdetails.txt then it will create a new file Walletdetails1.txt)
void findAndReplaceInFile(char* readfile, char* newfile, char*to_replace,char* replacement)
{
    FILE *ifp, *ofp;
    char word[100], ch, read[100], replace[100];
    int word_len, i, p = 0;
 
    ifp = fopen(readfile, "r");
    ofp = fopen(newfile, "w+");
    if (ifp == NULL || ofp == NULL) {
        printf("Can't open file.");
        exit(0);
    }
 
    // // displaying file contents
    // while (1) {
    //     ch = fgetc(ifp);
    //     if (ch == EOF) {
    //         break;
    //     }
    //     printf("%c", ch);
    // }
 
    strcpy(word, to_replace);
    strcpy(replace,replacement);
 
    // removes the newline character from the string
    // word[strlen(word) - 1] = word[strlen(word)];
 
 
    // // removes the newline character from the string
    // replace[strlen(replace) - 1] = replace[strlen(replace)];
 
    // fprintf(ofp, "%s - %s\n", word, replace);
 
    // comparing word with file
    rewind(ifp);
    while (!feof(ifp)) {
 
        fscanf(ifp, "%s", read);
 
        if (strcmp(read, word) == 0) {
 
            // for deleting the word
            strcpy(read, replace);
        }
 
        // In last loop it runs twice
        fprintf(ofp, "%s ", read);
    }
 
    // Printing the content of the Output file
    rewind(ofp);
    while (1) {
        ch = fgetc(ofp);
        if (ch == EOF) {
            break;
        }
        // fprintf("%c", ch);
    }
 
    fclose(ifp);
    fclose(ofp);
}





// check for memberships
// void cformem(char* carnum)
// {
//     FILE *fp;
//     char line[1024];
//     int retval = 0;
//     regex_t re;
//     regmatch_t rm[2];
//     const char *filename = "Personaldetails.txt";
  
//     if (regcomp(&re, "[A-Z][A-Z][A-Z]\\-[0-9][0-9][0-9]", REG_EXTENDED) != 0)
//     {
//         fprintf(stderr, "Failed to compile regex '%s'\n", "[A-Z][A-Z][A-Z]\\-[0-9][0-9][0-9]");
//     }
//     // printf("Regex: %s\n", "[A-Z][A-Z][A-Z]\\-[0-9][0-9][0-9]");
//     // printf("Number of captured expressions: %zu\n", re.re_nsub);

//     fp = fopen(filename, "r");
//     if (fp == 0)
//     {
//         fprintf(stderr, "Failed to open file %s (%d: %s)\n", filename, errno, strerror(errno));
//     }

//     while ((fgets(line, 1024, fp)) != NULL)
//     {
//         line[strcspn(line, "\n")] = '\0';
//         if ((retval = regexec(&re, line, 2, rm, 0)) == 0)
//         {
//             printf("%s\n", line);
//             // Complete match
//             char arr[8];
//             strcpy(arr,line + rm[0].rm_so);
//             removeSubstr(arr, " NO");
//             arr[8] = '\0';

//             printf("reg number %s\n",arr);
//             // printf("length %lu\n",strlen(arr));
//             // printf("strcmp %u\n",strcmp(carnum,arr));
            
//             if(strcmp(carnum,arr) == 0){
//                 printf("Line: %.*s\n", (int)(rm[0].rm_eo - rm[0].rm_so), line + rm[0].rm_so);
//                 // Match captured in (...) - the \( and \) match literal parenthesis
//                 printf("Text: %.*s\n", (int)(rm[1].rm_eo - rm[1].rm_so), line + rm[1].rm_so);
//                 char *src = line + rm[1].rm_so;
//                 char *end = line + rm[1].rm_eo;
//                 while (src < end)
//                 {
//                     size_t len = strcspn(src, " ");
//                     if (src + len > end)
//                         len = end - src;
//                     printf("Name: <<%.*s>>\n", (int)len, src);
//                     src += len;
//                     src += strspn(src, " ");
//                 }
//             }
//             break;
//         }
//     } 
// }
