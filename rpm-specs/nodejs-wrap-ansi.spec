%{?nodejs_find_provides_and_requires}

%global packagename wrap-ansi
%global enable_tests 0
# tests disabled until 'ava' is packaged in Fedora

Name:		nodejs-wrap-ansi
Version:	2.0.0
Release:	9%{?dist}
Summary:	Wordwrap a string with ANSI escape codes

License:	MIT
URL:		https://github.com/chalk/wrap-ansi.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.  Grab from the github
# commit that corresponds with the version listed above
Source1:	https://raw.githubusercontent.com/chalk/wrap-ansi/c890e95ea671779012fa73fd77b74198e8c5d09b/test.js
#
# Simple patch to fix an rpmlint warning
Patch0:		nodejs-wrap-ansi_fix-tests.patch

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(string-width)
%if 0%{?enable_tests}
BuildRequires:	npm(ava)
%endif

%description
Wordwrap a string with ANSI escape codes


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .
%patch0 -p1


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-2
- Add shebang to index.js

* Mon Feb 15 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
