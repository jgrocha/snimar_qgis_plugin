UIDIR = EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/
UIFILES := $(shell find $(UIDIR) -iname '*.ui')
PYUIFILES := $(patsubst %.ui,%.py,$(UIFILES))

build: build_rcc build_ui

build_rcc: EditorMetadadosMarswInforbiomares/resources.qrc
	pyrcc5 -o EditorMetadadosMarswInforbiomares/resources.py EditorMetadadosMarswInforbiomares/resources.qrc

build_ui: $(PYUIFILES)
	mkdir -p EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/
	touch EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/__init__.py
	mv EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/*.py EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/
	mv EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/dialogs/*.py EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/pyuic4GeneratedSourceFiles/dialogs/

EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/%.py: EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/%.ui
	pyuic5 $< -o $@

EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/dialogs%.py: EditorMetadadosMarswInforbiomares/snimarQtInterfaceView/templates/dialogs/%.ui
	pyuic5 $< -o $@

cleanUserFiles:
	rm -f EditorMetadadosMarswInforbiomares/userFiles/*.json
	echo "[]" >> EditorMetadadosMarswInforbiomares/userFiles/contact_list.json
	echo "{}" >> EditorMetadadosMarswInforbiomares/userFiles/filelist.json

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
