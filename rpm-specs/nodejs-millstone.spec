%bcond_with internet

Name:           nodejs-millstone
Version:        0.6.17
Release:        14%{?dist}
Summary:        Prepares data sources in an MML file for consumption in Mapnik

License:        BSD
URL:            https://github.com/tilemill-project/millstone
Source0:        https://registry.npmjs.org/millstone/-/millstone-%{version}.tgz
# Remove tests that need internet access
Patch0:         nodejs-millstone-internet.patch
# https://github.com/tilemill-project/millstone/pull/129
Patch1:         nodejs-millstone-json.patch
# https://github.com/tilemill-project/millstone/pull/130
Patch2:         nodejs-millstone-mime.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(generic-pool)
BuildRequires:  npm(mime)
BuildRequires:  npm(request)
BuildRequires:  npm(srs) >= 0.4.1
BuildRequires:  npm(step)
BuildRequires:  npm(underscore)
BuildRequires:  npm(zipfile) >= 0.5.5

%description
As of carto 0.2.0, the Carto module expects all data sources and
resources to be localized - remote references like URLs and providers
are not downloaded when maps are rendered.

Millstone now contains this logic - it provides two functions, resolve
and flush. Resolve takes an MML file and returns a localized version, and
flush can be used to clear the cache of a specific resource.


%prep
%setup -q -n package
%if ! %{with internet}
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1
%nodejs_fixdep generic-pool "^2.0.3"
%nodejs_fixdep mime "^2.0.3"
%nodejs_fixdep sqlite3 "^4.0.0"
%nodejs_fixdep step "^1.0.0"
%nodejs_fixdep underscore "^1.6.0"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/millstone
cp -pr package.json bin lib %{buildroot}/%{nodejs_sitelib}/millstone
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%{nodejs_sitelib}/mocha/bin/mocha -R spec --timeout 10000


%files
%doc README.md CHANGELOG.md architecture.md
%license LICENSE
%{nodejs_sitelib}/millstone


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Tom Hughes <tom@compton.nu> - 0.6.17-10
- Fix npm(sqlite3) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct  4 2017 Tom Hughes <tom@compton.nu> - 0.6.17-8
- Add patch for mime 2.x support
- Fix npm(mime) dependency

* Wed Oct 04 2017 Jared Smith <jsmith@fedoraproject.org> - 0.6.17-7
- Relax dependency on npm(mime)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Tom Hughes <tom@compton.nu> - 0.6.17-4
- Fix npm(step) dependency

* Fri Dec 23 2016 Tom Hughes <tom@compton.nu> - 0.6.17-3
- Add patch for test failures with Node 6.9

* Mon Mar  7 2016 Tom Hughes <tom@compton.nu> - 0.6.17-2
- Fix npm(underscore) dependency

* Sun Mar  6 2016 Tom Hughes <tom@compton.nu> - 0.6.17-1
- Update to 0.6.17 upstream release

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.16-7
- Allow newer version of npm(optimist)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.6.16-5
- Remove npm(mkdirp) fixdep

* Mon Nov 30 2015 Tom Hughes <tom@compton.nu> - 0.6.16-4
- Enable tests

* Sun Nov 29 2015 Tom Hughes <tom@compton.nu> - 0.6.16-3
- Update srs dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 14 2015 Tom Hughes <tom@compton.nu> - 0.6.16-1
- Update to 0.6.16 upstream release

* Thu Nov 20 2014 Tom Hughes <tom@compton.nu> - 0.6.15-1
- Update to 0.6.15 upstream release

* Mon Sep 22 2014 Tom Hughes <tom@compton.nu> - 0.6.14-2
- Update sqlite3 dependency

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Tom Hughes <tom@compton.nu> - 0.6.14-1
- Update to 0.6.14 upstream release

* Fri May  2 2014 Tom Hughes <tom@compton.nu> - 0.6.12-4
- Fix srs dependency

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.12-3
- fix version of npm(underscore) dependency

* Thu Apr 17 2014 Tom Hughes <tom@compton.nu> - 0.6.12-2
- Fix underscore dependency

* Wed Apr 16 2014 Tom Hughes <tom@compton.nu> - 0.6.12-1
- Update to 0.6.12 upstream release

* Sat Mar 15 2014 Tom Hughes <tom@compton.nu> - 0.6.11-2
- Fix zipfile dependency

* Sat Feb  8 2014 Tom Hughes <tom@compton.nu> - 0.6.11-1
- Update to 0.6.11 upstream release

* Thu Feb  6 2014 Tom Hughes <tom@compton.nu> - 0.6.10-1
- Update to 0.6.10 upstream release

* Sun Jan 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.8-2
- fix underscore for 1.5.1

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 0.6.8-1
- Update to 0.6.8 upstream release

* Tue Oct  1 2013 Tom Hughes <tom@compton.nu> - 0.6.5-1
- Update to 0.6.5 upstream release

* Tue Sep 24 2013 Tom Hughes <tom@compton.nu> - 0.6.4-1
- Update to 0.6.4 upstream release.

* Fri Sep 20 2013 Tom Hughes <tom@compton.nu> - 0.6.1-1
- Update to 0.6.1 upstream release
- Update to latest nodejs packaging standards

* Mon Aug 12 2013 Tom Hughes <tom@compton.nu> - 0.6.0-2
- Fix dependencies

* Sun Aug 11 2013 Tom Hughes <tom@compton.nu> - 0.6.0-1
- Update to 0.6.0 upstream release

* Fri Aug  9 2013 Tom Hughes <tom@compton.nu> - 0.5.15-5
- Rebuild against nodejs-srs 0.3.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr  4 2013 Tom Hughes <tom@compton.nu> - 0.5.15-3
- Rebuild against nodejs-request 2.16

* Thu Mar 14 2013 Tom Hughes <tom@compton.nu> - 0.5.15-2
- Rebuild against nodejs-request 2.14

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.5.15-1
- Initial build of 0.5.15
