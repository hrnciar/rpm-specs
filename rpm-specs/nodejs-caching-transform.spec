%{?nodejs_find_provides_and_requires}

%global packagename caching-transform
%global enable_tests 0
# Tests disabled due to missing 'ava' in Fedora

Name:		nodejs-caching-transform
Version:	1.0.1
Release:	9%{?dist}
Summary:	Wraps a transform and provides caching

License:	MIT
URL:		https://github.com/jamestalmage/caching-transform.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jamestalmage/caching-transform/v%{version}/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(md5-hex)
BuildRequires:	npm(mkdirp)
BuildRequires:	npm(write-file-atomic)
%if 0%{?enable_tests}
BuildRequires:	ava
%endif

%description
Wraps a transform and provides caching


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
%{_bindir}/ava
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  9 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
