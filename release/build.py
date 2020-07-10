#!/usr/bin/env python3
import os
import datetime
import json
import shutil
import zipfile
from urllib.parse import urljoin
import jinja2


def script_filesystem_location():
    """
    Returns the absolute path of the directory where the build script
    is stored.
    """
    return os.path.dirname(os.path.abspath(__file__))


def templates_filesystem_location():
    """
    Returns the absolute path of the directory that holds the templates
    used to generate the required release assets.
    """
    return os.path.join(script_filesystem_location(), 'templates')


def project_root_filesystem_location():
    """
    Returns the absolute path of the project root directory.
    """
    return os.path.abspath(os.path.dirname(script_filesystem_location()))


def public_filesystem_location():
    """
    Returns the absolute path of the public location where the release files should
    be stored after the build process.
    """
    return os.path.join(project_root_filesystem_location(), 'public')


def release_filesystem_location():
    """
    Returns the absolute path of the location where the release is built.
    """
    return os.path.join(public_filesystem_location(), 'source/EditorMetadadosMarswInforbiomares')


def source_filesystem_location():
    """
    Returns the absolute path of the directory that holds the source code for the
    project.
    """
    return os.path.join(project_root_filesystem_location(), 'EditorMetadadosMarswInforbiomares')


def version_filesystem_location():
    """
    Returns the absolute path of the JSON file with the project version.
    """
    return os.path.join(source_filesystem_location(), 'version.json')


def make_plugin_version_string():
    """
    Parses the version JSON file and returns a formatted string with the current
    version.
    """
    with open(version_filesystem_location(), encoding='utf-8') as fp:
        version = json.load(fp)
        return '{major}.{minor}.{revision}'.format(**version)


def make_plugin_release_filename():
    """
    Returns the name of the release ZIP asset, using the release version format string.
    """
    version = make_plugin_version_string()
    return 'EditorMetadadosMarswInforbiomares.{version}.zip'.format(version=version)


def make_plugin_download_url():
    """
    Returns the URL that can be used to download the plugin from the repository
    """
    return urljoin('https://marsw.ualg.pt/static/qgis/', make_plugin_release_filename())


def make_plugin_release_filesystem_location():
    """
    Returns the absolute path of the release ZIP file inside the public directory.
    """
    return os.path.join(public_filesystem_location(), make_plugin_release_filename())


def make_release_information():
    """
    Returns a dictionary with information used for the post processing stage of the
    build process.
    """
    return {
        'plugin_version': make_plugin_version_string(),
        'plugin_filename': make_plugin_release_filename(),
        'plugin_download_url': make_plugin_download_url(),
        'plugin_update_date': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
    }


def load_template(name):
    """
    Load a template from the templates directory.
    """
    env = jinja2.Environment()
    loader = jinja2.FileSystemLoader(templates_filesystem_location())
    return loader.load(env, name)


def make_repository_xml(data):
    """
    Make the repository XML file for the plugin repository.
    """
    template = load_template('editor_metadados_marsw_infobiomares.template.xml')
    return template.render(data)


def make_plugin_metadata(data):
    """
    Make the plugin metadata.txt file for the plugin release.
    """
    template = load_template('metadata.template.txt')
    return template.render(data)


def get_ignore_file_list(folder, files):
    """
    Returns a list of files that should be ignored by the build process.
    """
    ignore_extensions = ['.ui', '.svg', '.qrc', '.pyc', '.meLock']
    return [f for f in files if os.path.splitext(f)[-1] in ignore_extensions]


def make_release_zip():
    source = os.path.abspath(os.path.join(release_filesystem_location(), '..'))
    destination = make_plugin_release_filesystem_location()

    zf = zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(source)
    for folder, subfolder, files in os.walk(source):
        for f in files:
            absname = os.path.abspath(os.path.join(folder, f))
            arcname = absname[len(abs_src) + 1:]
            print('zipping {} as {}'.format(os.path.join(folder, f), arcname))
            zf.write(absname, arcname)
    zf.close()


if __name__ == '__main__':
    info = make_release_information()

    with open(os.path.join(public_filesystem_location(), 'editormetadadosmarswinfobiomares.xml'), 'w', encoding='utf-8') as fp:
        fp.write(make_repository_xml(info))

    shutil.copytree(source_filesystem_location(), release_filesystem_location(), ignore=get_ignore_file_list)

    with open(os.path.join(release_filesystem_location(), 'metadata.txt'), 'w', encoding='utf-8') as fp:
        fp.write(make_plugin_metadata(info))

    make_release_zip()

    shutil.rmtree(os.path.abspath(os.path.join(release_filesystem_location(), '..')))
