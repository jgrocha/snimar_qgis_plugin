UIDIR = EditorMetadadosSNIMar/snimarQtInterfaceView/templates/
UIFILES := $(shell find $(UIDIR) -iname '*.ui')
PYUIFILES := $(patsubst %.ui,%.py,$(UIFILES))

build: build_rcc build_ui

build_rcc: EditorMetadadosSNIMar/resources.qrc
	pyrcc5 -o EditorMetadadosSNIMar/resources.py EditorMetadadosSNIMar/resources.qrc

build_ui: $(PYUIFILES)
	mkdir -p EditorMetadadosSNIMar/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/
	touch EditorMetadadosSNIMar/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/__init__.py
	mv EditorMetadadosSNIMar/snimarQtInterfaceView/templates/*.py EditorMetadadosSNIMar/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/
	mv EditorMetadadosSNIMar/snimarQtInterfaceView/templates/dialogs/*.py EditorMetadadosSNIMar/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/

EditorMetadadosSNIMar/snimarQtInterfaceView/templates/%.py: EditorMetadadosSNIMar/snimarQtInterfaceView/templates/%.ui
	pyuic5 $< -o $@

EditorMetadadosSNIMar/snimarQtInterfaceView/templates/dialogs%.py: EditorMetadadosSNIMar/snimarQtInterfaceView/templates/dialogs/%.ui
	pyuic5 $< -o $@

cleanUserFiles:
	rm -f EditorMetadadosSNIMar/userFiles/*.json
	echo "[]" >> EditorMetadadosSNIMar/userFiles/contact_list.json
	echo "{}" >> EditorMetadadosSNIMar/userFiles/filelist.json

clean:
	find . -iname "*.pyc" -type f -delete
	find . -name __pycache__ -type d -delete
	rm -r public
	mkdir public

release: clean cleanUserFiles build
	./release/build.py

release_current: clean cleanUserFiles build
	python3 -c "import releaseManager; releaseManager.create_release()"

release_major: clean cleanUserFiles build
	python3 -c "import releaseManager; releaseManager.create_release(up_major=True)"

release_minor: clean cleanUserFiles build
	python3 -c "import releaseManager; releaseManager.create_release(up_minor=True)"

release_revision: clean cleanUserFiles build
	python3 -c "import releaseManager; releaseManager.create_release(up_revision=True)"
