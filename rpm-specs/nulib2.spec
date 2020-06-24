Name:		nulib2
Version:	3.1.0
Release:	5%{?dist}
Summary:	Disk and file archive program for NuFX (.SDK, .BXY) archives
License:	BSD
URL:		http://nulib.com/
Source0:	https://github.com/fadden/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
%description
NuLib2 is a command-line file archiver for Apple II archives. It can operate
on ShrinkIt and Binary II files (.shk, .sdk, .bxy, .bse, .bny, .bqy).

%prep
%setup -q

%build
cd nufxlib
%configure
# following make fails if smp_mflags used
make
cd ../nulib2
%configure
make %{?_smp_mflags}


%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 nulib2/nulib2 %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 nulib2/nulib2.1 %{buildroot}%{_mandir}/man1

%files
%license nulib2/COPYING
%{_bindir}/nulib2
%{_mandir}/man1/nulib2.1*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Eric Smith <eric@brouhaha.com> 3.1.0-1
- Initial version
