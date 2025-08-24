from socketify import App

def make_app(app: App):
    app.get("/", lambda res, req: res.end("Hello, World!\n"))

if __name__ == "__main__":
    app = App()
    make_app(app)
    app.listen(
        8000, 
        lambda config: print(f"Listening on port http://localhost:{ config.port} now\n"),
    )
    app.run()
