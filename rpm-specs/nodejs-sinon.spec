# missing test deps in Fedora
%global enable_tests 0

%global srcname sinon
%global gitname Sinon.JS

%global commit0 de6b53476dbcee95a366b719c0098af86a05d867
%global gittag0 v1.17.1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           nodejs-%{srcname}
Version:        1.17.1
Release:        9%{?dist}
Summary:        Test spies, stubs and mocks for JavaScript
License:        BSD
URL:            https://github.com/cjohansen/Sinon.JS
# use github as source, npm package does not contain tests
Source0:        https://github.com/cjohansen/%{gitname}/archive/%{commit0}/%{gitname}-%{commit0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(formatio)
BuildRequires:  npm(lolex)
BuildRequires:  npm(samsam)
BuildRequires:  npm(util)
BuildRequires:  npm(buster)
BuildRequires:  npm(buster-core)
BuildRequires:  npm(buster-istanbul)
%endif

%description
Standalone and test framework agnostic JavaScript test spies, stubs and mocks.

%prep
%setup -q -n %{srcname}-%{commit0}
rm -rf node_modules/
%nodejs_fixdep formatio '1.x'
%nodejs_fixdep lolex '1.3.x'

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
buster-test --config-group node
%endif

%files
%doc AUTHORS Changelog.txt CONTRIBUTING.md README.md RELEASE.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.17.1-1
- Update to upstream 1.17.1
- Add missing BR

* Sat Aug 29 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.16.1-1
- Update to upstream 1.16.1

* Mon Mar 23 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.14.1-1
- Update to upstream 1.14.1

* Tue Nov 18 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.12.1-1
- Initial package
