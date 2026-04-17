name = pyharp
build-time != date -u +"%F_%H-%M-%S"
pack-name=$(name)-$(build-time)
pack_dir = pack/$(pack-name)

export PYTHONPATH := $(CURDIR):$(CURDIR)/src/$(name):$(PYTHONPATH)

all: test

test:
	pytest tests/

test-verbose:
	pytest -v tests/

.ONESHELL:
package: clean
	mkdir -p $(pack_dir)
	cp -Rf src/$(name) $(pack_dir)
	cp -f etc/install.sh $(pack_dir)
	cp -f etc/pyharp.sh $(pack_dir)
	chmod +x $(pack_dir)/install.sh
	chmod +x $(pack_dir)/pyharp.sh
	cd pack
	zip -r  $(pack-name).zip $(pack-name)

clean:
	-rm -Rf src/$(name)/__pycache__
	-rm -Rf pack

.PHONY: all test clean package


