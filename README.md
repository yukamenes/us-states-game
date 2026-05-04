# U.S. States Guessing Game

An interactive Python game where you try to guess all U.S. states on a map.

Built with **Python, Turtle graphics, and Pandas**.

This project is based on a course exercise but significantly improved with custom logic and enhancements.

---

## 🎮 How it works

- You are shown a blank map of the United States
- You type state names one by one
- Correct answers are displayed directly on the map
- The game tracks your score in real time
- When you exit, a file with missing states is generated for learning

---

## 🚀 Improvements over the original course version

Compared to the original implementation, I added and improved:

- Case-insensitive input handling (better user experience)
- Input validation and cleanup (strip + normalization)
- Prevention of duplicate guesses
- Separate score tracking system
- Clean data processing using pandas filtering
- Improved game loop structure for better readability
- More structured and maintainable code

This version focuses on better UX, cleaner logic, and improved code organization.

---

## 🧠 What I learned

This project was created as part of:

**100 Days of Code™: The Complete Python Pro Bootcamp**

Through this project I practiced:

- working with **pandas DataFrames**
- handling **CSV data**
- using **turtle graphics for UI**
- processing **user input in real-time**
- building **game loops**
- filtering and comparing datasets
- improving existing code structure

---

## 📂 Project structure

```
.
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── states_to_learn.csv
```

---

## ▶️ How to run

```bash
python main.py
```

---

## 🖼️ Screenshots

### Game start
![Start](screenshots/start.png)

### Gameplay
![Gameplay](screenshots/gameplay.png)

### Results file
![Results](screenshots/result.png)

---

## 📄 License

This project is licensed under the **Creative Commons License**.

---

## ✨ Author

GitHub: https://github.com/yukamenes
