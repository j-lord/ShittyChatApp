PIP_LIBS=c:\users\ashton\appdata\local\programs\python\python310\lib\site-packages
#PIP_LIBS=$(shell pip show pip | grep "Location" | awk -F 'Location:' '//{print $2}')

all: install_deps clean build

install_deps:
	pip install -r requirements.txt
build:
	pyinstaller -p $(PIP_LIBS) \
	-p myapp \
	--add-data="myapp/templates;templates" \
	--add-data="myapp/static;static" \
	--add-data="myapp/database.db;." \
	--hidden-import=dns.versioned \
	--hidden-import=dns.tsigkeyring \
	--hidden-import=dns.namedict \
	--hidden-import=dns.e164 \
	--hidden-import=dns \
	--hidden-import=dns.asyncresolver \
	--hidden-import=dns.asyncquery \
	--hidden-import=dns.asyncbackend \
	--hidden-import=eventlet.hubs.epolls \
	--hidden-import=eventlet.hubs.kqueue \
	--hidden-import=eventlet.hubs.selects -F main.py --onefile
	rm -rf build
run_server:
	./dist/main
clean:
	rm -rf build
	rm -rf dist