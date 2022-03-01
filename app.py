{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "7dc67671",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "39ff7de3",
   "metadata": {},
   "outputs": [],
   "source": [
    "app=Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74135903",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request,render_template\n",
    "import joblib\n",
    "\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        Nikkei = request.form.get(\"Nikkei\")\n",
    "        print(Nikkei)\n",
    "        model1 = joblib.load(\"STI_REG\")\n",
    "        pred1 = model1.predict([[Nikkei]])\n",
    "        str1 = \"The prediction for STI using Regression is : \" + str(pred1)\n",
    "        return(render_template(\"index.html\",result=str1))\n",
    "    else:\n",
    "        return(render_template(\"index.html\",result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "54f0ec83",
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
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n",
      "1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:11] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:16] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py:63: FutureWarning: Arrays of bytes/strings is being converted to decimal numbers if dtype='numeric'. This behavior is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). Please convert your data to numeric values explicitly instead.\n",
      "  return f(*args, **kwargs)\n",
      "[2022-03-01 21:15:17,830] ERROR in app: Exception on / [POST]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\", line 653, in check_array\n",
      "    array = array.astype(np.float64)\n",
      "ValueError: could not convert string to float: ''\n",
      "\n",
      "The above exception was the direct cause of the following exception:\n",
      "\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-56-81aa27d87c73>\", line 10, in index\n",
      "    pred1 = model1.predict([[Nikkei]])\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_base.py\", line 238, in predict\n",
      "    return self._decision_function(X)\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_base.py\", line 220, in _decision_function\n",
      "    X = check_array(X, accept_sparse=['csr', 'csc', 'coo'])\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\", line 63, in inner_f\n",
      "    return f(*args, **kwargs)\n",
      "  File \"C:\\Users\\YUNRU\\Anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\", line 655, in check_array\n",
      "    raise ValueError(\n",
      "ValueError: Unable to convert array of bytes/strings into decimal numbers with dtype='numeric'\n",
      "127.0.0.1 - - [01/Mar/2022 21:15:17] \"\u001b[35m\u001b[1mPOST / HTTP/1.1\u001b[0m\" 500 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9ebd496",
   "metadata": {},
   "outputs": [],
   "source": []
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
