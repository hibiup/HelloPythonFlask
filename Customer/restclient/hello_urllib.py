import urllib.request
import urllib.parse
 
 
url = 'http://localhost:5000/hello/World'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
