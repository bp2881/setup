def ubuntu23_04():
    for line in content:
        for app in required_apps:
            d = False
            if app in line:
                if app == line[:len(app):]:
                    print("Already Installed")
                    d = True
            if app not in line or d!= True:
                print(app)