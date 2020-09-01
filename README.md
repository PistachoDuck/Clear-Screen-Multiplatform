# Clear Screen on any OS

I researched a bit about this, is an easy problem, but one that i wish i didn't have to look for, so here it is.

#How to install it on your Project (NO TERMINAL VERSION) 

1) Go to the "Code" button and save it to your computer.
2) Extract it
3) Put the "cls.py" on the projecto you are working on.
4) To use it inside your proyect you can use the import for this:
	
	"import cls"
	
	or alternatevly
	
	"from cls import cls"
	
	for a more direct acces
	(if you use the first method you will need to put first the name of the import and then the function.
	Something like this:
		
		cls.cls()
		
		else you will only need to use:
		
		cls()
	)
	
#How to install it on your Project (TERMINAL VERSION)

1) Go to your project folder in terminal
2) Put this command 
		$ git clone https://github.com/PistachoDuck/Python-Clear-Screen-Multiplatform-Module.git
3) Exctract it, and you're ready to use it on your project
4) put this at the beggining of your code:
	
		from cls import cls
		
That's it.
Have a nice day.
