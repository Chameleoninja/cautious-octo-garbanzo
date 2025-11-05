# 🧠 ADHD Life Manager

A comprehensive command-line tool designed specifically for ADHD brains to manage home, work, and everything in between.

## What Makes This Different

**Built for ADHD brains:**
- Focus on ONE thing at a time (max 3 tasks per day)
- Quick capture for when ideas strike
- Brain dump feature to clear mental clutter
- Context-based organization (work, home, errands)
- Energy and medication tracking
- No overwhelming features or complicated setup

## Features

### 🏠 HOME & LIFE
- **Brain Dump**: Clear everything from your mind onto lists
- **Quick Capture**: Add tasks/ideas in seconds
- **Today View**: See only what matters right now (max 3 tasks)
- **Daily Review**: Plan your day in 5 minutes

### 💼 WORK & FOCUS
- **Context Lists**: Organize by Work, Home, Errands, Calls, Waiting For
- **Focus Sessions**: Built-in timer support for focused work
- **Energy Check**: Track when you're most productive

### 📊 ORGANIZATION
- **Three-List System**: Today (max 3), This Week, Someday/Maybe
- **Project Tracking**: Break big goals into steps
- **Routine Builder**: Morning and evening routines
- **Habit Tracking**: Build tiny habits that stick

### 💊 MEDICATION & HEALTH
- **Medication Log**: Track Vyvanse timing and effectiveness
- **Energy Patterns**: Discover your peak productivity windows
- **Weekly Review**: Reflect and plan in 15 minutes

## Installation

### Quick Start (Linux/Mac)

1. Save the program file:
   ```bash
   # The program is saved as adhd_life_manager.py
   ```

2. Make it executable:
   ```bash
   chmod +x adhd_life_manager.py
   ```

3. Run it:
   ```bash
   python3 adhd_life_manager.py
   ```

### Optional: Add to PATH for Easy Access

Create an alias in your shell config:

```bash
# Add to ~/.bashrc or ~/.zshrc
alias adhd='python3 /path/to/adhd_life_manager.py'
```

Then just type `adhd` from anywhere to launch!

## How to Use

### First Time Setup (5 minutes)

1. Launch the program
2. Start with a Brain Dump (option 1)
   - Write everything on your mind
   - Don't organize, just dump
3. Sort items into Today/This Week/Someday
4. Choose your ONE thing for today

### Daily Workflow

**Morning (5 minutes):**
1. Run Daily Review (option 4)
2. Pick 1-3 things for Today from This Week
3. Start with your ONE thing

**During the Day:**
- Quick Capture when ideas strike (option 2)
- Start Focus Sessions when ready to work (option 6)
- Check Energy levels to find patterns (option 7)

**Evening (2 minutes):**
- Mark tasks complete in Today view (option 3)
- Brain dump anything still on your mind
- Plan tomorrow's ONE thing

**Weekly (15 minutes):**
- Run Weekly Review (option 12)
- Celebrate wins
- Move tasks between lists
- Plan next week

## Tips for Success

### The Rules
1. **ONE thing at a time** - Never more than 3 tasks for Today
2. **Make it stupidly easy** - Break big tasks into tiny steps
3. **Never miss twice** - Bad days happen, just start again tomorrow
4. **Future you doesn't exist** - Plan for tired you, not motivated you

### When You Feel Overwhelmed
1. Open the program
2. Do a Brain Dump (option 1)
3. Look at Today list (option 3)
4. Pick the ONE thing that would make you feel 10% better
5. Start a 15-minute Focus Session on it

### Medication Optimization
- Log your Vyvanse time daily (option 11)
- Check energy levels 2-3 times per day (option 7)
- After 2 weeks, look for patterns
- Schedule hard tasks during your peak window

## Data Storage

All your data is stored locally in:
```
~/.adhd_life_manager.json
```

**To backup:**
- Use Settings > Export Data (option 13)
- Or manually copy the .json file

**To reset:**
- Delete the .json file and restart

## Troubleshooting

**Program won't run:**
```bash
# Make sure Python 3 is installed
python3 --version

# Make file executable
chmod +x adhd_life_manager.py
```

**Can't find my data:**
```bash
# Data file location
ls ~/.adhd_life_manager.json
```

**Want to start fresh:**
```bash
# Backup first!
cp ~/.adhd_life_manager.json ~/adhd_backup.json

# Then delete
rm ~/.adhd_life_manager.json
```

## Philosophy

This tool follows ADHD-friendly principles:

- **Minimal friction**: 2-3 clicks to capture anything
- **Visible, not hidden**: See what matters on one screen
- **External brain**: Don't rely on memory
- **Forgiving**: No penalties for incomplete tasks
- **Adaptive**: Works with your brain, not against it

## What This Tool Does NOT Do

- Doesn't sync across devices (keeps it simple)
- Doesn't send notifications (use your phone's timer)
- Doesn't have a mobile app (terminal-based by design)
- Doesn't judge you (seriously, no guilt built in)

## Credits

Created for people with ADHD, by someone who understands ADHD.

Based on proven strategies from:
- Getting Things Done (GTD) methodology
- ADHD-specific productivity research
- Tiny Habits by BJ Fogg
- Real experience with executive dysfunction

## License

Free to use, modify, and share. Help others with ADHD!

---

**Remember: You don't have to use every feature. Start with Brain Dump and Today list. Add more as you get comfortable.**

**Progress > Perfection**
