import tkinter as tk
from predictor import predict_url

def check_url():
    url = entry.get().strip()
    if not url:
        result_label.config(text="Please enter a URL.", fg="gray", bg="#f8f8f8")
        return
    result, confidence = predict_url(url)
    if result == "PHISHING":
        result_label.config(
            text=f"⚠️  PHISHING DETECTED\nConfidence: {confidence}%",
            fg="#D85A30", bg="#FAECE7"
        )
    else:
        result_label.config(
            text=f"✅  SAFE WEBSITE\nConfidence: {confidence}%",
            fg="#0F6E56", bg="#E1F5EE"
        )

window = tk.Tk()
window.title("Phishing URL Detector")
window.geometry("520x280")
window.configure(bg="#f8f8f8")
window.resizable(False, False)

tk.Label(window, text="🛡️ Phishing URL Detector",
         font=("Arial", 15, "bold"), bg="#f8f8f8").pack(pady=(20, 4))

tk.Label(window, text="Enter a URL to check:",
         font=("Arial", 11), bg="#f8f8f8", fg="gray").pack()

entry = tk.Entry(window, width=55, font=("Arial", 11), bd=2, relief="groove")
entry.pack(pady=8)

tk.Button(window, text="Check URL", command=check_url,
          font=("Arial", 11, "bold"), bg="#378ADD", fg="white",
          padx=12, pady=6, relief="flat", cursor="hand2").pack()

result_label = tk.Label(window, text="", font=("Arial", 13, "bold"),
                        bg="#f8f8f8", pady=12, width=40)
result_label.pack(pady=10)

window.mainloop()