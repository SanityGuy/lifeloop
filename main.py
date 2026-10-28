import time
import sys
import datetime

def main():
    print("==================================================")
    print("            REAL LIFE LOOP SIMULATOR             ")
    print("==================================================\n")
    
    start = input("Ready to simulate life? (y/n)\nChoice: ").strip().lower()
    if start != "y":
        print("Goodbye.")
        sys.exit(0)

    print("\n[+] Initializing routine...\n")
    time.sleep(0.3)

    start_date = datetime.date(2026, 1, 1)

    for i in range(365):
        current_date = start_date + datetime.timedelta(days=i)
        date_str = current_date.strftime("%a, %b %d, %Y")
        
        print(f"[{date_str}]  Wake up  ->  Get ready  ->  Go to school/work  ->  Go back home  ->  Go to sleep")
        
        delay = 0.05
        time.sleep(delay)

    print("\n" + "=" * 50)
    print("365 DAYS COMPLETED.")
    print("=" * 50)
    time.sleep(0.2)
    
    print("\nAre you tired?")
    time.sleep(0.2)
    print("Living the same life over and over again is boring.")
    time.sleep(0.2)
    print("Exit the loop, be better.")
    time.sleep(0.2)
    print("Don't be like the snake eating its own tail.")
    quit = input("Exit? (y/n)\nChoice: ").strip().lower()
    if quit == "y":
        sys.exit(0)
    else:
        print("Goodbye.")
        sys.exit(0)

if __name__ == "__main__":
    main()