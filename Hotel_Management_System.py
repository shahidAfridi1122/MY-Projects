"""
Hotel Management System
A comprehensive hotel management application with GUI and database integration
"""

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import os

# ==================== DATABASE SETUP ====================

DB_FILE = "hotel_management.db"

def init_database():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create bookings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_no INTEGER NOT NULL,
            name TEXT NOT NULL,
            address TEXT,
            check_in_date TEXT NOT NULL,
            check_out_date TEXT NOT NULL,
            room_type TEXT,
            room_rent REAL DEFAULT 0,
            restaurant_bill REAL DEFAULT 0,
            laundry_bill REAL DEFAULT 0,
            game_bill REAL DEFAULT 0,
            service_charge REAL DEFAULT 1800,
            total_bill REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

# Initialize database on import
init_database()

# ==================== THEME COLORS ====================

PRIMARY_BG = "#1a1a2e"
SECONDARY_BG = "#16213e"
CARD_BG = "#0f3460"
ACCENT_COLOR = "#e94560"
SUCCESS_COLOR = "#00d9ff"
TEXT_COLOR = "#ffffff"
BUTTON_HOVER = "#c73954"
INPUT_BG = "#16213e"

# ==================== HOTEL MANAGEMENT CLASS ====================

class HotelManagement:
    def __init__(self):
        self.room_no_count = 0
        self.current_booking = None
        self.load_room_count()
    
    def load_room_count(self):
        """Load the highest room number from database"""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(room_no) FROM bookings")
        result = cursor.fetchone()
        self.room_no_count = result[0] if result[0] else 0
        conn.close()
    
    def get_next_room_no(self):
        """Get the next available room number"""
        self.room_no_count += 1
        return self.room_no_count
    
    def create_booking(self, name, address, check_in, check_out):
        """Create a new booking"""
        room_no = self.get_next_room_no()
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bookings (room_no, name, address, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?, ?)
        """, (room_no, name, address, check_in, check_out))
        booking_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return booking_id, room_no
    
    def update_room_rent(self, booking_id, room_type, nights):
        """Update room rent for a booking"""
        room_prices = {
            "Type A": 6000,
            "Type B": 5000,
            "Type C": 4000,
            "Type D": 3000
        }
        room_rent = room_prices.get(room_type, 0) * nights
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bookings 
            SET room_type = ?, room_rent = ?
            WHERE id = ?
        """, (room_type, room_rent, booking_id))
        conn.commit()
        conn.close()
        return room_rent
    
    def update_restaurant_bill(self, booking_id, amount):
        """Update restaurant bill"""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bookings 
            SET restaurant_bill = restaurant_bill + ?
            WHERE id = ?
        """, (amount, booking_id))
        conn.commit()
        conn.close()
    
    def update_laundry_bill(self, booking_id, amount):
        """Update laundry bill"""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bookings 
            SET laundry_bill = laundry_bill + ?
            WHERE id = ?
        """, (amount, booking_id))
        conn.commit()
        conn.close()
    
    def update_game_bill(self, booking_id, amount):
        """Update game bill"""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bookings 
            SET game_bill = game_bill + ?
            WHERE id = ?
        """, (amount, booking_id))
        conn.commit()
        conn.close()
    
    def get_booking(self, booking_id):
        """Get booking details"""
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings WHERE id = ?", (booking_id,))
        booking = cursor.fetchone()
        conn.close()
        return dict(booking) if booking else None
    
    def calculate_total(self, booking_id):
        """Calculate and update total bill"""
        booking = self.get_booking(booking_id)
        if not booking:
            return 0
        
        subtotal = (booking['room_rent'] + booking['restaurant_bill'] + 
                   booking['laundry_bill'] + booking['game_bill'])
        total = subtotal + booking['service_charge']
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE bookings 
            SET total_bill = ?
            WHERE id = ?
        """, (total, booking_id))
        conn.commit()
        conn.close()
        return total
    
    def get_all_bookings(self):
        """Get all bookings"""
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings ORDER BY created_at DESC")
        bookings = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return bookings

# ==================== GUI APPLICATION ====================

