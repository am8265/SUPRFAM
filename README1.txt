First Follow the instructions on README file in reagrds to dependencies and HOW TO INSTALL THE SCRIPTS AND ADD THEM TO YOUR PATH and then check for:
1)Checking your fasta file for formatting issues:
Run fasta_checker.pl as :

./fasta_checker.pl <fasta_file.fa> >tmp.fa

a cleaned fasta file tmp.fa would be created in the working directory

2) Run superfamily.pl as :
./superfamily.pl tmp.fa

the output file is a) tmp.ass and b) tmp.html 

