"""
    Commonly used constants

    See COPYING for license information
"""
__version__ = "0.5.2"

USER_AGENT = "sl-object-storage-python: %s" % __version__
ENDPOINTS = {
    'dal05': {
        'public': {
            'http': "http://dal05.objectstorage.softlayer.net/auth/v1.0",
            'https': "https://dal05.objectstorage.softlayer.net/auth/v1.0"
        },
        'private': {
            'http': "http://dal05.objectstorage.service.networklayer.com/auth/v1.0",
            'https': "https://dal05.objectstorage.service.networklayer.com/auth/v1.0"
        }
    },
     'hkg02': {
        'public': {
            'http': "http://hkg02.objectstorage.softlayer.net/auth/v1.0",
            'https': "https://hkg02.objectstorage.softlayer.net/auth/v1.0"
        },
        'private': {
            'http': "http://hkg02.objectstorage.service.networklayer.com/auth/v1.0",
            'https': "https://hkg02.objectstorage.service.networklayer.com/auth/v1.0"
        }
    },
    'lon02': {
        'public': {
            'http': "http://lon02.objectstorage.softlayer.net/auth/v1.0",
            'https': "https://lon02.objectstorage.softlayer.net/auth/v1.0"
        },
        'private': {
            'http': "http://lon02.objectstorage.service.networklayer.com/auth/v1.0",
            'https': "https://lon02.objectstorage.service.networklayer.com/auth/v1.0"
        }
    },
    'sjc01': {
        'public': {
            'http': "http://sjc01.objectstorage.softlayer.net/auth/v1.0",
            'https': "https://sjc01.objectstorage.softlayer.net/auth/v1.0"
        },
        'private': {
            'http': "http://sjc01.objectstorage.service.networklayer.com/auth/v1.0",
            'https': "https://sjc01.objectstorage.service.networklayer.com/auth/v1.0"
        }
    },
    'ams01': {
        'public': {
            'http': "http://ams01.objectstorage.softlayer.net/auth/v1.0",
            'https': "https://ams01.objectstorage.softlayer.net/auth/v1.0"
        },
        'private': {
            'http': "http://ams01.objectstorage.service.networklayer.com/auth/v1.0",
            'https': "https://ams01.objectstorage.service.networklayer.com/auth/v1.0"
        }
    },
    'sng01': {
        'public': {
            'http': "http://sng01.objectstorage.softlayer.net/auth/v1.0",
            'https': "https://sng01.objectstorage.softlayer.net/auth/v1.0"
        },
        'private': {
            'http': "http://sng01.objectstorage.service.networklayer.com/auth/v1.0",
            'https': "https://sng01.objectstorage.service.networklayer.com/auth/v1.0"
        }
    }
}
