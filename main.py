import frida
import pathlib
process_name: str = "My Andoird App Name"
def main():
    device: frida.core.Device = frida.get_usb_device()
    sess: frida.core.Session
    sess = device.attach(process_name)
    script_path: pathlib.Path = pathlib.Path("_agent.js")
    assert script_path.exists()
    script: frida.core.Script = sess.create_script(script_path.read_text())
    script.load()
if __name__ == "__main__":
    main()

