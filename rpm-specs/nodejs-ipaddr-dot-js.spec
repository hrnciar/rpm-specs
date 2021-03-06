%{?nodejs_find_provides_and_requires}

%global packagename ipaddr.js
%global enable_tests 0
# Tests disabled due to missing 'lab" test suite

Name:		nodejs-ipaddr-dot-js
Version:	1.5.2
Release:	7%{?dist}
Summary:	A library for manipulating IPv4 and IPv6 addresses in JavaScript

License:	MIT
URL:		https://github.com/whitequark/ipaddr.js
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(code)
BuildRequires:	npm(coffee-script)
BuildRequires:	npm(lab)
BuildRequires:	npm(nodeunit)
BuildRequires:	npm(uglify-js)
%endif

Requires:	nodejs

%description
A library for manipulating IPv4 and IPv6 addresses in JavaScript.


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package



%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
ln -s %{nodejs_sitelib}/uglify-js %{buildroot}%{nodejs_sitelib}/uglify-js
/usr/bin/cake test
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Jared Smith <jsmith@fedoraproject.org> - 1.5.2-1
- Update to upstream 1.5.2 release

* Thu Nov  5 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.3-1
- Initial packaging
