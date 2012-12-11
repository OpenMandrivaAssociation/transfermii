%define name transfermii
%define version 0.6
%define beta 0
%define rel 3
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


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6-3mdv2010.0
+ Revision: 445548
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-2mdv2009.1
+ Revision: 347734
- rebuild for latest bluez libs
- fix bluez libs API changes
- fix GUI building
- use proper opts flags

* Sun Mar 02 2008 Olivier Blin <oblin@mandriva.com> 0.6-1mdv2008.1
+ Revision: 177635
- 0.6
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Olivier Blin <oblin@mandriva.com> 0.5.2-1mdv2008.0
+ Revision: 69150
- 0.5.2

* Fri Apr 20 2007 Olivier Blin <oblin@mandriva.com> 0.5-0.rc2.1mdv2008.0
+ Revision: 15752
- initial Mandriva release
- Create transfermii

