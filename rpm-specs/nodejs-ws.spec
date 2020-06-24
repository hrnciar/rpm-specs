# Although there are tests
# the dependancies aren't in Fedora yet
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       Web socket client, server and console for nodejs
Name:          nodejs-ws
Version:       7.1.2
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/einaros/ws
Source0:       https://github.com/einaros/ws/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: nodejs-devel
BuildRequires: npm(async-limiter)
%if 0%{?enable_tests}
BuildRequires: npm(ansi)
BuildRequires: npm(benchmark)
BuildRequires: npm(expect.js)
BuildRequires: npm(mocha)
BuildRequires: npm(should)
BuildRequires: npm(tinycolor)
%endif
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Simple to use, blazing fast and thoroughly tested 
web socket client, server and console for nodejs, 
up-to-date against RFC-6455

%prep
%autosetup -p 1 -n ws-%{version}

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ws
cp -pr index.js lib package.json %{buildroot}%{nodejs_sitelib}/ws
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
make test
%endif

%files
%license LICENSE
%doc README.md SECURITY.md
%{nodejs_sitelib}/ws

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Tom Hughes <tom@compton.nu> - 7.1.2-2
- Update to 7.1.2 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Jared Smith <jsmith@fedoraproject.org> - 3.3.2-1
- Update to upstream 3.3.2 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Tom Hughes <tom@compton.nu> - 1.1.1-3
- Use %%{nodejs_arches}

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 29 2016 Troy Dawson <tdawson@redhat.com> - 1.1.1-1
- Update to 1.1.1 (#1351230,1351231)

* Thu Apr 28 2016 Troy Dawson <tdawson@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Troy Dawson <tdawson@redhat.com> - 1.0.1-1
- Update to 1.0.1 - Security Fix - (#1295717,1295718,1295719)

* Fri Dec 11 2015 Troy Dawson <tdawson@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Mon Sep 21 2015 Troy Dawson <tdawson@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 0.7.2-1
- Update to 0.7.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Troy Dawson <tdawson@redhat.com> - 0.7.1-2
- Make package noarch, because now it is

* Mon Feb 02 2015 Troy Dawson <tdawson@redhat.com> - 0.7.1-1
- Updated to latest release
- Fixed up dependencies

* Thu Jan 22 2015 Troy Dawson <tdawson@redhat.com> - 0.7.0-1
- Updated to latest release

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 0.4.32-1
- Updated to latest release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.31-3
- rebuild for icu-53 (via v8)

* Fri Feb 07 2014 Troy Dawson <tdawson@redhat.com> - 0.4.31-2
- Fix nan dependency

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 0.4.31-1
- Update to version 0.4.31
- add macro to invoke dependency generator on EL6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Troy Dawson <tdawson@redhat.com> - 0.4.25-4
- add nodejs exclusive arch

* Wed May 29 2013 Troy Dawson <tdawson@redhat.com> - 0.4.25-3
- Use nodejs_fixdep instead of sed to fix dependancy

* Wed May 29 2013 Troy Dawson <tdawson@redhat.com> - 0.4.25-2
- Fixed Summary and Description spelling errors
- Fixed nodejs-commander version dependancy
- Cleanup extra files and strange permissions

* Fri Mar 01 2013 Troy Dawson <tdawson@redhat.com> - 0.4.25-1
- Update to 0.4.25
- Update spec to Fedora nodejs standards

* Fri Nov 16 2012 Troy Dawson <tdawson@redhat.com> - 0.4.22-3
- Fix for building native modules

* Wed Nov 14 2012 Troy Dawson <tdawson@redhat.com> - 0.4.22-1
- Initial build using tchor spec template

