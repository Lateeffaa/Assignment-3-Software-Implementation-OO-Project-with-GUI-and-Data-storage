import pickle
import os
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

infoPath = "data"  # The data will be stored here
if not os.path.exists(infoPath):
    os.makedirs(infoPath)

# Functions to save and load the employee information
def saveInfo(employees):
    try:
        with open(os.path.join(infoPath, 'employees.pkl'), 'wb') as dumpf:
            pickle.dump(employees, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadInfo():
    try:
        with open(os.path.join(infoPath, 'employees.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Employee not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load event information
def saveEventInfo(events):
    try:
        with open(os.path.join(infoPath, 'events.pkl'), 'wb') as dumpf:
            pickle.dump(events, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadEventInfo():
    try:
        with open(os.path.join(infoPath, 'events.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Event not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load supplier information
def saveSupplierInfo(supplier):
    try:
        with open(os.path.join(infoPath, 'suppliers.pkl'), 'wb') as dumpf:
            pickle.dump(supplier, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadSupplierInfo():
    try:
        with open(os.path.join(infoPath, 'suppliers.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Supplier not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load guest information
def saveGuestInfo(guests):
    try:
        with open(os.path.join(infoPath, 'guests.pkl'), 'wb') as dumpf:
            pickle.dump(guests, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadGuestInfo():
    try:
        with open(os.path.join(infoPath, 'guests.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Guest not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load client information
def saveClientInfo(clients):
    try:
        with open(os.path.join(infoPath, 'clients.pkl'), 'wb') as dumpf:
            pickle.dump(clients, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadClientInfo():
    try:
        with open(os.path.join(infoPath, 'clients.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Client not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}


# Functions to save and load venue information
def saveVenueInfo(venues):
    try:
        with open(os.path.join(infoPath, 'venues.pkl'), 'wb') as dumpf:
            pickle.dump(venues, dumpf)
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the information: {e}")

def loadVenueInfo():
    try:
        with open(os.path.join(infoPath, 'venues.pkl'), 'rb') as loadf:
            return pickle.load(loadf)
    except FileNotFoundError:
        messagebox.showinfo("Information", "Venue not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the information: {e}")
        return {}

