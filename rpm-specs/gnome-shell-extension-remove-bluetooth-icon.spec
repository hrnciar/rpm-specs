%global uuid remove-bluetooth-icon@affolter-engineering.ch
%global shortname remove-bluetooth-icon

Name:           gnome-shell-extension-remove-bluetooth-icon
Version:        0.5.1
Release:        13%{?dist}
Summary:        A gnome-shell extension for removing the bluetooth icon

License:        GPLv3+
URL:            http://www.affolter-engineering.ch/index.php?page=remove-bluetooth-icon
Source0:        http://www.affolter-engineering.ch/uploads/remove-bluetooth-icon/%{shortname}-%{version}.tar.bz2
BuildArch:      noarch

Requires:       gnome-shell >= 3.2.0


%description
This simple extension does nothing more than to remove the bluetooth
icon from the GNOME panel. 


%prep
%setup -q -n %{shortname}-%{version}


%build
# Nothing to build


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS COPYING README
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Updated to new upstream release 0.5.1

* Mon Feb 25 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Updated to new upstream release 0.5.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.3-1
- Updated to new upstream release 0.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jan 02 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.1-1
- Updated to new upstream release 0.2.1

* Sun Nov 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.2-1
- Updated to new upstream release 0.2

* Thu Jun 02 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-1
- Initial package for Fedora
