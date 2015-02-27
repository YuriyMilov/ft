# This Python file uses the following encoding: utf-8
 
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp2.RequestHandler):
    
    
    def get(self):                
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.out.write('<html><body>')
        self.response.out.write('ййй, webapp World!')
        self.response.out.write('</body></html>')

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)



def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
