%{?nodejs_find_provides_and_requires}

Name:       nodejs-methods
Version:    1.1.2
Release:    7%{?dist}
Summary:    HTTP methods that node supports
License:    MIT
URL:        https://npmjs.org/package/methods
Source0:    https://github.com/jshttp/methods/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  mocha

%description
%{summary}.


%prep
%autosetup -n methods-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/methods
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/methods

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

mocha --reporter spec --check-leaks test/


%files
%doc HISTORY.md README.md
%license LICENSE
%{nodejs_sitelib}/methods


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- update to upstream release 0.1.0

* Sat Jul 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.1-4
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.1-3
- rebuild for missing npm(methods) provides on EL6

* Thu Feb 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.1-2
- add a copy of the MIT license to comply with licensing requirements

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.1-1
- initial package