class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.hotel = HotelManagement()
        self.current_booking_id = None
        self.setup_window()
        self.create_main_ui()
    
    def setup_window(self):
        """Configure main window"""
        self.root.title("🏨 Thunder Hotel Management System")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        self.root.configure(bg=PRIMARY_BG)
        
        # Center window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_main_ui(self):
        """Create main user interface"""
        # Header
        header = tk.Frame(self.root, bg=PRIMARY_BG, pady=20)
        header.pack(fill="x")
        
        title = tk.Label(header, 
                        text="🏨 Thunder Hotel Management System",
                        font=('Arial', 28, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack()
        
        subtitle = tk.Label(header,
                           text="Professional Hotel Management Solution",
                           font=('Arial', 12),
                           bg=PRIMARY_BG, fg=TEXT_COLOR)
        subtitle.pack(pady=5)
        
        # Main container with notebook (tabs)
        main_container = tk.Frame(self.root, bg=PRIMARY_BG)
        main_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Create notebook style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=PRIMARY_BG, borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background=SECONDARY_BG,
                       foreground=TEXT_COLOR,
                       padding=[20, 10],
                       font=('Arial', 11, 'bold'))
        style.map('TNotebook.Tab',
                 background=[('selected', ACCENT_COLOR)],
                 foreground=[('selected', TEXT_COLOR)])
        
        notebook = ttk.Notebook(main_container)
        notebook.pack(fill="both", expand=True)
        
        # Create tabs
        self.tab_customer = tk.Frame(notebook, bg=PRIMARY_BG)
        self.tab_room = tk.Frame(notebook, bg=PRIMARY_BG)
        self.tab_restaurant = tk.Frame(notebook, bg=PRIMARY_BG)
        self.tab_laundry = tk.Frame(notebook, bg=PRIMARY_BG)
        self.tab_games = tk.Frame(notebook, bg=PRIMARY_BG)
        self.tab_bill = tk.Frame(notebook, bg=PRIMARY_BG)
        self.tab_bookings = tk.Frame(notebook, bg=PRIMARY_BG)
        
        notebook.add(self.tab_customer, text="👤 Customer Data")
        notebook.add(self.tab_room, text="🛏️ Room Booking")
        notebook.add(self.tab_restaurant, text="🍽️ Restaurant")
        notebook.add(self.tab_laundry, text="👔 Laundry")
        notebook.add(self.tab_games, text="🎮 Games")
        notebook.add(self.tab_bill, text="💰 Bill")
        notebook.add(self.tab_bookings, text="📋 All Bookings")
        
        # Setup each tab
        self.setup_customer_tab()
        self.setup_room_tab()
        self.setup_restaurant_tab()
        self.setup_laundry_tab()
        self.setup_games_tab()
        self.setup_bill_tab()
        self.setup_bookings_tab()
    
    def setup_customer_tab(self):
        """Setup customer data entry tab"""
        frame = tk.Frame(self.tab_customer, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title = tk.Label(frame, text="Customer Information",
                        font=('Arial', 20, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack(pady=10)
        
        # Form fields
        form_frame = tk.Frame(frame, bg=CARD_BG, padx=30, pady=20)
        form_frame.pack(expand=True, fill="both")
        
        # Name
        tk.Label(form_frame, text="Full Name *", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=0, column=0, sticky="w", pady=10, padx=10)
        self.name_entry = tk.Entry(form_frame, font=('Arial', 12), 
                                   width=40, bg=INPUT_BG, fg=TEXT_COLOR,
                                   insertbackground=TEXT_COLOR)
        self.name_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # Address
        tk.Label(form_frame, text="Address", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=1, column=0, sticky="w", pady=10, padx=10)
        self.address_entry = tk.Entry(form_frame, font=('Arial', 12), 
                                      width=40, bg=INPUT_BG, fg=TEXT_COLOR,
                                      insertbackground=TEXT_COLOR)
        self.address_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Check-in date
        tk.Label(form_frame, text="Check-in Date *", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=2, column=0, sticky="w", pady=10, padx=10)
        self.checkin_entry = tk.Entry(form_frame, font=('Arial', 12), 
                                      width=40, bg=INPUT_BG, fg=TEXT_COLOR,
                                      insertbackground=TEXT_COLOR)
        self.checkin_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.checkin_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Check-out date
        tk.Label(form_frame, text="Check-out Date *", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=3, column=0, sticky="w", pady=10, padx=10)
        self.checkout_entry = tk.Entry(form_frame, font=('Arial', 12), 
                                      width=40, bg=INPUT_BG, fg=TEXT_COLOR,
                                      insertbackground=TEXT_COLOR)
        self.checkout_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.checkout_entry.grid(row=3, column=1, pady=10, padx=10)
        
        # Status label
        self.customer_status = tk.Label(form_frame, text="",
                                       font=('Arial', 11),
                                       bg=CARD_BG, fg=SUCCESS_COLOR)
        self.customer_status.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Submit button
        submit_btn = tk.Button(form_frame, text="Create Booking",
                              font=('Arial', 14, 'bold'),
                              bg=ACCENT_COLOR, fg=TEXT_COLOR,
                              activebackground=BUTTON_HOVER,
                              activeforeground=TEXT_COLOR,
                              cursor="hand2", width=20, height=2,
                              command=self.create_customer_booking)
        submit_btn.grid(row=5, column=0, columnspan=2, pady=20)
    
    def create_customer_booking(self):
        """Create a new customer booking"""
        name = self.name_entry.get().strip()
        address = self.address_entry.get().strip()
        check_in = self.checkin_entry.get().strip()
        check_out = self.checkout_entry.get().strip()
        
        if not name or not check_in or not check_out:
            messagebox.showwarning("Validation", 
                                 "Please fill in all required fields (Name, Check-in, Check-out)!")
            return
        
        try:
            booking_id, room_no = self.hotel.create_booking(name, address, check_in, check_out)
            self.current_booking_id = booking_id
            self.customer_status.config(
                text=f"✅ Booking created successfully! Room No: {room_no} | Booking ID: {booking_id}",
                fg=SUCCESS_COLOR
            )
            messagebox.showinfo("Success", 
                              f"Booking created successfully!\nRoom No: {room_no}\nBooking ID: {booking_id}")
            # Clear form
            self.name_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.checkin_entry.delete(0, tk.END)
            self.checkin_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
            self.checkout_entry.delete(0, tk.END)
            self.checkout_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create booking: {str(e)}")
    
    def setup_room_tab(self):
        """Setup room booking tab"""
        frame = tk.Frame(self.tab_room, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title = tk.Label(frame, text="Room Booking",
                        font=('Arial', 20, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack(pady=10)
        
        # Room types
        room_frame = tk.Frame(frame, bg=CARD_BG, padx=30, pady=20)
        room_frame.pack(expand=True, fill="both")
        
        tk.Label(room_frame, text="Available Room Types:",
                font=('Arial', 14, 'bold'),
                bg=CARD_BG, fg=TEXT_COLOR).pack(pady=10)
        
        rooms_info = [
            ("Type A", "Rs 6,000 per night", "Luxury Suite"),
            ("Type B", "Rs 5,000 per night", "Deluxe Room"),
            ("Type C", "Rs 4,000 per night", "Standard Room"),
            ("Type D", "Rs 3,000 per night", "Economy Room")
        ]
        
        for room_type, price, desc in rooms_info:
            room_card = tk.Frame(room_frame, bg=SECONDARY_BG, padx=15, pady=10)
            room_card.pack(fill="x", pady=5)
            tk.Label(room_card, text=f"{room_type} - {price}",
                    font=('Arial', 12, 'bold'),
                    bg=SECONDARY_BG, fg=ACCENT_COLOR).pack(anchor="w")
            tk.Label(room_card, text=desc,
                    font=('Arial', 10),
                    bg=SECONDARY_BG, fg=TEXT_COLOR).pack(anchor="w")
        
        # Booking form
        form_frame = tk.Frame(room_frame, bg=CARD_BG)
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="Booking ID:", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=0, column=0, sticky="w", pady=10, padx=10)
        self.room_booking_id = tk.Entry(form_frame, font=('Arial', 12), 
                                       width=20, bg=INPUT_BG, fg=TEXT_COLOR,
                                       insertbackground=TEXT_COLOR)
        self.room_booking_id.grid(row=0, column=1, pady=10, padx=10)
        
        tk.Label(form_frame, text="Room Type:", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=1, column=0, sticky="w", pady=10, padx=10)
        self.room_type_var = tk.StringVar(value="Type A")
        room_type_menu = ttk.Combobox(form_frame, textvariable=self.room_type_var,
                                     values=["Type A", "Type B", "Type C", "Type D"],
                                     state="readonly", width=17)
        room_type_menu.grid(row=1, column=1, pady=10, padx=10)
        
        tk.Label(form_frame, text="Number of Nights:", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).grid(
                row=2, column=0, sticky="w", pady=10, padx=10)
        self.nights_entry = tk.Entry(form_frame, font=('Arial', 12), 
                                    width=20, bg=INPUT_BG, fg=TEXT_COLOR,
                                    insertbackground=TEXT_COLOR)
        self.nights_entry.grid(row=2, column=1, pady=10, padx=10)
        
        self.room_status = tk.Label(form_frame, text="",
                                   font=('Arial', 11),
                                   bg=CARD_BG, fg=SUCCESS_COLOR)
        self.room_status.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(form_frame, text="Calculate Room Rent",
                 font=('Arial', 12, 'bold'),
                 bg=ACCENT_COLOR, fg=TEXT_COLOR,
                 activebackground=BUTTON_HOVER,
                 activeforeground=TEXT_COLOR,
                 cursor="hand2", width=20,
                 command=self.calculate_room_rent).grid(
                 row=4, column=0, columnspan=2, pady=20)
    
    def calculate_room_rent(self):
        """Calculate room rent"""
        try:
            booking_id = int(self.room_booking_id.get().strip())
            nights = int(self.nights_entry.get().strip())
            room_type = self.room_type_var.get()
            
            if nights <= 0:
                messagebox.showwarning("Validation", "Number of nights must be greater than 0!")
                return
            
            room_rent = self.hotel.update_room_rent(booking_id, room_type, nights)
            self.room_status.config(
                text=f"✅ Room rent calculated: Rs {room_rent:,.2f}",
                fg=SUCCESS_COLOR
            )
            messagebox.showinfo("Success", 
                              f"Room rent calculated successfully!\nRoom Type: {room_type}\nNights: {nights}\nTotal: Rs {room_rent:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid booking ID and number of nights!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate room rent: {str(e)}")
    
    def setup_restaurant_tab(self):
        """Setup restaurant tab"""
        frame = tk.Frame(self.tab_restaurant, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title = tk.Label(frame, text="Restaurant Menu",
                        font=('Arial', 20, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack(pady=10)
        
        # Menu items
        menu_frame = tk.Frame(frame, bg=CARD_BG, padx=30, pady=20)
        menu_frame.pack(expand=True, fill="both")
        
        menu_items = [
            ("Water", 20),
            ("Tea", 10),
            ("Breakfast Combo", 90),
            ("Lunch", 110),
            ("Dinner", 150)
        ]
        
        self.restaurant_items = {}
        for i, (item, price) in enumerate(menu_items):
            item_frame = tk.Frame(menu_frame, bg=SECONDARY_BG, padx=15, pady=10)
            item_frame.pack(fill="x", pady=5)
            
            tk.Label(item_frame, text=f"{item} - Rs {price}",
                    font=('Arial', 12, 'bold'),
                    bg=SECONDARY_BG, fg=ACCENT_COLOR).pack(side="left", padx=10)
            
            quantity_var = tk.StringVar(value="0")
            quantity_entry = tk.Entry(item_frame, textvariable=quantity_var,
                                     width=10, bg=INPUT_BG, fg=TEXT_COLOR,
                                     insertbackground=TEXT_COLOR)
            quantity_entry.pack(side="right", padx=10)
            
            self.restaurant_items[item] = (price, quantity_var)
        
        # Booking ID and calculate
        calc_frame = tk.Frame(menu_frame, bg=CARD_BG)
        calc_frame.pack(pady=20)
        
        tk.Label(calc_frame, text="Booking ID:", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).pack(side="left", padx=10)
        self.restaurant_booking_id = tk.Entry(calc_frame, font=('Arial', 12), 
                                             width=15, bg=INPUT_BG, fg=TEXT_COLOR,
                                             insertbackground=TEXT_COLOR)
        self.restaurant_booking_id.pack(side="left", padx=10)
        
        tk.Button(calc_frame, text="Add to Bill",
                 font=('Arial', 12, 'bold'),
                 bg=ACCENT_COLOR, fg=TEXT_COLOR,
                 activebackground=BUTTON_HOVER,
                 activeforeground=TEXT_COLOR,
                 cursor="hand2", width=15,
                 command=self.calculate_restaurant_bill).pack(side="left", padx=10)
    
    def calculate_restaurant_bill(self):
        """Calculate restaurant bill"""
        try:
            booking_id = int(self.restaurant_booking_id.get().strip())
            total = 0
            
            for item, (price, quantity_var) in self.restaurant_items.items():
                try:
                    qty = int(quantity_var.get())
                    if qty > 0:
                        total += price * qty
                except ValueError:
                    pass
            
            if total > 0:
                self.hotel.update_restaurant_bill(booking_id, total)
                messagebox.showinfo("Success", 
                                  f"Restaurant bill added!\nTotal: Rs {total:,.2f}")
                # Reset quantities
                for item, (price, quantity_var) in self.restaurant_items.items():
                    quantity_var.set("0")
            else:
                messagebox.showwarning("Validation", "Please select at least one item!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid booking ID!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate restaurant bill: {str(e)}")
    
    def setup_laundry_tab(self):
        """Setup laundry tab"""
        frame = tk.Frame(self.tab_laundry, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title = tk.Label(frame, text="Laundry Service",
                        font=('Arial', 20, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack(pady=10)
        
        menu_frame = tk.Frame(frame, bg=CARD_BG, padx=30, pady=20)
        menu_frame.pack(expand=True, fill="both")
        
        laundry_items = [
            ("Shorts", 3),
            ("Trousers", 4),
            ("Shirt", 5),
            ("Jeans", 6),
            ("Girl Suit", 8)
        ]
        
        self.laundry_items = {}
        for item, price in laundry_items:
            item_frame = tk.Frame(menu_frame, bg=SECONDARY_BG, padx=15, pady=10)
            item_frame.pack(fill="x", pady=5)
            
            tk.Label(item_frame, text=f"{item} - Rs {price}",
                    font=('Arial', 12, 'bold'),
                    bg=SECONDARY_BG, fg=ACCENT_COLOR).pack(side="left", padx=10)
            
            quantity_var = tk.StringVar(value="0")
            quantity_entry = tk.Entry(item_frame, textvariable=quantity_var,
                                     width=10, bg=INPUT_BG, fg=TEXT_COLOR,
                                     insertbackground=TEXT_COLOR)
            quantity_entry.pack(side="right", padx=10)
            
            self.laundry_items[item] = (price, quantity_var)
        
        calc_frame = tk.Frame(menu_frame, bg=CARD_BG)
        calc_frame.pack(pady=20)
        
        tk.Label(calc_frame, text="Booking ID:", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).pack(side="left", padx=10)
        self.laundry_booking_id = tk.Entry(calc_frame, font=('Arial', 12), 
                                          width=15, bg=INPUT_BG, fg=TEXT_COLOR,
                                          insertbackground=TEXT_COLOR)
        self.laundry_booking_id.pack(side="left", padx=10)
        
        tk.Button(calc_frame, text="Add to Bill",
                 font=('Arial', 12, 'bold'),
                 bg=ACCENT_COLOR, fg=TEXT_COLOR,
                 activebackground=BUTTON_HOVER,
                 activeforeground=TEXT_COLOR,
                 cursor="hand2", width=15,
                 command=self.calculate_laundry_bill).pack(side="left", padx=10)
    
    def calculate_laundry_bill(self):
        """Calculate laundry bill"""
        try:
            booking_id = int(self.laundry_booking_id.get().strip())
            total = 0
            
            for item, (price, quantity_var) in self.laundry_items.items():
                try:
                    qty = int(quantity_var.get())
                    if qty > 0:
                        total += price * qty
                except ValueError:
                    pass
            
            if total > 0:
                self.hotel.update_laundry_bill(booking_id, total)
                messagebox.showinfo("Success", 
                                  f"Laundry bill added!\nTotal: Rs {total:,.2f}")
                for item, (price, quantity_var) in self.laundry_items.items():
                    quantity_var.set("0")
            else:
                messagebox.showwarning("Validation", "Please select at least one item!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid booking ID!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate laundry bill: {str(e)}")
    
    def setup_games_tab(self):
        """Setup games tab"""
        frame = tk.Frame(self.tab_games, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title = tk.Label(frame, text="Games & Recreation",
                        font=('Arial', 20, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack(pady=10)
        
        menu_frame = tk.Frame(frame, bg=CARD_BG, padx=30, pady=20)
        menu_frame.pack(expand=True, fill="both")
        
        game_items = [
            ("Table Tennis", 60),
            ("Bowling", 80),
            ("Snooker", 70),
            ("Video Games", 90),
            ("Pool", 50)
        ]
        
        self.game_items = {}
        for item, price_per_hour in game_items:
            item_frame = tk.Frame(menu_frame, bg=SECONDARY_BG, padx=15, pady=10)
            item_frame.pack(fill="x", pady=5)
            
            tk.Label(item_frame, text=f"{item} - Rs {price_per_hour}/hour",
                    font=('Arial', 12, 'bold'),
                    bg=SECONDARY_BG, fg=ACCENT_COLOR).pack(side="left", padx=10)
            
            hours_var = tk.StringVar(value="0")
            hours_entry = tk.Entry(item_frame, textvariable=hours_var,
                                  width=10, bg=INPUT_BG, fg=TEXT_COLOR,
                                  insertbackground=TEXT_COLOR)
            hours_entry.pack(side="right", padx=10)
            
            self.game_items[item] = (price_per_hour, hours_var)
        
        calc_frame = tk.Frame(menu_frame, bg=CARD_BG)
        calc_frame.pack(pady=20)
        
        tk.Label(calc_frame, text="Booking ID:", 
                font=('Arial', 12), bg=CARD_BG, fg=TEXT_COLOR).pack(side="left", padx=10)
        self.game_booking_id = tk.Entry(calc_frame, font=('Arial', 12), 
                                       width=15, bg=INPUT_BG, fg=TEXT_COLOR,
                                       insertbackground=TEXT_COLOR)
        self.game_booking_id.pack(side="left", padx=10)
        
        tk.Button(calc_frame, text="Add to Bill",
                 font=('Arial', 12, 'bold'),
                 bg=ACCENT_COLOR, fg=TEXT_COLOR,
                 activebackground=BUTTON_HOVER,
                 activeforeground=TEXT_COLOR,
                 cursor="hand2", width=15,
                 command=self.calculate_game_bill).pack(side="left", padx=10)
    
    def calculate_game_bill(self):
        """Calculate game bill"""
        try:
            booking_id = int(self.game_booking_id.get().strip())
            total = 0
            
            for item, (price_per_hour, hours_var) in self.game_items.items():
                try:
                    hours = int(hours_var.get())
                    if hours > 0:
                        total += price_per_hour * hours
                except ValueError:
                    pass
            
            if total > 0:
                self.hotel.update_game_bill(booking_id, total)
                messagebox.showinfo("Success", 
                                  f"Game bill added!\nTotal: Rs {total:,.2f}")
                for item, (price_per_hour, hours_var) in self.game_items.items():
                    hours_var.set("0")
            else:
                messagebox.showwarning("Validation", "Please enter hours for at least one game!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid booking ID!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate game bill: {str(e)}")
    
    def setup_bill_tab(self):
        """Setup bill display tab"""
        frame = tk.Frame(self.tab_bill, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title = tk.Label(frame, text="Hotel Bill",
                        font=('Arial', 20, 'bold'),
                        bg=PRIMARY_BG, fg=ACCENT_COLOR)
        title.pack(pady=10)
        
        # Bill display area
        bill_frame = tk.Frame(frame, bg=CARD_BG, padx=30, pady=20)
        bill_frame.pack(expand=True, fill="both")
        
        # Booking ID input
        input_frame = tk.Frame(bill_frame, bg=CARD_BG)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Booking ID:", 
                font=('Arial', 12, 'bold'),
                bg=CARD_BG, fg=TEXT_COLOR).pack(side="left", padx=10)
        self.bill_booking_id = tk.Entry(input_frame, font=('Arial', 12), 
                                       width=20, bg=INPUT_BG, fg=TEXT_COLOR,
                                       insertbackground=TEXT_COLOR)
        self.bill_booking_id.pack(side="left", padx=10)
        
        tk.Button(input_frame, text="Generate Bill",
                 font=('Arial', 12, 'bold'),
                 bg=ACCENT_COLOR, fg=TEXT_COLOR,
                 activebackground=BUTTON_HOVER,
                 activeforeground=TEXT_COLOR,
                 cursor="hand2", width=15,
                 command=self.generate_bill).pack(side="left", padx=10)
        
        # Bill display
        self.bill_text = scrolledtext.ScrolledText(bill_frame,
                                                   font=('Courier', 11),
                                                   bg=INPUT_BG, fg=TEXT_COLOR,
                                                   width=70, height=25,
                                                   wrap=tk.WORD)
        self.bill_text.pack(expand=True, fill="both", pady=10)
    
    def generate_bill(self):
        """Generate and display bill"""
        try:
            booking_id = int(self.bill_booking_id.get().strip())
            booking = self.hotel.get_booking(booking_id)
            
            if not booking:
                messagebox.showerror("Error", "Booking not found!")
                return
            
            # Calculate total
            total = self.hotel.calculate_total(booking_id)
            booking = self.hotel.get_booking(booking_id)  # Refresh with updated total
            
            # Generate bill text
            bill_content = f"""
{'='*60}
            Thunder HOTEL - BILL RECEIPT
{'='*60}

Customer Details:
    Name: {booking['name']}
    Address: {booking['address'] or 'N/A'}
    Room No: {booking['room_no']}
    Check-in Date: {booking['check_in_date']}
    Check-out Date: {booking['check_out_date']}
    Room Type: {booking['room_type'] or 'Not selected'}

{'='*60}
BILL BREAKDOWN:
{'='*60}

    Room Rent:              Rs {booking['room_rent']:>12,.2f}
    Restaurant Bill:        Rs {booking['restaurant_bill']:>12,.2f}
    Laundry Bill:           Rs {booking['laundry_bill']:>12,.2f}
    Game Bill:              Rs {booking['game_bill']:>12,.2f}
    {'-'*60}
    Subtotal:                Rs {(booking['room_rent'] + booking['restaurant_bill'] + booking['laundry_bill'] + booking['game_bill']):>12,.2f}
    Service Charge:         Rs {booking['service_charge']:>12,.2f}
    {'='*60}
    GRAND TOTAL:            Rs {booking['total_bill']:>12,.2f}
    {'='*60}

    Booking ID: {booking_id}
    Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Thank you for choosing Thunder Hotel!
{'='*60}
"""
            
            self.bill_text.delete(1.0, tk.END)
            self.bill_text.insert(1.0, bill_content)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid booking ID!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate bill: {str(e)}")
    
    def setup_bookings_tab(self):
        """Setup all bookings display tab"""
        frame = tk.Frame(self.tab_bookings, bg=PRIMARY_BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)
        
        title_frame = tk.Frame(frame, bg=PRIMARY_BG)
        title_frame.pack(fill="x", pady=10)
        
        tk.Label(title_frame, text="All Bookings",
                font=('Arial', 20, 'bold'),
                bg=PRIMARY_BG, fg=ACCENT_COLOR).pack(side="left")
        
        tk.Button(title_frame, text="Refresh",
                 font=('Arial', 11, 'bold'),
                 bg=ACCENT_COLOR, fg=TEXT_COLOR,
                 activebackground=BUTTON_HOVER,
                 activeforeground=TEXT_COLOR,
                 cursor="hand2", width=12,
                 command=self.refresh_bookings).pack(side="right")
        
        # Treeview for bookings
        columns = ("ID", "Room No", "Name", "Check-in", "Check-out", "Total Bill")
        self.bookings_tree = ttk.Treeview(frame, columns=columns, show="headings", height=20)
        
        for col in columns:
            self.bookings_tree.heading(col, text=col)
            self.bookings_tree.column(col, width=120, anchor="center")
        
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.bookings_tree.yview)
        self.bookings_tree.configure(yscrollcommand=scrollbar.set)
        
        self.bookings_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.refresh_bookings()
    
    def refresh_bookings(self):
        """Refresh bookings list"""
        # Clear existing items
        for item in self.bookings_tree.get_children():
            self.bookings_tree.delete(item)
        
        # Load bookings
        bookings = self.hotel.get_all_bookings()
        
        for booking in bookings:
            self.bookings_tree.insert("", "end", values=(
                booking['id'],
                booking['room_no'],
                booking['name'],
                booking['check_in_date'],
                booking['check_out_date'],
                f"Rs {booking['total_bill']:,.2f}"
            ))

# ==================== MAIN ====================

def main():
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
