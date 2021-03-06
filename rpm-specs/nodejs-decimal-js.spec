# See https://fedoraproject.org/wiki/Packaging:Node.js?rd=Node.js/Packagers for
# the nodejs-specific packaging guidelines.

# See https://fedoraproject.org/wiki/Packaging:Node.js?rd=Node.js/Packagers#Automatic_Requires_and_Provides
# (required for EPEL compatibility)
%{?nodejs_find_provides_and_requires}

%global npm_name decimal.js
%global enable_tests 1

Name:		nodejs-decimal-js
Version:	10.2.0
Release:	5%{?dist}
Summary:	A library for arbitrary-precision arithmetic

License:	MIT
URL:		https://github.com/MikeMcl/decimal.js/
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch
BuildRequires:	nodejs-packaging dos2unix

%description
A JavaScript library for arbitrary-precision decimal and non-decimal arithmetic.

%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
dos2unix README.md CHANGELOG.md

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json decimal.d.ts decimal.js decimal.min.js decimal.mjs \
       %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
  %__nodejs test/test.js
%else
  %{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md CHANGELOG.md doc/API.html
%license LICENCE.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Timothée Floure <fnux@fedoraproject.org> - 10.2.0-1
- New upstream release

* Sun Mar 17 2019 Timothée Floure <fnux@fedoraproject.org> - 10.1.1-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Timothée Floure <fnux@fedoraproject.org> - 10.0.1-1
- Updated to 10.0.1

* Thu Mar 29 2018 Timothée Floure <fnux@fedoraproject.org> - 10.0.0-1
- Updated to 10.0.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Timothée Floure <fnux@fedoraproject.org> - 9.0.1-2
- use dl-test.sh to download tests from upstream version control repository
- run tests in the check section
- Automatic Requires and Provices: add compatibility with EPFL

* Thu Jan 18 2018 Timothée Floure <fnux@fedoraproject.org> - 9.0.1-1
- Update to 9.0.1
- Remove the deprecated 'Group' tag
- Add the 'check' section to comply with packaging guidelines
- Fix end of line encoding for README.md and CHANGELOG.md

* Mon Jun 26 2017 Timothée Floure <fnux@fnux.ch> - 7.2.3-1
- Let there be package
