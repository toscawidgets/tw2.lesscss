import os

from distutils.core import setup, Command
from BeautifulSoup import BeautifulSoup
import urllib2

from posixpath import basename
import re

class SetupBuildCommand(Command):
    """
    Master setup build command to subclass from.
    """

    user_options = []

    def initialize_options(self):
        """
        Setup the current dir.
        """
        self._dir = os.getcwd()

    def finalize_options(self):
        """
        Set final values for all the options that this command supports.
        """
        pass

class UpdateLessCSSCommand(SetupBuildCommand):
    '''
    Updates the Less CSS Runtime library
    '''
    
    description = "updates LessCSS with latest version"

    def run(self):
        page = urllib2.urlopen('http://lesscss.org')
        soup = BeautifulSoup(page)

        download_link = soup.findAll(id='download')
        try:
            link_obj = download_link[0]
        except IndexError:
            raise Exception, "Can't find the download link. The page must\
                have changed. File a bug-report and we will fix it!"

        # Get the download link and extract the version number
        dl_link = link_obj['href']
        file_name = basename(dl_link)
        r = re.compile('less-([\d.]+)')
        ver_num = r.match(file_name).groups()[0][:-1]

        # Check to see if the directory already exists, if not make it
        if not os.path.exists('tw2/lesscss/static/lesscss/%s' % ver_num):
            os.mkdir('tw2/lesscss/static/lesscss/%s' % ver_num)

        # Download LessCSS
        less_js = urllib2.urlopen(dl_link)
        with open('tw2/lesscss/static/lesscss/%s/less.min.js'%ver_num, 'w') as js:
            print "Downloading %s to static/%s" % (file_name, ver_num)
            js.write(less_js.read())
       
        # Update version.py
        vs_file = """
            version_num = '{ver_num}'
        """.format(ver_num=ver_num)
        
        with open('tw2/lesscss/version.py', 'w') as vs_py:
            print "Writing new version.py"
            vs_py.write(vs_file)

        # Done!
        print 'Updated LessCSS to %s...' % ver_num
