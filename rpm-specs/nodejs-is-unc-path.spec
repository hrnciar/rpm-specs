%{?nodejs_find_provides_and_requires}

%global packagename is-unc-path
%global enable_tests 1

Name:		nodejs-is-unc-path
Version:	1.0.0
Release:	5%{?dist}
Summary:	Returns true if a filepath is a windows UNC file path

License:	MIT
URL:		https://github.com/jonschlinkert/is-unc-path.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.  The releases aren't
# tagged in GitHub either, so we'll pull from "master"
Source1:	https://raw.githubusercontent.com/jonschlinkert/is-unc-path/master/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(unc-path-regex)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Returns true if a filepath is a windows UNC file path.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .



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
/usr/bin/mocha -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Update to upstream 1.0.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-3
- Include proper test.js file

* Sat Dec 19 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-2
- Add missing build requirement

* Wed Dec 16 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-1
- Initial packaging
