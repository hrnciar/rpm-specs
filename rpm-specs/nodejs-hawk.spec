%global enable_tests 0

Name:           nodejs-hawk
Version:        4.1.2
Release:        8%{?dist}
Summary:        HTTP Hawk authentication scheme
License:        BSD
URL:            https://github.com/hueniverse/hawk
Source0:        https://registry.npmjs.org/hawk/-/hawk-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(boom)
BuildRequires:  npm(cryptiles)
BuildRequires:  npm(hoek)
BuildRequires:  npm(sntp)

%if 0%{?enable_tests}
BuildRequires:  npm(lab)
BuildRequires:  npm(code)
%endif

%description
Hawk is an HTTP authentication scheme using a message authentication code (MAC)
algorithm to provide partial HTTP request cryptographic verification.

%prep
%autosetup -n package
%nodejs_fixdep cryptiles "^2.0.5"
%nodejs_fixdep boom "^2.10.1"
%nodejs_fixdep hoek "^0.9.1"
chmod a-x README.md LICENSE package.json client.js example/* images/* lib/*
sed -i 's/\r$//' README.md
sed -i 's/\r$//' example/usage.js


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/hawk
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/hawk
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
%{nodejs_sitelib}/lab/bin/lab -a code -t 100 -L
%endif


%files
%doc README.md example images
%license LICENSE
%{nodejs_sitelib}/hawk


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Piotr Popieluch <piotr1212@gmail.com> - 4.1.2-1
- Update to 4.1.2
- Fixes CVE-2016-2515 rhbz#1309722

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 4.1.0-1
- Update to 4.1.0 upstream release

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 4.0.1-1
- Update to 4.0.1 upstream release

* Sun Dec 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-5
- Fixdep sntp

* Tue Dec 01 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-4
- Fixdep boom and cryptiles

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- new upstream release 1.0.0

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.15.0-1
- new upstream release 0.15.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-2
- add macro for EPEL6 dependency generation

* Tue Apr 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-1
- new upstream release 0.12.1

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.11.1-2
- fix rpmlint warnings

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.11.1-1
- initial package
