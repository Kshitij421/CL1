%{
	#include"y.tab.h"
%}

%%

[ \t\n]+			;
\+|\-|\/|\*|\&|\!|\|		{ return OP; }
main			{ return MAIN; }
#include<[.a-zA-Z ]*> {return HEADER;}

if			{ return IF; }
else			{ return ELSE; }
for			{ return FOR; }
while			{ return WHILE; }
int|float|double|short|long|void	{return DT; }

\>|\<|\>\=|\<\=|\=\=	{ return RELATIONAL; }

\+\+			{ return INC; }
\-\-			{ return DEC; }

[0-9]+			{ return NUMBER; }
[a-zA-Z][a-zA-Z0-9]*	{ return ID; }
.			{ return yytext[0]; }

%%


a4.y
%{
	#include<stdio.h>
	extern FILE *yyin;
	int flag = 1;
%}

%start s
%token ID MAIN OP CONDITIONAL IF FOR WHILE RELATIONAL INC DEC NUMBER DT ELSE HEADER
%left '+''-'
%left '/''*'

%%

s:	HEADER MAIN'('')' '{' prog '}' { if(flag) printf("PROGRAM IS VALID\n"); else printf("INVALID PROGRAM\n");  }
	;

prog:	stmtlist prog
	|
	;

stmtlist:stmtlist stmt|;

stmt:	ID '=' expr ';'	{ printf("Valid Statement\n"); }
	| HEADER {printf("Header File\n");}
	| expr ';'	{ printf("Valid Statement\n"); }
	| forstmt	{ printf("for statement is a Valid Statement\n"); }
	| whilestmt 	{ printf("while statement is a Valid Statement\n"); }
	| ifstmt	{ printf("if statement is a Valid Statement\n"); }
	| vardeclare    { printf("Incorrect declaration statement\n"); flag = 0;}
	| vardeclare ';'{ printf("variable declaration statment is a Valid Statement\n"); }
	;
vardeclist: vardeclist vardeclare|;

vardeclare:	DT ID	{}
		| DT ID '=' NUMBER	{}
		| ID '=' NUMBER	{}
		| DT ID '=' NUMBER ',' vardeclist	{}
		| ID '=' NUMBER  ',' vardeclist	{}
		;

expr:	expr OP expr	{}
	| ID '=' expr OP NUMBER	{}
	| ID '='  OP ID	{}		
	| ID		{}
	| NUMBER {}
	
	;

ifstmt:	IF'(' condition ')' '{' stmtlist '}'	{}
	| IF'(' condition ')' '{' stmtlist '}' ELSE'{' stmtlist '}'	{}
	| IF'(' condition ')'  stmtlist  ELSE stmtlist	{}
	;

forstmt:	FOR '(' assigning ';' condition ';' incdec ')' '{' stmtlist '}'	{}
		;
			
condition:	expr RELATIONAL expr		{}
		;

incdec:	ID INC	{}
	| ID DEC	{}
	;

assigning:	ID '=' expr	{}
		;

whilestmt:	WHILE'(' condition ')' '{' stmtlist '}'	{}
		;

%%

main()
{
	FILE *fin;
	fin=fopen("expressions.txt", "r");
	yyin=fin;
	yyparse();
}

int yywrap()
{
	return 1;
}

int yyerror()
{
	printf("**Syntax Error**");
	return 1;
}

expressions.txt

#include<stdio.h>
main()
{
	a+b;
	a-b*a;
	a*b;
	a|b;
	c=a/b;
	3+5;
	if(a==b)
	{
		a+b;
	}
	
	if(a==b)
	{	
		a+b;
		a+b;
	}
	else
	{
		a-b;
	}
	
	if(a>=b)
		a+b;
	else
		a-b;
	
	for(i=5;i<=10;i++)
	{
		a=a*i;
		a=a*i;
	}
	
	while(i<=5)
	{
		a+b;
		a=a*i;
		a+b;
	}
	
	int a=5,b=4;
	float c;
}