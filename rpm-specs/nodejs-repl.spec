%{?nodejs_find_provides_and_requires}

Name:           nodejs-repl
Version:        0.1.3
Release:        15%{?dist}
Summary:        A lightweight templating library for Node.js
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

# package.json indicates MIT, but no license file included
# upstream notified in https://github.com/firejune/repl/pull/1
# we're including a copy of the MIT license in order to comply with the terms of 
# the MIT license, as required by:
# https://fedoraproject.org/wiki/Packaging:LicensingGuidelines#License_Text
License:        MIT
URL:            https://github.com/firejune/repl
Source0:        https://registry.npmjs.org/repl/-/repl-%{version}.tgz
Source1:        https://raw.github.com/tchollingsworth/repl/8658350d7c0d1d4577f1a802de7032803c934301/LICENSE
BuildRequires:  nodejs-packaging

%description
%{summary}.

%prep
%setup -q -n package

#copy LICENSE file to %%{_builddir} so it works with %%doc
cp %{SOURCE1} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/repl
cp -pr lib index.js package.json %{buildroot}%{nodejs_sitelib}/repl

%nodejs_symlink_deps

%check
%{__nodejs} test.js

%files
%{nodejs_sitelib}/repl
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.1.3-8
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3-3
- add macro for Provides and Requires

* Sat Jul 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3-2
- rebuild for missing Provides

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.3-1
- initial package
