Name:	VirtualBox-extensions
Version: 6.1.12
Release: 1%{?dist}
Summary: VirtualBox Extensions Pack

License: Oracle
Source0: Oracle_VM_VirtualBox_Extension_Pack-6.1.12.vbox-extpack

%description
Virtualbox Extensions Pack

%install
mkdir -p %{buildroot}/usr/lib/virtualbox/ExtensionPacks/
install -p -m 644 %{SOURCE0} %{buildroot}/usr/lib/virtualbox/ExtensionPacks/

%files
/usr/lib/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack-6.1.12.vbox-extpack

%changelog
