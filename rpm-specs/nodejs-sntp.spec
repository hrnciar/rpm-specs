%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-sntp
Epoch:          1
Version:        2.0.1
Release:        8%{?dist}
Summary:        SNTP v4 client (RFC4330) for Node.js

License:        BSD
URL:            https://github.com/hueniverse/sntp
Source0:        https://github.com/hueniverse/sntp/archive/v%{version}/sntp-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(hoek)

%description
An SNTP v4 client (RFC4330) for Node.js. Simply connects to the NTP or SNTP
server requested and returns the server time along with the round-trip duration
and clock offset. To adjust the local time to the NTP time, add the returned 
time offset to the local time.


%prep
%autosetup -n sntp-%{version}
%{nodejs_fixdep} hoek

#drop exec bit from everything
chmod 0644 *.js* README.md LICENSE examples/* lib/*


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/sntp
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/sntp
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
#Yet Another Unpackaged Test Framework (lab)
#make test
%endif


%files
%{nodejs_sitelib}/sntp
%doc README.md examples
%license LICENSE


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Tom Hughes <tom@compton.nu> - 1:2.0.1-1
- Update to 2.0.1 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Stephen Gallagher <sgallagh@redhat.com> - 1:2.0.0-2
- Update to 2.0.0 (again)

* Mon Dec 14 2015 Tom Hughes <tom@compton.nu> - 1:1.0.9-2
- Add index.js back to package

* Mon Dec 14 2015 Piotr Popieluch <piotr1212@gmail.com> - 1:1.0.9-1
- Revert to 1.0.9, we don't have node 4.x yet

* Sun Dec 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Wed Nov 18 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.9-1
- Update to 1.0.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.4-1
- new upstream release 0.2.4

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-2
- add macro for EPEL6 dependency generation

* Tue Apr 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-1
- new upstream release 0.2.1

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-2
- fix rpmlint warnings

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package
