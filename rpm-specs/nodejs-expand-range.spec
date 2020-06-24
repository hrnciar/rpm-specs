%{?nodejs_find_provides_and_requires}

%global packagename expand-range
%global enable_tests 1

Name:		nodejs-expand-range
Version:	2.0.1
Release:	6%{?dist}
Summary:	Fast, bash-like range expansion

License:	MIT
URL:		https://github.com/jonschlinkert/expand-range.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# The 1.8.2 release is not yet tagged in github, so we'll just grab the test from master
Source1:	https://raw.githubusercontent.com/jonschlinkert/expand-range/master/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(extend-shallow)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(fill-range)
BuildRequires:	npm(should)
%endif

%description
Fast, bash-like range expansion. Expand a range of numbers or letters, uppercase
or lowercase. See the benchmarks. Used by micromatch.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep extend-shallow

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
%{_bindir}/mocha -R spec --require should
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue May 09 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.1-1
- Update to upstream 2.0.1 release

* Tue May 09 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Mon Apr 17 2017 Jared Smith <jsmith@fedoraproject.org> - 1.8.2-2
- Relax dependency on npm(fill-range)

* Sat Jun 18 2016 Jared Smith <jsmith@fedoraproject.org> - 1.8.2-1
- Update to upstream 1.8.2 release

* Thu Feb  4 2016 Jared Smith <jsmith@fedoraproject.org> - 1.8.1-1
- Initial packaging
