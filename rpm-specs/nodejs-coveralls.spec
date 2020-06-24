%{?nodejs_find_provides_and_requires}

%global packagename coveralls
%global enable_tests 0
# tests disabled due to failing git tests, despite the patch to fix some of them

Name:		nodejs-coveralls
Version:	2.11.6
Release:	8%{?dist}
Summary:	Takes json-cov output into stdin and POSTs to coveralls.io

License:	BSD
URL:		https://github.com/nickmerwin/node-coveralls.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

# Add a patch to fix syntax of the 'should' module.  It has changed from
# should.be.a.("string") to should.be.a.String()
Patch0:		coveralls-2.11.4-fix-should-syntax.patch


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(js-yaml)
BuildRequires:	npm(minimist)
BuildRequires:	npm(lcov-parse)
BuildRequires:	npm(log-driver)
BuildRequires:	npm(request)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(sinon-restore)
%endif

Requires:	nodejs

%description
takes json-cov output into stdin and POSTs to coveralls.io


%prep
%setup -q -n package
%patch0 -p1

%nodejs_fixdep js-yaml
%nodejs_fixdep lcov-parse '~0.0.6'
%nodejs_fixdep log-driver '~1.2.4'
%nodejs_fixdep request '^2.40.0'

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js fixtures/ lib/ test/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/coveralls.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}/bin/coveralls.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/coveralls.js \
    %{buildroot}%{_bindir}/coveralls


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
%{nodejs_sitelib}/%{packagename}
%{_bindir}/coveralls



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Jared Smith <jsmith@fedoraproject.org> - 2.11.6-1
- Update to upstream 2.11.6 release

* Sat Oct 31 2015 Jared Smith <jsmith@fedoraproject.org> - 2.11.4-2
- Fixup dependency versions

* Thu Oct 15 2015 Jared Smith <jsmith@fedoraproject.org> - 2.11.4-1
- Initial packaging
