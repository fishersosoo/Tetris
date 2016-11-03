#encoding=utf-8
from restful_app import db,init_db,app,api,register_resource
if __name__ == '__main__':
    init_db(db)
    register_resource(api)
    app.run(debug=True,port=9000)
