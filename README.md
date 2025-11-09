# 🐍 Python Basics
A growing collection of Python functions, mini-projects, and notes as I master the fundamentals.
## 📂 Structure
- **functions/** — reusable Python functions grouped by topic  
- **mini_projects/** — small practice scripts using those functions  
- **notes/** — my personal explanations and summaries of Python concepts
## 💡 Goal
To build a clean, beginner-friendly Python reference library while learning step by step.
🧠 Created by [Ryan Gupta](https://github.com/RyanGupta-Ataraxia)

# 🧭 Python Basics Toolkit — 30-Day Plan

*(This is the roadmap for this repository, documenting daily progress and future goals.)*


from datetime import date
from textwrap import dedent

plan_md = dedent(f"""
# 🧭 Python Basics Toolkit — 30-Day Plan

**Author:** Ryan Gupta  
**Start Date:** {date.today().strftime('%B %d, %Y')}  
**Goal:** Build a complete beginner-to-intermediate Python toolkit and portfolio.

---

## ✅ Completed So Far
| Day | Focus | Description |
|-----|--------|-------------|
| 1–2 | Setup | Created GitHub repo, VS Code setup, commit practice |
| 3–4 | String Functions | reverse_string, count_vowels, is_palindrome, capitalize_words |
| 5–6 | List Functions | sum_list, average_list, find_max, remove_duplicates |
| 7 | Dictionary Functions | merge_dicts, key/value exploration |
| 8 | Math Functions | add, subtract, multiply, divide |
| 9 | File Functions | write_to_file, read_from_file, append_to_file |
| 10 | Integration | Built main.py CLI integrating all modules |
| 11 | Error Handling & Polish | Added try/except, input validation, graceful handling |

---

## 🚀 Phase 2: Professional Polish (Days 12–18)
| Day | Focus | Description |
|-----|--------|-------------|
| 12 | Logging System | Add `logger.py` — record every operation (timestamp, function used, result) |
| 13 | Colors & Readability | Optional — integrate `colorama` for visual polish |
| 14 | Modular Cleanup | Refactor modules for clarity and consistency |
| 15 | Automated Testing | Add `test_functions.py` to test toolkit automatically |
| 16 | Documentation | Write clean docstrings and comments for every function |
| 17 | README Upgrade | Improve README with usage examples and screenshots |
| 18 | GitHub Sync | Organize folders, commit final toolkit version, tag v1.0 |

---

## 🧪 Phase 3: Mini-Projects (Days 19–27)
| Day | Project | Description |
|-----|----------|-------------|
| 19–20 | Text Analyzer | Reads text file, counts words, finds most common words, etc. |
| 21–22 | Expense Tracker | Simple budget app using file I/O and validation |
| 23–24 | Math Quiz App | Random math quiz using your math module + scoring system |
| 25–26 | File Organizer | Sorts files in a folder by type (uses `os` module) |
| 27 | Refactor & Polish | Improve naming, fix bugs, add logs if needed |

---

## 🧩 Phase 4: Final Polish + Showcase (Days 28–30)
| Day | Focus | Description |
|-----|--------|-------------|
| 28 | Packaging | Add `requirements.txt`, prepare clean layout |
| 29 | README Showcase | Add screenshots, description, and GitHub formatting |
| 30 | Final Commit & Wrap-Up | Final GitHub push, version tag, reflection summary |

---

## 🏁 End Result
✅ Full working toolkit  
✅ 3 mini-projects  
✅ GitHub-ready project portfolio  
✅ Strong foundation for intermediate Python (OOP, APIs, libraries)

---

> 

with open("/mnt/data/30_day_plan.md", "w", encoding="utf-8") as f:
    f.write(plan_md)

"/mnt/data/30_day_plan.md"
