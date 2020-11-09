{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3  is an odd number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2  is an even number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1  is an odd number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5  is an odd number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3  is an odd number\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Congrats you picked 4!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  done\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done!\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    Var1 = (input('Enter a number: '))\n",
    "    if Var1 == 'done':\n",
    "        print('Done!')\n",
    "        break\n",
    "    elif Var1.isnumeric() == False:\n",
    "        print('Not a number try again')\n",
    "    else:\n",
    "        Var1 = int(Var1)\n",
    "        if Var1 == 4:\n",
    "            print('Congrats you picked 4!')\n",
    "        elif (Var1 % 2) == 0:\n",
    "            print(Var1 ,' is an even number')\n",
    "        else:\n",
    "            print(Var1, ' is an odd number')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  Zack\n",
      "Enter your age:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The year you will turn 100 is  2100\n",
      "There are  29184  until the year you turn 100\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  done\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done!\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    name = input('Enter your name: ')\n",
    "    if name == 'done':\n",
    "        print('Done!')\n",
    "        break\n",
    "    age = (input('Enter your age: '))\n",
    "    if age == 'done':\n",
    "        print('Done!')\n",
    "        break\n",
    "    elif age.isnumeric() == False:\n",
    "        print('Not a number try again')\n",
    "    else:\n",
    "        age1 = int(age)\n",
    "        year = (2020 + (100 - age1))\n",
    "        print('The year you will turn 100 is ', year)\n",
    "        import datetime\n",
    "        today = datetime.date.today()\n",
    "        birthyear = datetime.date(year,1,1)\n",
    "        diff = birthyear - today\n",
    "        print ('There are ', diff.days, ' until the year you turn 100')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
