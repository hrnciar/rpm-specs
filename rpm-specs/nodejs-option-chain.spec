%{?nodejs_find_provides_and_requires}

%global packagename option-chain

# tests missing due to missing npm(ava)
%global enable_tests 0

Name:		nodejs-option-chain
Version:	1.0.0
Release:	7%{?dist}
Summary:	Use fluent property chains in lieu of options objects

License:	MIT
URL:		https://github.com/jamestalmage/option-chain
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jamestalmage/%{packagename}/v%{version}/test.js

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(object-assign)
%if 0%{?enable_tests}
BuildRequires:	npm(ava)
%endif

%description
Use fluent property chains in lieu of options objects


%prep
%autosetup -n package
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
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Update to upstream 1.0.0 release

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-1
- Initial packaging
