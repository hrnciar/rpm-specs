%{?nodejs_find_provides_and_requires}

%global packagename object-copy
%global enable_tests 1

Name:		nodejs-object-copy
Version:	0.1.0
Release:	7%{?dist}
Summary:	Copy static or prototype properties, descriptors from one object to another

License:	MIT
URL:		https://github.com/jonschlinkert/object-copy
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/%{packagename}/%{version}/test.js
# README
Source2:	https://raw.githubusercontent.com/jonschlinkert/%{packagename}/%{version}/README.md
# Source3 is generated by running Source10, which pulls from the upstream
# version control repository.
Source3:	fixtures-%{version}.tar.bz2
Source10:	dl-tests.sh

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(copy-descriptor)
BuildRequires:	npm(define-property)
BuildRequires:	npm(kind-of)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Copy static properties, prototype properties, and descriptors from one object
to another.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .
# copy the README
cp -p %{SOURCE2} .
# copy the fixtures
%autosetup -T -D -a 3 -n package

%nodejs_fixdep define-property

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-2
- Relax dependency on npm(define-property)

* Sat Apr 15 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-1
- Initial packaging