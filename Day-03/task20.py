default_settings = {
    "theme": "Light",
    "language": "English",
    "font_size": 12,
    "notifications": True
}

user_settings = {
    "theme": "Dark",
    "font_size": 16
}

# Merging dictionaries
final_settings = default_settings.copy()
final_settings.update(user_settings)

print("Final Settings:", final_settings)