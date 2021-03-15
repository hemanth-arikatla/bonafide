from flaskblog import app
import os



'''if __name__ == '__main__':
    app.run(debug=True)'''

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
