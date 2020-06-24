Name:           nodejs-mapnik-reference
Version:        8.10.0
Release:        4%{?dist}
Summary:        Reference for Mapnik Styling Options

License:        Public Domain
URL:            https://github.com/mapnik/mapnik-reference
Source0:        https://github.com/mapnik/mapnik-reference/archive/v%{version}/mapnik-reference-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(glob)
BuildRequires:  npm(lodash)
BuildRequires:  npm(semver)

%description
Provides a parseable spec of what Mapnik can do - what main structures
it supports (like layers, styles, and symbolizers) and the properties
they can contain. It's useful for building parsers, tests, compilers, and
syntax highlighting/checking for languages


%prep
%autosetup -n mapnik-reference-%{version}
%nodejs_fixdep --dev --move lodash


%build
%nodejs_symlink_deps --build
%__nodejs generate.js


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/mapnik-reference
cp -pr package.json index.js %{buildroot}/%{nodejs_sitelib}/mapnik-reference
mkdir -p %{buildroot}/%{_datadir}/%{name}
for dir in 2.* 3.*
do
  cp -pr ${dir} %{buildroot}/%{_datadir}/%{name}
  ln -sf %{_datadir}/%{name}/${dir} %{buildroot}/%{nodejs_sitelib}/mapnik-reference
done
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec --timeout 50000


%files
%doc README.md CHANGELOG.md
%license LICENSE.md 
%{nodejs_sitelib}/mapnik-reference
%{_datadir}/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Tom Hughes <tom@compton.nu> - 8.10.0-1
- Update to 8.10.0 upstream release

* Mon Aug 13 2018 Tom Hughes <tom@compton.nu> - 8.9.1-1
- Update to 8.9.1 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Tom Hughes <tom@compton.nu> - 8.8.1-1
- Update to 8.8.1 upstream release

* Wed Jul 12 2017 Tom Hughes <tom@compton.nu> - 8.8.0-1
- Update to 8.8.0 upstream release

* Wed May 31 2017 Tom Hughes <tom@compton.nu> - 8.7.0-1
- Update to 8.7.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Tom Hughes <tom@compton.nu> - 8.6.1-2
- Revert npm(lodash) to a build time dependency

* Mon Jan  9 2017 Tom Hughes <tom@compton.nu> - 8.6.1-1
- Update to 8.6.1 upstream release

* Sat Jan  7 2017 Tom Hughes <tom@compton.nu> - 8.6.0-1
- Update to 8.6.0 upstream release

* Fri Dec 23 2016 Tom Hughes <tom@compton.nu> - 8.5.6-1
- Update to 8.5.6 upstream release

* Sun Mar  6 2016 Tom Hughes <tom@compton.nu> - 8.5.5-1
- Update to 8.5.5 upstream release

* Sat Feb 27 2016 Tom Hughes <tom@compton.nu> - 8.5.3-1
- Update to 8.5.3 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Tom Hughes <tom@compton.nu> - 8.5.2-1
- Update to 8.5.2 upstream release

* Thu Oct 15 2015 Tom Hughes <tom@compton.nu> - 8.5.1-1
- Update to 8.5.1 upstream release

* Fri Oct  9 2015 Tom Hughes <tom@compton.nu> - 8.5.0-1
- Update to 8.5.0 upstream release

* Wed Sep 23 2015 Tom Hughes <tom@compton.nu> - 8.4.0-1
- Update to 8.4.0 upstream release

* Sat Sep 12 2015 Tom Hughes <tom@compton.nu> - 8.3.0-1
- Update to 8.3.0 upstream release

* Sat Aug 15 2015 Tom Hughes <tom@compton.nu> - 8.2.0-1
- Update to 8.2.0 upstream release

* Sat Jun 27 2015 Tom Hughes <tom@compton.nu> - 8.1.0-1
- Update to 8.1.0 upstream release

* Thu Jun 25 2015 Tom Hughes <tom@compton.nu> - 8.0.1-1
- Update to 8.0.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Tom Hughes <tom@compton.nu> - 8.0.0-1
- Update to 8.0.0 upstream release
- Switch to %%license for the license file

* Fri Feb 20 2015 Tom Hughes <tom@compton.nu> - 7.0.1-1
- Update to 7.0.1 upstream release

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 7.0.0-1
- Update to 7.0.0 upstream release

* Wed Dec 17 2014 Tom Hughes <tom@compton.nu> - 6.0.5-1
- Update to 6.0.5 upstream release

* Thu Nov 20 2014 Tom Hughes <tom@compton.nu> - 6.0.4-1
- Update to 6.0.4 upstream release

* Wed Oct  1 2014 Tom Hughes <tom@compton.nu> - 6.0.3-1
- Update to 6.0.3 upstream release

* Sat Sep 27 2014 Tom Hughes <tom@compton.nu> - 6.0.2-1
- Update to 6.0.2 upstream release

* Fri Sep 26 2014 Tom Hughes <tom@compton.nu> - 6.0.1-1
- Update to 6.0.1 upstream release

* Wed Sep 24 2014 Tom Hughes <tom@compton.nu> - 5.1.1-1
- Update to 5.1.1 upstream release

* Fri Sep  5 2014 Tom Hughes <tom@compton.nu> - 5.1.0-1
- Update to 5.1.0 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 Tom Hughes <tom@compton.nu> - 5.0.9-1
- Update to 5.0.9 upstream release

* Mon Apr 14 2014 Tom Hughes <tom@compton.nu> - 5.0.8-1
- Update to 5.0.8 upstream release

* Wed Oct 30 2013 Tom Hughes <tom@compton.nu> - 5.0.7-1
- Update to 5.0.7 upstream release

* Fri Sep 27 2013 Tom Hughes <tom@compton.nu> - 5.0.6-1
- Update to 5.0.6 upstream release

* Fri Sep 20 2013 Tom Hughes <tom@compton.nu> - 5.0.5-1
- Update to 5.0.5 upstream release
- Update to latest nodejs packaging standards

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar  2 2013 Tom Hughes <tom@compton.nu> - 5.0.4-2
- Use %%{__python} instead of %%{__python2}
- Run tests against an unpatched copy of the package
- Removed hyphen from parseable in description

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 5.0.4-1
- Initial build of 5.0.4
