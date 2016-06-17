
all:
	@(cd sipgen; $(MAKE))
	@(cd siplib; $(MAKE))

install:
	@(cd sipgen; $(MAKE) install)
	@(cd siplib; $(MAKE) install)
	@test -d $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages || mkdir -p $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages
	cp -f sipconfig.py $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/sipconfig.py
	cp -f /Users/alim/GitHub/DonorUniverseGit/venv/build/sip-4.18/sipdistutils.py $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/sipdistutils.py

clean:
	@(cd sipgen; $(MAKE) clean)
	@(cd siplib; $(MAKE) clean)
