# A custom Paths text wrapper

class Paths:
    assetsDir = 'assets/' # Default folder where assets will be stored.

    @staticmethod
    def getPath(file:str, library:str = None):
        if library != None:
            return Paths.getLibraryPath(file, library)

        return Paths.getPreloadPath(file)

    @staticmethod
    def getLibraryPath(file:str, library:str = 'preload'):
        return Paths.getPreloadPath(file) if (library == 'preload' or library == 'default') else Paths.getLibraryPathForce(file, library)

    getLibraryPathForce = staticmethod(lambda file, library : f'{Paths.assetsDir}{library}/{file}')
    getPreloadPath = staticmethod(lambda file : f'{Paths.assetsDir}{file}')

    # Some file types that it can search (text, xml, json and images).
    # eg. If you want to get path of an image stored in "assets/images", use Paths.image("image-name")
    # Or if you want to find from another location "assets/folder-name": Paths.image("image-name", "folder-name")

    txt = staticmethod(lambda key, library = None: Paths.getPath(f'{key}.txt', library))
    xml = staticmethod(lambda key, library = None: Paths.getPath(f'{key}.xml', library))
    json = staticmethod(lambda key, library = None: Paths.getPath(f'{key}.json', library))
    image = staticmethod(lambda key, library = None: Paths.getPath(f'images/{key}.png', library))