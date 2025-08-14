# 📱🚗 Python OOP Assignments

Welcome to the **Week 05 Python Assignments**!  
This repository is a playground for mastering Object-Oriented Programming (OOP) concepts in Python.  
Get ready to explore inheritance, polymorphism, method overriding, and more—all with fun, real-world examples! 🚀

---

## 📱 Assignment 1: Smartphone Classes

**File:** [`assignment1.py`](assignment1.py)

### 📝 What You'll Learn

- How to design a base class (`Smartphone`) with common attributes.
- How to create subclasses (`AndroidPhone` 🤖 and `IPhone` 🍏) that inherit and extend functionality.
- How to use **polymorphism** to call overridden methods.
- How to implement **static methods** and platform-specific behaviors.

### 🏗️ Class Structure

- `Smartphone`: brand, model, price, and a generic `specs()` method.
- `AndroidPhone`: adds `android_version`, overrides `specs()`, and installs apps via Google Play.
- `IPhone`: adds `ios_version`, overrides `specs()`, and installs apps via App Store.

### 💡 Features

- Print detailed specs for each phone.
- Simulate making calls and installing apps.
- Demonstrates OOP principles in a relatable context.

### 🖥️ Example Output

```
AndroidOS Manufacturer, Galaxy S22, costing $799, Android 13
Dialing 123-456-7890
Installing Maps from Google Play Store.
---
Apple, iPhone 15, costing $999, iOS 18
Dialing 123-456-7890
Installing Safari from App Store.
---
```

---

## 🚗 Assignment 2: Vehicle Classes

**File:** [`assignment2.py`](assignment2.py)

### 📝 What You'll Learn

- How to use **abstract base classes** (`Vehicle`) to enforce method implementation.
- How to create subclasses (`Car` 🚗, `Plane` ✈️, `Boat` 🚤) with unique behaviors.
- How to leverage **polymorphism** to interact with different vehicle types seamlessly.

### 🏗️ Class Structure

- `Vehicle`: abstract class with a `move()` method.
- `Car`: implements `move()` to drive on roads.
- `Plane`: implements `move()` to fly in the sky.
- `Boat`: implements `move()` to sail on water.

### 💡 Features

- Demonstrates how different objects can share a common interface but behave differently.
- Great for understanding the power of abstraction and polymorphism.

### 🖥️ Example Output

```
🚗 Driving on the road
✈️ Flying in the sky
🚤 Sailing on water
```

---

## 🛠️ How to Run

1. Make sure you have **Python 3** installed.  
   _(Download from [python.org](https://www.python.org/downloads/) if needed)_
2. Open your terminal in this folder.
3. Run each assignment file:
   ```sh
   python assignment1.py
   python assignment2.py
   ```

---

## 📚 Concepts Covered

- **Inheritance** 🧬
- **Polymorphism** 🦄
- **Method Overriding** 🔄
- **Static Methods** 🏷️
- **Abstract Classes** 🏛️
- **Type Checking** ✅

---

## 🎯 Why These Assignments Matter

- Build a strong foundation in OOP for real-world Python projects.
- Practice designing flexible, reusable code.
- Prepare for interviews and advanced programming challenges.

---

## 🤩 Tips for Success

- Try adding your own subclasses (e.g., `Tablet`, `Helicopter`).
- Experiment with new methods and attributes.
- Refactor code to improve readability and efficiency.
- Share your solutions and insights with classmates!

---

Happy Coding! 🎉  
\*May your classes be clean and your objects
