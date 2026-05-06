import time
import random

class NursePlayer:
    def __init__(self, name):
        self.name = name
        self.rank = "New Grad"
        self.xp = 0
        self.specialty = None
        self.streak = 5
        self.credits = 100

    def show_huddle_stats(self):
        print(f"\n--- {self.name}'S PRE-SHIFT MIRROR ---")
        print(f"RANK: {self.rank} | XP: {self.xp}/1000")
        print(f"STREAK: {self.streak} Safe Shifts 🔥")
        print(f"CREDITS: {self.credits} 🪙")
        print("----------------------------------\n")

def game_huddle(player):
    player.show_huddle_stats()
    print("CHOOSE YOUR SPECIALTY FOR THE NIGHT:")
    print("1. Sepsis Scout (+ Detection)")
    print("2. IV Ninja (+ Speed)")
    print("3. Family Whisperer (+ Communication)")
    
    choice = input("Select (1-3): ")
    specialties = {"1": "Sepsis Scout", "2": "IV Ninja", "3": "Family Whisperer"}
    player.specialty = specialties.get(choice, "Generalist")
    print(f"\n[HUDDLE] Locked in as {player.specialty}. 'Let's have a safe shift, team!'")
    time.sleep(1)

def run_shift():
    score = {"Safety": 0, "Detective": 0, "Teamwork": 0}
    rooms = ["Bed 1", "Bed 2", "Bed 3 (Mystery Patient)"]
    
    print("\n--- SHIFT START: THE FIRST SWEEP ---")
    
    for room in rooms:
        print(f"\nEntering {room}...")
        time.sleep(1)
        
        # COZY TASK (Low Load)
        print(f"[COZY TASK] Scanning wristband and checking vitals...")
        time.sleep(1.5)
        print("Done! +10 Safety")
        score["Safety"] += 10
        
        # THE DETECTIVE CUE (The Hook)
        if "Mystery" in room:
            print("\n[!!!] SIXTH SENSE TRIGGERED: You notice the patient is breathing slightly faster than the monitor shows.")
            investigate = input("Investigate further? (y/n): ").lower()
            if investigate == 'y':
                print("SUCCESS: You found a subtle sign of occult sepsis! +50 Detective Score.")
                score["Detective"] += 50
            else:
                print("REASONING: You ignored the cue. The patient may deteriorate later.")
        
        # SOCIAL QUICK CHAT
        print(f"Social Ping: [1] 'Eyes on {room}' | [2] 'Need help' | [3] 'Nice Save'")
        ping = input("Send Ping? (1-3 or Enter to skip): ")
        if ping in ["1", "2", "3"]:
            score["Teamwork"] += 5

    return score

def post_shift_analysis(score, player):
    print("\n================================")
    print("      POST-SHIFT ANALYSIS      ")
    print("================================")
    total = sum(score.values())
    
    grade = "Functional Team"
    if total > 80: grade = "Elite Night Crew"
    if total > 100: grade = "MAGNET-LEVEL SHIFT"

    print(f"FINAL GRADE: {grade}")
    print(f"Patient Safety: {score['Safety']}")
    print(f"Detective Work: {score['Detective']}")
    print(f"Teamwork: {score['Teamwork']}")
    
    player.xp += total
    print(f"\nXP EARNED: {total}. Progressing to next rank...")
    print("================================\n")

# --- EXECUTION ---
user_nurse = NursePlayer("Tiffany")
game_huddle(user_nurse)
shift_results = run_shift()
post_shift_analysis(shift_results, user_nurse)