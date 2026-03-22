import tkinter as tk
import random
import time

class ReactionTimeLab:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaction Time Lab")
        self.root.geometry("500x450")
        
        # experiment variables
        self.trials = 0
        self.correct = 0
        self.sumRT = 0.0
        self.stimulus = ""
        self.expected = ""
        self.startTime = 0
        self.waiting = False
        
        # GUI
        tk.Label(root, text="Reaction Time Test", font=("Arial",16)).pack(pady=10)
        tk.Label(root, text="Press A for LETTERS   Press L for NUMBERS", font=("Arial",12)).pack(pady=5)
        tk.Label(root, text="Press SPACE to reset", font=("Arial",10)).pack(pady=2)
        
        self.display = tk.Label(root, text="", font=("Arial",80,"bold"),
                                bg="white", width=10, height=2)
        self.display.pack(pady=30)
        
        stats_frame = tk.Frame(root)
        stats_frame.pack(pady=20)
        self.trials_label = tk.Label(stats_frame, text="trials: 0", font=("Courier",12))
        self.trials_label.grid(row=0,column=0,padx=20)
        self.correct_label = tk.Label(stats_frame, text="correct: 0", font=("Courier",12))
        self.correct_label.grid(row=0,column=1,padx=20)
        self.accuracy_label = tk.Label(stats_frame, text="accuracy: 0%", font=("Courier",12))
        self.accuracy_label.grid(row=0,column=2,padx=20)
        self.avgRT_label = tk.Label(stats_frame, text="avgRT: 0 ms", font=("Courier",12))
        self.avgRT_label.grid(row=1,column=0,columnspan=3,pady=10)
        
        self.feedback = tk.Label(root, text="Ready", font=("Arial",11))
        self.feedback.pack(pady=10)
        
        # key bindings
        root.bind('<KeyPress-a>', self.check_key)
        root.bind('<KeyPress-l>', self.check_key)
        root.bind('<KeyPress-space>', self.reset)
        
        # start first round
        self.next_round()
    
    def next_round(self):
        # pick random stimulus
        if random.random() < 0.5:
            self.stimulus = chr(random.randint(65,90))
            self.expected = 'A'
        else:
            self.stimulus = str(random.randint(0,9))
            self.expected = 'L'
        
        # display stimulus and force GUI update before starting timer
        self.display.config(text=self.stimulus)
        self.root.update()           # <-- ensures the label shows before timer
        self.startTime = time.time()*1000
        
        self.waiting = True
        self.feedback.config(text="Press A or L", fg="blue")
    
    def check_key(self, event):
        if not self.waiting:
            return
        key = event.keysym.upper()
        if key not in ['A','L']:
            self.feedback.config(text="Invalid key", fg="orange")
            return
        
        self.waiting = False
        rt = time.time()*1000 - self.startTime
        self.trials +=1
        
        if key == self.expected:
            self.correct +=1
            self.sumRT += rt
            self.feedback.config(text=f"Correct! {int(rt)} ms", fg="green")
        else:
            msg = "A for letter" if self.expected=='A' else "L for number"
            self.feedback.config(text=f"Wrong! Should press {msg}", fg="red")
        
        # update stats
        acc = int(self.correct/self.trials*100)
        avg_rt = int(self.sumRT/self.correct) if self.correct else 0
        self.trials_label.config(text=f"trials: {self.trials}")
        self.correct_label.config(text=f"correct: {self.correct}")
        self.accuracy_label.config(text=f"accuracy: {acc}%")
        self.avgRT_label.config(text=f"avgRT: {avg_rt} ms")
        
        # next round faster
        self.root.after(500, self.next_round)  # 0.5s delay
    
    def reset(self, event):
        self.trials = 0
        self.correct = 0
        self.sumRT = 0
        self.waiting = False
        self.display.config(text="")
        self.trials_label.config(text="trials: 0")
        self.correct_label.config(text="correct: 0")
        self.accuracy_label.config(text="accuracy: 0%")
        self.avgRT_label.config(text="avgRT: 0 ms")
        self.feedback.config(text="Reset! Starting over", fg="orange")
        self.root.after(500, self.next_round)

# run program
root = tk.Tk()
app = ReactionTimeLab(root)
root.mainloop()