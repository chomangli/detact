const { app, BrowserWindow } = require("electron")

function createWindow() {

  const win = new BrowserWindow({
    width: 1200,
    height: 800
  })

  win.loadURL("https://web-production-76462.up.railway.app/")

}

app.whenReady().then(createWindow)