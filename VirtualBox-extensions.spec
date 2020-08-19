Name:	VirtualBox-extensions
Version: 6.1.12
Release: 2%{?dist}
Summary: VirtualBox Extensions Pack

License: Oracle
Source0: Oracle_VM_VirtualBox_Extension_Pack-6.1.12.vbox-extpack

%description
Virtualbox Extensions Pack

%install
mkdir -p %{buildroot}/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/
tar xvfz %{SOURCE0} -C %{buildroot}/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/

%files
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack-license.html
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack-license.rtf
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack-license.txt
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack.manifest
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack.signature
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack.xml
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/PXE-Intel.rom
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxEhciR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxEhciR3.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxHostWebcam.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxNvmeR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxNvmeR3.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxPuelMain.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxPuelMainVM.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxUsbCardReaderR3.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxUsbWebcamR3.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VBoxVRDP.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/darwin.amd64/VDPluginCrypt.dylib
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxEhciR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxEhciR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxHostWebcam.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxNvmeR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxNvmeR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxPuelMain.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxPuelMainVM.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxUsbCardReaderR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxUsbWebcamR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxVRDP.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VDPluginCrypt.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxEhciR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxEhciR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxHostWebcam.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxNvmeR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxNvmeR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxPuelMain.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxPuelMainVM.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxUsbCardReaderR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxUsbWebcamR3.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VBoxVRDP.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/solaris.amd64/VDPluginCrypt.so
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxEhciR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxEhciR3.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxHostWebcam.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxNvmeR0.r0
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxNvmeR3.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxPuelMain.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxPuelMainVM.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxUsbCardReaderR3.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxUsbWebcamR3.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VBoxVRDP.dll
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/win.amd64/VDPluginCrypt.dll


%changelog
