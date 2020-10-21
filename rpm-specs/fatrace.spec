Name:		fatrace
Version:	0.15
Release:	3%{?dist}
Summary:	Reports file access events from all running processes

License:	GPLv3
URL:		https://launchpad.net/fatrace
Source0:	https://launchpad.net/fatrace/trunk/%{version}/+download/fatrace-%{version}.tar.xz
BuildRequires:  gcc

%description
fatrace reports file access events from all running processes.

Its main purpose is to find processes which keep waking up the disk
unnecessarily and thus prevent some power saving.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
export PREFIX=%{_prefix}
make install DESTDIR=%{buildroot}

%files
%doc COPYING NEWS
%{_sbindir}/fatrace
%{_sbindir}/power-usage-report
%{_mandir}/man*/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Kevin Fenzi <kevin@scrye.com> - 0.15-1
- Update to 0.15. Fixes bug #1768275

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Kevin Fenzi <kevin@scrye.com> - 0.13-3
- Fix FTBFS by adding BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Kevin Fenzi <kevin@scrye.com> - 0.13-1
- Update really to 0.13.

* Sun Mar 25 2018 Kevin Fenzi <kevin@scrye.com> - 0.12-1
- Update to 0.12. Fixes bug #1560256

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12-2
- Rebuild for Python 3.6

* Mon Apr 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.12-1
- Update to 0.12. Fixes bug #1330341

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Kevin Fenzi <kevin@scrye.com> - 0.11-1
- Update to 0.11. Fixes bug #1279842

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Kevin Fenzi <kevin@scrye.com> 0.10-1
- Update to 0.10. Fixes bug #1217026

* Wed Nov 12 2014 Kevin Fenzi <kevin@scrye.com> 0.9-1
- Update to 0.9. Fixes bug #1163129

* Wed Sep 24 2014 Kevin Fenzi <kevin@scrye.com> 0.8-1
- Update to 0.8. Fixes bug #1145907

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Kevin Fenzi <kevin@scrye.com> 0.7-1
- Update to 0.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 08 2014 Kevin Fenzi <kevin@scrye.com> 0.6-1
- Update to 0.6 bugfix release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Kevin Fenzi <kevin@scrye.com> 0.5-1
- Initial version for Fedora
