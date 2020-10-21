# Missing test deps in Fedora
%global enable_tests 0
%global srcname samsam

Name:           nodejs-%{srcname}
Version:        1.1.2
Release:        10%{?dist}
Summary:        Value identification and comparison functions
License:        BSD
URL:            https://github.com/busterjs/samsam
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(buster)
%endif


%description
samsam is a collection of predicate and comparison functions useful to 
identify the type of values and to compare values with varying degrees of 
strictness.

samsam is a general-purpose library with no dependencies. It works in browsers 
(including old and rowdy ones, like IE6) and Node. It will define itself as an 
AMD module if you want it to (i.e. if there's a define function available).

samsam was originally extracted from the referee assertion library, which 
ships with the Buster.JS testing framework.


%prep
%setup -q -n package


%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} test/samsam-test.js
%endif

%files
%doc AUTHORS Readme.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 29 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-1
- new version

* Tue Nov 18 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-1
- Initial package
