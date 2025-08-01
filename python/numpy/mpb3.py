##-----Author -----
#Pravish Tripathi



import ast
import traceback
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, ttk
import openai

# --- Replace this with your OpenAI API Key ---
##if needed further in future
client = openai.OpenAI(api_key="your-api-key-here")

FRIENDLY_TIPS = {
    "SyntaxError": "Check colons, brackets, or indentation.",
    "NameError": "You're using an undefined variable or function.",
    "TypeError": "Incompatible data types used.",
    "IndexError": "List index out of range.",
    "KeyError": "Missing dictionary key.",
    "IndentationError": "Inconsistent indentation (use 4 spaces).",
    "ValueError": "A function received an invalid value.",
    "ZeroDivisionError": "Division by zero is not allowed."
}

def explain_error(error_type, message):
    tip = FRIENDLY_TIPS.get(error_type, "Unknown error.")
    return f"🔍 Error Type: {error_type}\n🧠 What it means:\n{tip}\n\n📋 Details:\n{message}"

def check_syntax(code):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, explain_error("SyntaxError", f"{e.msg} on line {e.lineno}"), e.lineno

def execute_code(code):
    try:
        exec(code, {})
        return True, "✅ Code ran successfully!", None
    except Exception as e:
        tb = traceback.format_exc()
        error_type = type(e).__name__
        return False, explain_error(error_type, tb), e.__traceback__.tb_lineno

def ai_explain_and_fix(code, error_msg):
    try:
        prompt = (
            f"You're an expert Python tutor. The user wrote:\n\n{code}\n\n"
            f"Which caused this error:\n{error_msg}\n\n"
            f"Explain the error clearly and give a corrected version of the code."
        )
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600,
            temperature=0.4
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ AI Solve Failed: {e}"

def ai_auto_fix(code):
    try:
        prompt = f"This Python code has errors:\n\n{code}\n\nExplain and fix it."
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600,
            temperature=0.4
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ AI Solve Failed: {e}"

# --- GUI Logic ---
def analyze_code():
    clear_highlights()
    code = code_input.get("1.0", tk.END)
    if not code.strip():
        messagebox.showwarning("Input Needed", "Please enter some Python code.")
        return

    is_valid, result, line = check_syntax(code)
    if not is_valid:
        highlight_error_line(line)
        ai_help = ai_explain_and_fix(code, result)
        raw_output_tab(result)
        ai_suggestion_tab(ai_help)
        return

    ran_ok, result, line = execute_code(code)
    if not ran_ok:
        highlight_error_line(line)
        ai_help = ai_explain_and_fix(code, result)
        raw_output_tab(result)
        ai_suggestion_tab(ai_help)
        return

    raw_output_tab(result)
    ai_suggestion_tab("✅ No errors to explain!")

def ai_solve_code():
    code = code_input.get("1.0", tk.END)
    if not code.strip():
        messagebox.showwarning("Input Needed", "Please enter some Python code.")
        return

    ai_result = ai_auto_fix(code)
    ai_suggestion_tab(ai_result)

    if messagebox.askyesno("Apply Fix", "Apply the AI-corrected code to the editor?"):
        # Try to extract only code block from response
        lines = ai_result.splitlines()
        code_block = []
        recording = False
        for line in lines:
            if line.strip().startswith("```"):
                recording = not recording
                continue
            if recording:
                code_block.append(line)
        fixed_code = "\n".join(code_block).strip()
        if fixed_code:
            code_input.delete("1.0", tk.END)
            code_input.insert(tk.END, fixed_code)

def highlight_error_line(line):
    if line:
        index = f"{line}.0"
        code_input.tag_add("error", index, f"{line}.end")
        code_input.tag_config("error", background="#ffcccc")

def clear_highlights():
    code_input.tag_remove("error", "1.0", tk.END)

def raw_output_tab(text):
    raw_output.config(state='normal')
    raw_output.delete("1.0", tk.END)
    raw_output.insert(tk.END, text)
    raw_output.config(state='disabled')

def ai_suggestion_tab(text):
    ai_output.config(state='normal')
    ai_output.delete("1.0", tk.END)
    ai_output.insert(tk.END, text)
    ai_output.config(state='disabled')

def insert_example(type_):
    examples = {
        "turtle": "import turtle\nt = turtle.Turtle()\nt.forward(100)\nt.circle(50)\nturtle.done()",
        "error": "for i in range(5)\nprint(i)"
    }
    code_input.delete("1.0", tk.END)
    code_input.insert(tk.END, examples[type_])

def clear_all():
    code_input.delete("1.0", tk.END)
    raw_output_tab("")
    ai_suggestion_tab("")
    clear_highlights()

def save_code():
    file = filedialog.asksaveasfilename(defaultextension=".py")
    if file:
        with open(file, "w") as f:
            f.write(code_input.get("1.0", tk.END))

def load_code():
    file = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file:
        with open(file, "r") as f:
            code_input.delete("1.0", tk.END)
            code_input.insert(tk.END, f.read())

# --- GUI Setup --- for  better user experience
root = tk.Tk()
root.title("🐢 AI-Powered Python Debugger (with Turtle Support)")
root.geometry("1100x800")
root.resizable(True, True)

tk.Label(root, text="💻 Python Code Editor:", font=("Arial", 12)).pack(anchor='w', padx=10, pady=(10, 0))
code_input = scrolledtext.ScrolledText(root, height=15, width=130, font=("Courier", 11))
code_input.pack(padx=10, pady=5)

# Buttons Row
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="🔍 Analyze with AI", command=analyze_code, bg="#3f51b5", fg="white").pack(side='left', padx=5)
tk.Button(btn_frame, text="🛠️ Auto-Fix & Apply", command=ai_solve_code, bg="#4caf50", fg="white").pack(side='left', padx=5)
tk.Button(btn_frame, text="🐢 Sample Turtle", command=lambda: insert_example("turtle")).pack(side='left', padx=5)
tk.Button(btn_frame, text="🐞 Syntax Error", command=lambda: insert_example("error")).pack(side='left', padx=5)
tk.Button(btn_frame, text="💾 Save", command=save_code).pack(side='left', padx=5)
tk.Button(btn_frame, text="📂 Load", command=load_code).pack(side='left', padx=5)
tk.Button(btn_frame, text="🧹 Clear", command=clear_all).pack(side='left', padx=5)

# Tabbed Output
tabs = ttk.Notebook(root)
tabs.pack(expand=1, fill='both', padx=10, pady=10)

raw_output = scrolledtext.ScrolledText(tabs, font=("Courier", 11), state='disabled', bg="#f5f5f5")
ai_output = scrolledtext.ScrolledText(tabs, font=("Courier", 11), state='disabled', bg="#f5f5f5")

tabs.add(raw_output, text="📝 Raw Output")
tabs.add(ai_output, text="🤖 AI Suggestions")

root.mainloop()
