WKDIR=.
PROG=python3
EXT=py
INSTALL = install
TRAIN = train
PRICE = price
PRECISION = precision
SCRIPT_TRAIN=$(WKDIR)/$(TRAIN).$(EXT)
SCRIPT_PRICE=$(WKDIR)/$(PRICE).$(EXT)
SCRIPT_PRECISION=$(WKDIR)/$(PRECISION).$(EXT)
TRASH = /dev/null
FILE_CONSTANTS = $(WKDIR)/constants.csv
FILE_DATA = $(WKDIR)/data.csv


NAME : all
all : $(PRICE)
$(PRICE) : $(TRAIN)
	@echo "\033[1;33mComputing Price...\033[0m"
	$(PROG) $(SCRIPT_PRICE)
	@echo; echo


$(TRAIN): $(INSTALL)
	@echo "\033[1;33mTraining model...\033[0m"
	$(PROG) $(SCRIPT_TRAIN)
	@echo; echo


$(INSTALL):
	@echo "\033[1;33mInstalling python modules...\033[0m"
	$(PROG) -m pip install pandas > $(TRASH)
	$(PROG) -m pip install matplotlib > $(TRASH)
	@echo "\033[1;32mModule installation: Successful \033[0m"
	@echo; echo



$(PRECISION):
	@echo "\033[1;33mComputing precision statistic (r square)...\033[0m"
	$(PROG) $(SCRIPT_PRECISION)
	@echo; echo

# remove all support files
fclean:
	rm -rf __pycache__ $(FILE_CONSTANTS) $(FILE_DATA)

# remove final target files
clean: fclean

# recompile everything
re: clean all

.PHONY : all fclean clean re train_model estimate_price install


