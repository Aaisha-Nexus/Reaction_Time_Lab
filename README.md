# Reaction Time Lab

A **simple reaction time experiment** built with Python and Tkinter. This program measures how quickly you can respond to letters (A-Z) and numbers (0-9) by pressing the correct key. It tracks trials, accuracy, and reaction time to help understand human cognitive processing.

---

##  Experiment Overview

**The Basic Concept:**  

When you see something on screen, your brain goes through several steps before pressing a key:

1. See the letter/number (**visual processing**)  
2. Recognize if it's a letter or number (**categorization**)  
3. Decide which key to press (**decision making**)  
4. Press the key (**motor response**)  

The **reaction time (RT)** is the time between seeing the stimulus and pressing the key.

**The Task:**

- A letter (A-Z) or number (0-9) appears randomly on the screen  
- Press `A` if it’s a letter  
- Press `L` if it’s a number  
- The program measures how fast you press the correct key  

---

##  Why This Matters

1. **Stimulus-Response Compatibility**  
   Your brain has to map what you see (letter/number) to a response (A/L key). This is called **choice reaction time**.

2. **Speed-Accuracy Tradeoff**  
   People balance:  
   - Going fast → might make mistakes  
   - Being accurate → might be slower  
   This experiment shows that relationship.

3. **Cognitive Processing**  
   Measures:  
   - Visual recognition time  
   - Categorization speed (letter vs number)  
   - Decision making time  
   - Motor execution time  

---

## Variables We Measure

| Variable | Meaning |
|----------|---------|
| `trials` | Number of attempts so far |
| `correct` | Number of correct responses |
| `accuracy` | Percentage correct = (correct / trials) × 100 |
| `avgRT` | Average reaction time across all trials |
etc

---

##  Python Implementation

- **Python version:** 3.x  
- **Libraries used:**  
  - `tkinter` → GUI  
  - `random` → generate letters/numbers  
  - `time` → measure reaction time  
