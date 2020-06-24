Name:           sysreporter
Version:        3.0.4
Release:        8%{?dist}
Summary:        Basic system reporter with emailing
License:        MIT
URL:            https://github.com/onesimus-systems/sysreporter
Source0:        https://github.com/onesimus-systems/sysreporter/archive/v%{version}.tar.gz

BuildArch:      noarch

Requires: sysstat

%description
Basic system reporter with emailing

%prep
%autosetup -n sysreporter-3.0.4

%build

%install
%__make install DESTDIR="%{buildroot}" prefix="/usr"

%files
%license LICENSE.md
%doc README.md
%{_bindir}/sysreport
%config(noreplace) %{_sysconfdir}/%name
%{_mandir}/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Nick Bebout <nb@fedoraproject.org> - 3.0.4-1
- Upgrade to 3.0.4
* Tue Apr 04 2016 Nick Bebout <nb@fedoraproject.org> - 3.0.3-1
- Upgrade to 3.0.3
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Dec 18 2015 Nick Bebout <nb@fedoraproject.org> - 3.0.2-1
- Upgrade to 3.0.2
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 3.0.0-0.4.alpha4
- Upgrade to 3.0.0-alpha4, fix reports.d path
* Mon Dec 14 2015 Nick Bebout <nb@fedoraproject.org> - 3.0.0-0.1.alpha3
- Initial package
