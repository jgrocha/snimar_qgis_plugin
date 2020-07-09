UIDIR = EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/
UIFILES := $(shell find $(UIDIR) -iname '*.ui')
PYUIFILES := $(patsubst %.ui,%.py,$(UIFILES))

build: build_rcc build_ui

build_rcc: EditorMetadadosMarswInfobiomares/resources.qrc
	pyrcc5 -o EditorMetadadosMarswInfobiomares/resources.py EditorMetadadosMarswInfobiomares/resources.qrc

build_ui: $(PYUIFILES)
	mkdir -p EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/
	touch EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/__init__.py
	mv EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/*.py EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/
	mv EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/dialogs/*.py EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/

EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/%.py: EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/%.ui
	pyuic5 $< -o $@

EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/dialogs%.py: EditorMetadadosMarswInfobiomares/snimarQtInterfaceView/templates/dialogs/%.ui
	pyuic5 $< -o $@

cleanUserFiles:
	rm -f EditorMetadadosMarswInfobiomares/userFiles/*.json
	echo "[]" >> EditorMetadadosMarswInfobiomares/userFiles/contact_list.json
	echo "{}" >> EditorMetadadosMarswInfobiomares/userFiles/filelist.json

clean:
	find . -iname "*.pyc" -type f -delete
	find . -name __pycache__ -type d -delete
	rm -rf public
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
