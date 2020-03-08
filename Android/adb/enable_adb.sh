settings put global development_settings_enabled 1
settings put global adb_enabled 1

echo "mtp,adb" > /data/property/persist.sys.usb.config
