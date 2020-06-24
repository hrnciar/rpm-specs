%global enable_tests 1
%global srcname node-int64

Name:           nodejs-%{srcname}
Version:        0.4.0
Release:        9%{?dist}
Summary:        Support for representing 64-bit integers in JavaScript
License:        MIT
URL:            https://github.com/broofa/node-int64
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging


%description
JavaScript Numbers are represented as IEEE 754 double-precision floats. 
Unfortunately, this means they lose integer precision for values beyond +/- 
2^^53. For projects that need to accurately handle 64-bit ints, such as 
node-thrift, a performant, Number-like class is needed. Int64 is that class.


%prep
%setup -q -n package
rm -rf node_modules/


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json Int64.js %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
node test.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 18 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.4.0-1
- Update to latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb  3 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.3.3-1
- Update to latest upstream
- Remove separately distributed license

* Mon Dec 22 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.3.2-1
- Initial package
