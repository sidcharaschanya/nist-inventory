pyinstaller \
    --windowed \
    --add-data="images:images" \
    --name="Resource Room Inventory" \
    --icon=inventory-icon.icns \
    login_window.py
