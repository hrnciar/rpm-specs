%{?nodejs_find_provides_and_requires}

Name:       nodejs-inherits1
Version:    1.0.0
Release:    23%{?dist}
Summary:    A tiny simple way to do classic inheritance in JS - legacy version
#the license is not included with the tarball so we retrieve it from the
#upstream git repository in Source1
License:    WTFPL
URL:        https://github.com/isaacs/inherits
Source0:    https://registry.npmjs.org/inherits/-/inherits-%{version}.tgz
Source1:    https://raw.github.com/isaacs/inherits/112807f2670160b6e3bafdf39e395c10ae7d0fac/LICENSE
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
A tiny simple way to do classic inheritance in JavaScript.

This is the legacy version used by many Node.js modules for many years, and is
retained for backward compatibility.  New modules should use the inheritance
functionality available in core Node.js or use the new version of inherits if
they need browser support as well.

%prep
%setup -q -n package

#copy the license into %%{_builddir} so it works with %%doc
cp -p %{SOURCE1} LICENSE

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/inherits@1
cp -pr inherits.js package.json %{buildroot}%{nodejs_sitelib}/inherits@1

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/inherits@1
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-16
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-11
- restrict to compatible arches

* Fri Jun 07 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-10
- include LICENSE file from upstream git

* Tue Jun 04 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-9
- rename to nodejs-inherits1

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-8
- add macro for EPEL6 dependency generation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-6
- add missing build section

* Thu Jan 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-5
- correct license tag (thanks to Robin Lee)

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-4
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-3
- guard Requires for F17 automatic depedency generation

* Sat Feb 11 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-2
- switch to automatically generated provides/requires

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
