# coding=utf-8
import distutils
import json
import os
import datetime
import shutil
import zipfile


def create_release(up_major=False, up_minor=False, up_revision=False):
    with open(os.path.join(os.path.dirname(__file__), 'EditorMetadadosSNIMar/version.json'), "r") as data_file:
        version = json.load(data_file)

    if up_major:
        version["major"] += 1
        version["minor"] = 0
        version["revision"] = 0
    elif up_minor:
        version["minor"] += 1
        version["revision"] = 0
    elif up_revision:
        version["revision"] += 1
    if up_major or up_minor or up_revision:
        with open(os.path.join(os.path.dirname(__file__), 'EditorMetadadosSNIMar/version.json'), 'w') as data_file:
            json.dump(version, data_file)
    #_gen_and_create_metadata_txt_file()

    current_version = ".".join([str(version["major"]), str(version["minor"]), str(version["revision"])])
    # create new Release folder
    if os.path.exists("Releases/version." + current_version):
        for root, dirs, files in os.walk("Releases/version." + current_version + "/", topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
    else:
        os.makedirs("Releases/version." + current_version)

    # copy plugin
    shutil.copytree("EditorMetadadosSNIMar", "Releases/version." + current_version + "/toZip/EditorMetadadosSNIMar",
                    ignore=ignore_stuff)
    # copy repository xml
    #_gen_create_repository_xml_file("Releases/version." + current_version)

    # make zip
    zipDic("Releases/version." + current_version + "/toZip/",
           "Releases/version." + current_version + "/EditorMetadadosSNIMar." + current_version)
    # delete redundant Editor folder
    for root, dirs, files in os.walk("Releases/version." + current_version + "/toZip/", topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir("Releases/version." + current_version + "/toZip/")


def ignore_stuff(folder, files):
    ignore_list = []
    for file in files:
        if ".ui" in file or ".svg" in file or ".qrc" in file or ".pyc" in file or ".meLock" in file:
            ignore_list.append(file)
    return ignore_list


def zipDic(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print('zipping %s as %s' % (os.path.join(dirname, filename), arcname))
            zf.write(absname, arcname)
    zf.close()


def _gen_and_create_metadata_txt_file():
    with open(os.path.join(os.path.dirname(__file__), 'EditorMetadadosSNIMar/version.json'), "r") as data_file:
        version = json.load(data_file)
    current_version = ".".join([str(version["major"]), str(version["minor"]), str(version["revision"])])
    try:
        os.remove(os.path.join(os.path.dirname(__file__), "EditorMetadadosSNIMar/metadata.txt"))
    except OSError:
        pass

    with open(os.path.join(os.path.dirname(__file__), "EditorMetadadosSNIMar/metadata.txt"), 'w') as meta:
        meta.write('\n'.join(["[general]",
                              "name=EditorMetadadosSNIMar",
                              "email=suporte.snimar@ipma.pt",
                              "author= Main Developers: Pedro Dias, Eduardo Castanho;\n Contributors: Joana Teixeira , Alexandre Neto",
                              "qgisMinimumVersion=3.0",
                              "description=Plugin para a criação e edição de metadados segundo o perfil SNIMar",
                              "about= O Editor de Metadados SNIMar foi desenvolvido no âmbito do Projecto SNIMar",
                              "       com o objectivo de ser a ferramenta destinada à criação dos metadados",
                              "       em conformidade com o Perfil de Metadados SNIMar",
                              "       email: suporte.snimar@ipma.pt.",
                              "version=" + current_version,
                              "ChangeLog: >1.0.0 - Primeira versão",
                              "           >...",
                              "           >2.0.0 - Actualização do Perfil",
                              "           >2.0.1 - Correçao Bugs",
                              "            -actualizar palavras-chave SNIMar",
                              "           >2.1.0 - Bugs fix( Contact list corruption,gml versions,...)",
                              "           >3.0.0 - Code update for QGIS3",
                              "tags=Metadata, metadados, SNIMar, EEAgrants, Governo Portugal",
                              "homepage=http://editor.snimar.pt/",
                              "icon=resourcesFolder/icons/main_icon.svg",
                              "experimental=False",
                              "deprecated=False"]))


def _gen_create_repository_xml_file(dest_absol_path):
    with open(os.path.join(os.path.dirname(__file__), 'EditorMetadadosSNIMar/version.json'), "r") as data_file:
        version = json.load(data_file)
    current_version = ".".join([str(version["major"]), str(version["minor"]), str(version["revision"])])

    with open(os.path.join(dest_absol_path, "editormetadadossnimar.xml"), 'w') as meta:
        meta.write('\n'.join(["<?xml version = '1.0' encoding = 'UTF-8'?>",
                              "<plugins>",
                              "  <pyqgis_plugin name='EditorMetadadosSNIMar' version='" + current_version + "'>",
                              "       <description><![CDATA[Plugin para a criação e edição de metadados segundo o perfil SNIMar]]></description>",
                              "        <about><![CDATA[O Editor de Metadados SNIMar foi desenvolvido no âmbito do Projecto SNIMar com o objectivo de ser a ferramenta destinada à criação dos metadados em conformidade com o Perfil de Metadados SNIMar.]]></about>",
                              "        <version>" + current_version + "</version>",
                              "        <qgis_minimum_version>3.0.0</qgis_minimum_version>",
                              "        <homepage>http://editor.snimar.pt/</homepage>",
                              "        <file_name>EditorMetadadosSNIMar." + current_version + ".zip</file_name>",
                              "        <icon>../main_icon.png</icon>",
                              "        <author_name><![CDATA[Main Developers: Pedro Dias, Eduardo Castanho;\n Contributors: Joana Teixeira, Alexandre Neto]]></author_name>",
                              "        <download_url>http://editor.snimar.pt/QgisPluginRepository/EditorMetadadosSNIMar." + current_version + ".zip</download_url>",
                              "        <uploaded_by><![CDATA[Team WP4-SNIMar]]></uploaded_by>",
                              "        <create_date>2015-08-10T12:07:15.672750</create_date>",
                              "        <update_date>" + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + "</update_date>",
                              "       <tags><![CDATA[Metadata,Metadados,SNIMar, EEAgrants, Governo Portugal]]></tags>",
                              "       <experimental>False</experimental>",
                              "  </pyqgis_plugin>",
                              "</plugins>"]))

def publish():
    """
    Publishes the current release into the public path.
    """
    pass
