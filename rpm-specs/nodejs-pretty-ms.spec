%{?nodejs_find_provides_and_requires}

%global packagename pretty-ms

# Tests disabled until 'ava' is packaged in Fedora
# See https://bugzilla.redhat.com/show_bug.cgi?id=1194923
%global enable_tests 0

Name:		nodejs-pretty-ms
Version:	2.1.0
Release:	9%{?dist}
Summary:	Convert milliseconds to a human readable string: 1337000000 → 15d 11h 23m 20s

License:	MIT
URL:		https://github.com/sindresorhus/pretty-ms
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Grab them from the upstream GitHub repo instead
Source1:	https://raw.githubusercontent.com/sindresorhus/pretty-ms/v%{version}/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(is-finite)
BuildRequires:	npm(parse-ms)
BuildRequires:	npm(plur)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Convert milliseconds to a human readable string: 1337000000 → 15d 11h 23m 20s


%prep
%setup -q -n package
cp -p %{SOURCE1} .

%nodejs_fixdep plur

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
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 22 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.0-2
- Fix dependency version on npm(plur)

* Thu Oct 22 2015 Jared Smith <jsmith@fedoraproject.org> - 2.1.0-1
- Initial packaging
