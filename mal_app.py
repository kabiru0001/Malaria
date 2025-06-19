{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5726f15b-002d-4be8-8136-9a87fc034b91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "malaria_ap.py created\n"
     ]
    }
   ],
   "source": [
    "app_code = \"\"\"\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "#Load trained model\n",
    "model = pickle.load(open(\"malaria_model.pkl\", \"rb\"))\n",
    "\n",
    "st.title(\"Malaria Prediction\")\n",
    "\n",
    "#User inputs\n",
    "fever = st.selectbox(\"fever\", [0,1])\n",
    "headache = st.selectbox(\"headache\", [0,1])\n",
    "chills = st.selectbox(\"chills\", [0,1])\n",
    "fatigue = st.selectbox(\"fatigue\", [0,1])\n",
    "vomiting = st.selectbox(\"vomiting\", [0,1])\n",
    "joint_pain = st.selectbox(\"joint_pain\", [0,1])\n",
    "sweating = st.selectbox(\"sweating\", [0,1])\n",
    "nausea = st.selectbox(\"nausea\", [0,1])\n",
    "anemia = st.selectbox(\"anemia\", [0,1])\n",
    "\n",
    "if st.button(\"Check Malaria\"):\n",
    "    patient = pd.DataFrame([{\n",
    "        'fever': fever,\n",
    "        'headache': headache,\n",
    "        'chills': chills,\n",
    "        'fatigue': fatigue,\n",
    "        'vomiting': vomiting,\n",
    "        'joint_pain': joint_pain,\n",
    "        'sweating': sweating,\n",
    "        'nausea': nausea,\n",
    "        'anemia': anemia,\n",
    "        'malaria': malaria\n",
    "}])\n",
    "result = model.predict(patient)[0]\n",
    "st.success(\"Likely malaria\" if result else \"Not malaria\")\n",
    "\"\"\"\n",
    "with open(\"malaria_ap.py\", \"w\") as f:\n",
    "    f.write(app_code)\n",
    "print(\"malaria_ap.py created\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "07d84212-993b-4550-a496-78910143f4a6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
