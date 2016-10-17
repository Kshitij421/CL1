%{
  	#include<string.h>
        int insert(char str[]);
        int insert_for_error(char str1[]);
        FILE *fin, *fout;
        char c1[25], c2[25];
        unsigned int n=1, count=0,count1 =0, i,j;
        struct st
        {
                char name[25];
                int value;
        }*symbol[50];
        struct t
	   {
    		char error_ala[50];
    		int kai_ala;
		}*table[50];
         
%}

%%

[ \t]+          ;
	
[\n]+           { fprintf(yyout, "\n"); n++;}


\/\*.*\*\/[ \t\n]*	{ n++; }

\/\/.*[ \t\n]*          { n++; }

\/.+[ \t]*           {fprintf(yyout, " %s ", yytext);  printf("\n%d\t%s\t\t:Unidentified comment\t\t%d", n, yytext, insert_for_error(yytext));}

#               { fprintf(yyout, "# "); printf("\n%d\t#\t\t:Preprocessor", n); }

include         { fprintf(yyout, "include "); printf("\n%d\tinclude\t\t:Keyword", n); }

\<              { fprintf(yyout, "< "); printf("\n%d\t<\t\t:LT", n); }


\>              { fprintf(yyout, "> "); printf("\n%d\t>\t\t:GT", n); }

[a-zA-Z0-9]+\.h { fprintf(yyout, "%s ", yytext); printf("\n%d\t%s\t\t:Header file", n, yytext); }

\(              { fprintf(yyout, "( "); printf("\n%d\t(\t\t:Left bracket", n); }

\)              { fprintf(yyout, ") "); printf("\n%d\t)\t\t:Right bracket", n); }

\{              { fprintf(yyout, "{ "); printf("\n%d\t{\t\t:Opening brace", n); }

\}              { fprintf(yyout, "} "); printf("\n%d\t}\t\t:Closing brace", n); }

\,              { fprintf(yyout, ", "); printf("\n%d\t,\t\t:Comma", n); }

\;              { fprintf(yyout, "; "); printf("\n%d\t;\t\t:End of stmt", n); }


\=|\+|\-|\/|\*  { fprintf(yyout, "%s ", yytext); printf("\n%d\t%s\t\t:Operator", n, yytext); }


void|short|int|long|float|double|char|struct            { fprintf(yyout, "%s ", yytext); printf("\n%d\t%s\t\t:Datatype", n, yytext); }


main|printf|scanf	{ fprintf(yyout, "%s ", yytext); printf("\n%d\t%s\t\t:Built in function", n, yytext); }

\""([^\n\"\\]*(\\[.\n])*)*"\"                       { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:String constant", n, yytext); }

'[a-zA-Z0-9]'                       { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:Character constant", n, yytext); }

[0-9]+          { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:Integer constant", n, yytext); }

[0-9]+\.[0-9]+  { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:Real constant", n, yytext); }

([a-zA-Z]+[_a-zA-Z0-9]*)               { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:Identifier\t\t%d", n, yytext, insert(yytext)); }

\"[_a-zA-Z]* { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:Unidentified delimiter\t\t%d", n, yytext, insert_for_error(yytext)); }

[0-9]+[_a-zA-Z]+ { fprintf(yyout, "%s ", yytext);  printf("\n%d\t%s\t\t:Unidentified token\t\t%d", n, yytext, insert_for_error(yytext)); }

%%

main()
{
        
        fin=fopen("input.txt", "r");
        fout=fopen("output.txt", "w");
        yyin=fin;
        yyout=fout;
        printf("\n_________________________________________________________");
        printf("\nLINE NO\tLEXEME\t\tTOKEN\t\tATTRIBUTE");
        printf("\n_________________________________________________________");
        yylex();
        printf("\n_________________________________________________________");
        printf("\nSYMBOL TABLE");
        printf("\n_______________________________________");
        printf("\nNAME\t\tVALUE");
        printf("\n_______________________________________");
        for(i=0; i<count; i++)
                printf("\n%s\t\t%d", symbol[i]->name, symbol[i]->value);
        printf("\n_______________________________________");
        printf("\n LEXICAL ERROR");
		printf("\n_______________________________________");
		printf("\nERROR\tKUTHLA");
		printf("\n_________________________________________");
		for(j=0; j<count1; j++)
                printf("\n%s\t\t%d", table[j]->error_ala,table[j]->kai_ala);
        
        fclose(fin);
        fclose(fout);

        printf("\nParsing done!!\n");
}
int insert(char str[])
{
        int i;
        for(i=0; i<count; i++)
        {
                if(strcmp(str, symbol[i]->name)==0)     return i;
        }
	symbol[count]=(struct st*)malloc(sizeof(struct st));
        strcpy(symbol[count]->name, str);
        symbol[count]->value=0;
        return count++;
}
int insert_for_error(char str1[])
{
        int j;
        for(j=0; j<count1; j++)
        {
                if(strcmp(str1, table[j]->error_ala)==0)     return j;
        }
		table[count1]=(struct t*)malloc(sizeof(struct t));
        strcpy(table[count1]->error_ala, str1);
        table[count1]->kai_ala=count1	;
        return count1++;
}

int yywrap(){
return 1;
}





input.txt
#include<stdio.h>
main()
{
//int a,b,c=10;
//float d;
/d=c+b;
printf("%f /_n",d);
int a,h;
int 0b;

}