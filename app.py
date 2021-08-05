{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d1d17222",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "from flask_restful import Resource, Api, reqparse\n",
    "import pandas as pd\n",
    "import ast\n",
    "app = Flask(__name__)\n",
    "api = Api(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c90f687e",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bloomberg(Resource):\n",
    "    def get(self):\n",
    "        data = pd.read_csv('BDO-Securities-BB.csv')  # read CSV\n",
    "        \n",
    "        parser = reqparse.RequestParser()  # initialize\n",
    "        \n",
    "        parser.add_argument('ISIN', required=True)  # add args\n",
    "        parser.add_argument('Date', required=True)\n",
    "        args = parser.parse_args()  # parse arguments to dictionary\n",
    "        \n",
    "        vSecID = args['ISIN']\n",
    "        vDate = args['Date']\n",
    "        \n",
    "        data = data.query('SecurityID== @vSecID and Date == @vDate').head()\n",
    "        \n",
    "        #data = data.to_dict()  # convert dataframe to dictionary\n",
    "        \n",
    "        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary\n",
    "\n",
    "        return {'data': data}, 200  # return data and 200 OK code\n",
    "\n",
    "    pass\n",
    "    \n",
    "    \n",
    "api.add_resource(Bloomberg, '/BB')  # '/users' is our entry point"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5016210b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Reuters(Resource):\n",
    "    def get(self):\n",
    "        data = pd.read_csv('BDO-Securities-REUTERS.csv')  # read CSV\n",
    "        \n",
    "        parser = reqparse.RequestParser()  # initialize\n",
    "        \n",
    "        parser.add_argument('ISIN', required=True)  # add args\n",
    "        parser.add_argument('Date', required=True)\n",
    "        args = parser.parse_args()  # parse arguments to dictionary\n",
    "        \n",
    "        vSecID = args['ISIN']\n",
    "        vDate = args['Date']\n",
    "        \n",
    "        data = data.query('SecurityID== @vSecID and Date == @vDate').head()\n",
    "        \n",
    "        #data = data.to_dict()  # convert dataframe to dictionary\n",
    "        \n",
    "        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary\n",
    "\n",
    "        return {'data': data}, 200  # return data and 200 OK code\n",
    "\n",
    "    pass\n",
    "    \n",
    "    \n",
    "api.add_resource(Reuters, '/REUTERS')  # '/users' is our entry point\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "62ab48c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "class IDC(Resource):\n",
    "    def get(self):\n",
    "        data = pd.read_csv('BDO-Securities-IDC.csv')  # read CSV\n",
    "        \n",
    "        parser = reqparse.RequestParser()  # initialize\n",
    "        \n",
    "        parser.add_argument('ISIN', required=True)  # add args\n",
    "        parser.add_argument('Date', required=True)\n",
    "        args = parser.parse_args()  # parse arguments to dictionary\n",
    "        \n",
    "        vSecID = args['ISIN']\n",
    "        vDate = args['Date']\n",
    "        \n",
    "        data = data.query('SecurityID== @vSecID and Date == @vDate').head()\n",
    "        \n",
    "        #data = data.to_dict()  # convert dataframe to dictionary\n",
    "        \n",
    "        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary\n",
    "\n",
    "        return {'data': data}, 200  # return data and 200 OK code\n",
    "\n",
    "    pass\n",
    "    \n",
    "    \n",
    "api.add_resource(IDC, '/IDC')  # '/users' is our entry point"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a28dd269",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Markit(Resource):\n",
    "    def get(self):\n",
    "        data = pd.read_csv('BDO-Securities-MARKIT.csv')  # read CSV\n",
    "        \n",
    "        parser = reqparse.RequestParser()  # initialize\n",
    "        \n",
    "        parser.add_argument('ISIN', required=True)  # add args\n",
    "        parser.add_argument('Date', required=True)\n",
    "        args = parser.parse_args()  # parse arguments to dictionary\n",
    "        \n",
    "        vSecID = args['ISIN']\n",
    "        vDate = args['Date']\n",
    "        \n",
    "        data = data.query('SecurityID== @vSecID and Date == @vDate').head()\n",
    "        \n",
    "        #data = data.to_dict()  # convert dataframe to dictionary\n",
    "        \n",
    "        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary\n",
    "\n",
    "        return {'data': data}, 200  # return data and 200 OK code\n",
    "\n",
    "    pass\n",
    "    \n",
    "    \n",
    "api.add_resource(Markit, '/MARKIT')  # '/users' is our entry point"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0be8724",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c200517",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc757238",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cb038db",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e8efbb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [05/Aug/2021 11:18:33] \"\u001b[33mGET / HTTP/1.1\u001b[0m\" 404 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run()  # run our Flask app"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
