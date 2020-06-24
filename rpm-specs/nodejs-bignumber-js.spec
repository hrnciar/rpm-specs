%global npm_name bignumber.js
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Summary:       Library for arbitrary-precision decimal and non-decimal arithmetic 
Name:          nodejs-bignumber-js
Version:       2.4.0
Release:       9%{?dist}
License:       MIT
URL:           http://github.com/MikeMcl/bignumber.js
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
A JavaScript library for arbitrary-precision decimal and non-decimal arithmetic. 

%prep
%setup -q -n package

# wrong end-of-file encoding
sed -i 's/\r//' README.md LICENCE

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr bignumber.js bignumber.js.map bignumber.min.js doc package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%if 0%{?enable_tests}
%check
node ./test/every-test.js
%endif

%files
%doc README.md
%license LICENCE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Piotr Popieluch <piotr1212@gmail.com> - 2.4.0-3
- Update nodejs arches to fix ftbfs
- Update br: nodejs-devel -> nodejs-packaging

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 09 2016 Troy Dawson <tdawson@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Thu Apr 28 2016 Troy Dawson <tdawson@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Troy Dawson <tdawson@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Fri Dec 11 2015 Troy Dawson <tdawson@redhat.com> - 2.1.2-1
- Updated to latest release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Troy Dawson <tdawson@redhat.com> - 2.0.7-1
- Updated to latest release

* Wed Feb 25 2015 Troy Dawson <tdawson@redhat.com> - 2.0.3-1
- Add exclusivearch
- add macro to invoke dependency generator
- Update to 2.0.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 03 2013 Troy Dawson <tdawson@redhat.com> - 1.2.0-2
- Changed rpm name to nodejs-bignumber-js

* Thu Oct 03 2013 Troy Dawson <tdawson@redhat.com> - 1.2.0-1
- Updated to version 1.2.0

* Wed May 22 2013 Troy Dawson <tdawson@redhat.com> - 1.0.1-1
- Initial build

