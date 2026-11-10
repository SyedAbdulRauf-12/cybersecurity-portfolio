test_settings = {
    'theme': 'light',
    'language': 'English',
    'notifications': 'enabled',
    'volume': 'high'
}

def add_setting(d,t):
    key, val = t
    lower_key = key.lower()
    if lower_key in d.keys():
        return (f"Setting '{lower_key}' already exists! Cannot add a new setting with this name.")
        
    d[lower_key] = val.lower() if isinstance(val, str) else val

    return f"Setting '{lower_key}' added with value '{val}' successfully!"

def update_setting(d, t):
    key, val = t
    lower_key = key.lower()

    if lower_key not in d.keys():
        return f"Setting '{lower_key}' does not exist! Cannot update a non-existing setting."

    d[lower_key] = val.lower() if isinstance(val, str) else val

    return f"Setting '{lower_key}' updated to '{val}' successfully!"

def delete_setting(d, t):
    key = t
    lower_key = key.lower()
    if lower_key not in d.keys():
        return "Setting not found!"
    del d[lower_key]

    return f"Setting '{lower_key}' deleted successfully!"

def view_settings(d):

    if d == {}:
        return "No settings available."

    lines = [f"{k.title()}: {v}" for k, v in d.items()]
    return "Current User Settings:\n" + "\n".join(lines) + "\n"
    
add = add_setting({'theme': 'light'}, ('volume', 'high'))

update = update_setting({'theme': 'light'}, ('volume', 'high'))

delete = delete_setting({'theme': 'light', 'language': 'English'}, 'theme')

view = view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})

print(view)

