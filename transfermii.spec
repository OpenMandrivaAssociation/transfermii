%define name transfermii
%define version 0.5.2
%define beta 0
%define rel 1
%if %{beta}
%define release %mkrel 0.%{beta}.%{rel}
%define distname %{name}-%{version}-%{beta}
%else
%define release %mkrel %{rel}
%define distname %{name}-%{version}
%endif

Summary: Transfer miis to/from a Nintendo wiimote
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.stacktic.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cwiid-devel gtk+2-devel

%description
This is a program which allows you to transfer miis to/from a Nintendo
wiimote with the possibility to change the mii mac address so as to be
able to modify the mii directly on your Wii.

%prep
%setup -q -n %{distname}

%build
make -f Makefile.old cli gui

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
