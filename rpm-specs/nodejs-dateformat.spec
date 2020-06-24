%global enable_tests 1

%global packagename dateformat

Name:       nodejs-dateformat
Version:    3.0.3
Release:    6%{?dist}
Summary:    Steven Levithan's excellent dateFormat() function for Node.js
License:    MIT
URL:        https://github.com/felixge/node-dateformat
Source0:    https://registry.npmjs.com/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:        tests-%{version}.tar.bz2
Source10:       dl-tests.sh

# Patch to fix failing test.
# see also https://github.com/felixge/node-dateformat/issues/41
Patch0:     dateformat-fix-unit-test.patch

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(underscore)
%endif

%description
This is a JavaScript port of Steven Levithan's excellent dateFormat()
function, which provides a simple way to format dates and times
according to a user-specified mask.


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
cd test
%patch0 -p1

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/dateformat
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/dateformat

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
TZ="UTC" %{_bindir}/mocha -R spec
%endif


%files
%doc Readme.md
%license LICENSE
%{nodejs_sitelib}/dateformat


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Ben Rosser <rosser.bjr@gmail.com> - 3.0.3-5
- Fix FTBFS and unretire the package!

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 jsmith <jsmith.fedora@gmail.com> - 3.0.3-1
- Update to upstream 3.0.3 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 <piotrp@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.12-3
- Add missing BuildRequires for tests

* Fri Jul 15 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.12-2
- Fix dependency on nodejs-get-stdin

* Fri Apr 22 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.12-1
- Update to upstream 1.0.12 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.6-1
- initial package
