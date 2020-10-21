Name:		detox
Version:	1.3.0
Release:	10%{?dist}
Summary:	Utility to replace problematic characters in file names

License:	BSD
URL:		https://github.com/dharple/detox
Source0:	https://github.com/dharple/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf automake flex flex-static
BuildRequires:	gcc

%description
Detox is a utility designed to clean up file names. It replaces difficult to
work with characters, such as spaces, with standard equivalents. It will also
clean up file names with UTF-8 or Latin-1 (or CP-1252) characters in them.

%prep
%autosetup


%build
autoreconf --install
%configure
%make_build


%install
%make_install
rm %{buildroot}/etc/detoxrc.sample


%files
%config(noreplace) %{_sysconfdir}/%{name}rc
%{_bindir}/%{name}
%{_bindir}/inline-%{name}
%{_datadir}/%{name}
%doc CHANGELOG.md README.md THANKS.md
%license LICENSE
%{_mandir}/man5/detox*
%{_mandir}/man1/inline-detox.1.gz
%{_mandir}/man1/detox*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.0-5
- added gcc as BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.0-1
- Rebuilt for new upstream version 1.3.0 fixes rhbz #1445839

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-10
- Fix rhbz #1037034 (format-security-patch), spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Sven Lankes <sven@lank.es> - 1.2.0-4
- Really fix FTBFS

* Thu Dec 09 2010 Sven Lankes <sven@lank.es> - 1.2.0-3
- Fix FTBFS (rhbz #661090)

* Tue Mar 16 2010 Sven Lankes <sven@lank.es> - 1.2.0-2
- Review fixes

* Sun Feb 28 2010 Sven Lankes <sven@lank.es> - 1.2.0-1
- Initial package
