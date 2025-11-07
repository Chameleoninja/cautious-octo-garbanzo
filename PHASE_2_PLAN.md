# Phase 2: Core Enhancements - Implementation Plan

**Status:** Starting Now!
**Estimated Time:** 2-3 hours
**Features:** 4 major enhancements

---

## 🎯 Phase 2 Features

### 7. ⏰ Time Blocking with Drag & Drop (Medium Complexity)
**Current State:** Time blocks exist visually but can't drag tasks to them

**What to implement:**
- Make time blocks droppable zones
- Store time block assignment in task data
- Display tasks within their time blocks
- Visual feedback during drag
- Remove from time block functionality
- Persist time block assignments

**User Story:** "I want to drag tasks to Morning/Midday/Afternoon blocks to schedule my day"

**Estimated Time:** 45 minutes

---

### 8. ⌨️ Enhanced Keyboard Shortcuts (Easy)
**Current State:** Only Enter (submit) and Escape (close modal) work

**What to implement:**
- Ctrl+B: Open Brain Dump
- Ctrl+F: Focus search box
- Ctrl+T: Open Focus Timer
- Ctrl+E: Open Energy Check
- Ctrl+W: Open Weekly Review
- Ctrl+N: Add task to Today
- Delete: Remove selected task
- Arrow keys: Navigate between tasks
- Space: Toggle task completion
- Help modal (Ctrl+/ or ?)

**User Story:** "I want to navigate the app without using my mouse"

**Estimated Time:** 30 minutes

---

### 9. 📝 Task Notes/Details (Medium Complexity)
**Current State:** Tasks only have title and basic metadata

**What to implement:**
- Notes field in task data structure
- 📝 Notes button on each task
- Expandable notes section (like subtasks)
- Save/edit notes
- Visual indicator when task has notes
- Rich text support (optional)
- Links detection (optional)

**User Story:** "I want to add context, links, and details to my tasks"

**Estimated Time:** 45 minutes

---

### 10. 🔄 Recurring Tasks (Complex)
**Current State:** No recurring functionality

**What to implement:**
- Recurring pattern options:
  - Daily
  - Weekly (select days)
  - Monthly (specific date)
  - Every X days
- Recurrence configuration in task
- Auto-create next occurrence on completion
- Option to skip occurrence
- Visual indicator for recurring tasks (🔄)
- Edit/stop recurrence
- "Complete for today" vs "Mark complete forever"

**User Story:** "I want my daily routines to auto-add without manual work"

**Estimated Time:** 60 minutes

---

## 📋 Implementation Order

### Session 1: Time Blocking (45 min)
1. Add timeBlock field to task data
2. Update drag/drop to support time blocks
3. Render tasks in time blocks
4. Add remove from time block
5. Test and commit

### Session 2: Keyboard Shortcuts (30 min)
1. Create keyboard shortcut handler
2. Add all shortcuts
3. Create help modal
4. Add visual hints
5. Test and commit

### Session 3: Task Notes (45 min)
1. Add notes field to task data
2. Add notes button and UI
3. Expandable notes section
4. Save/edit functionality
5. Visual indicators
6. Test and commit

### Session 4: Recurring Tasks (60 min)
1. Add recurrence data structure
2. Create recurrence modal
3. Pattern selection UI
4. Auto-create on complete logic
5. Visual indicators
6. Edit/stop functionality
7. Test and commit

---

## 🎨 UI/UX Considerations

### Time Blocking:
- Highlight time blocks on drag over
- Show task count in each block
- Compact task display in blocks
- Easy removal option

### Keyboard Shortcuts:
- Non-intrusive help button
- Tooltip hints on buttons
- Doesn't conflict with browser shortcuts
- Clear documentation

### Task Notes:
- Similar UI to subtasks
- Markdown-style formatting
- Auto-link URLs
- Character counter (optional)

### Recurring Tasks:
- Clear recurrence icon
- Simple pattern selection
- Smart defaults (e.g., daily = every weekday)
- Easy to disable

---

## 🔧 Technical Approach

### Data Structure Updates:

```javascript
// Task with Phase 2 fields
{
  id: 123,
  text: "Task name",
  category: "work",
  priority: "high",
  completed: false,
  subtasks: [],
  timeBlock: "morning",  // NEW: morning/midday/afternoon/null
  notes: "Detailed notes...",  // NEW
  recurrence: {  // NEW
    enabled: true,
    pattern: "daily",  // daily/weekly/monthly/custom
    interval: 1,
    daysOfWeek: [1,3,5],  // for weekly
    dayOfMonth: 15,  // for monthly
    lastCompleted: "2025-11-07"
  }
}
```

### Keyboard Shortcuts Handler:
```javascript
document.addEventListener('keydown', (e) => {
  if (e.ctrlKey || e.metaKey) {
    switch(e.key) {
      case 'b': openBrainDump(); break;
      case 'f': focusSearch(); break;
      // etc...
    }
  }
});
```

---

## ✅ Success Criteria

### Time Blocking:
- [ ] Can drag tasks to time blocks
- [ ] Tasks display in their time blocks
- [ ] Can remove from time block
- [ ] Persists after refresh
- [ ] Works with drag between lists

### Keyboard Shortcuts:
- [ ] All 10+ shortcuts work
- [ ] Help modal shows all shortcuts
- [ ] No conflicts with browser
- [ ] Works in all modals
- [ ] Visual feedback

### Task Notes:
- [ ] Can add/edit notes
- [ ] Notes save properly
- [ ] Expandable section works
- [ ] Visual indicator when notes exist
- [ ] Links are clickable

### Recurring Tasks:
- [ ] Can set recurrence pattern
- [ ] Auto-creates next occurrence
- [ ] Visual indicator (🔄)
- [ ] Can skip occurrence
- [ ] Can edit/stop recurrence
- [ ] Works with all patterns

---

## 📊 Risk Assessment

### Low Risk:
- Keyboard shortcuts (isolated, easy to implement)

### Medium Risk:
- Task notes (UI complexity)
- Time blocking (drag/drop edge cases)

### High Risk:
- Recurring tasks (complex logic, date handling, edge cases)

**Mitigation:**
- Test thoroughly
- Handle edge cases
- Clear user feedback
- Easy to disable if issues

---

## 🚀 Ready to Start!

**Next Step:** Implement Feature 7 (Time Blocking Drag & Drop)

Let's go! 💪
