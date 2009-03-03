%define name transfermii
%define version 0.6
%define beta 0
%define rel 2
%if %{beta}
%define release %mkrel 0.%{beta}.%{rel}
%define distname %{name}-%{version}-%{beta}
%else
%define release %mkrel %{rel}
%define distname %{name}-%{version}
%endif

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Transfer miis to/from a Nintendo wiimote
License:    GPL
Group:      System/Kernel and hardware
Url:        http://www.stacktic.org/
Source0:    %{distname}.tgz
Patch:      transfermii-0.6-fix-bluez-API-change.patch
BuildRequires: cwiid-devel
BuildRequires: gtk+2-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}

%description
This is a program which allows you to transfer miis to/from a Nintendo
wiimote with the possibility to change the mii mac address so as to be
able to modify the mii directly on your Wii.

%prep
%setup -q -n %{distname}
%patch -p 1

%build
make -f Makefile.old cli CFLAGS="%{optflags}"
make -f Makefile.old gui CFLAGS="%{optflags} `pkg-config gtk+-2.0 --cflags`"

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 %{name}_{cli,gui} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}_*
