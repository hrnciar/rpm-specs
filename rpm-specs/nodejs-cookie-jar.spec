%{?nodejs_find_provides_and_requires}

Name:           nodejs-cookie-jar
Epoch:          1
Version:        0.3.0
Release:        13%{?dist}
Summary:        A cookie handling and cookie jar library for Node.js
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

#ASL 2.0 added upstream
#https://github.com/mikeal/cookie-jar/blob/master/LICENSE
License:        ASL 2.0
URL:            https://github.com/mikeal/cookie-jar
Source0:        https://registry.npmjs.org/cookie-jar/-/cookie-jar-%{version}.tgz

#this needs to get renamed to nodejs-cookie-jar soon
Provides:       nodejs-tobi-cookie = %{epoch}:%{version}
Obsoletes:      nodejs-tobi-cookie < 1:0.2.0-3

BuildRequires:  nodejs-packaging

%description
%summary.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cookie-jar
cp -p index.js jar.js package.json %{buildroot}%{nodejs_sitelib}/cookie-jar

%nodejs_symlink_deps

%check
%{__nodejs} tests/run.js

%files
%{nodejs_sitelib}/cookie-jar

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 1:0.3.0-6
- Cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.3.0-1
- new upstream release 0.3.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-6
- restrict to compatible arches

* Tue Apr 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-5
- run tests

* Fri Apr 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-4
- fix Obsoletes as sugessted during rename review

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.0-3
- rename to nodejs-cookie-jar

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.2.1-1
- now unbundled from tobi, called cookie-jar upstream

* Sat Jan 26 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-2
- add missing build section

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-1
- initial package
