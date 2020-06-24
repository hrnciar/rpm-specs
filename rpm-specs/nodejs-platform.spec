%{?nodejs_find_provides_and_requires}

%global packagename platform
# Tests disabled due to changes in npm(qunit-extras)
%global enable_tests 0

Name:		nodejs-platform
Version:	1.3.5
Release:	4%{?dist}
Summary:	A platform detection library that works on nearly all JavaScript platforms

License:	MIT
URL:		https://github.com/bestiejs/platform.js
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source2:	docs-%{version}.tar.bz2
Source10:	dl-tests.sh


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(qunitjs)
BuildRequires:	npm(qunit-extras)
%endif

Requires:	nodejs

%description
A platform detection library that works on nearly all JavaScript platforms.


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
%setup -q -T -D -a 2 -n package



%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs test/test
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md doc/*.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.3.5-1
- Update to upstream 1.3.5 release
- Disable tests due to changes in npm(qunit-extras)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 18 2016 Jared Smith <jsmith@fedoraproject.org> - 1.3.1-1
- Update to upstream 1.3.1 release

* Mon Nov 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.3.0-1
- Initial packaging