%global enable_tests 1
%global srcname util

Name:           nodejs-%{srcname}
Version:        0.10.3
Release:        11%{?dist}
Summary:        Node.JS util module
License:        MIT
URL:            https://github.com/defunctzombie/node-util
Source0:        http://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(inherits)
%endif


%description
%{summary}.


%prep
%setup -q -n package
rm -rf node_modules/
%nodejs_fixdep inherits '2.x'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json util.js support/ %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} test/node/*.js
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{srcname}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 13 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.10.3-2
- fixdep nodejs-inherits, 2.0.1 is not available on < fc20

* Tue Nov 18 2014 Piotr Popieluch <piotr1212@gmail.com> - 0.10.3-1
- Initial package
