<div style="text-align: center;">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) [![Tkinter](https://img.shields.io/badge/Tkinter-✓-green.svg)](https://docs.python.org/3/library/tkinter.html)

</div>

# 🍅 Pomodoro Timer App

A clean, minimalist **Pomodoro Technique timer** built with **Tkinter** in Python. This app helps you focus for 25 minutes, take short breaks, and complete full cycles — all in a simple, intuitive interface.

---

## 📌 Features

✅ **Full Pomodoro Cycle**  
- 25-minute work sessions  
- 5-minute short breaks (after every 2 sessions)  
- 20-minute long breaks (after every 4 work sessions)

✅ **Visual Feedback**  
- Color-coded timers:  
  - 🟩 **Green** = Work session  
  - 🌸 **Pink** = Short break  
  - 🔴 **Red** = Long break  
- Auto-updates time display with `00:00` format  
- Shows checkmarks (✓) after each completed work session

✅ **User-Friendly Controls**  
- **Start** button: Begins the next session  
- **Reset** button: Stops the timer, resets all values, and clears checkmarks  

✅ **Responsive Design**  
- Fixed window size (non-resizable) for consistent layout  
- Clean, modern layout with centered elements  
- Uses a tomato image to represent the "work" state  

✅ **Automatic Session Tracking**  
- Automatically tracks completed work sessions  
- Displays a count of checkmarks (✓) based on how many work blocks you’ve completed  

---

## 🔧 How It Works

1. The app starts in **Work mode** (25 minutes).
2. After 25 minutes, it switches to a **Break** (5 minutes for every 2 sessions).
3. After every **4 work sessions**, it triggers a **Long Break** (20 minutes).
4. When a session ends, the timer resets and the next one starts automatically.
5. After each work session, a **✓ checkmark** appears in the bottom label to show progress.

> 🚀 This creates a **natural rhythm of focus and recovery** — helping you stay productive without burnout.

---

## 📂 Tech Stack

- **Python 3.x**  
- **Tkinter** (built-in GUI library)  
- **No external dependencies** — fully self-contained  

> ✅ Lightweight, portable, and runs on any system with Python installed.

---

## 📝 How to Run

1. Ensure you have **Python 3.x** installed.  
   🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Save the code as `pomodoro_timer.py`.

3. Place a file named `tomato.png` in the same directory as your script.  
   📎 This image is used as the background for the work session.

4. Run the app:
   ```bash
   python pomodoro_timer.py
   ```

> ⚠️ If the tomato image is missing, the app will still run — but the work session will not display the image.

---


## 📚 Documentation & Inspiration

- 📖 **Pomodoro Technique**: [https://www.pomodoro.org](https://www.pomodoro.org)  
- 📚 **Tkinter Documentation**: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

> This app is inspired by the Pomodoro Technique — a proven method for improving focus, reducing distractions, and maintaining long-term productivity.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🎉 Why This Matters

This small app demonstrates:
- How to build a **complete productivity tool** with minimal code
- How to use **Tkinter** for responsive, user-friendly GUIs
- How to implement **state management** (reps, timer, checkmarks)
- How to create **visual feedback** and **user engagement**

> 💡 Perfect for beginners learning Python GUI programming — or as a foundation for a more advanced timer with sound, notifications, or data tracking.


---

> 🍅 Made with ❤️ and Python simplicity — one focused session at a time.
