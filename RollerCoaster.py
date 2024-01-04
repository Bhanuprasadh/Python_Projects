{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Welcome to the Roller Coaster\")\n",
    "Height = int(input(\"Enter Your Height - \"))\n",
    "Age = int(input(\"Enter Your Age - \"))\n",
    "\n",
    "bill = 0\n",
    "\n",
    "\n",
    "if Height >= 120:\n",
    "    print(\"You Can Ride the Roller Coaster\")\n",
    "    if Age<12:\n",
    "        bill = 250\n",
    "        print(\"child tickets are 250 Rupees\")\n",
    "    elif 12<Age<18:\n",
    "        bill = 350\n",
    "        print(\"Youth tickets are 350 Rupees\")\n",
    "    else:\n",
    "        bill = 500\n",
    "        print(\"Adult tickets are 500 Rupees\")\n",
    "        \n",
    "    wants_photo = input(\"Do you want to take photo Yes or No\")\n",
    "    if wants_photo == \"Yes\":\n",
    "        bill += 50\n",
    "    \n",
    "        print(f\"Your Final bill is {bill}\")\n",
    "else:\n",
    "    print(\"You Can not Ride the Roller Coaster\")"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
