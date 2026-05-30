# -*- mode: python ; coding: utf-8 -*-

datas = [
    ("Assets/paissa.ico", "Assets"),
    ("Data/hq.png", "Data"),
    ("Data/item.Pdt", "Data"),
    ("Data/marketable.py", "Data"),
    ("Data/version", "Data"),
    ("UI", "UI"),
]

a = Analysis(
    ["Paissa.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pytest", "black", "flake8"],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Paissa",
    icon="Assets/paissa.ico",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Paissa",
)
