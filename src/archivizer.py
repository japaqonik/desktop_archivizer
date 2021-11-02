import pathlib
import datetime
import shutil
import stat
import progressbar

class PathStorage():
    def __init__(self, archivename) -> None:
        self.__dektoppath__ = pathlib.Path.joinpath(pathlib.Path.home(), "Desktop")
        self.__common_archive_path__ = pathlib.Path.joinpath(self.__dektoppath__, archivename)
        self.__todays_archive_path__ = pathlib.Path.joinpath(self.__common_archive_path__, datetime.date.today().isoformat())

    def get_desktop_path(self):
        return self.__dektoppath__

    def get_common_archive_path(self):
        return self.__common_archive_path__

    def get_todays_archive_path(self):
        return self.__todays_archive_path__

def move_files(archivename, silent, verbose):
    pathS = PathStorage(archivename)
    pathS.get_common_archive_path().mkdir(exist_ok=True)

    def create_dest_path(sourcepath):
        return pathlib.Path.joinpath(pathS.get_todays_archive_path(), sourcepath.name)

    def is_valid(sourcepath):
        return not sourcepath.name.endswith(".lnk") and not sourcepath.name == archivename and not bool(sourcepath.stat().st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

    filesmap = [(sourcepath, create_dest_path(sourcepath))
                for sourcepath in pathS.get_desktop_path().iterdir()
                if is_valid(sourcepath)]

    if not silent and verbose:
        print("Desktop files will be moved as following (source path -> target path):")
        for sourcepath, destpath in filesmap:
            print(str(sourcepath) + " -> " + str(destpath))
        print()
    
    if filesmap: pathS.get_todays_archive_path().mkdir(exist_ok=True)
    
    filespathsgenerator = filesmap
    
    if not silent: filespathsgenerator = progressbar.iter(filesmap, prefix="Moving files:", suffix="completed.")

    for sourcepath, destpath in filespathsgenerator:
        shutil.move(sourcepath, destpath)

