#Day Ten
#Modules and Packages
#External packages : pip install packagename
#Modules = .py scripts used in pther .py script
#Package = Collectiojn of modules
from myprogram import my_func #remember how import is used

my_func()


#how to aggregate modules to form package
from mymainpackage import mymainscript #happens with blank __init__.py within the folder
from mymainpackage.subpackage import mysubpackagescript #Demostrating subdirectory
mymainscript.report_main()
mysubpackagescript.sub_report()

#__name__ and __main__
#if __name__ == "__main__": #run directly or imported. More common use is code organisation
	#block of code
#built in variable __name__. 2 _ so that it is not accidentally overwritten
