%global gitowner axel-download-accelerator

Name:       axel
Version:    2.16
Release:    5%{?dist}
Summary:    Light command line download accelerator for Linux and Unix

License:    GPLv2+
URL:        https://github.com/%{gitowner}/%{name}
Source0:    https://github.com/%{gitowner}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: gettext-devel
BuildRequires: pkgconfig(libssl)
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc

%description
Axel tries to accelerate HTTP/FTP downloading process by using
multiple connections for one file. It can use multiple mirrors for a
download. Axel has no dependencies and is lightweight, so it might
be useful as a wget clone on byte-critical systems.

%prep
%autosetup -n %{name}-%{version}

%build
./autogen.sh
%{configure}
%make_build


%install
%make_install \

install -m 755 -p src/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 -p -T doc/axelrc.example %{buildroot}%{_sysconfdir}/axelrc

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%doc ChangeLog CREDITS AUTHORS README.md doc/API
%license COPYING
%config(noreplace) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.16-1
- Update to latest upstream release
- Add gcc g++ to BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.15-1
- Update to latest release
- Update upstream location

* Sun Sep 10 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.13.1-2
- Spec update

* Sun Sep 10 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.13.1-1
- Update to latest upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.5-1
- Update to new release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 17 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-4
- rebuilt to fix 583210

* Mon Feb 15 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-3
- rebuilt to fix 564650

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.4-1
- initial rpm build
