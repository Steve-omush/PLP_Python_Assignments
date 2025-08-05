# 🧪 Week 02 - Custom List Operations in Python

📅 **Date:** 05/08/2025  
📁 **Folder:** `Week02_Date_05_08_25`  
📝 **Main File:** `list.py`

---

## 📌 Description

This project demonstrates how to manually implement basic list operations without relying on Python's built-in list methods. It introduces a custom class `MyList` that mimics list behavior, offering full control over:

- Adding elements (`append`)
- Removing elements (`pop`, `remove_at`)
- Inserting at a specific index (`insert`)
- Sorting elements (`custom_sort`)

The purpose is to understand the internal logic behind Python’s list-like structures and how they work under the hood.

---

## 🧰 Features Implemented

- ✅ `append(value)` – Adds an element to the end of the list  
- ✅ `pop()` – Removes and returns the last element (LIFO behavior)  
- ✅ `insert(index, value)` – Inserts a value at a specific index  
- ✅ `pop()` – Removes the element at a specific index  
- ✅ `sort()` – Sorts the list using Bubble Sort (ascending order)  
- ✅ `index()` – Returns the index of an element in the list

---

## 🧪 Example Usage

```python
# Add elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert an element at a specific index
my_list.insert(1, 15)

# Extend the list with another list
another_list = [50, 60, 70]
my_list.extend(another_list)

# Remove an element from the list (Last element)
removed_element = my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of an element in the list
index_of_30 = my_list.index(30)      # [10, 20]
```

---

## 📁 File Structure
```
Week02_Date_05_08_25/
├── list.py
├── README.md
```

## ▶️ How to Run the Program

1. Make sure you have Python installed.
2. Save the calculator script as `list.py`.
3. Open a terminal and navigate to the project directory.
4. Run the program:

   ```bash
   python list.py
   ```

