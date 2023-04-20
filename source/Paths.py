# A custom Paths text wrapper (won't explain how it works since it's unused).

class Paths:
    assetsDir = 'assets/'

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

    txt = staticmethod(lambda key, library: Paths.getPath(f'{key}.txt', library))
    xml = staticmethod(lambda key, library: Paths.getPath(f'{key}.xml', library))
    json = staticmethod(lambda key, library: Paths.getPath(f'{key}.json', library))