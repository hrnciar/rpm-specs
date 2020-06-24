%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-isodate
Version:    0.1.4
Release:    15%{?dist}
Summary:    JavaScript ISO 8601 date/time parser for Node.js

License:    MIT
URL:        https://github.com/pvorb/node-isodate
Source0:    http://registry.npmjs.org/isodate/-/isodate-%{version}.tgz
# One test file is not included in the npm tarball.
Source1:    https://raw.github.com/pvorb/node-isodate/4864e664cabba43003424453a82d50fd8f133737/test.js

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs

%description
%{summary}.

%prep
%setup -q -n package
cp -a %{SOURCE1} .

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/isodate
cp -pr package.json isodate.js %{buildroot}%{nodejs_sitelib}/isodate
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%__nodejs test.js
%endif

%files
%doc LICENSE README.md
%{nodejs_sitelib}/isodate

%changelog
* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.4-15
- Clean-up

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-3
- restrict to compatible arches

* Sun Jun 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-2
- include test.js

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-1
- initial package
