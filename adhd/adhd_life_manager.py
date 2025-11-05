#!/usr/bin/env python3
"""
ADHD Life Manager - A comprehensive daily organization tool
Designed specifically for ADHD brains with executive function support
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import sys

class ADHDLifeManager:
    def __init__(self):
        self.data_file = Path.home() / '.adhd_life_manager.json'
        self.data = self.load_data()
        
    def load_data(self):
        """Load existing data or create new structure"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {
            'tasks': {
                'today': [],
                'this_week': [],
                'someday': []
            },
            'routines': {
                'morning': [],
                'after_work': [],
                'evening': []
            },
            'contexts': {
                'home': [],
                'work': [],
                'errands': [],
                'calls': [],
                'waiting': []
            },
            'projects': {},
            'habits': {},
            'brain_dumps': [],
            'medication_log': [],
            'energy_log': [],
            'wins': [],
            'settings': {
                'medication_time': '08:00',
                'work_start': '09:00',
                'work_end': '17:00',
                'focus_duration': 25,
                'break_duration': 5
            }
        }
    
    def save_data(self):
        """Save data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
        print("\n✓ Data saved successfully")
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_header(self, title):
        """Print styled header"""
        print("\n" + "="*60)
        print(f"  {title}")
        print("="*60 + "\n")
    
    def get_timestamp(self):
        """Get formatted timestamp"""
        return datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header("🧠 ADHD LIFE MANAGER")
        
        now = datetime.now()
        print(f"📅 {now.strftime('%A, %B %d, %Y')}")
        print(f"🕐 {now.strftime('%I:%M %p')}\n")
        
        # Quick status
        today_count = len(self.data['tasks']['today'])
        week_count = len(self.data['tasks']['this_week'])
        
        print(f"📋 Today's Tasks: {today_count} (max 3 recommended)")
        print(f"📅 This Week: {week_count} tasks")
        
        if today_count == 0:
            print("⚠️  No tasks for today - let's add one!\n")
        
        print("\n🏠 HOME & LIFE")
        print("  1. Brain Dump (clear your mind)")
        print("  2. Quick Capture (add task/idea)")
        print("  3. View Today (what to do now)")
        print("  4. Daily Review (plan your day)")
        print("\n💼 WORK & FOCUS")
        print("  5. Work Tasks (by context)")
        print("  6. Focus Session (start timer)")
        print("  7. Energy Check (log how you feel)")
        print("\n📊 ORGANIZATION")
        print("  8. Projects (multi-step goals)")
        print("  9. Routines (morning/evening)")
        print("  10. Habits (track patterns)")
        print("\n💊 MEDICATION & HEALTH")
        print("  11. Medication Log")
        print("  12. Weekly Review")
        print("  13. Settings")
        print("\n  0. Exit")
        print("\n" + "-"*60)
        
        choice = input("\nWhat would you like to do? (1-13 or 0): ").strip()
        return choice
    
    def brain_dump(self):
        """Capture everything on your mind"""
        self.clear_screen()
        self.print_header("🧠 BRAIN DUMP - Get It All Out")
        
        print("Type everything that's on your mind. One item per line.")
        print("Don't organize, don't filter - just dump it all out.")
        print("Press Enter twice when done.\n")
        
        items = []
        empty_count = 0
        
        while True:
            line = input("→ ")
            if line.strip():
                items.append({
                    'text': line.strip(),
                    'timestamp': self.get_timestamp(),
                    'processed': False
                })
                empty_count = 0
            else:
                empty_count += 1
                if empty_count >= 2:
                    break
        
        if items:
            self.data['brain_dumps'].extend(items)
            self.save_data()
            
            print(f"\n✓ Captured {len(items)} items!")
            print("\nNow let's process these:")
            print("  1. Sort into Today/This Week/Someday")
            print("  2. Leave for later")
            
            choice = input("\nChoose (1-2): ").strip()
            if choice == '1':
                self.process_brain_dump(items)
        else:
            print("\nNo items captured.")
        
        input("\nPress Enter to continue...")
    
    def process_brain_dump(self, items):
        """Sort brain dump items into lists"""
        for item in items:
            print(f"\n'{item['text']}'")
            print("  1. Today (do it today)")
            print("  2. This Week")
            print("  3. Someday/Maybe")
            print("  4. Delete (not important)")
            
            choice = input("Where? (1-4): ").strip()
            
            task = {
                'text': item['text'],
                'added': self.get_timestamp(),
                'completed': False
            }
            
            if choice == '1' and len(self.data['tasks']['today']) < 3:
                self.data['tasks']['today'].append(task)
                print("  → Added to Today")
            elif choice == '1':
                print("  ⚠️  Today is full (3 max). Adding to This Week.")
                self.data['tasks']['this_week'].append(task)
            elif choice == '2':
                self.data['tasks']['this_week'].append(task)
                print("  → Added to This Week")
            elif choice == '3':
                self.data['tasks']['someday'].append(task)
                print("  → Added to Someday/Maybe")
            else:
                print("  → Deleted")
            
            item['processed'] = True
        
        self.save_data()
    
    def quick_capture(self):
        """Quickly add a task or idea"""
        self.clear_screen()
        self.print_header("⚡ QUICK CAPTURE")
        
        text = input("What do you need to capture? ").strip()
        if not text:
            return
        
        print("\nWhere should this go?")
        print("  1. Today (if < 3 tasks)")
        print("  2. This Week")
        print("  3. Someday/Maybe")
        print("  4. Work Context")
        print("  5. Home Context")
        
        choice = input("\nChoose (1-5): ").strip()
        
        task = {
            'text': text,
            'added': self.get_timestamp(),
            'completed': False
        }
        
        if choice == '1' and len(self.data['tasks']['today']) < 3:
            self.data['tasks']['today'].append(task)
            print("\n✓ Added to Today")
        elif choice == '1':
            print("\n⚠️  Today is full (3 max). Adding to This Week.")
            self.data['tasks']['this_week'].append(task)
        elif choice == '2':
            self.data['tasks']['this_week'].append(task)
            print("\n✓ Added to This Week")
        elif choice == '3':
            self.data['tasks']['someday'].append(task)
            print("\n✓ Added to Someday/Maybe")
        elif choice == '4':
            self.data['contexts']['work'].append(task)
            print("\n✓ Added to Work context")
        elif choice == '5':
            self.data['contexts']['home'].append(task)
            print("\n✓ Added to Home context")
        
        self.save_data()
        input("\nPress Enter to continue...")
    
    def view_today(self):
        """View and manage today's tasks"""
        while True:
            self.clear_screen()
            self.print_header("📋 TODAY - Your ONE Thing")
            
            tasks = self.data['tasks']['today']
            
            if not tasks:
                print("No tasks for today yet!\n")
                print("Remember: Pick just ONE thing to start with.")
                print("\nOptions:")
                print("  1. Add a task from This Week")
                print("  2. Add a new task")
                print("  0. Back to menu")
                
                choice = input("\nChoose: ").strip()
                if choice == '1':
                    self.move_to_today()
                elif choice == '2':
                    self.quick_capture()
                else:
                    break
                continue
            
            # Show tasks
            for i, task in enumerate(tasks, 1):
                status = "✓" if task['completed'] else "○"
                print(f"{i}. [{status}] {task['text']}")
            
            print("\n" + "-"*60)
            print("\nWhat would you like to do?")
            print("  [number] - Complete/uncomplete task")
            print("  a - Add task (if < 3)")
            print("  d - Delete task")
            print("  m - Move task to This Week")
            print("  0 - Back to menu")
            
            choice = input("\nChoice: ").strip().lower()
            
            if choice == '0':
                break
            elif choice == 'a' and len(tasks) < 3:
                self.quick_capture()
            elif choice == 'a':
                print("\n⚠️  You already have 3 tasks today. Complete one first!")
                input("Press Enter...")
            elif choice == 'd':
                idx = input("Delete which task? (number): ").strip()
                try:
                    tasks.pop(int(idx) - 1)
                    self.save_data()
                    print("✓ Deleted")
                except:
                    print("Invalid number")
                input("Press Enter...")
            elif choice == 'm':
                idx = input("Move which task? (number): ").strip()
                try:
                    task = tasks.pop(int(idx) - 1)
                    self.data['tasks']['this_week'].append(task)
                    self.save_data()
                    print("✓ Moved to This Week")
                except:
                    print("Invalid number")
                input("Press Enter...")
            elif choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]['completed'] = not tasks[idx]['completed']
                    if tasks[idx]['completed']:
                        tasks[idx]['completed_at'] = self.get_timestamp()
                        self.data['wins'].append({
                            'text': tasks[idx]['text'],
                            'date': self.get_timestamp()
                        })
                        print(f"\n🎉 Great job! You completed: {tasks[idx]['text']}")
                    self.save_data()
                    input("Press Enter...")
    
    def move_to_today(self):
        """Move task from This Week to Today"""
        self.clear_screen()
        self.print_header("📅 THIS WEEK → TODAY")
        
        week_tasks = self.data['tasks']['this_week']
        if not week_tasks:
            print("No tasks in This Week list!")
            input("Press Enter...")
            return
        
        print("Select a task to move to Today:\n")
        for i, task in enumerate(week_tasks, 1):
            print(f"{i}. {task['text']}")
        
        choice = input("\nWhich task? (number or 0 to cancel): ").strip()
        try:
            idx = int(choice) - 1
            if idx >= 0:
                task = week_tasks.pop(idx)
                self.data['tasks']['today'].append(task)
                self.save_data()
                print(f"\n✓ Moved to Today: {task['text']}")
        except:
            pass
        
        input("Press Enter...")
    
    def daily_review(self):
        """Plan your day"""
        self.clear_screen()
        self.print_header("🌅 DAILY REVIEW - Plan Your Day")
        
        now = datetime.now()
        print(f"{now.strftime('%A, %B %d, %Y')}\n")
        
        # Review yesterday's wins
        print("🎉 YESTERDAY'S WINS:")
        recent_wins = [w for w in self.data['wins'] if w['date'].startswith(
            (now - timedelta(days=1)).strftime('%Y-%m-%d'))]
        if recent_wins:
            for win in recent_wins:
                print(f"  ✓ {win['text']}")
        else:
            print("  (No completed tasks yesterday)")
        
        print("\n" + "-"*60)
        
        # Today's plan
        print("\n📋 TODAY'S PLAN:")
        today_tasks = self.data['tasks']['today']
        if today_tasks:
            for i, task in enumerate(today_tasks, 1):
                status = "✓" if task['completed'] else "○"
                print(f"  {i}. [{status}] {task['text']}")
        else:
            print("  No tasks yet!")
        
        if len(today_tasks) < 3:
            print(f"\n💡 You have room for {3 - len(today_tasks)} more task(s) today")
        
        print("\n" + "-"*60)
        
        # This week preview
        print("\n📅 THIS WEEK (choose tasks for today):")
        week_tasks = self.data['tasks']['this_week']
        if week_tasks:
            for i, task in enumerate(week_tasks[:5], 1):
                print(f"  {i}. {task['text']}")
            if len(week_tasks) > 5:
                print(f"  ... and {len(week_tasks) - 5} more")
        else:
            print("  (Empty - add some tasks!)")
        
        print("\n" + "-"*60)
        
        print("\nOptions:")
        print("  1. Move task from This Week to Today")
        print("  2. Add new task to Today")
        print("  3. Continue to main menu")
        
        choice = input("\nChoose: ").strip()
        if choice == '1':
            self.move_to_today()
        elif choice == '2':
            self.quick_capture()
    
    def work_tasks(self):
        """View tasks by context"""
        while True:
            self.clear_screen()
            self.print_header("💼 WORK TASKS - By Context")
            
            contexts = self.data['contexts']
            
            print("Choose a context:\n")
            print(f"  1. 💼 Work ({len(contexts['work'])} tasks)")
            print(f"  2. 🏠 Home ({len(contexts['home'])} tasks)")
            print(f"  3. 🚗 Errands ({len(contexts['errands'])} tasks)")
            print(f"  4. 📞 Calls/Emails ({len(contexts['calls'])} tasks)")
            print(f"  5. ⏳ Waiting For ({len(contexts['waiting'])} tasks)")
            print("  0. Back")
            
            choice = input("\nChoose: ").strip()
            
            context_map = {
                '1': 'work', '2': 'home', '3': 'errands',
                '4': 'calls', '5': 'waiting'
            }
            
            if choice == '0':
                break
            elif choice in context_map:
                self.manage_context(context_map[choice])
    
    def manage_context(self, context_name):
        """Manage tasks in a specific context"""
        while True:
            self.clear_screen()
            self.print_header(f"📋 {context_name.upper()} TASKS")
            
            tasks = self.data['contexts'][context_name]
            
            if not tasks:
                print("No tasks in this context.\n")
                print("  a - Add task")
                print("  0 - Back")
                choice = input("\nChoose: ").strip().lower()
                if choice == 'a':
                    text = input("\nTask: ").strip()
                    if text:
                        tasks.append({
                            'text': text,
                            'added': self.get_timestamp(),
                            'completed': False
                        })
                        self.save_data()
                elif choice == '0':
                    break
                continue
            
            for i, task in enumerate(tasks, 1):
                status = "✓" if task['completed'] else "○"
                print(f"{i}. [{status}] {task['text']}")
            
            print("\n  [number] - Toggle complete")
            print("  a - Add task")
            print("  d - Delete task")
            print("  0 - Back")
            
            choice = input("\nChoose: ").strip().lower()
            
            if choice == '0':
                break
            elif choice == 'a':
                text = input("\nTask: ").strip()
                if text:
                    tasks.append({
                        'text': text,
                        'added': self.get_timestamp(),
                        'completed': False
                    })
                    self.save_data()
            elif choice == 'd':
                idx = input("Delete which? ").strip()
                try:
                    tasks.pop(int(idx) - 1)
                    self.save_data()
                except:
                    pass
            elif choice.isdigit():
                try:
                    idx = int(choice) - 1
                    tasks[idx]['completed'] = not tasks[idx]['completed']
                    if tasks[idx]['completed']:
                        tasks[idx]['completed_at'] = self.get_timestamp()
                    self.save_data()
                except:
                    pass
    
    def focus_session(self):
        """Start a focus timer"""
        self.clear_screen()
        self.print_header("🎯 FOCUS SESSION")
        
        duration = self.data['settings']['focus_duration']
        
        print(f"Standard focus session: {duration} minutes")
        print("Just START - you don't have to finish!\n")
        
        print("What are you working on?")
        task = input("→ ").strip()
        
        if not task:
            return
        
        print(f"\n⏱️  Starting {duration}-minute focus session...")
        print(f"Task: {task}")
        print("\nSet a timer on your phone/computer and come back when done.")
        print("This program will wait for you.")
        
        input("\nPress Enter when your focus session is complete...")
        
        print("\n🎉 Focus session complete!")
        print("\nHow did it go?")
        print("  1. Completed the task!")
        print("  2. Made good progress")
        print("  3. Got distracted but tried")
        print("  4. Too hard, need to break it down")
        
        result = input("\nChoose: ").strip()
        
        # Log the session
        self.data['energy_log'].append({
            'type': 'focus_session',
            'task': task,
            'duration': duration,
            'result': result,
            'timestamp': self.get_timestamp()
        })
        self.save_data()
        
        if result == '4':
            print("\n💡 That's okay! Let's break it into smaller steps.")
            print("What's ONE tiny thing you could do in 5 minutes?")
            smaller = input("→ ").strip()
            if smaller:
                self.data['tasks']['today'].append({
                    'text': smaller,
                    'added': self.get_timestamp(),
                    'completed': False,
                    'parent': task
                })
                self.save_data()
                print("\n✓ Added smaller task to Today")
        
        input("\nPress Enter to continue...")
    
    def energy_check(self):
        """Log energy and focus levels"""
        self.clear_screen()
        self.print_header("⚡ ENERGY CHECK")
        
        print("How are you feeling right now?\n")
        print("Energy Level:")
        print("  1. 🔴 Exhausted (can barely function)")
        print("  2. 🟡 Low (tired, need rest)")
        print("  3. 🟢 Okay (normal)")
        print("  4. 🔵 Good (productive)")
        print("  5. 🟣 Excellent (peak performance)")
        
        energy = input("\nEnergy (1-5): ").strip()
        
        print("\nFocus Level:")
        print("  1. 🔴 Can't focus at all")
        print("  2. 🟡 Very distracted")
        print("  3. 🟢 Somewhat focused")
        print("  4. 🔵 Focused")
        print("  5. 🟣 Hyperfocused")
        
        focus = input("\nFocus (1-5): ").strip()
        
        print("\nNotes (optional):")
        notes = input("→ ").strip()
        
        self.data['energy_log'].append({
            'energy': energy,
            'focus': focus,
            'notes': notes,
            'timestamp': self.get_timestamp()
        })
        self.save_data()
        
        print("\n✓ Energy check logged!")
        
        # Provide suggestions
        if energy in ['1', '2']:
            print("\n💡 Low energy detected:")
            print("  • Take a break")
            print("  • Drink water")
            print("  • Do a 2-minute task")
            print("  • Accept you might not be super productive right now")
        elif focus in ['1', '2']:
            print("\n💡 Focus is low:")
            print("  • Try a 15-minute focus session")
            print("  • Change your environment")
            print("  • Do the 'body reset' (stand, water, breathe)")
            print("  • Pick an easier task")
        
        input("\nPress Enter to continue...")
    
    def medication_log(self):
        """Log medication and track patterns"""
        self.clear_screen()
        self.print_header("💊 MEDICATION LOG")
        
        print("Track your Vyvanse to find optimal timing\n")
        print("  1. Log medication taken now")
        print("  2. View medication history")
        print("  3. Set reminder time")
        print("  0. Back")
        
        choice = input("\nChoose: ").strip()
        
        if choice == '1':
            print("\nLogging medication taken now...")
            print("Did you eat before taking it? (y/n)")
            food = input("→ ").strip().lower() == 'y'
            
            self.data['medication_log'].append({
                'time': self.get_timestamp(),
                'food': food,
                'notes': ''
            })
            self.save_data()
            
            print("\n✓ Medication logged!")
            print("\n💡 Set a timer for 30-60 minutes from now.")
            print("That's when it should start working.")
            print("Use that window for your hardest task!")
            
        elif choice == '2':
            print("\nRecent medication logs:\n")
            recent = self.data['medication_log'][-7:]
            if recent:
                for log in recent:
                    food_text = "with food" if log.get('food') else "empty stomach"
                    print(f"  {log['time']} - {food_text}")
            else:
                print("  No logs yet")
        
        elif choice == '3':
            print(f"\nCurrent reminder: {self.data['settings']['medication_time']}")
            new_time = input("New time (HH:MM format): ").strip()
            if new_time:
                self.data['settings']['medication_time'] = new_time
                self.save_data()
                print("✓ Updated")
        
        input("\nPress Enter to continue...")
    
    def weekly_review(self):
        """Weekly reflection and planning"""
        self.clear_screen()
        self.print_header("📊 WEEKLY REVIEW")
        
        print("Take 15 minutes to reflect and plan\n")
        
        # Show wins
        print("🎉 THIS WEEK'S WINS:")
        now = datetime.now()
        week_start = now - timedelta(days=7)
        week_wins = [w for w in self.data['wins'] 
                     if datetime.strptime(w['date'], '%Y-%m-%d %H:%M') > week_start]
        
        if week_wins:
            for win in week_wins[-10:]:
                print(f"  ✓ {win['text']}")
        else:
            print("  (No completed tasks this week)")
        
        print(f"\n📊 Total wins: {len(week_wins)}")
        
        print("\n" + "-"*60)
        
        # Process unfinished tasks
        print("\n🔄 TODAY'S UNFINISHED TASKS:")
        unfinished = [t for t in self.data['tasks']['today'] if not t['completed']]
        if unfinished:
            for task in unfinished:
                print(f"  • {task['text']}")
            
            print("\nWhat should we do with these?")
            print("  1. Move all to This Week")
            print("  2. Delete all (they weren't important)")
            print("  3. Keep for tomorrow")
            
            choice = input("\nChoose: ").strip()
            if choice == '1':
                self.data['tasks']['this_week'].extend(unfinished)
                self.data['tasks']['today'] = [t for t in self.data['tasks']['today'] 
                                               if t['completed']]
                self.save_data()
                print("✓ Moved to This Week")
            elif choice == '2':
                self.data['tasks']['today'] = [t for t in self.data['tasks']['today'] 
                                               if t['completed']]
                self.save_data()
                print("✓ Deleted")
        
        print("\n" + "-"*60)
        
        # Plan next week
        print("\n📅 NEXT WEEK PREVIEW:")
        print(f"This Week list: {len(self.data['tasks']['this_week'])} tasks")
        print(f"Someday list: {len(self.data['tasks']['someday'])} tasks")
        
        print("\nAnything from Someday/Maybe ready to move up?")
        print("  1. Yes, let me review Someday list")
        print("  2. No, I'm good")
        
        choice = input("\nChoose: ").strip()
        if choice == '1':
            self.review_someday()
        
        print("\n✓ Weekly review complete!")
        input("\nPress Enter to continue...")
    
    def review_someday(self):
        """Review and promote items from Someday list"""
        someday = self.data['tasks']['someday']
        if not someday:
            print("\nSomeday list is empty!")
            return
        
        print("\n📋 SOMEDAY/MAYBE LIST:\n")
        for i, task in enumerate(someday, 1):
            print(f"{i}. {task['text']}")
        
        print("\nMove any to This Week? (comma-separated numbers, or 0 for none)")
        choice = input("→ ").strip()
        
        if choice and choice != '0':
            try:
                indices = [int(x.strip()) - 1 for x in choice.split(',')]
                for idx in sorted(indices, reverse=True):
                    if 0 <= idx < len(someday):
                        task = someday.pop(idx)
                        self.data['tasks']['this_week'].append(task)
                        print(f"✓ Moved: {task['text']}")
                self.save_data()
            except:
                print("Invalid input")
    
    def settings(self):
        """Configure settings"""
        self.clear_screen()
        self.print_header("⚙️  SETTINGS")
        
        settings = self.data['settings']
        
        print("Current Settings:\n")
        print(f"  Medication Time: {settings['medication_time']}")
        print(f"  Work Hours: {settings['work_start']} - {settings['work_end']}")
        print(f"  Focus Duration: {settings['focus_duration']} minutes")
        print(f"  Break Duration: {settings['break_duration']} minutes")
        
        print("\n  1. Change medication time")
        print("  2. Change work hours")
        print("  3. Change focus duration")
        print("  4. Export all data")
        print("  5. View data location")
        print("  0. Back")
        
        choice = input("\nChoose: ").strip()
        
        if choice == '1':
            new_time = input("New medication time (HH:MM): ").strip()
            if new_time:
                settings['medication_time'] = new_time
                self.save_data()
        elif choice == '2':
            start = input("Work start time (HH:MM): ").strip()
            end = input("Work end time (HH:MM): ").strip()
            if start:
                settings['work_start'] = start
            if end:
                settings['work_end'] = end
            self.save_data()
        elif choice == '3':
            duration = input("Focus session minutes (default 25): ").strip()
            if duration.isdigit():
                settings['focus_duration'] = int(duration)
                self.save_data()
        elif choice == '4':
            export_file = Path.home() / f'adhd_backup_{datetime.now().strftime("%Y%m%d")}.json'
            with open(export_file, 'w') as f:
                json.dump(self.data, f, indent=2)
            print(f"\n✓ Data exported to: {export_file}")
        elif choice == '5':
            print(f"\nData file location: {self.data_file}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main program loop"""
        while True:
            choice = self.main_menu()
            
            if choice == '0':
                print("\n👋 Take care of yourself!")
                break
            elif choice == '1':
                self.brain_dump()
            elif choice == '2':
                self.quick_capture()
            elif choice == '3':
                self.view_today()
            elif choice == '4':
                self.daily_review()
            elif choice == '5':
                self.work_tasks()
            elif choice == '6':
                self.focus_session()
            elif choice == '7':
                self.energy_check()
            elif choice == '11':
                self.medication_log()
            elif choice == '12':
                self.weekly_review()
            elif choice == '13':
                self.settings()

if __name__ == '__main__':
    manager = ADHDLifeManager()
    manager.run()
