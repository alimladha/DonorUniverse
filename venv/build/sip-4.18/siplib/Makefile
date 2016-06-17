TARGET = sip.so
OFILES = siplib.o apiversions.o descriptors.o qtlib.o threads.o objmap.o voidptr.o array.o bool.o
HFILES = sip.h sipint.h array.h 

CC = cc
CXX = c++
LINK = c++
CPPFLAGS = -DNDEBUG -I. -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
CFLAGS = -pipe -fPIC -Os -Wall -W
CXXFLAGS = -pipe -fPIC -Os -Wall -W
LFLAGS = -headerpad_max_install_names -bundle -undefined dynamic_lookup
LIBS = 
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages || mkdir -p $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages
	cp -f $(TARGET) $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/$(TARGET)
	@test -d $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/bin/../include/python2.7 || mkdir -p $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/bin/../include/python2.7
	cp -f /Users/alim/GitHub/DonorUniverseGit/venv/build/sip-4.18/siplib/sip.h $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/bin/../include/python2.7/sip.h
	@test -d $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages || mkdir -p $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages
	cp -f /Users/alim/GitHub/DonorUniverseGit/venv/build/sip-4.18/sip.pyi $(DESTDIR)/Users/alim/GitHub/DonorUniverseGit/venv/lib/python2.7/site-packages/sip.pyi

clean:
	-rm -f $(TARGET)
	-rm -f siplib.o
	-rm -f apiversions.o
	-rm -f descriptors.o
	-rm -f qtlib.o
	-rm -f threads.o
	-rm -f objmap.o
	-rm -f voidptr.o
	-rm -f array.o
	-rm -f bool.o
